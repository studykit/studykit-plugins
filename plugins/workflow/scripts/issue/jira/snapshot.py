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

_JIRA_MARKDOWN_RESERVED = {"parent", "children", "issue_links", "external_links"}


def render_jira_relationships_markdown(
    relationships: Mapping[str, Any], *, issue_key: str
) -> str:
    """Render the normalized Jira relationship block as readable markdown.

    Jira keeps its machine source in the native ``issue.json`` /
    ``remote-links.json``; this is the human/LLM view written to
    ``relationships.md`` so an agent can follow linked issues from a fetch.
    The sections follow Jira's relationship model (parent / children / mapped
    link buckets / unmapped issue links / external links) and intentionally
    differ from GitHub's projection.
    """

    workflow = relationships.get("workflow") if isinstance(relationships, Mapping) else None
    workflow = workflow if isinstance(workflow, Mapping) else {}

    lines: list[str] = [f"# Relationships — {issue_key}", ""]
    rendered_any = False

    parent = _jira_ref_text(workflow.get("parent"))
    if parent:
        rendered_any = True
        lines.extend(["## Parent", f"- {parent}", ""])

    children = _jira_ref_texts(workflow.get("children"))
    if children:
        rendered_any = True
        lines.append("## Children")
        lines.extend(f"- {child}" for child in children)
        lines.append("")

    for name in sorted(workflow):
        if name in _JIRA_MARKDOWN_RESERVED:
            continue
        refs = _jira_ref_texts(workflow.get(name))
        if refs:
            rendered_any = True
            lines.append(f"## {name}")
            lines.extend(f"- {ref}" for ref in refs)
            lines.append("")

    issue_link_bullets = _jira_issue_link_bullets(workflow.get("issue_links"))
    if issue_link_bullets:
        rendered_any = True
        lines.append("## Issue links")
        lines.extend(issue_link_bullets)
        lines.append("")

    external_bullets = _jira_external_link_bullets(workflow.get("external_links"))
    if external_bullets:
        rendered_any = True
        lines.append("## External links")
        lines.extend(external_bullets)
        lines.append("")

    if not rendered_any:
        lines.extend(["_No linked issues._", ""])
    return "\n".join(lines).rstrip("\n") + "\n"


def _jira_ref_text(value: Any) -> str | None:
    if isinstance(value, Mapping):
        ref = value.get("key") or value.get("issue") or value.get("id")
        if not ref:
            return None
        title = _normalize_optional(value.get("title"))
        return f"{ref} — {title}" if title else str(ref)
    return _workflow_ref(value)


def _jira_ref_texts(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    refs: list[str] = []
    for item in value:
        text = _jira_ref_text(item)
        if text:
            refs.append(text)
    return refs


def _jira_issue_link_bullets(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    bullets: list[str] = []
    for link in value:
        if not isinstance(link, Mapping):
            continue
        target = _jira_ref_text(link.get("target"))
        if not target:
            continue
        label = _normalize_optional(link.get("type")) or "link"
        direction = _normalize_optional(link.get("direction"))
        suffix = f" ({direction})" if direction else ""
        bullets.append(f"- {label} → {target}{suffix}")
    return bullets


def _jira_external_link_bullets(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    bullets: list[str] = []
    for link in value:
        if not isinstance(link, Mapping):
            continue
        url = _normalize_optional(link.get("url"))
        title = _normalize_optional(link.get("title")) or url
        if url:
            bullets.append(f"- [{title}]({url})")
        elif title:
            bullets.append(f"- {title}")
    return bullets


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
