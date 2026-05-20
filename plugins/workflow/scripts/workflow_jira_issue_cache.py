#!/usr/bin/env python3
"""Jira Data Center issue cache carrier for workflow provider projections."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from workflow_cache import (
    CACHE_ROOT_NAME,
    FreshnessMetadata,
    WorkflowCacheCorrupt,
    WorkflowCacheError,
    WorkflowCacheMiss,
    _atomic_write_text,
    _format_markdown,
    _normalize_optional,
    _read_frontmatter_markdown,
    _require_schema,
    _safe_file_segment,
    _safe_path_segment,
    _utc_now,
)
from workflow_jira_data_center_client import JiraDataCenterSite
from workflow_jira_issue_relationships import (
    filter_jira_payload,
    normalize_jira_data_center_issue,
)
from workflow_jira_issue_refs import normalize_jira_issue_key
from workflow_jira_issue_snapshot import render_jira_snapshot


_COMMENT_FILENAME_RE = re.compile(r"^comment-.*\.md$")


def is_jira_issue_cache_body_path(path: Path, project: Path) -> bool:
    """Return whether ``path`` is a Jira issue body or comment cache projection.

    Recognizes ``issue.md`` and sibling ``comment-*.md`` files under the Jira
    issue cache directory layout ``<project>/.workflow-cache/issues/<key>/``.
    """

    name = path.name
    if name != "issue.md" and not _COMMENT_FILENAME_RE.match(name):
        return False
    try:
        parts = path.expanduser().resolve(strict=False).relative_to(
            project.expanduser().resolve(strict=False) / CACHE_ROOT_NAME
        ).parts
    except ValueError:
        return False
    return len(parts) == 3 and parts[0] == "issues"


class JiraDataCenterIssueCache:
    """Repo-local Jira Data Center cache with native JSON plus an LLM snapshot."""

    def __init__(self, root: Path):
        self.root = root

    @classmethod
    def for_project(cls, project: Path) -> JiraDataCenterIssueCache:
        return cls(project.expanduser().resolve(strict=False) / CACHE_ROOT_NAME)

    def issue_dir(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.root / "issues" / _safe_path_segment(normalize_jira_issue_key(issue_key))

    def issue_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "issue.md"

    def issue_json_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "issue.json"

    def remote_links_json_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "remote-links.json"

    def has_issue_projection(self, site: JiraDataCenterSite, issue_key: str) -> bool:
        return self.issue_json_file(site, issue_key).is_file()

    def comment_files(self, site: JiraDataCenterSite, issue_key: str) -> list[Path]:
        """Return cached comment files sorted by filename (chronological)."""

        issue_dir = self.issue_dir(site, issue_key)
        if not issue_dir.is_dir():
            return []
        return sorted(path for path in issue_dir.glob("comment-*.md") if path.is_file())

    def read_freshness_metadata(
        self,
        site: JiraDataCenterSite,
        issue_key: str,
        *,
        target: str = "issue",
    ) -> FreshnessMetadata:
        path = self.issue_file(site, issue_key)
        if not path.is_file():
            raise WorkflowCacheMiss(f"Jira issue cache does not exist: {path}")
        frontmatter, _body = _read_frontmatter_markdown(path)
        _require_schema(frontmatter, path)
        return FreshnessMetadata(
            source_updated_at=_normalize_optional(frontmatter.get("source_updated_at")),
            fetched_at=_normalize_optional(frontmatter.get("fetched_at")),
            path=path,
            target=target,
        )

    def read_issue(
        self,
        site: JiraDataCenterSite,
        issue_key: str,
        *,
        include_body: bool = True,
        include_comments: bool = True,
        include_relationships: bool = True,
    ) -> dict[str, Any]:
        """Read a cached Jira Data Center issue projection."""

        key = normalize_jira_issue_key(issue_key)
        issue_json_path = self.issue_json_file(site, key)
        issue_md_path = self.issue_file(site, key)
        if not issue_json_path.is_file():
            raise WorkflowCacheMiss(f"Jira issue cache does not exist: {issue_json_path}")
        if not issue_md_path.is_file():
            raise WorkflowCacheMiss(f"Jira issue body cache does not exist: {issue_md_path}")

        try:
            frontmatter, _body = _read_frontmatter_markdown(issue_md_path)
            _require_schema(frontmatter, issue_md_path)
            issue = _read_json_mapping(issue_json_path)
            remote_links = _read_json_list_if_exists(self.remote_links_json_file(site, key))
            payload = normalize_jira_data_center_issue(issue, site=site, remote_links=remote_links)
            payload["cache"] = {
                "hit": True,
                "issue_dir": str(self.issue_dir(site, key)),
                "issue_file": str(issue_md_path),
                "fetchedAt": _normalize_optional(frontmatter.get("fetched_at")),
                "sourceUpdatedAt": _normalize_optional(frontmatter.get("source_updated_at")),
            }
            return filter_jira_payload(
                payload,
                include_body=include_body,
                include_comments=include_comments,
                include_relationships=include_relationships,
            )
        except WorkflowCacheError:
            raise
        except Exception as exc:
            raise WorkflowCacheCorrupt(f"could not read Jira issue cache {issue_json_path}: {exc}") from exc

    def read_issue_json(self, site: JiraDataCenterSite, issue_key: str) -> Mapping[str, Any]:
        key = normalize_jira_issue_key(issue_key)
        issue_json_path = self.issue_json_file(site, key)
        if not issue_json_path.is_file():
            raise WorkflowCacheMiss(f"Jira issue cache does not exist: {issue_json_path}")
        return _read_json_mapping(issue_json_path)

    def write_issue_bundle(
        self,
        site: JiraDataCenterSite,
        issue: Mapping[str, Any],
        *,
        remote_links: list[Mapping[str, Any]] | None = None,
        fetched_at: str | None = None,
        hidden_comment_markers: Sequence[str] = (),
    ) -> dict[str, str]:
        """Write native JSON, metadata, generated snapshot, and per-comment files."""

        key = normalize_jira_issue_key(issue.get("key") or "")
        links = [dict(item) for item in (remote_links or [])]
        normalized = normalize_jira_data_center_issue(issue, site=site, remote_links=links)
        now = fetched_at or _utc_now()
        source_updated_at = _normalize_optional(normalized.get("updatedAt")) or now

        issue_dir = self.issue_dir(site, key)
        issue_dir.mkdir(parents=True, exist_ok=True)
        issue_json_path = self.issue_json_file(site, key)
        remote_links_path = self.remote_links_json_file(site, key)
        issue_md_path = self.issue_file(site, key)

        _atomic_write_text(issue_json_path, _format_json(issue))
        _atomic_write_text(remote_links_path, _format_json(links))
        _atomic_write_text(
            issue_md_path,
            render_jira_snapshot(
                normalized,
                source_updated_at=source_updated_at,
                fetched_at=now,
            ),
        )
        self._write_comment_files(
            site,
            key,
            normalized,
            fetched_at=now,
            hidden_comment_markers=hidden_comment_markers,
        )
        return {
            "issue_dir": str(issue_dir),
            "issue_file": str(issue_md_path),
        }

    def _write_comment_files(
        self,
        site: JiraDataCenterSite,
        issue_key: str,
        normalized: Mapping[str, Any],
        *,
        fetched_at: str,
        hidden_comment_markers: Sequence[str],
    ) -> None:
        """Write ``comment-*.md`` files, skipping comments matching hidden markers."""

        issue_dir = self.issue_dir(site, issue_key)
        issue_dir.mkdir(parents=True, exist_ok=True)
        raw_comments = normalized.get("comments")
        comments = raw_comments if isinstance(raw_comments, list) else []
        markers = tuple(marker for marker in hidden_comment_markers if marker)
        expected_files: set[str] = set()

        for position, comment in enumerate(comments, start=1):
            if not isinstance(comment, Mapping):
                continue
            body = str(comment.get("body") or "")
            if markers and any(marker in body for marker in markers):
                continue

            comment_id = _normalize_optional(comment.get("id")) or str(position)
            created_at = (
                _normalize_optional(comment.get("createdAt"))
                or _normalize_optional(comment.get("created"))
                or fetched_at
            )
            updated_at = (
                _normalize_optional(comment.get("updatedAt"))
                or _normalize_optional(comment.get("updated"))
                or created_at
            )
            author = _comment_author_name(comment.get("author"))
            file_name = (
                f"comment-{_compact_timestamp(created_at)}-{_safe_file_segment(comment_id)}.md"
            )
            expected_files.add(file_name)

            comment_frontmatter: dict[str, Any] = {
                "author": author,
                "provider_comment_id": comment_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
            _atomic_write_text(
                issue_dir / file_name,
                _format_markdown(comment_frontmatter, body),
            )

        for path in issue_dir.glob("comment-*.md"):
            if path.name not in expected_files:
                path.unlink()

def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise WorkflowCacheCorrupt(f"invalid JSON cache file: {path}: {exc}") from exc
    if not isinstance(value, Mapping):
        raise WorkflowCacheCorrupt(f"JSON cache file must contain an object: {path}")
    return value


def _read_json_list_if_exists(path: Path) -> list[Mapping[str, Any]]:
    if not path.is_file():
        return []
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise WorkflowCacheCorrupt(f"invalid JSON cache file: {path}: {exc}") from exc
    return _mapping_list(value)


def _format_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def _mapping_list(value: Any) -> list[Mapping[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _comment_author_name(value: Any) -> str:
    if isinstance(value, Mapping):
        for key in ("displayName", "name", "key", "accountId"):
            raw = value.get(key)
            if raw:
                return str(raw)
    if value:
        return str(value)
    return "unknown"


def _compact_timestamp(value: str) -> str:
    normalized = value.strip()
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})", normalized)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}T{match.group(4)}{match.group(5)}{match.group(6)}Z"
    return _safe_file_segment(normalized) or "unknown-time"
