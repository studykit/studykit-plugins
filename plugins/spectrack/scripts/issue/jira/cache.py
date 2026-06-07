#!/usr/bin/env python3
"""Jira Data Center issue cache carrier for workflow provider projections."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from issue.cache import (
    CACHE_ROOT_NAME,
    SCHEMA_VERSION,
    FreshnessMetadata,
    WorkflowCacheCorrupt,
    WorkflowCacheError,
    WorkflowCacheMiss,
    _atomic_write_text,
    _format_markdown,
    _normalize_optional,
    _require_schema,
    _safe_file_segment,
    _safe_path_segment,
    _utc_now,
    comments_fingerprint,
    content_fingerprint,
    relationships_fingerprint,
)
from issue.jira.refs import normalize_jira_issue_key
from issue.jira.relationships import (
    filter_jira_payload,
    normalize_jira_data_center_issue,
)
from issue.jira.snapshot import (
    _jira_person_display_name,
    jira_relationship_fingerprint_block,
    render_jira_attachments_markdown,
    render_jira_relationships_markdown,
    render_jira_state_markdown,
)
from issue.jira.client import JiraDataCenterSite


_COMMENT_FILENAME_RE = re.compile(r"^comment-.*\.md$")


def is_jira_issue_cache_body_path(path: Path, project: Path) -> bool:
    """Return whether ``path`` is a read-only Jira issue content projection.

    Recognizes ``issue.md``, the readable ``state.md``, ``relation.md`` and
    ``attachment.md`` projections, and sibling ``comment-*.md`` files under
    the Jira issue cache directory layout
    ``<project>/.spectrack-cache/issues/<key>/``. The internal dotfiles
    (``.meta.json`` and the native ``.issue.json`` / ``.remote-links.json``
    machine sources) are matched by :func:`is_jira_issue_cache_meta_path` and
    are not editable projections.
    """

    name = path.name
    if name not in {"issue.md", "state.md", "relation.md", "attachment.md"} and not _COMMENT_FILENAME_RE.match(name):
        return False
    return _jira_issue_cache_dir_match(path, project)


def is_jira_issue_cache_meta_path(path: Path, project: Path) -> bool:
    """Return whether ``path`` is an internal Jira cache dotfile.

    Covers the ``.meta.json`` bookkeeping file and the native
    ``.issue.json`` / ``.remote-links.json`` machine sources. All are dotfiles
    the dispatchers maintain; readers consume the ``*.md`` projections instead.
    """

    if path.name not in {".meta.json", ".issue.json", ".remote-links.json"}:
        return False
    return _jira_issue_cache_dir_match(path, project)


def _jira_issue_cache_dir_match(path: Path, project: Path) -> bool:
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

    def state_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "state.md"

    def meta_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / ".meta.json"

    def issue_json_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / ".issue.json"

    def remote_links_json_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / ".remote-links.json"

    def relationships_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "relation.md"

    def attachments_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "attachment.md"

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
        meta_path = self.meta_file(site, issue_key)
        if not meta_path.is_file():
            raise WorkflowCacheMiss(f"Jira freshness cache does not exist: {meta_path}")
        meta = _read_json_mapping(meta_path)
        _require_schema(meta, meta_path)
        fingerprints = meta.get("fingerprints")
        if not isinstance(fingerprints, Mapping):
            raise WorkflowCacheCorrupt(f"missing fingerprints in {meta_path}")
        key = "content" if target == "issue" else target
        return FreshnessMetadata(
            fingerprint=_normalize_optional(fingerprints.get(key)),
            path=meta_path,
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
        relationship_mappings: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Read a cached Jira Data Center issue projection."""

        key = normalize_jira_issue_key(issue_key)
        issue_json_path = self.issue_json_file(site, key)
        issue_md_path = self.issue_file(site, key)
        meta_path = self.meta_file(site, key)
        if not issue_json_path.is_file():
            raise WorkflowCacheMiss(f"Jira issue cache does not exist: {issue_json_path}")
        if not issue_md_path.is_file():
            raise WorkflowCacheMiss(f"Jira issue body cache does not exist: {issue_md_path}")
        if not meta_path.is_file():
            raise WorkflowCacheMiss(f"Jira issue meta cache does not exist: {meta_path}")

        try:
            _require_schema(_read_json_mapping(meta_path), meta_path)
            issue = _read_json_mapping(issue_json_path)
            remote_links = _read_json_list_if_exists(self.remote_links_json_file(site, key))
            payload = normalize_jira_data_center_issue(
                issue,
                site=site,
                remote_links=remote_links,
                relationship_mappings=relationship_mappings,
            )
            payload["cache"] = {
                "hit": True,
                "issue_dir": str(self.issue_dir(site, key)),
                "issue_file": str(issue_md_path),
                "state_file": str(self.state_file(site, key)),
                "meta_file": str(meta_path),
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
        relationship_mappings: Mapping[str, Any] | None = None,
    ) -> dict[str, str]:
        """Write native JSON, metadata, body/state snapshots, and per-comment files."""

        key = normalize_jira_issue_key(issue.get("key") or "")
        links = [dict(item) for item in (remote_links or [])]
        normalized = normalize_jira_data_center_issue(
            issue,
            site=site,
            remote_links=links,
            relationship_mappings=relationship_mappings,
        )
        now = fetched_at or _utc_now()

        issue_dir = self.issue_dir(site, key)
        issue_dir.mkdir(parents=True, exist_ok=True)
        issue_json_path = self.issue_json_file(site, key)
        remote_links_path = self.remote_links_json_file(site, key)
        issue_md_path = self.issue_file(site, key)
        meta_path = self.meta_file(site, key)

        relationships = normalized.get("relationships")
        _atomic_write_text(issue_json_path, _format_json(issue))
        _atomic_write_text(remote_links_path, _format_json(links))
        _atomic_write_text(issue_md_path, str(normalized.get("body") or ""))
        state_path = self.state_file(site, key)
        _atomic_write_text(
            state_path, render_jira_state_markdown(normalized, issue_key=key)
        )
        relationships_md = render_jira_relationships_markdown(
            relationships if isinstance(relationships, Mapping) else {},
            issue_key=key,
        )
        relationships_path = self.relationships_file(site, key)
        if relationships_md is None:
            relationships_path.unlink(missing_ok=True)
        else:
            _atomic_write_text(relationships_path, relationships_md)
        attachments_md = render_jira_attachments_markdown(
            normalized.get("attachments"),
            issue_key=key,
        )
        attachments_path = self.attachments_file(site, key)
        if attachments_md is None:
            attachments_path.unlink(missing_ok=True)
        else:
            _atomic_write_text(attachments_path, attachments_md)
        meta = {
            "schema_version": SCHEMA_VERSION,
            "fingerprints": jira_fingerprints(
                normalized, hidden_comment_markers=hidden_comment_markers
            ),
        }
        _atomic_write_text(meta_path, _format_json(meta))
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
            "state_file": str(state_path),
            "meta_file": str(meta_path),
            "relationships_file": str(self.relationships_file(site, key)),
            "attachments_file": str(self.attachments_file(site, key)),
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


