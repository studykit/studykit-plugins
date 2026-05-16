#!/usr/bin/env python3
"""Generated Jira issue snapshot renderer."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

def render_jira_snapshot(issue: Mapping[str, Any]) -> str:
    """Render an LLM-facing, generated Jira issue snapshot."""

    lines = [
        f"# {issue.get('key')}: {issue.get('title') or ''}".rstrip(),
        "",
        "Generated read-only Jira Data Center snapshot.",
        "",
        f"- Provider: Jira Data Center",
        f"- Site: {issue.get('jira', {}).get('base_url') if isinstance(issue.get('jira'), Mapping) else ''}",
        f"- Status: {issue.get('state') or ''}",
        f"- Updated: {issue.get('updatedAt') or ''}",
        f"- Labels: {', '.join(str(label) for label in issue.get('labels') or []) or 'none'}",
        "",
        "## Description",
        "",
        str(issue.get("body") or "").strip() or "(empty)",
        "",
        "## Comments",
        "",
    ]

    comments = issue.get("comments") if isinstance(issue.get("comments"), list) else []
    if comments:
        for comment in comments:
            if not isinstance(comment, Mapping):
                continue
            author = _author_name(comment.get("author"))
            lines.extend(
                [
                    f"### {comment.get('createdAt') or 'unknown time'} - {author}",
                    "",
                    str(comment.get("body") or "").strip() or "(empty)",
                    "",
                ]
            )
    else:
        lines.extend(["No comments cached.", ""])

    relationships = issue.get("relationships") if isinstance(issue.get("relationships"), Mapping) else {}
    assert isinstance(relationships, Mapping)
    lines.extend(["## Remote Links", ""])
    remote_links = relationships.get("remote_links") if isinstance(relationships.get("remote_links"), list) else []
    if remote_links:
        for link in remote_links:
            if not isinstance(link, Mapping):
                continue
            title = link.get("title") or link.get("url") or "remote link"
            relationship = f" ({link.get('relationship')})" if link.get("relationship") else ""
            url = f" — {link.get('url')}" if link.get("url") else ""
            lines.append(f"- {title}{relationship}{url}")
    else:
        lines.append("No remote links cached.")

    workflow = relationships.get("workflow") if isinstance(relationships.get("workflow"), Mapping) else {}
    if workflow:
        lines.extend(["", "## Workflow Relationships", ""])
        assert isinstance(workflow, Mapping)
        parent = workflow.get("parent")
        if isinstance(parent, Mapping):
            lines.append(f"- Parent: {_relationship_issue_label(parent)}")
        children = workflow.get("children") if isinstance(workflow.get("children"), list) else []
        if children:
            lines.append(f"- Children: {', '.join(_relationship_issue_label(child) for child in children if isinstance(child, Mapping))}")
        dependencies = workflow.get("dependencies") if isinstance(workflow.get("dependencies"), Mapping) else {}
        if isinstance(dependencies, Mapping):
            blocked_by = dependencies.get("blocked_by") if isinstance(dependencies.get("blocked_by"), list) else []
            blocking = dependencies.get("blocking") if isinstance(dependencies.get("blocking"), list) else []
            if blocked_by:
                lines.append(
                    f"- Blocked by: {', '.join(_relationship_issue_label(item) for item in blocked_by if isinstance(item, Mapping))}"
                )
            if blocking:
                lines.append(
                    f"- Blocking: {', '.join(_relationship_issue_label(item) for item in blocking if isinstance(item, Mapping))}"
                )
        related = workflow.get("related") if isinstance(workflow.get("related"), list) else []
        if related:
            lines.append(f"- Related: {', '.join(_relationship_issue_label(item) for item in related if isinstance(item, Mapping))}")

    issue_links = relationships.get("issue_links") if isinstance(relationships.get("issue_links"), list) else []
    if issue_links:
        lines.extend(["", "## Issue Links", ""])
        for link in issue_links:
            if not isinstance(link, Mapping):
                continue
            lines.append(f"- {_format_issue_link(link)}")

    lines.extend(["", "## Raw Cache", "", "- `issue.json`", "- `remote-links.json`", "- `metadata.yml`", ""])
    return "\n".join(lines)


def _author_name(value: Any) -> str:
    if isinstance(value, Mapping):
        for key in ("displayName", "name", "key", "accountId"):
            raw = value.get(key)
            if raw:
                return str(raw)
    if value:
        return str(value)
    return "unknown"


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
