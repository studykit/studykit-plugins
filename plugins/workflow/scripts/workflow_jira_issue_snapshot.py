#!/usr/bin/env python3
"""Generated Jira issue snapshot renderer."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from workflow_cache import (
    SCHEMA_VERSION,
    _format_markdown,
)


def render_jira_snapshot(
    issue: Mapping[str, Any],
    *,
    source_updated_at: str | None,
    fetched_at: str,
) -> str:
    """Render a Jira issue projection as YAML frontmatter plus issue body.

    Metadata, relationships, and remote links live in the frontmatter; the
    Markdown body is the description verbatim. Comments live in sibling
    ``comment-*.md`` files.
    """

    frontmatter = build_jira_snapshot_frontmatter(
        issue,
        source_updated_at=source_updated_at,
        fetched_at=fetched_at,
    )
    body = str(issue.get("body") or "")
    return _format_markdown(frontmatter, body)


def build_jira_snapshot_frontmatter(
    issue: Mapping[str, Any],
    *,
    source_updated_at: str | None,
    fetched_at: str,
) -> dict[str, Any]:
    """Return the frontmatter mapping written into issue.md."""

    frontmatter: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "title": str(issue.get("title") or ""),
        "state": _normalize_optional(issue.get("state")),
        "state_reason": _normalize_optional(issue.get("stateReason")),
        "labels": [str(label) for label in issue.get("labels") or []],
        "source_updated_at": source_updated_at,
        "fetched_at": fetched_at,
        "url": _normalize_optional(issue.get("url")),
    }

    relationships = issue.get("relationships") if isinstance(issue.get("relationships"), Mapping) else {}
    assert isinstance(relationships, Mapping)

    remote_links = _compact_remote_links(relationships.get("remote_links"))
    if remote_links:
        frontmatter["remote_links"] = remote_links

    relationship_block = _build_relationship_frontmatter_block(
        relationships,
        source_updated_at=source_updated_at,
        fetched_at=fetched_at,
    )
    if relationship_block:
        frontmatter["relationships"] = relationship_block

    return frontmatter


def _build_relationship_frontmatter_block(
    relationships: Mapping[str, Any],
    *,
    source_updated_at: str | None,
    fetched_at: str,
) -> dict[str, Any]:
    workflow = relationships.get("workflow") if isinstance(relationships.get("workflow"), Mapping) else {}
    assert isinstance(workflow, Mapping)

    current: dict[str, Any] = {}

    parent_ref = _workflow_ref(workflow.get("parent"))
    if parent_ref:
        current["parent"] = parent_ref

    children = _workflow_refs(workflow.get("children"))
    if children:
        current["children"] = children

    dependencies = workflow.get("dependencies") if isinstance(workflow.get("dependencies"), Mapping) else {}
    assert isinstance(dependencies, Mapping)
    dependency_block: dict[str, Any] = {}
    blocked_by = _workflow_refs(dependencies.get("blocked_by"))
    if blocked_by:
        dependency_block["blocked_by"] = blocked_by
    blocking = _workflow_refs(dependencies.get("blocking"))
    if blocking:
        dependency_block["blocking"] = blocking
    if dependency_block:
        current["dependencies"] = dependency_block

    related = _workflow_refs(workflow.get("related"))
    if related:
        current["related"] = related

    issue_links = _compact_issue_links(relationships.get("issue_links"))
    if issue_links:
        current["issue_links"] = issue_links

    if not current:
        return {}

    block: dict[str, Any] = {}
    if source_updated_at is not None:
        block["source_updated_at"] = source_updated_at
    block["fetched_at"] = fetched_at
    block["current"] = current
    return block


def _workflow_refs(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    refs: list[str] = []
    for item in value:
        ref = _workflow_ref(item)
        if ref is not None:
            refs.append(ref)
    return refs


def _workflow_ref(value: Any) -> str | None:
    if isinstance(value, Mapping):
        for key in ("key", "issue", "id"):
            raw = value.get(key)
            if raw:
                return str(raw)
        return None
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _compact_remote_links(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    links: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, Mapping):
            continue
        entry: dict[str, Any] = {}
        title = _normalize_optional(item.get("title"))
        if title is not None:
            entry["title"] = title
        url = _normalize_optional(item.get("url"))
        if url is not None:
            entry["url"] = url
        relationship = _normalize_optional(item.get("relationship"))
        if relationship is not None:
            entry["relationship"] = relationship
        global_id = _normalize_optional(item.get("global_id"))
        if global_id is not None:
            entry["global_id"] = global_id
        if entry:
            links.append(entry)
    return links


def _compact_issue_links(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    entries: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, Mapping):
            continue
        link_type = _normalize_optional(item.get("type"))
        outward_issue = item.get("outward_issue")
        inward_issue = item.get("inward_issue")
        if isinstance(outward_issue, Mapping):
            target = _workflow_ref(outward_issue)
            direction = "outward"
        elif isinstance(inward_issue, Mapping):
            target = _workflow_ref(inward_issue)
            direction = "inward"
        else:
            continue
        if target is None:
            continue
        entry: dict[str, Any] = {}
        if link_type is not None:
            entry["type"] = link_type
        entry["direction"] = direction
        entry["target"] = target
        entries.append(entry)
    return entries


def _normalize_optional(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