def jira_fingerprints(
    normalized: Mapping[str, Any],
    *,
    hidden_comment_markers: Sequence[str] = (),
) -> dict[str, str]:
    """All three per-target fingerprints for a normalized Jira issue."""

    return {
        "content": _jira_content_fingerprint(normalized),
        "relationships": _jira_relationships_fingerprint(normalized),
        "comments": _jira_comments_fingerprint(
            normalized, hidden_comment_markers=hidden_comment_markers
        ),
    }


def jira_target_fingerprint(
    normalized: Mapping[str, Any],
    target: str,
    *,
    hidden_comment_markers: Sequence[str] = (),
) -> str:
    """One target's fingerprint, used by the provider write-back check."""

    if target == "comments":
        return _jira_comments_fingerprint(
            normalized, hidden_comment_markers=hidden_comment_markers
        )
    if target == "relationships":
        return _jira_relationships_fingerprint(normalized)
    return _jira_content_fingerprint(normalized)


def _jira_content_fingerprint(normalized: Mapping[str, Any]) -> str:
    return content_fingerprint(normalized.get("title"), normalized.get("body"))


def _jira_relationships_fingerprint(normalized: Mapping[str, Any]) -> str:
    relationships = normalized.get("relationships")
    block = jira_relationship_fingerprint_block(
        relationships if isinstance(relationships, Mapping) else {}
    )
    return relationships_fingerprint(block)


def _jira_comments_fingerprint(
    normalized: Mapping[str, Any],
    *,
    hidden_comment_markers: Sequence[str] = (),
) -> str:
    return comments_fingerprint(
        _jira_comment_fingerprint_items(normalized, hidden_comment_markers)
    )


def _jira_comment_fingerprint_items(
    normalized: Mapping[str, Any],
    hidden_comment_markers: Sequence[str],
) -> list[dict[str, str | None]]:
    raw = normalized.get("comments")
    comments = raw if isinstance(raw, list) else []
    markers = tuple(marker for marker in hidden_comment_markers if marker)
    items: list[dict[str, str | None]] = []
    for position, comment in enumerate(comments, start=1):
        if not isinstance(comment, Mapping):
            continue
        body = str(comment.get("body") or "")
        if markers and any(marker in body for marker in markers):
            continue
        comment_id = _normalize_optional(comment.get("id")) or str(position)
        revision = (
            _normalize_optional(comment.get("updatedAt"))
            or _normalize_optional(comment.get("updated"))
            or _normalize_optional(comment.get("createdAt"))
            or _normalize_optional(comment.get("created"))
        )
        items.append({"id": comment_id, "updated_at": revision})
    items.sort(key=lambda item: (item["id"], item["updated_at"] or ""))
    return items


def _mapping_list(value: Any) -> list[Mapping[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _comment_author_name(value: Any) -> str:
    resolved = _jira_person_display_name(value)
    if resolved is not None:
        return resolved
    if value and not isinstance(value, Mapping):
        return str(value)
    return "unknown"


def _compact_timestamp(value: str) -> str:
    normalized = value.strip()
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})", normalized)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}T{match.group(4)}{match.group(5)}{match.group(6)}Z"
    return _safe_file_segment(normalized) or "unknown-time"
