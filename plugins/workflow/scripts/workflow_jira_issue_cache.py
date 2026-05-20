#!/usr/bin/env python3
"""Jira Data Center issue cache carrier for workflow provider projections."""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from workflow_cache import (
    CACHE_ROOT_NAME,
    SCHEMA_VERSION,
    FreshnessMetadata,
    WorkflowCacheCorrupt,
    WorkflowCacheError,
    WorkflowCacheMiss,
    _atomic_write_text,
    _dump_yaml,
    _label_names,
    _read_yaml_mapping,
    _require_schema,
    _safe_path_segment,
    _utc_now,
)
from workflow_jira_data_center_client import (
    DEPLOYMENT_DATA_CENTER,
    JiraDataCenterSite,
)
from workflow_jira_issue_relationships import (
    filter_jira_payload,
    normalize_jira_data_center_issue,
)
from workflow_jira_issue_refs import normalize_jira_issue_key
from workflow_jira_issue_snapshot import render_jira_snapshot


def is_jira_issue_cache_body_path(path: Path, project: Path) -> bool:
    """Return whether ``path`` is a Jira issue body cache projection.

    Recognizes ``snapshot.md`` files under the Jira issue cache directory layout
    ``<project>/.workflow-cache/jira/<site>/issues/<key>/snapshot.md``.
    """

    if path.name != "snapshot.md":
        return False
    try:
        parts = path.expanduser().resolve(strict=False).relative_to(
            project.expanduser().resolve(strict=False) / CACHE_ROOT_NAME
        ).parts
    except ValueError:
        return False
    return len(parts) == 5 and parts[0] == "jira" and parts[2] == "issues"


class JiraDataCenterIssueCache:
    """Repo-local Jira Data Center cache with native JSON plus an LLM snapshot."""

    def __init__(self, root: Path):
        self.root = root

    @classmethod
    def for_project(cls, project: Path) -> JiraDataCenterIssueCache:
        return cls(project.expanduser().resolve(strict=False) / CACHE_ROOT_NAME)

    def issue_dir(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return (
            self.root
            / "jira"
            / _safe_path_segment(site.cache_site_segment)
            / "issues"
            / _safe_path_segment(normalize_jira_issue_key(issue_key))
        )

    def snapshot_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "snapshot.md"

    def metadata_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "metadata.yml"

    def issue_json_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "issue.json"

    def remote_links_json_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "remote-links.json"

    def has_issue_projection(self, site: JiraDataCenterSite, issue_key: str) -> bool:
        return self.issue_json_file(site, issue_key).is_file()

    def read_freshness_metadata(
        self,
        site: JiraDataCenterSite,
        issue_key: str,
        *,
        target: str = "issue",
    ) -> FreshnessMetadata:
        path = self.metadata_file(site, issue_key)
        if not path.is_file():
            raise WorkflowCacheMiss(f"Jira freshness cache does not exist: {path}")
        data = _read_yaml_mapping(path)
        _require_schema(data, path)
        return FreshnessMetadata(
            source_updated_at=_normalize_optional(data.get("source_updated_at")),
            fetched_at=_normalize_optional(data.get("fetched_at")),
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
        issue_path = self.issue_json_file(site, key)
        metadata_path = self.metadata_file(site, key)
        if not issue_path.is_file():
            raise WorkflowCacheMiss(f"Jira issue cache does not exist: {issue_path}")
        if not metadata_path.is_file():
            raise WorkflowCacheMiss(f"Jira metadata cache does not exist: {metadata_path}")

        try:
            metadata = _read_yaml_mapping(metadata_path)
            _require_schema(metadata, metadata_path)
            issue = _read_json_mapping(issue_path)
            remote_links = _read_json_list_if_exists(self.remote_links_json_file(site, key))
            payload = normalize_jira_data_center_issue(issue, site=site, remote_links=remote_links)
            payload["cache"] = {
                "hit": True,
                "issue_dir": str(self.issue_dir(site, key)),
                "snapshot": str(self.snapshot_file(site, key)),
                "metadata_file": str(metadata_path),
                "issue_json": str(issue_path),
                "remote_links_json": str(self.remote_links_json_file(site, key)),
                "fetchedAt": metadata.get("fetched_at"),
                "sourceUpdatedAt": metadata.get("source_updated_at"),
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
            raise WorkflowCacheCorrupt(f"could not read Jira issue cache {issue_path}: {exc}") from exc

    def read_issue_json(self, site: JiraDataCenterSite, issue_key: str) -> Mapping[str, Any]:
        key = normalize_jira_issue_key(issue_key)
        issue_path = self.issue_json_file(site, key)
        if not issue_path.is_file():
            raise WorkflowCacheMiss(f"Jira issue cache does not exist: {issue_path}")
        return _read_json_mapping(issue_path)

    def write_issue_bundle(
        self,
        site: JiraDataCenterSite,
        issue: Mapping[str, Any],
        *,
        remote_links: list[Mapping[str, Any]] | None = None,
        fetched_at: str | None = None,
        snapshot_hidden_comment_markers: Sequence[str] = (),
    ) -> dict[str, str]:
        """Write native JSON, metadata, and generated Markdown snapshot."""

        key = normalize_jira_issue_key(issue.get("key") or "")
        links = [dict(item) for item in (remote_links or [])]
        normalized = normalize_jira_data_center_issue(issue, site=site, remote_links=links)
        now = fetched_at or _utc_now()
        source_updated_at = _normalize_optional(normalized.get("updatedAt")) or now

        issue_dir = self.issue_dir(site, key)
        issue_dir.mkdir(parents=True, exist_ok=True)
        issue_path = self.issue_json_file(site, key)
        remote_links_path = self.remote_links_json_file(site, key)
        metadata_path = self.metadata_file(site, key)
        snapshot_path = self.snapshot_file(site, key)

        _atomic_write_text(issue_path, _format_json(issue))
        _atomic_write_text(remote_links_path, _format_json(links))
        _atomic_write_text(
            snapshot_path,
            render_jira_snapshot(normalized, hidden_comment_markers=snapshot_hidden_comment_markers),
        )
        _atomic_write_text(
            metadata_path,
            _dump_yaml(
                {
                    "schema_version": SCHEMA_VERSION,
                    "provider": "jira",
                    "deployment": DEPLOYMENT_DATA_CENTER,
                    "site": site.base_url,
                    "api_version": site.api_version,
                    "key": key,
                    "project": key.split("-", 1)[0],
                    "state": _normalize_optional(normalized.get("state")),
                    "source_updated_at": source_updated_at,
                    "created_at": _normalize_optional(normalized.get("createdAt")),
                    "fetched_at": now,
                    "url": normalized.get("url"),
                    "snapshot": "snapshot.md",
                    "issue_json": "issue.json",
                    "remote_links_json": "remote-links.json",
                }
            ),
        )
        return {
            "issue_dir": str(issue_dir),
            "snapshot": str(snapshot_path),
            "metadata_file": str(metadata_path),
            "issue_json": str(issue_path),
            "remote_links_json": str(remote_links_path),
        }

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


def _normalize_optional(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
