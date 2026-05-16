#!/usr/bin/env python3
"""Jira Data Center issue cache carrier for workflow provider projections."""

from __future__ import annotations

import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from workflow_cache import (
    CACHE_ROOT_NAME,
    SCHEMA_VERSION,
    FreshnessMetadata,
    PendingIssueComment,
    PendingIssueDraft,
    PendingIssueRelationshipOperation,
    WorkflowCacheCorrupt,
    WorkflowCacheError,
    WorkflowCacheMiss,
    _atomic_write_text,
    _dump_yaml,
    _label_names,
    _move_path_if_exists,
    _read_frontmatter_markdown,
    _read_pending_comments,
    _read_pending_relationships,
    _read_yaml_mapping,
    _remove_empty_parents,
    _require_schema,
    _safe_path_segment,
)
from workflow_jira import (
    DEPLOYMENT_DATA_CENTER,
    JiraDataCenterSite,
    filter_jira_payload,
    normalize_jira_data_center_issue,
    normalize_jira_issue_key,
    render_jira_snapshot,
    _format_json,
    _normalize_optional,
    _read_json_list_if_exists,
    _read_json_mapping,
    _utc_now,
)

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

    def pending_issue_dir(self, site: JiraDataCenterSite, local_id: str) -> Path:
        return (
            self.root
            / "jira"
            / _safe_path_segment(site.cache_site_segment)
            / "issues-pending"
            / _safe_path_segment(local_id)
        )

    def pending_issue_file(self, site: JiraDataCenterSite, local_id: str) -> Path:
        return self.pending_issue_dir(site, local_id) / "issue.md"

    def created_issue_archive_dir(self, site: JiraDataCenterSite, local_id: str, issue_key: str) -> Path:
        key = normalize_jira_issue_key(issue_key)
        return (
            self.root
            / "jira"
            / _safe_path_segment(site.cache_site_segment)
            / "issues-created"
            / f"{_safe_path_segment(key)}-{_safe_path_segment(local_id)}"
        )

    def comments_pending_dir(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "comments-pending"

    def relationships_pending_file(self, site: JiraDataCenterSite, issue_key: str) -> Path:
        return self.issue_dir(site, issue_key) / "relationships-pending.yml"

    def pending_issue_relationships_pending_file(self, site: JiraDataCenterSite, local_id: str) -> Path:
        return self.pending_issue_dir(site, local_id) / "relationships-pending.yml"

    def has_issue_projection(self, site: JiraDataCenterSite, issue_key: str) -> bool:
        return self.issue_json_file(site, issue_key).is_file()

    def read_pending_issue_draft(self, site: JiraDataCenterSite, local_id: str) -> PendingIssueDraft:
        path = self.pending_issue_file(site, local_id)
        if not path.is_file():
            raise WorkflowCacheMiss(f"Jira pending issue draft does not exist: {path}")

        frontmatter, body = _read_frontmatter_markdown(path)
        if frontmatter.get("schema_version") is not None:
            _require_schema(frontmatter, path)

        title = str(frontmatter.get("title") or "").strip()
        if not title:
            raise WorkflowCacheCorrupt(f"Jira pending issue draft is missing title: {path}")
        return PendingIssueDraft(
            local_id=_safe_path_segment(local_id),
            path=path,
            title=title,
            body=body,
            labels=tuple(_label_names(frontmatter.get("labels"))),
            state=str(frontmatter.get("state") or "open").strip().lower(),
            state_reason=_normalize_optional(frontmatter.get("state_reason") or frontmatter.get("stateReason")),
        )

    def read_pending_issue_comments(self, site: JiraDataCenterSite, issue_key: str) -> list[PendingIssueComment]:
        key = normalize_jira_issue_key(issue_key)
        return _read_pending_comments(
            self.comments_pending_dir(site, key),
            target_kind="issue",
            target_id=key,
        )

    def read_pending_issue_relationships(
        self,
        site: JiraDataCenterSite,
        issue_key: str,
    ) -> list[PendingIssueRelationshipOperation]:
        """Read pending relationship operations for an existing Jira issue projection."""

        key = normalize_jira_issue_key(issue_key)
        return _read_pending_relationships(
            self.relationships_pending_file(site, key),
            target_kind="issue",
            target_id=key,
        )

    def read_pending_draft_relationships(
        self,
        site: JiraDataCenterSite,
        local_id: str,
    ) -> list[PendingIssueRelationshipOperation]:
        """Read pending relationship operations for a pending Jira issue projection."""

        safe_local_id = _safe_path_segment(local_id)
        return _read_pending_relationships(
            self.pending_issue_relationships_pending_file(site, safe_local_id),
            target_kind="pending_issue",
            target_id=safe_local_id,
        )

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
        _atomic_write_text(snapshot_path, render_jira_snapshot(normalized))
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

    def remove_pending_issue_comments(
        self,
        site: JiraDataCenterSite,
        issue_key: str,
        comments: list[PendingIssueComment],
    ) -> list[Path]:
        key = normalize_jira_issue_key(issue_key)
        pending_dir = self.comments_pending_dir(site, key)
        removed: list[Path] = []
        for comment in comments:
            if comment.path.parent.resolve(strict=False) != pending_dir.resolve(strict=False):
                raise WorkflowCacheError(f"pending comment is outside Jira issue pending directory: {comment.path}")
            if comment.path.exists():
                comment.path.unlink()
                removed.append(comment.path)
        _remove_empty_parents(pending_dir, stop_at=self.issue_dir(site, key))
        return removed

    def remove_pending_issue_relationships(
        self,
        site: JiraDataCenterSite,
        issue_key: str,
        operations: list[PendingIssueRelationshipOperation],
    ) -> list[Path]:
        """Remove a successfully consumed Jira pending relationship file."""

        key = normalize_jira_issue_key(issue_key)
        path = self.relationships_pending_file(site, key)
        return self._remove_pending_relationship_file(path, operations, stop_at=self.issue_dir(site, key))

    def remove_pending_draft_relationships(
        self,
        site: JiraDataCenterSite,
        local_id: str,
        operations: list[PendingIssueRelationshipOperation],
    ) -> list[Path]:
        """Remove a consumed pending relationship file from a pending Jira issue projection."""

        safe_local_id = _safe_path_segment(local_id)
        path = self.pending_issue_relationships_pending_file(site, safe_local_id)
        return self._remove_pending_relationship_file(
            path,
            operations,
            stop_at=self.pending_issue_dir(site, safe_local_id),
        )

    def _remove_pending_relationship_file(
        self,
        path: Path,
        operations: list[PendingIssueRelationshipOperation],
        *,
        stop_at: Path,
    ) -> list[Path]:
        expected = path.resolve(strict=False)
        seen = False
        for operation in operations:
            seen = True
            if operation.path.resolve(strict=False) != expected:
                raise WorkflowCacheError(f"pending relationship operation is outside Jira pending file: {operation.path}")
        if not seen or not path.exists():
            return []
        path.unlink()
        _remove_empty_parents(path.parent, stop_at=stop_at)
        return [path]

    def finalize_pending_issue_creation(
        self,
        site: JiraDataCenterSite,
        local_id: str,
        issue_key: str,
    ) -> dict[str, str | None]:
        pending_dir = self.pending_issue_dir(site, local_id)
        draft_path = pending_dir / "issue.md"
        archive_dir = self.created_issue_archive_dir(site, local_id, issue_key)
        archived_issue: Path | None = None
        if draft_path.exists():
            archive_dir.mkdir(parents=True, exist_ok=True)
            archived_issue = archive_dir / "issue.md"
            os.replace(draft_path, archived_issue)

        issue_dir = self.issue_dir(site, issue_key)
        issue_dir.mkdir(parents=True, exist_ok=True)
        moved_comments = _move_path_if_exists(pending_dir / "comments-pending", issue_dir / "comments-pending")
        moved_relationships = _move_path_if_exists(
            pending_dir / "relationships-pending.yml",
            issue_dir / "relationships-pending.yml",
        )
        _remove_empty_parents(pending_dir, stop_at=self.root / "jira" / _safe_path_segment(site.cache_site_segment))
        return {
            "archived_issue": str(archived_issue) if archived_issue is not None else None,
            "comments_pending": str(moved_comments) if moved_comments is not None else None,
            "relationships_pending": str(moved_relationships) if moved_relationships is not None else None,
        }
