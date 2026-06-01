#!/usr/bin/env python3
"""Generated Jira issue snapshot renderer."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

def jira_relationship_fingerprint_block(relationships: Mapping[str, Any]) -> dict[str, Any]:
    """Relationship fields used for the Jira ``relationships`` fingerprint.

    Reuses the relationship block builder but strips the freshness timestamps so
    cache-write and write-back-check compute an identical value for the same
    provider state.
    """

    if not isinstance(relationships, Mapping):
        return {}
    block = _build_relationship_frontmatter_block(relationships, updated_at=None, fetched_at="")
    block.pop("updated_at", None)
    block.pop("fetched_at", None)
    return block


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


def _jira_person_display_name(value: Any) -> str | None:
    """Resolve the best Jira person display name from a user mapping.

    Mirrors the fallback chain Jira's REST API documents for user objects:
    ``displayName`` is preferred, then ``name`` (Data Center username),
    then ``key``, then ``accountId`` (Cloud). Returns ``None`` when the
    input is not a mapping or carries none of these keys with a truthy
    value.
    """

    if isinstance(value, Mapping):
        for key in ("displayName", "name", "key", "accountId"):
            raw = value.get(key)
            if raw:
                return str(raw)
    return None


def _normalize_optional(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
