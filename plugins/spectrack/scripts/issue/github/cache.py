#!/usr/bin/env python3
"""GitHub Issues cache carrier for workflow provider projections."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
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
    _dump_json,
    _format_markdown,
    _label_names,
    _normalize_freshness_target,
    _normalize_optional,
    _normalize_state,
    _normalize_state_reason,
    _read_frontmatter_markdown,
    _read_json_mapping,
    _require_schema,
    _safe_file_segment,
    _safe_path_segment,
    _utc_now,
    comments_fingerprint,
    content_fingerprint,
    relationships_fingerprint,
)
from issue.github.gh import GitHubRepository, normalize_issue_number


_COMMENT_FILENAME_RE = re.compile(r"^comment-.*\.md$")

# The fingerprint builders (``content_fingerprint`` / ``relationships_fingerprint``
# / ``comments_fingerprint``) are shared from ``issue.cache`` so cache writes
# and provider write-back checks normalize identically. The per-comment item
# extraction below is GitHub-specific (provider comment ids).


def _comment_fingerprint_items(source: Mapping[str, Any]) -> list[dict[str, str | None]]:
    """Stable per-comment identity+revision tuples for the comments fingerprint."""

    items: list[dict[str, str | None]] = []
    for position, comment in enumerate(_comments_from_issue(source), start=1):
        provider_comment_id, _node = _comment_ids(comment, fallback=str(position))
        revision = _normalize_optional(
            comment.get("updatedAt") or comment.get("updated_at")
        ) or _normalize_optional(comment.get("createdAt") or comment.get("created_at"))
        items.append({"id": str(provider_comment_id), "updated_at": revision})
    items.sort(key=lambda item: (item["id"], item["updated_at"] or ""))
    return items


def is_github_issue_cache_body_path(path: Path, project: Path) -> bool:
    """Return whether ``path`` is a read-only GitHub issue content projection.

    Recognizes the ``issue.md`` body, the readable ``state.md`` and
    ``relation.md`` projections, and any ``comment-*.md`` sibling in the flat
    per-issue directory layout. Configured-repo issues sit at
    ``.spectrack-cache/issues/<n>/`` and external repos are namespaced under
    ``.spectrack-cache/<host>/<owner>/<repo>/issues/<n>/``. The internal
    ``.meta.json`` / ``.relation.json`` machine sources are matched by
    :func:`is_github_issue_cache_meta_path`.
    """

    name = path.name
    if name not in {"issue.md", "state.md", "relation.md"} and not _COMMENT_FILENAME_RE.match(name):
        return False
    return _github_issue_cache_dir_match(path, project)


def is_github_issue_cache_meta_path(path: Path, project: Path) -> bool:
    """Return whether ``path`` is an internal GitHub cache projection.

    Covers the ``.meta.json`` bookkeeping file and the ``.relation.json``
    machine source. Both are dotfiles the dispatchers maintain; readers consume
    ``issue.md`` / ``relation.md`` instead.
    """

    if path.name not in {".meta.json", ".relation.json"}:
        return False
    return _github_issue_cache_dir_match(path, project)


def _github_issue_cache_dir_match(path: Path, project: Path) -> bool:
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
    state_file: Path
    meta_file: Path
    relationship_location: Path

    def to_json(self) -> dict[str, str]:
        return {
            "issue_dir": str(self.issue_dir),
            "issue_file": str(self.issue_file),
            "state_file": str(self.state_file),
            "meta_file": str(self.meta_file),
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

    def meta_file(self, repo: GitHubRepository, issue: int | str) -> Path:
        return self.issue_dir(repo, issue) / ".meta.json"

    def state_file(self, repo: GitHubRepository, issue: int | str) -> Path:
        return self.issue_dir(repo, issue) / "state.md"

    def relationships_file(self, repo: GitHubRepository, issue: int | str) -> Path:
        return self.issue_dir(repo, issue) / "relation.md"

    def relationships_source_file(self, repo: GitHubRepository, issue: int | str) -> Path:
        return self.issue_dir(repo, issue) / ".relation.json"

    def freshness_file(self, repo: GitHubRepository, issue: int | str, target: str) -> Path:
        normalized = _normalize_freshness_target(target)
        if normalized not in {"issue", "comments", "relationships"}:
            raise WorkflowCacheError(f"unsupported freshness target: {target}")
        return self.meta_file(repo, issue)

    def has_issue_projection(self, repo: GitHubRepository, issue: int | str) -> bool:
        return self.meta_file(repo, issue).is_file()

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
        """Read the per-target fingerprint from ``.meta.json``."""

        normalized = _normalize_freshness_target(target)
        if normalized not in {"issue", "comments", "relationships"}:
            raise WorkflowCacheError(f"unsupported freshness target: {target}")

        meta_path = self.meta_file(repo, issue)
        if not meta_path.is_file():
            raise WorkflowCacheMiss(f"freshness cache does not exist: {meta_path}")

        meta = _read_json_mapping(meta_path)
        _require_schema(meta, meta_path)
        fingerprints = meta.get("fingerprints")
        if not isinstance(fingerprints, Mapping):
            raise WorkflowCacheCorrupt(f"missing fingerprints in {meta_path}")
        key = "content" if normalized == "issue" else normalized
        return FreshnessMetadata(
            fingerprint=_normalize_optional(fingerprints.get(key)),
            path=meta_path,
            target=normalized,
        )

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

        meta_path = self.meta_file(repo, issue)
        if not meta_path.is_file():
            raise WorkflowCacheMiss(f"issue cache does not exist: {meta_path}")

        try:
            meta = _read_json_mapping(meta_path)
            _require_schema(meta, meta_path)
            for key in ("title", "state", "state_reason", "labels"):
                if key not in meta:
                    raise WorkflowCacheCorrupt(f"missing issue meta field {key}: {meta_path}")

            labels = meta.get("labels")
            if labels is None:
                labels = []
            if not isinstance(labels, list):
                raise WorkflowCacheCorrupt(f"issue labels must be a list: {meta_path}")

            issue_path = self.issue_file(repo, issue)
            cache_metadata: dict[str, Any] = {
                "hit": True,
                "issue_file": str(issue_path),
                "state_file": str(self.state_file(repo, issue)),
                "meta_file": str(meta_path),
            }

            payload: dict[str, Any] = {
                "number": int(normalize_issue_number(issue)),
                "title": str(meta.get("title") or ""),
                "state": meta.get("state"),
                "stateReason": meta.get("state_reason"),
                "labels": [str(label) for label in labels],
                "repository": repo.to_json(),
                "cache": cache_metadata,
            }
            projects = meta.get("projects")
            if projects:
                payload["projects"] = projects
            if include_body:
                payload["body"] = issue_path.read_text(encoding="utf-8") if issue_path.is_file() else ""
            if include_comments:
                payload["comments"] = self.read_comments(repo, issue, include_body=include_body)["comments"]
            if include_relationships:
                payload["relationships"] = self.read_relationships(repo, issue)
            return payload
        except WorkflowCacheError:
            raise
        except Exception as exc:
            raise WorkflowCacheCorrupt(f"could not read issue cache {meta_path}: {exc}") from exc

    def read_comments(
        self,
        repo: GitHubRepository,
        issue: int | str,
        *,
        include_body: bool = True,
    ) -> dict[str, Any]:
        meta_path = self.meta_file(repo, issue)
        if not meta_path.is_file():
            raise WorkflowCacheMiss(f"comments cache does not exist: {meta_path}")
        meta = _read_json_mapping(meta_path)
        _require_schema(meta, meta_path)

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

        return {
            "repository": repo.to_json(),
            "issue": normalize_issue_number(issue),
            "comments": result_comments,
            "cache": {
                "hit": True,
                "issue_file": str(self.issue_file(repo, issue)),
                "meta_file": str(meta_path),
            },
        }

    def read_relationships(self, repo: GitHubRepository, issue: int | str) -> dict[str, Any]:
        rel_path = self.relationships_source_file(repo, issue)
        if not rel_path.is_file():
            raise WorkflowCacheMiss(f"relationships cache does not exist: {rel_path}")
        rel = _read_json_mapping(rel_path)
        _require_schema(rel, rel_path)
        compact = {key: value for key, value in rel.items() if key != "schema_version"}
        data: dict[str, Any] = {"schema_version": SCHEMA_VERSION}
        data.update(_relationships_from_issue(compact))
        return data

    def write_relationships_projection(
        self,
        repo: GitHubRepository,
        issue: int | str,
        relationship_payload: Mapping[str, Any],
    ) -> Path:
        """Rewrite the relationship projection and only the relationships fingerprint.

        The content fingerprint in ``.meta.json`` is left untouched, so a link
        operation can never make a later body write look conflicted.
        """

        issue_number = normalize_issue_number(issue)
        meta_path = self.meta_file(repo, issue_number)
        if not meta_path.is_file():
            raise WorkflowCacheMiss(f"issue cache does not exist: {meta_path}")
        compact = _compact_relationships_for_frontmatter(
            _relationships_from_issue(relationship_payload)
        )
        self._write_relationships_file(repo, issue_number, compact)
        self._update_meta_fingerprint(
            meta_path, "relationships", relationships_fingerprint(compact)
        )
        return self.relationships_file(repo, issue_number)

    def write_issue_bundle(
        self,
        repo: GitHubRepository,
        issue: Mapping[str, Any],
        *,
        fetched_at: str | None = None,
    ) -> CacheWriteResult:
        """Write the body, ``.meta.json``, relationship projection, and comments."""

        issue_number = normalize_issue_number(issue.get("number") or issue.get("issue") or "")
        now = fetched_at or _utc_now()
        issue_dir = self.issue_dir(repo, issue_number)
        issue_dir.mkdir(parents=True, exist_ok=True)
        body = str(issue.get("body") or "")
        compact_relationships = _compact_relationships_for_frontmatter(
            _relationships_from_issue(issue)
        )

        meta_path = self.meta_file(repo, issue_number)
        if _has_comment_projection_payload(issue):
            self._write_comment_files(repo, issue_number, issue, fetched_at=now)
            comments_fp = comments_fingerprint(_comment_fingerprint_items(issue))
        else:
            comments_fp = self._existing_meta_fingerprint(meta_path, "comments")

        issue_path = self.issue_file(repo, issue_number)
        _atomic_write_text(issue_path, body)
        self._write_relationships_file(repo, issue_number, compact_relationships)

        meta: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "title": str(issue.get("title") or ""),
            "state": _normalize_state(issue.get("state")),
            "state_reason": _normalize_state_reason(issue.get("stateReason") or issue.get("state_reason")),
            "assignees": _github_assignees(issue.get("assignees")),
            "labels": _label_names(issue.get("labels")),
            "fingerprints": {
                "content": content_fingerprint(issue.get("title"), body),
                "relationships": relationships_fingerprint(compact_relationships),
                "comments": comments_fp,
            },
        }
        projects = _project_items_for_frontmatter(issue.get("projectItems") or issue.get("projects"))
        if projects:
            meta["projects"] = projects
        _atomic_write_text(meta_path, _dump_json(meta))

        state_path = self.state_file(repo, issue_number)
        _atomic_write_text(
            state_path,
            _render_github_state_markdown(
                title=meta["title"],
                state=meta["state"],
                state_reason=meta["state_reason"],
                assignees=meta["assignees"],
                labels=meta["labels"],
            ),
        )

        return CacheWriteResult(
            issue_dir=issue_dir,
            issue_file=issue_path,
            state_file=state_path,
            meta_file=meta_path,
            relationship_location=self.relationships_file(repo, issue_number),
        )

    def promote_body(
        self,
        repo: GitHubRepository,
        issue: int | str,
        *,
        title: str | None,
        body: str,
    ) -> CacheWriteResult:
        """Reuse a just-written body as the cache projection without re-fetching.

        Safe only when the provider stores the body verbatim (GitHub). Rewrites
        ``issue.md`` and the ``content`` fingerprint (and title) in ``.meta.json``;
        the relationships and comments fingerprints are left untouched. Callers
        must fall back to :meth:`write_issue_bundle` when metadata (labels, state,
        assignees) also changed, since those are not refreshed here.
        """

        issue_number = normalize_issue_number(issue)
        meta_path = self.meta_file(repo, issue_number)
        if not meta_path.is_file():
            raise WorkflowCacheMiss(f"issue cache does not exist: {meta_path}")
        issue_path = self.issue_file(repo, issue_number)
        _atomic_write_text(issue_path, str(body or ""))

        meta = _read_json_mapping(meta_path)
        _require_schema(meta, meta_path)
        if title is not None:
            meta["title"] = str(title or "")
        fingerprints = meta.get("fingerprints")
        if not isinstance(fingerprints, dict):
            fingerprints = {}
        fingerprints["content"] = content_fingerprint(meta.get("title"), body)
        meta["fingerprints"] = fingerprints
        _atomic_write_text(meta_path, _dump_json(meta))

        return CacheWriteResult(
            issue_dir=self.issue_dir(repo, issue_number),
            issue_file=issue_path,
            state_file=self.state_file(repo, issue_number),
            meta_file=meta_path,
            relationship_location=self.relationships_file(repo, issue_number),
        )

    def _write_relationships_file(
        self, repo: GitHubRepository, issue: int | str, compact: Mapping[str, Any]
    ) -> Path:
        # ``.relation.json`` is the machine source ``read_relationships``
        # parses back; ``relation.md`` is the readable projection surfaced
        # to fetch callers and the LLM.
        source_path = self.relationships_source_file(repo, issue)
        data: dict[str, Any] = {"schema_version": SCHEMA_VERSION}
        data.update(compact)
        _atomic_write_text(source_path, _dump_json(data))
        rel_path = self.relationships_file(repo, issue)
        markdown = _render_github_relationships_markdown(issue, compact)
        if markdown is None:
            rel_path.unlink(missing_ok=True)
        else:
            _atomic_write_text(rel_path, markdown)
        return rel_path

    def _update_meta_fingerprint(self, meta_path: Path, key: str, value: str) -> None:
        meta = _read_json_mapping(meta_path)
        _require_schema(meta, meta_path)
        fingerprints = meta.get("fingerprints")
        if not isinstance(fingerprints, dict):
            fingerprints = {}
        fingerprints[key] = value
        meta["fingerprints"] = fingerprints
        _atomic_write_text(meta_path, _dump_json(meta))

    def _existing_meta_fingerprint(self, meta_path: Path, key: str) -> str | None:
        if not meta_path.is_file():
            return None
        try:
            meta = _read_json_mapping(meta_path)
        except WorkflowCacheError:
            return None
        fingerprints = meta.get("fingerprints")
        if not isinstance(fingerprints, Mapping):
            return None
        return _normalize_optional(fingerprints.get(key))

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


# Relationship kinds in display order; the key doubles as the inline label.
_GITHUB_RELATIONSHIP_KINDS: tuple[str, ...] = (
    "parent",
    "children",
    "blocked_by",
    "blocking",
    "related",
)


def _render_github_state_markdown(
    *,
    title: str,
    state: str,
    state_reason: str | None,
    assignees: list[str],
    labels: list[str],
) -> str:
    """Render native GitHub state as a readable ``state.md`` projection.

    Surfaces ``title`` / ``state`` / ``state_reason`` / ``assignees`` /
    ``labels`` so a fetch caller (and the LLM) can read the issue title and
    lifecycle state without opening the internal ``.meta.json``. Frontmatter
    carries the machine-readable fields; the body is empty. Always written.
    """

    frontmatter: dict[str, Any] = {
        "title": title,
        "state": state,
        "state_reason": state_reason,
        "assignees": list(assignees),
        "labels": list(labels),
    }
    return _format_markdown(frontmatter, "")


def _render_github_relationships_markdown(
    issue: int | str, compact: Mapping[str, Any]
) -> str | None:
    """Render the compact relationship projection as concise markdown.

    One line per relationship kind (refs comma-joined) so the LLM can scan
    linked issues at a glance. The machine source stays in
    ``.relation.json``; this is the human/LLM view. Returns ``None`` when the
    issue has no relationships so the caller skips writing ``relation.md``.
    """

    rendered: list[str] = []
    for key in _GITHUB_RELATIONSHIP_KINDS:
        refs = compact.get(key)
        if refs is None:
            continue
        ref_list = refs if isinstance(refs, list) else [refs]
        texts = [_github_relationship_ref_text(ref) for ref in ref_list if ref is not None]
        if texts:
            rendered.append(f"- {key}: {', '.join(texts)}")
    if not rendered:
        return None
    heading = f"#{normalize_issue_number(issue)}"
    return "\n".join([heading, *rendered]) + "\n"


def _github_relationship_ref_text(ref: Any) -> str:
    if isinstance(ref, int):
        return f"#{ref}"
    text = str(ref).strip()
    if text.isdigit():
        return f"#{text}"
    return text


def _compact_relationships_for_frontmatter(current: Mapping[str, Any]) -> dict[str, Any]:
    """Return the compact relationship projection stored in ``.relation.json``."""

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


def _github_person_display_name(value: Any) -> str | None:
    """Resolve the best GitHub user display name from an assignee mapping.

    GitHub user objects always carry ``login``; ``name`` is optional and
    only populated when the user has set a public display name. Prefer
    ``name`` when present so the frontmatter is human-friendly, fall back
    to ``login`` otherwise. Returns ``None`` when the input is not a
    mapping or carries neither key with a truthy value.
    """

    if isinstance(value, Mapping):
        for key in ("name", "login"):
            raw = value.get(key)
            if raw:
                return str(raw)
    return None


def _github_assignees(value: Any) -> list[str]:
    """Project a GitHub assignees list into resolved display names.

    Preserves provider order and skips entries that resolve to ``None``
    (no ``name`` and no ``login``). Returns ``[]`` for missing or
    non-list inputs so the frontmatter always carries a list.
    """

    if not isinstance(value, list):
        return []
    names: list[str] = []
    for item in value:
        resolved = _github_person_display_name(item)
        if resolved is not None:
            names.append(resolved)
    return names


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
