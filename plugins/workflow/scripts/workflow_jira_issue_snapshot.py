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
    updated_at: str | None,
    fetched_at: str,
) -> str:
    """Render a Jira issue projection as YAML frontmatter plus issue body.

    Metadata, relationships, and remote links live in the frontmatter; the
    Markdown body is the description verbatim. Comments live in sibling
    ``comment-*.md`` files.
    """

    frontmatter = build_jira_snapshot_frontmatter(
        issue,
        updated_at=updated_at,
        fetched_at=fetched_at,
    )
    body = str(issue.get("body") or "")
    return _format_markdown(frontmatter, body)


def build_jira_snapshot_frontmatter(
    issue: Mapping[str, Any],
    *,
    updated_at: str | None,
    fetched_at: str,
) -> dict[str, Any]:
    """Return the frontmatter mapping written into issue.md."""

    frontmatter: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "title": str(issue.get("title") or ""),
        "state": _normalize_optional(issue.get("state")),
        "state_reason": _normalize_optional(issue.get("stateReason")),
        "labels": [str(label) for label in issue.get("labels") or []],
        "updated_at": updated_at,
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
        updated_at=updated_at,
        fetched_at=fetched_at,
    )
    if relationship_block:
        frontmatter["relationships"] = relationship_block

    return frontmatter


_RESERVED_WORKFLOW_KEYS = {"parent", "issue_links", "external_links"}


def _build_relationship_frontmatter_block(
    relationships: Mapping[str, Any],
    *,
    updated_at: str | None,
    fetched_at: str,
) -> dict[str, Any]:
    workflow = relationships.get("workflow") if isinstance(relationships.get("workflow"), Mapping) else {}
    assert isinstance(workflow, Mapping)

    fields: dict[str, Any] = {}

    parent_ref = _workflow_ref(workflow.get("parent"))
    if parent_ref:
        fields["parent"] = parent_ref

    for key, value in workflow.items():
        if key in _RESERVED_WORKFLOW_KEYS:
            continue
        refs = _workflow_refs(value)
        if refs:
            fields[key] = refs

    unmapped_links = _compact_unmapped_issue_links(workflow.get("issue_links"))
    if unmapped_links:
        fields["issue_links"] = unmapped_links

    if not fields:
        return {}

    block: dict[str, Any] = {}
    if updated_at is not None:
        block["updated_at"] = updated_at
    block["fetched_at"] = fetched_at
    block.update(fields)
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


def _compact_unmapped_issue_links(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    entries: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, Mapping):
            continue
        target = _workflow_ref(item.get("target"))
        if target is None:
            continue
        entry: dict[str, Any] = {}
        link_type = _normalize_optional(item.get("type"))
        if link_type is not None:
            entry["type"] = link_type
        direction = _normalize_optional(item.get("direction"))
        if direction is not None:
            entry["direction"] = direction
        entry["target"] = target
        entries.append(entry)
    return entries


def _normalize_optional(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
