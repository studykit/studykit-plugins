#!/usr/bin/env python3
"""Jira issue payload and relationship normalization helpers."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from issue.jira.refs import normalize_jira_issue_key
from workflow_jira_data_center_client import JiraDataCenterSite

def normalize_jira_data_center_issue(
    issue: Mapping[str, Any],
    *,
    site: JiraDataCenterSite,
    remote_links: list[Mapping[str, Any]] | None = None,
    relationship_mappings: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Normalize Jira Data Center REST JSON into the workflow provider payload shape."""

    key = normalize_jira_issue_key(issue.get("key") or "")
    fields = issue.get("fields") if isinstance(issue.get("fields"), Mapping) else {}
    assert isinstance(fields, Mapping)

    status = fields.get("status") if isinstance(fields.get("status"), Mapping) else {}
    assert isinstance(status, Mapping)
    status_category = status.get("statusCategory") if isinstance(status.get("statusCategory"), Mapping) else {}
    assert isinstance(status_category, Mapping)

    raw_comments = fields.get("comment") if isinstance(fields.get("comment"), Mapping) else {}
    assert isinstance(raw_comments, Mapping)
    comments = [_normalize_data_center_comment(comment) for comment in _mapping_list(raw_comments.get("comments"))]

    relationships = _provider_relationships(
        fields,
        remote_links=remote_links,
        relationship_mappings=relationship_mappings,
    )
    payload: dict[str, Any] = {
        "issue": key,
        "key": key,
        "id": _normalize_optional(issue.get("id")),
        "title": str(fields.get("summary") or ""),
        "body": _text_field(fields.get("description")),
        "state": _normalize_optional(status.get("name")) or "unknown",
        "stateReason": _normalize_optional(status_category.get("key")),
        "labels": [str(label) for label in fields.get("labels") or [] if label is not None],
        "createdAt": _normalize_optional(fields.get("created")),
        "updatedAt": _normalize_optional(fields.get("updated")),
        "url": f"{site.base_url}/browse/{key}",
        "jira": {**site.to_json(), "key": key},
        "comments": comments,
    }
    if payload["id"] is None:
        payload.pop("id")
    if relationships:
        payload["relationships"] = relationships
    return payload


def normalize_jira_remote_links(raw_links: Any) -> list[dict[str, Any]]:
    """Return a compact provider-native remote link projection."""

    links: list[dict[str, Any]] = []
    for item in _mapping_list(raw_links):
        raw_object = item.get("object") if isinstance(item.get("object"), Mapping) else {}
        assert isinstance(raw_object, Mapping)
        entry: dict[str, Any] = {
            "id": str(item.get("id")) if item.get("id") is not None else None,
            "global_id": _normalize_optional(item.get("globalId") or item.get("global_id")),
            "relationship": _normalize_optional(item.get("relationship")),
            "url": _normalize_optional(raw_object.get("url")),
            "title": _normalize_optional(raw_object.get("title")),
        }
        links.append({key: value for key, value in entry.items() if value is not None})
    return links


def filter_jira_payload(
    payload: Mapping[str, Any],
    *,
    include_body: bool,
    include_comments: bool,
    include_relationships: bool,
) -> dict[str, Any]:
    """Apply read include flags to a normalized Jira issue payload."""

    result = dict(payload)
    if not include_body:
        result.pop("body", None)
    if not include_comments:
        result.pop("comments", None)
    if not include_relationships:
        result.pop("relationships", None)
    return result


