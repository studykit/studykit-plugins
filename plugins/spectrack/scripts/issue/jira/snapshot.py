#!/usr/bin/env python3
"""Generated Jira issue snapshot renderer."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from issue.cache import _format_markdown


def render_jira_state_markdown(
    normalized: Mapping[str, Any], *, issue_key: str
) -> str:
    """Render native Jira state as a readable ``state.md`` projection.

    Surfaces ``status`` / ``type`` / ``resolution`` / ``assignee`` / ``labels``
    so a fetch caller (and the LLM) can read lifecycle state and the issue type
    without opening the internal native ``.issue.json``. Frontmatter carries the
    machine-readable fields; the body is a one-line human summary. Always
    written — every issue has a status.
    """

    status = _normalize_optional(normalized.get("state")) or "unknown"
    issue_type = _normalize_optional(normalized.get("type"))
    # Jira leaves resolution unset until an issue is resolved; mirror the UI's
    # "Unresolved" label (also the JQL token for an empty resolution) instead of null.
    resolution = _normalize_optional(normalized.get("resolution")) or "Unresolved"
    assignee = _jira_person_display_name(normalized.get("assignee"))
    labels = [str(label) for label in normalized.get("labels") or [] if label is not None]
    frontmatter: dict[str, Any] = {
        "status": status,
        "type": issue_type,
        "resolution": resolution,
        "assignee": assignee,
        "labels": labels,
    }
    summary = (
        f"{issue_key} — {issue_type or 'issue'}, {status} ({resolution}), "
        f"assignee {assignee or 'unassigned'}"
    )
    return _format_markdown(frontmatter, summary + "\n")


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


_RESERVED_SPECTRACK_KEYS = {"parent", "issue_links", "external_links"}

_JIRA_MARKDOWN_RESERVED = {"parent", "children", "issue_links", "external_links"}


def render_jira_relationships_markdown(
    relationships: Mapping[str, Any], *, issue_key: str
) -> str | None:
    """Render the normalized Jira relationship block as concise markdown.

    One line per relationship kind (issue keys comma-joined) so an agent can
    follow linked issues from a fetch. Jira keeps its machine source in the
    native ``.issue.json`` / ``.remote-links.json``; this is the human/LLM view.
    The kinds follow Jira's relationship model (parent / children / mapped link
    buckets / unmapped issue links / external links) and intentionally differ
    from GitHub's projection. Returns ``None`` when the issue has no links so
    the caller skips writing ``relation.md``.
    """

    workflow = relationships.get("workflow") if isinstance(relationships, Mapping) else None
    workflow = workflow if isinstance(workflow, Mapping) else {}

    rendered: list[str] = []

    parent = _jira_ref_key(workflow.get("parent"))
    if parent:
        rendered.append(f"- parent: {parent}")

    children = _jira_ref_keys(workflow.get("children"))
    if children:
        rendered.append(f"- children: {', '.join(children)}")

    for name in sorted(workflow):
        if name in _JIRA_MARKDOWN_RESERVED:
            continue
        refs = _jira_ref_keys(workflow.get(name))
        if refs:
            rendered.append(f"- {name}: {', '.join(refs)}")

    rendered.extend(_jira_issue_link_lines(workflow.get("issue_links")))
    rendered.extend(_jira_external_link_lines(workflow.get("external_links")))

    if not rendered:
        return None
    return "\n".join([issue_key, *rendered]) + "\n"


def render_jira_attachments_markdown(
    attachments: Any, *, issue_key: str
) -> str | None:
    """Render the normalized Jira attachment list as concise markdown.

    One line per attachment (``- <id>: <filename> (<size> bytes)``) so an
    agent can see what is attached from a fetch and pass the id to
    ``issue attach get`` for download. Kept in a sibling ``attachment.md``
    rather than ``issue.md`` frontmatter or body so the authored issue
    content stays unpolluted. Returns ``None`` when the issue has no
    attachments so the caller skips writing the file.
    """

    if not isinstance(attachments, list):
        return None
    lines: list[str] = []
    for item in attachments:
        if not isinstance(item, Mapping):
            continue
        attachment_id = _normalize_optional(item.get("id"))
        filename = _normalize_optional(item.get("filename")) or "(unnamed)"
        size = item.get("size")
        size_suffix = f" ({size} bytes)" if isinstance(size, int) else ""
        prefix = f"- {attachment_id}: " if attachment_id else "- "
        lines.append(f"{prefix}{filename}{size_suffix}")
    if not lines:
        return None
    return "\n".join([issue_key, *lines]) + "\n"


def _jira_ref_key(value: Any) -> str | None:
    if isinstance(value, Mapping):
        ref = value.get("key") or value.get("issue") or value.get("id")
        return str(ref) if ref else None
    return _workflow_ref(value)


def _jira_ref_keys(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    keys: list[str] = []
    for item in value:
        key = _jira_ref_key(item)
        if key:
            keys.append(key)
    return keys


def _jira_issue_link_lines(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    lines: list[str] = []
    for link in value:
        if not isinstance(link, Mapping):
            continue
        target = _jira_ref_key(link.get("target"))
        if not target:
            continue
        label = _normalize_optional(link.get("type")) or "link"
        direction = _normalize_optional(link.get("direction"))
        suffix = f" ({direction})" if direction else ""
        lines.append(f"- {label}: {target}{suffix}")
    return lines


def _jira_external_link_lines(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    lines: list[str] = []
    for link in value:
        if not isinstance(link, Mapping):
            continue
        url = _normalize_optional(link.get("url"))
        title = _normalize_optional(link.get("title")) or url
        if url:
            lines.append(f"- external: [{title}]({url})")
        elif title:
            lines.append(f"- external: {title}")
    return lines


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
        if key in _RESERVED_SPECTRACK_KEYS:
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
