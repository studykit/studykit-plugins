#!/usr/bin/env python3
"""GitHub Issues cache carrier for workflow provider projections."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
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
    _format_markdown,
    _label_names,
    _normalize_freshness_target,
    _normalize_optional,
    _normalize_state,
    _normalize_state_reason,
    _read_frontmatter_markdown,
    _require_schema,
    _safe_file_segment,
    _safe_path_segment,
    _utc_now,
)
from workflow_github import GitHubRepository, normalize_issue_number


_COMMENT_FILENAME_RE = re.compile(r"^comment-.*\.md$")


def is_github_issue_cache_body_path(path: Path, project: Path) -> bool:
    """Return whether ``path`` is a GitHub issue body cache projection.

    Recognizes the ``issue.md`` body and any ``comment-*.md`` sibling in the
    flat per-issue directory layout. Configured-repo issues sit at
    ``.workflow-cache/issues/<n>/`` and external repos are namespaced under
    ``.workflow-cache/<host>/<owner>/<repo>/issues/<n>/``.
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

    if len(parts) == 3:
        return parts[0] == "issues"
    if len(parts) == 6:
        return parts[3] == "issues"
    return False


@dataclass(frozen=True)
class CacheWriteResult:
    """Paths written for one cache projection refresh."""

    issue_dir: Path
    issue_file: Path
    relationship_location: Path

    def to_json(self) -> dict[str, str]:
        return {
            "issue_dir": str(self.issue_dir),
            "issue_file": str(self.issue_file),
            "relationship_location": str(self.relationship_location),
        }