def _provider_relationships(
    fields: Mapping[str, Any],
    *,
    remote_links: list[Mapping[str, Any]] | None,
    relationship_mappings: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    relationships: dict[str, Any] = {}
    if remote_links is not None:
        relationships["remote_links"] = [dict(item) for item in remote_links]

    issue_links = [_normalize_issue_link(item) for item in _mapping_list(fields.get("issuelinks"))]
    if issue_links:
        relationships["issue_links"] = issue_links

    parent = fields.get("parent")
    if isinstance(parent, Mapping):
        relationships["parent"] = _issue_stub(parent)

    subtasks = [_issue_stub(item) for item in _mapping_list(fields.get("subtasks"))]
    if subtasks:
        relationships["subtasks"] = subtasks
    workflow_relationships = _workflow_relationships(
        relationships,
        fields=fields,
        relationship_mappings=relationship_mappings,
    )
    if workflow_relationships:
        relationships["workflow"] = workflow_relationships
    return relationships


def _normalize_issue_link(link: Mapping[str, Any]) -> dict[str, Any]:
    raw_type = link.get("type") if isinstance(link.get("type"), Mapping) else {}
    assert isinstance(raw_type, Mapping)
    entry: dict[str, Any] = {
        "id": str(link.get("id")) if link.get("id") is not None else None,
        "type": _normalize_optional(raw_type.get("name")),
        "inward": _normalize_optional(raw_type.get("inward")),
        "outward": _normalize_optional(raw_type.get("outward")),
    }
    inward_issue = link.get("inwardIssue")
    outward_issue = link.get("outwardIssue")
    if isinstance(inward_issue, Mapping):
        entry["inward_issue"] = _issue_stub(inward_issue)
    if isinstance(outward_issue, Mapping):
        entry["outward_issue"] = _issue_stub(outward_issue)
    return {key: value for key, value in entry.items() if value is not None}


def _workflow_relationships(
    provider_relationships: Mapping[str, Any],
    *,
    fields: Mapping[str, Any] | None = None,
    relationship_mappings: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Map Jira-native relationship fields into workflow relationship buckets.

    Issue-link buckets are resolved from ``providers.issues.relationship_mappings``.
    Links whose ``(link_type, direction)`` matches a mapping land in that bucket;
    unmapped links are preserved verbatim under ``issue_links``. Mappings with
    ``surface: field`` (and ``write_to: source``) are resolved by reading the
    configured field from the raw issue payload.
    """

    workflow: dict[str, Any] = {}

    parent = provider_relationships.get("parent")
    if isinstance(parent, Mapping):
        workflow["parent"] = _workflow_issue(parent)

    subtasks = provider_relationships.get("subtasks")
    if isinstance(subtasks, list):
        children = [_workflow_issue(item) for item in subtasks if isinstance(item, Mapping)]
        if children:
            workflow["children"] = children

    inverse_mapping = _inverse_issue_link_mapping(relationship_mappings or {})
    buckets: dict[str, list[dict[str, Any]]] = {}
    unmapped_links: list[dict[str, Any]] = []
    issue_links = provider_relationships.get("issue_links")
    if isinstance(issue_links, list):
        for link in issue_links:
            if not isinstance(link, Mapping):
                continue
            target, direction, _label = _issue_link_target_and_label(link)
            if target is None:
                continue
            mapped = _workflow_issue(target)
            link_type = _normalize_optional(link.get("type"))
            bucket = inverse_mapping.get((link_type, direction)) if link_type else None
            if bucket is not None:
                buckets.setdefault(bucket, []).append(mapped)
            else:
                entry: dict[str, Any] = {"target": mapped, "direction": direction}
                if link_type:
                    entry["type"] = link_type
                unmapped_links.append(entry)

    for name in sorted(buckets):
        workflow[name] = buckets[name]
    if unmapped_links:
        workflow["issue_links"] = unmapped_links

    for name, ref in _field_surface_workflow_entries(fields or {}, relationship_mappings or {}):
        if name in workflow:
            continue
        workflow[name] = [_workflow_issue({"key": ref})]

    remote_links = provider_relationships.get("remote_links")
    if isinstance(remote_links, list):
        external_links = [_workflow_external_link(item) for item in remote_links if isinstance(item, Mapping)]
        if external_links:
            workflow["external_links"] = external_links

    return workflow


def _field_surface_workflow_entries(
    fields: Mapping[str, Any],
    relationship_mappings: Mapping[str, Any],
) -> list[tuple[str, str]]:
    """Yield ``(name, resolved_key)`` for each readable ``surface: field`` mapping."""

    entries: list[tuple[str, str]] = []
    for name, mapping in relationship_mappings.items():
        if not isinstance(name, str) or not isinstance(mapping, Mapping):
            continue
        if mapping.get("surface") != "field":
            continue
        write_to = mapping.get("write_to") or "source"
        if write_to != "source":
            continue
        field_id = mapping.get("field")
        if not isinstance(field_id, str) or not field_id:
            continue
        raw_value = fields.get(field_id)
        if raw_value is None:
            continue
        value_kind = mapping.get("value") or "string"
        resolved = _field_relationship_key(raw_value, value_kind)
        if resolved is None:
            continue
        entries.append((name, resolved))
    return entries


def _field_relationship_key(raw_value: Any, value_kind: Any) -> str | None:
    """Extract the issue key string from a raw Jira field value."""

    kind = str(value_kind) if value_kind is not None else "string"
    if kind == "string":
        return _normalize_optional(raw_value)
    if kind in {"key", "key_object"}:
        if isinstance(raw_value, Mapping):
            return _normalize_optional(raw_value.get("key"))
        return None
    return None


def _inverse_issue_link_mapping(
    relationship_mappings: Mapping[str, Any],
) -> dict[tuple[str, str], str]:
    """Build ``(link_type, direction) -> workflow relationship name`` from config."""

    inverse: dict[tuple[str, str], str] = {}
    for name, mapping in relationship_mappings.items():
        if not isinstance(mapping, Mapping):
            continue
        if mapping.get("surface") != "issue_link":
            continue
        link_type = mapping.get("link_type")
        direction = mapping.get("direction")
        if isinstance(link_type, str) and isinstance(direction, str) and isinstance(name, str):
            inverse[(link_type, direction)] = name
    return inverse


def _issue_link_target_and_label(link: Mapping[str, Any]) -> tuple[Mapping[str, Any] | None, str, str | None]:
    if isinstance(link.get("outward_issue"), Mapping):
        return link["outward_issue"], "outward", _normalize_optional(link.get("outward"))
    if isinstance(link.get("inward_issue"), Mapping):
        return link["inward_issue"], "inward", _normalize_optional(link.get("inward"))
    return None, "unknown", None


def _workflow_issue(issue: Mapping[str, Any]) -> dict[str, Any]:
    key = _normalize_optional(issue.get("key"))
    result: dict[str, Any] = {
        "provider": "jira",
        "key": key,
        "issue": key,
        "id": _normalize_optional(issue.get("id")),
        "title": _normalize_optional(issue.get("summary") or issue.get("title")),
        "state": _normalize_optional(issue.get("status") or issue.get("state")),
    }
    return {name: value for name, value in result.items() if value is not None}


def _workflow_external_link(link: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "source": "remote_links",
        "title": _normalize_optional(link.get("title")),
        "url": _normalize_optional(link.get("url")),
        "relationship": _normalize_optional(link.get("relationship")),
        "global_id": _normalize_optional(link.get("global_id")),
        "id": _normalize_optional(link.get("id")),
    }
    return {name: value for name, value in result.items() if value is not None}


def _issue_stub(issue: Mapping[str, Any]) -> dict[str, Any]:
    fields = issue.get("fields") if isinstance(issue.get("fields"), Mapping) else {}
    assert isinstance(fields, Mapping)
    status = fields.get("status") if isinstance(fields.get("status"), Mapping) else {}
    assert isinstance(status, Mapping)
    result: dict[str, Any] = {
        "key": _normalize_optional(issue.get("key")),
        "id": _normalize_optional(issue.get("id")),
        "summary": _normalize_optional(fields.get("summary")),
        "status": _normalize_optional(status.get("name")),
    }
    return {key: value for key, value in result.items() if value is not None}


def _normalize_data_center_comment(comment: Mapping[str, Any]) -> dict[str, Any]:
    author = comment.get("author") if isinstance(comment.get("author"), Mapping) else {}
    assert isinstance(author, Mapping)
    return {
        "id": str(comment.get("id") or ""),
        "author": {str(key): value for key, value in author.items()},
        "body": _text_field(comment.get("body")),
        "createdAt": _normalize_optional(comment.get("created")),
        "updatedAt": _normalize_optional(comment.get("updated")),
    }


def _format_issue_link(link: Mapping[str, Any]) -> str:
    type_name = link.get("type") or "link"
    if isinstance(link.get("outward_issue"), Mapping):
        issue = link["outward_issue"]
        assert isinstance(issue, Mapping)
        return f"{type_name} outward {issue.get('key')}: {issue.get('summary') or ''}".rstrip()
    if isinstance(link.get("inward_issue"), Mapping):
        issue = link["inward_issue"]
        assert isinstance(issue, Mapping)
        return f"{type_name} inward {issue.get('key')}: {issue.get('summary') or ''}".rstrip()
    return str(type_name)


def _relationship_issue_label(issue: Mapping[str, Any]) -> str:
    key = issue.get("key") or issue.get("issue") or "unknown"
    title = issue.get("title")
    return f"{key} ({title})" if title else str(key)


def _mapping_list(value: Any) -> list[Mapping[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _text_field(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return str(value)


def _normalize_optional(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