class GitHubIssueCache:
    """Repo-local cache for GitHub issue read projections."""

    def __init__(self, root: Path, *, configured_repo: GitHubRepository | None = None):
        self.root = root
        self.configured_repo = configured_repo

    @classmethod
    def for_project(
        cls,
        project: Path,
        *,
        configured_repo: GitHubRepository | None = None,
    ) -> GitHubIssueCache:
        return cls(
            project.expanduser().resolve(strict=False) / CACHE_ROOT_NAME,
            configured_repo=configured_repo,
        )

    def issue_dir(self, repo: GitHubRepository, issue: int | str) -> Path:
        if self.configured_repo is None or _same_github_repo(repo, self.configured_repo):
            return self.root / "issues" / normalize_issue_number(issue)
        return (
            self.root
            / _safe_path_segment(repo.host)
            / _safe_path_segment(repo.owner)
            / _safe_path_segment(repo.name)
            / "issues"
            / normalize_issue_number(issue)
        )

    def issue_file(self, repo: GitHubRepository, issue: int | str) -> Path:
        return self.issue_dir(repo, issue) / "issue.md"

    def freshness_file(self, repo: GitHubRepository, issue: int | str, target: str) -> Path:
        normalized = _normalize_freshness_target(target)
        if normalized not in {"issue", "comments", "relationships"}:
            raise WorkflowCacheError(f"unsupported freshness target: {target}")
        return self.issue_file(repo, issue)

    def has_issue_projection(self, repo: GitHubRepository, issue: int | str) -> bool:
        return self.issue_file(repo, issue).is_file()

    def comment_files(self, repo: GitHubRepository, issue: int | str) -> list[Path]:
        """Return cached comment files sorted by filename (chronological)."""

        issue_dir = self.issue_dir(repo, issue)
        if not issue_dir.is_dir():
            return []
        return sorted(path for path in issue_dir.glob("comment-*.md") if path.is_file())

    def read_freshness_metadata(
        self,
        repo: GitHubRepository,
        issue: int | str,
        *,
        target: str = "issue",
    ) -> FreshnessMetadata:
        """Read freshness metadata from ``issue.md`` frontmatter for one target."""

        normalized = _normalize_freshness_target(target)
        if normalized not in {"issue", "comments", "relationships"}:
            raise WorkflowCacheError(f"unsupported freshness target: {target}")

        issue_path = self.issue_file(repo, issue)
        if not issue_path.is_file():
            raise WorkflowCacheMiss(f"freshness cache does not exist: {issue_path}")

        frontmatter, _body = _read_frontmatter_markdown(issue_path)
        _require_schema(frontmatter, issue_path)
        issue_source = _normalize_optional(frontmatter.get("updated_at"))
        issue_fetched = _normalize_optional(frontmatter.get("fetched_at"))
        if normalized == "issue":
            source: str | None = issue_source
            fetched: str | None = issue_fetched
        elif normalized == "comments":
            source = self._latest_cached_comment_timestamp(repo, issue) or issue_source
            fetched = issue_fetched
        else:
            block = frontmatter.get(normalized)
            if isinstance(block, Mapping):
                source = _normalize_optional(block.get("updated_at"))
                fetched = _normalize_optional(block.get("fetched_at"))
            elif block is not None:
                raise WorkflowCacheCorrupt(
                    f"{normalized} freshness frontmatter must be a mapping: {issue_path}"
                )
            else:
                source = None
                fetched = None
        return FreshnessMetadata(
            updated_at=source,
            fetched_at=fetched,
            path=issue_path,
            target=normalized,
        )

    def _latest_cached_comment_timestamp(self, repo: GitHubRepository, issue: int | str) -> str | None:
        latest: str | None = None
        for comment_path in self.comment_files(repo, issue):
            try:
                comment_frontmatter, _body = _read_frontmatter_markdown(comment_path)
            except WorkflowCacheError:
                continue
            updated = _normalize_optional(comment_frontmatter.get("updated_at")) or _normalize_optional(
                comment_frontmatter.get("created_at")
            )
            if updated is not None and (latest is None or updated > latest):
                latest = updated
        return latest

    def read_issue(
        self,
        repo: GitHubRepository,
        issue: int | str,
        *,
        include_body: bool = True,
        include_comments: bool = True,
        include_relationships: bool = True,
    ) -> dict[str, Any]:
        """Read a cached issue projection.

        The caller controls whether raw Markdown body files are loaded. Missing or
        malformed projections raise cache-specific errors so provider dispatch can
        treat them as misses.
        """

        issue_path = self.issue_file(repo, issue)
        if not issue_path.is_file():
            raise WorkflowCacheMiss(f"issue cache does not exist: {issue_path}")

        try:
            frontmatter, body = _read_frontmatter_markdown(issue_path)
            _require_schema(frontmatter, issue_path)
            for key in ("title", "state", "state_reason", "labels", "updated_at"):
                if key not in frontmatter:
                    raise WorkflowCacheCorrupt(f"missing issue frontmatter field {key}: {issue_path}")

            labels = frontmatter.get("labels")
            if labels is None:
                labels = []
            if not isinstance(labels, list):
                raise WorkflowCacheCorrupt(f"issue labels must be a list: {issue_path}")

            updated_at = _normalize_optional(frontmatter.get("updated_at"))
            fetched_at = _normalize_optional(frontmatter.get("fetched_at"))
            cache_metadata: dict[str, Any] = {
                "hit": True,
                "issue_file": str(issue_path),
                "fetchedAt": fetched_at,
                "sourceUpdatedAt": updated_at,
            }

            payload: dict[str, Any] = {
                "number": int(normalize_issue_number(issue)),
                "title": str(frontmatter.get("title") or ""),
                "state": frontmatter.get("state"),
                "stateReason": frontmatter.get("state_reason"),
                "labels": [str(label) for label in labels],
                "updatedAt": updated_at,
                "repository": repo.to_json(),
                "cache": cache_metadata,
            }
            projects = _project_items_for_frontmatter(frontmatter.get("projects"))
            if projects:
                payload["projects"] = projects
            if include_body:
                payload["body"] = body
            if include_comments:
                payload["comments"] = self.read_comments(repo, issue, include_body=include_body)["comments"]
            if include_relationships:
                payload["relationships"] = self.read_relationships(repo, issue)
            return payload
        except WorkflowCacheError:
            raise
        except Exception as exc:
            raise WorkflowCacheCorrupt(f"could not read issue cache {issue_path}: {exc}") from exc

    def read_comments(
        self,
        repo: GitHubRepository,
        issue: int | str,
        *,
        include_body: bool = True,
    ) -> dict[str, Any]:
        issue_path = self.issue_file(repo, issue)
        if not issue_path.is_file():
            raise WorkflowCacheMiss(f"comments cache does not exist: {issue_path}")
        frontmatter, _body = _read_frontmatter_markdown(issue_path)
        _require_schema(frontmatter, issue_path)

        result_comments: list[dict[str, Any]] = []
        for comment_path in self.comment_files(repo, issue):
            try:
                comment_frontmatter, comment_body = _read_frontmatter_markdown(comment_path)
            except WorkflowCacheError:
                raise
            except Exception as exc:
                raise WorkflowCacheCorrupt(f"could not read comment cache {comment_path}: {exc}") from exc
            provider_comment_id = comment_frontmatter.get("provider_comment_id")
            author = comment_frontmatter.get("author")
            if provider_comment_id in (None, "") or not author:
                raise WorkflowCacheCorrupt(
                    f"comment cache is missing provider_comment_id or author: {comment_path}"
                )
            created_at = _normalize_optional(comment_frontmatter.get("created_at")) or _timestamp_from_comment_filename(
                comment_path.name
            )
            comment: dict[str, Any] = {
                "id": str(provider_comment_id),
                "author": {"login": str(author)},
                "createdAt": created_at,
            }
            provider_node_id = comment_frontmatter.get("provider_node_id")
            if provider_node_id:
                comment["nodeId"] = str(provider_node_id)
            updated_at = _normalize_optional(comment_frontmatter.get("updated_at"))
            if updated_at is not None:
                comment["updatedAt"] = updated_at
            if include_body:
                comment["body"] = comment_body
            result_comments.append(comment)

        comments_freshness = self.read_freshness_metadata(repo, issue, target="comments")
        return {
            "repository": repo.to_json(),
            "issue": normalize_issue_number(issue),
            "comments": result_comments,
            "cache": {
                "hit": True,
                "issue_file": str(issue_path),
                "fetchedAt": comments_freshness.fetched_at,
                "sourceUpdatedAt": comments_freshness.updated_at,
            },
        }

    def read_relationships(self, repo: GitHubRepository, issue: int | str) -> dict[str, Any]:
        issue_path = self.issue_file(repo, issue)
        frontmatter_current = _read_frontmatter_current_relationships(issue_path)
        if frontmatter_current is None:
            raise WorkflowCacheMiss(f"relationship frontmatter does not exist: {issue_path}")
        data: dict[str, Any] = {"schema_version": SCHEMA_VERSION}
        try:
            freshness = self.read_freshness_metadata(repo, issue, target="relationships")
        except WorkflowCacheError:
            freshness = None
        if freshness is not None:
            data["updated_at"] = freshness.updated_at
            data["fetched_at"] = freshness.fetched_at
        data.update(frontmatter_current)
        return data

    def write_relationships_projection(
        self,
        repo: GitHubRepository,
        issue: int | str,
        relationship_payload: Mapping[str, Any],
        *,
        fetched_at: str | None = None,
    ) -> Path:
        """Write only the current relationship projection for one issue."""

        now = fetched_at or _utc_now()
        issue_number = normalize_issue_number(issue)
        issue_path = self.issue_file(repo, issue_number)
        if not issue_path.is_file():
            raise WorkflowCacheMiss(f"issue cache does not exist: {issue_path}")
        current = _relationships_from_issue(relationship_payload)
        updated_at = _normalize_optional(
            relationship_payload.get("updatedAt") or relationship_payload.get("updated_at")
        ) or now
        self._update_issue_frontmatter(
            issue_path,
            relationships_current=current,
            relationships_updated_at=updated_at,
            relationships_fetched_at=now,
        )
        return issue_path

    def write_issue_bundle(
        self,
        repo: GitHubRepository,
        issue: Mapping[str, Any],
        *,
        fetched_at: str | None = None,
    ) -> CacheWriteResult:
        """Write issue, comments, and relationships projections atomically per file."""

        issue_number = normalize_issue_number(issue.get("number") or issue.get("issue") or "")
        now = fetched_at or _utc_now()
        issue_dir = self.issue_dir(repo, issue_number)
        issue_dir.mkdir(parents=True, exist_ok=True)
        updated_at = _normalize_optional(issue.get("updatedAt") or issue.get("updated_at")) or now
        current_relationships = _relationships_from_issue(issue)

        if _has_comment_projection_payload(issue):
            self._write_comment_files(repo, issue_number, issue, fetched_at=now)

        issue_frontmatter: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "title": str(issue.get("title") or ""),
            "state": _normalize_state(issue.get("state")),
            "state_reason": _normalize_state_reason(issue.get("stateReason") or issue.get("state_reason")),
            "labels": _label_names(issue.get("labels")),
            "updated_at": updated_at,
            "fetched_at": now,
        }
        projects = _project_items_for_frontmatter(issue.get("projectItems") or issue.get("projects"))
        if projects:
            issue_frontmatter["projects"] = projects
        issue_frontmatter["relationships"] = _relationship_frontmatter_block(
            current=current_relationships,
            updated_at=updated_at,
            fetched_at=now,
        )

        issue_path = self.issue_file(repo, issue_number)
        _atomic_write_text(issue_path, _format_markdown(issue_frontmatter, str(issue.get("body") or "")))

        return CacheWriteResult(
            issue_dir=issue_dir,
            issue_file=issue_path,
            relationship_location=issue_path,
        )

    def _write_comment_files(
        self,
        repo: GitHubRepository,
        issue_number: str,
        issue: Mapping[str, Any],
        *,
        fetched_at: str,
    ) -> None:
        """Write flat ``comment-*.md`` files; comments freshness is derived on read."""

        issue_dir = self.issue_dir(repo, issue_number)
        issue_dir.mkdir(parents=True, exist_ok=True)
        raw_comments = _comments_from_issue(issue)
        expected_files: set[str] = set()

        for position, comment in enumerate(raw_comments, start=1):
            provider_comment_id, provider_node_id = _comment_ids(comment, fallback=str(position))
            created_at = _normalize_optional(comment.get("createdAt") or comment.get("created_at")) or fetched_at
            updated_at = _normalize_optional(comment.get("updatedAt") or comment.get("updated_at")) or created_at
            author = _author_login(comment.get("author"))
            file_name = f"comment-{_compact_timestamp(created_at)}-{_safe_file_segment(provider_comment_id)}.md"
            expected_files.add(file_name)

            comment_frontmatter: dict[str, Any] = {
                "author": author,
                "provider_comment_id": provider_comment_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
            if provider_node_id:
                comment_frontmatter["provider_node_id"] = provider_node_id

            _atomic_write_text(
                issue_dir / file_name,
                _format_markdown(comment_frontmatter, str(comment.get("body") or "")),
            )

        for path in issue_dir.glob("comment-*.md"):
            if path.name not in expected_files:
                path.unlink()

    def _update_issue_frontmatter(
        self,
        issue_path: Path,
        *,
        relationships_current: Mapping[str, Any] | None = None,
        relationships_updated_at: str | None = None,
        relationships_fetched_at: str | None = None,
    ) -> None:
        frontmatter, body = _read_frontmatter_markdown(issue_path)
        existing_relationships = _frontmatter_relationship_block(frontmatter, issue_path, create=True)
        if relationships_current is None:
            relationships_current = existing_relationships
        if relationships_updated_at is None:
            relationships_updated_at = _normalize_optional(
                existing_relationships.get("updated_at")
            )
        if relationships_fetched_at is None:
            relationships_fetched_at = _normalize_optional(existing_relationships.get("fetched_at"))
        frontmatter["relationships"] = _relationship_frontmatter_block(
            current=relationships_current,
            updated_at=relationships_updated_at,
            fetched_at=relationships_fetched_at,
        )
        _atomic_write_text(issue_path, _format_markdown(frontmatter, body))


def _frontmatter_relationship_block(
    frontmatter: dict[str, Any],
    path: Path,
    *,
    create: bool,
) -> dict[str, Any] | None:
    raw = frontmatter.get("relationships")
    if raw is None:
        if not create:
            return None
        raw = {}
        frontmatter["relationships"] = raw
    if not isinstance(raw, dict):
        raise WorkflowCacheCorrupt(f"issue relationships frontmatter must be a mapping: {path}")
    return raw


def _read_frontmatter_current_relationships(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    frontmatter, _body = _read_frontmatter_markdown(path)
    relationships = _frontmatter_relationship_block(frontmatter, path, create=False)
    if relationships is None:
        return None
    return _relationships_from_issue(relationships)


def _relationship_frontmatter_block(
    *,
    current: Mapping[str, Any],
    updated_at: str | None,
    fetched_at: str | None,
) -> dict[str, Any]:
    block: dict[str, Any] = {}
    if updated_at is not None:
        block["updated_at"] = updated_at
    if fetched_at is not None:
        block["fetched_at"] = fetched_at
    block.update(_compact_relationships_for_frontmatter(current))
    return block


def _compact_relationships_for_frontmatter(current: Mapping[str, Any]) -> dict[str, Any]:
    """Return the human-authored relationship projection stored in issue frontmatter."""

    compact: dict[str, Any] = {}

    parent = _compact_relationship_ref(
        current.get("parent") or current.get("parentIssue") or current.get("parent_issue")
    )
    if parent is not None:
        compact["parent"] = parent

    children = _compact_relationship_refs(
        current.get("children") or current.get("subIssues") or current.get("sub_issues")
    )
    if children:
        compact["children"] = children

    dependencies = current.get("dependencies")
    blocked_by = blocking = None
    if isinstance(dependencies, Mapping):
        blocked_by = dependencies.get("blocked_by") or dependencies.get("blockedBy")
        blocking = dependencies.get("blocking") or dependencies.get("blocks")
    blocked_by = blocked_by or current.get("blocked_by") or current.get("blockedBy")
    blocking = blocking or current.get("blocking") or current.get("blocks")
    blocked_by_refs = _compact_relationship_refs(blocked_by)
    if blocked_by_refs:
        compact["blocked_by"] = blocked_by_refs
    blocking_refs = _compact_relationship_refs(blocking)
    if blocking_refs:
        compact["blocking"] = blocking_refs

    related = _compact_relationship_refs(current.get("related"))
    if related:
        compact["related"] = related

    return compact


def _compact_relationship_refs(value: Any) -> list[int | str]:
    if value is None:
        return []
    if isinstance(value, Mapping):
        nodes = value.get("nodes")
        if isinstance(nodes, list):
            return [ref for item in nodes if (ref := _compact_relationship_ref(item)) is not None]
        ref = _compact_relationship_ref(value)
        return [ref] if ref is not None else []
    if isinstance(value, list | tuple | set):
        return [ref for item in value if (ref := _compact_relationship_ref(item)) is not None]
    ref = _compact_relationship_ref(value)
    return [ref] if ref is not None else []


def _compact_relationship_ref(value: Any) -> int | str | None:
    if value is None:
        return None
    raw = value
    if isinstance(value, Mapping):
        raw = value.get("number") or value.get("issue") or value.get("target_ref") or value.get("target") or value.get("id")
        if raw is None:
            return None
    try:
        return int(normalize_issue_number(raw))
    except Exception:
        text = str(raw).strip()
        return text or None




def _project_items_for_frontmatter(value: Any) -> list[dict[str, Any]]:
    items = _project_item_list(value)
    projects: list[dict[str, Any]] = []
    for item in items:
        project = item.get("project")
        project_data = project if isinstance(project, Mapping) else item
        entry: dict[str, Any] = {}

        owner = _project_owner(project_data) or _project_owner(item)
        if owner:
            entry["owner"] = owner
        number = _project_scalar(project_data, "number", "projectNumber")
        if number is not None:
            try:
                entry["number"] = int(str(number))
            except ValueError:
                entry["number"] = str(number)
        title = _project_scalar(project_data, "title", "name", "projectTitle")
        if title is not None:
            entry["title"] = str(title)
        url = _project_scalar(project_data, "url", "projectUrl")
        if url is not None:
            entry["url"] = str(url)
        item_id = _project_scalar(item, "id", "node_id", "nodeId", "item_id", "itemId")
        if item_id is not None:
            entry["item_id"] = str(item_id)
        status = _project_item_status(item)
        if status is not None:
            entry["status"] = status

        if entry:
            projects.append(entry)
    return projects


def _project_item_list(value: Any) -> list[Mapping[str, Any]]:
    if value is None:
        return []
    if isinstance(value, Mapping):
        nodes = value.get("nodes")
        if isinstance(nodes, list):
            return [item for item in nodes if isinstance(item, Mapping)]
        return [value]
    if isinstance(value, list | tuple):
        return [item for item in value if isinstance(item, Mapping)]
    return []


def _project_scalar(value: Mapping[str, Any], *keys: str) -> Any:
    for key in keys:
        raw = value.get(key)
        if raw is not None and str(raw).strip():
            return raw
    return None


def _project_owner(value: Mapping[str, Any]) -> str | None:
    raw_owner = value.get("owner")
    if isinstance(raw_owner, Mapping):
        owner = _project_scalar(raw_owner, "login", "name")
        return str(owner) if owner is not None else None
    if raw_owner is not None and str(raw_owner).strip():
        return str(raw_owner)
    return None


def _project_item_status(item: Mapping[str, Any]) -> str | None:
    direct = item.get("status")
    if isinstance(direct, Mapping):
        value = _project_scalar(direct, "name", "title", "value")
        return str(value) if value is not None else None
    if direct is not None and str(direct).strip():
        return str(direct)

    field_values = item.get("fieldValues") or item.get("field_values")
    for field_value in _project_item_list(field_values):
        field = field_value.get("field")
        field_name = None
        if isinstance(field, Mapping):
            field_name = _project_scalar(field, "name")
        elif field is not None:
            field_name = field
        if str(field_name or "").strip().lower() != "status":
            continue
        status = _project_scalar(field_value, "name", "text", "value", "title")
        if status is not None:
            return str(status)
    return None


def _comments_from_issue(issue: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    comments = issue.get("comments") or []
    if isinstance(comments, Mapping):
        nodes = comments.get("nodes")
        if isinstance(nodes, list):
            comments = nodes
    if not isinstance(comments, list):
        return []
    return [item for item in comments if isinstance(item, Mapping)]


def _has_comment_projection_payload(issue: Mapping[str, Any]) -> bool:
    """Return true when the provider payload explicitly carries comments.

    Some targeted provider reads omit the ``comments`` field. Treat that as
    unknown comment state and preserve any existing comment projection instead
    of overwriting it with an empty layout.
    """

    return "comments" in issue


def _comment_ids(comment: Mapping[str, Any], *, fallback: str) -> tuple[str, str | None]:
    for key in ("databaseId", "databaseID", "database_id"):
        value = comment.get(key)
        if value is not None:
            return str(value), _node_id(comment)

    url = str(comment.get("url") or "")
    match = re.search(r"issuecomment-(\d+)", url)
    if match:
        return match.group(1), _node_id(comment)

    raw_id = comment.get("id")
    if raw_id is not None:
        text = str(raw_id)
        if text.isdigit():
            return text, _node_id(comment)
        return text, text

    return fallback, _node_id(comment)


def _node_id(comment: Mapping[str, Any]) -> str | None:
    for key in ("nodeId", "nodeID", "node_id"):
        value = comment.get(key)
        if value:
            return str(value)
    raw_id = comment.get("id")
    if raw_id is not None and not str(raw_id).isdigit():
        return str(raw_id)
    return None


def _author_login(value: Any) -> str:
    if isinstance(value, Mapping):
        for key in ("login", "name", "username", "displayName"):
            raw = value.get(key)
            if raw:
                return str(raw)
    if value:
        return str(value)
    return "unknown"


def _latest_comment_timestamp(comments: list[Mapping[str, Any]]) -> str | None:
    values = [
        str(value)
        for comment in comments
        for value in (comment.get("updatedAt"), comment.get("updated_at"), comment.get("createdAt"), comment.get("created_at"))
        if value
    ]
    if not values:
        return None
    return max(values)


def _relationships_from_issue(issue: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}

    parent = _relationship_item(
        issue.get("parent") or issue.get("parentIssue") or issue.get("parent_issue")
    )
    if parent:
        result["parent"] = parent

    children = _relationship_items(
        issue.get("children") or issue.get("subIssues") or issue.get("sub_issues")
    )
    if children:
        result["children"] = children

    dependencies = issue.get("dependencies")
    blocked_by = blocking = None
    if isinstance(dependencies, Mapping):
        blocked_by = dependencies.get("blocked_by") or dependencies.get("blockedBy")
        blocking = dependencies.get("blocking") or dependencies.get("blocks")
    blocked_by = blocked_by or issue.get("blocked_by") or issue.get("blockedBy")
    blocking = blocking or issue.get("blocking") or issue.get("blocks")
    blocked_by_items = _relationship_items(blocked_by)
    if blocked_by_items:
        result["blocked_by"] = blocked_by_items
    blocking_items = _relationship_items(blocking)
    if blocking_items:
        result["blocking"] = blocking_items

    related = _relationship_items(issue.get("related"))
    if related:
        result["related"] = related

    return result


def _relationship_items(value: Any) -> list[dict[str, Any]]:
    if value is None:
        return []
    if isinstance(value, Mapping):
        nodes = value.get("nodes")
        if isinstance(nodes, list):
            return [_relationship_item(item) for item in nodes if _relationship_item(item)]
        item = _relationship_item(value)
        return [item] if item else []
    if isinstance(value, list | tuple | set):
        result: list[dict[str, Any]] = []
        for item in value:
            normalized = _relationship_item(item)
            if normalized:
                result.append(normalized)
        return result
    item = _relationship_item(value)
    return [item] if item else []


def _relationship_item(value: Any) -> dict[str, Any] | None:
    if value is None:
        return None
    if isinstance(value, Mapping):
        number = value.get("number") or value.get("issue") or value.get("id")
        if number is None:
            return None
        item: dict[str, Any] = {"number": int(normalize_issue_number(number))}
        if value.get("title") is not None:
            item["title"] = str(value.get("title"))
        if value.get("state") is not None:
            item["state"] = _normalize_state(value.get("state"))
        state_reason = value.get("stateReason") or value.get("state_reason")
        item["state_reason"] = _normalize_state_reason(state_reason)
        return item
    try:
        return {"number": int(normalize_issue_number(value))}
    except Exception:
        return None


def _compact_timestamp(value: str) -> str:
    normalized = value.strip()
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})", normalized)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}T{match.group(4)}{match.group(5)}{match.group(6)}Z"
    return _safe_file_segment(normalized) or "unknown-time"


def _timestamp_from_comment_filename(file_name: str) -> str | None:
    match = re.match(r"^comment-(\d{4}-\d{2}-\d{2})T(\d{2})(\d{2})(\d{2})Z-", file_name)
    if not match:
        return None
    return f"{match.group(1)}T{match.group(2)}:{match.group(3)}:{match.group(4)}Z"


def _same_github_repo(left: GitHubRepository, right: GitHubRepository) -> bool:
    return (
        left.host.lower(),
        left.owner.lower(),
        left.name.lower(),
    ) == (
        right.host.lower(),
        right.owner.lower(),
        right.name.lower(),
    )
