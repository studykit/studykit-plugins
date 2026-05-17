#!/usr/bin/env python3
"""Workflow operator subagent context helpers.

Operator-specific detection and bootstrap context generation are shared by hook
adapters. Host adapters pass concrete project configuration and launcher paths
so this module never reads runtime-specific environment variables directly.
"""

from __future__ import annotations

import shlex
from pathlib import Path
from typing import Any

WORKFLOW_OPERATOR_AGENT_NAME = "workflow-operator"

_GITHUB_ISSUE_COMMANDS = {
    "ISSUE_FETCH": "github_issue_fetch.py",
    "ISSUE_DRAFTS": "github_issue_drafts.py",
    "ISSUE_WRITEBACK": "github_issue_writeback.py",
    "ISSUE_COMMENTS": "github_issue_comments.py",
    "ISSUE_RELATIONSHIPS": "github_issue_relationships.py",
    "ISSUE_METADATA": "github_issue_metadata.py",
}

_JIRA_ISSUE_COMMANDS = {
    "ISSUE_FETCH": "jira_issue_fetch.py",
    "ISSUE_DRAFTS": "jira_issue_drafts.py",
    "ISSUE_WRITEBACK": "jira_issue_writeback.py",
    "ISSUE_COMMENTS": "jira_issue_comments.py",
    "ISSUE_RELATIONSHIPS": "jira_issue_relationships.py",
    "ISSUE_METADATA": "jira_issue_metadata.py",
}


def agent_name_matches_operator(name: str | None) -> bool:
    return bool(name) and name.strip() == WORKFLOW_OPERATOR_AGENT_NAME


def build_operator_session_context(config: Any, *, launcher: Path) -> str:
    """Build project-specific operator bootstrap context for SessionStart."""

    issue_kind = _provider_kind(config, "issues")
    knowledge_kind = _provider_kind(config, "knowledge")
    lines = [
        "## workflow operator bootstrap",
        "",
        "Use this workflow launcher path before running workflow commands:",
        "",
        "```bash",
        f"WORKFLOW={shlex.quote(str(launcher))}",
        "```",
        "",
        "Use `$WORKFLOW` for bundled workflow scripts. The launcher owns Codex",
        "session translation; do not derive the launcher from project layout",
        "or inspect runtime-specific session files directly.",
        "",
        "## configured workflow providers",
        "",
        f"Issues: {issue_kind or 'unknown'}",
        f"Knowledge: {knowledge_kind or 'unknown'}",
        "",
    ]
    lines.extend(_issue_command_context(issue_kind))
    lines.append("")
    lines.extend(_knowledge_context(knowledge_kind))
    lines.extend(
        [
            "",
            "## response boundary",
            "",
            "Return compact operational results only: operation, affected refs, paths,",
            "verification, and intentionally remaining local changes.",
            "Do not quote or summarize issue bodies, comments, or knowledge documents.",
        ]
    )
    return "\n".join(lines)


def _issue_command_context(issue_kind: str | None) -> list[str]:
    if issue_kind == "github":
        return [
            "## configured issue commands",
            "",
            "Use only the GitHub issue command family for this project:",
            "",
            *_command_assignment_block(_GITHUB_ISSUE_COMMANDS),
            "",
            "Do not use another issue provider command family in this project.",
            *_common_issue_operation_lines(),
        ]
    if issue_kind == "jira":
        return [
            "## configured issue commands",
            "",
            "Use only the Jira issue command family for this project:",
            "",
            *_command_assignment_block(_JIRA_ISSUE_COMMANDS),
            "",
            "Do not use another issue provider command family in this project.",
            *_common_issue_operation_lines(),
        ]
    if issue_kind == "filesystem":
        return [
            "## configured issue commands",
            "",
            "No provider issue command family is configured for filesystem issues.",
            "Resolve authoring paths with `authoring_resolver.py` when the caller asks",
            "about workflow issue content.",
        ]
    return [
        "## configured issue commands",
        "",
        "No supported issue provider is configured. Return the unsupported operation",
        "instead of choosing GitHub or Jira commands.",
    ]


def _common_issue_operation_lines() -> list[str]:
    return [
        "",
        "Resolve authoring paths with `authoring_resolver.py`.",
        "Fetch or refresh issues with `$ISSUE_FETCH`.",
        "Prepare new issues as pending drafts with `$ISSUE_DRAFTS prepare`.",
        "Create provider issues from drafts only after explicit user approval and",
        "`--confirm-provider-create`.",
        "Use `$ISSUE_WRITEBACK`, `$ISSUE_COMMENTS`, `$ISSUE_RELATIONSHIPS`, and",
        "`$ISSUE_METADATA` for provider/cache mutations they support.",
        "If a requested provider operation is unsupported, return that limitation",
        "instead of guessing another provider command.",
    ]


def _knowledge_context(knowledge_kind: str | None) -> list[str]:
    if knowledge_kind == "github":
        return [
            "## configured knowledge provider",
            "",
            "GitHub knowledge documents are repository Markdown files under `wiki/`.",
            "Resolve authoring paths only; the caller chooses and edits the target file.",
            "Do not create, modify, publish, or summarize GitHub knowledge content.",
        ]
    if knowledge_kind == "confluence":
        return [
            "## configured knowledge provider",
            "",
            "Confluence knowledge documents require Confluence authoring paths.",
            "Return unsupported for provider writes that workflow scripts do not support.",
            "Do not use GitHub `wiki/` paths for this project.",
        ]
    if knowledge_kind == "filesystem":
        return [
            "## configured knowledge provider",
            "",
            "Filesystem knowledge documents use configured local repository paths.",
            "Resolve authoring paths and return local path context when needed.",
            "Do not use GitHub `wiki/` or Confluence provider commands.",
        ]
    return [
        "## configured knowledge provider",
        "",
        "No supported knowledge provider is configured. Return unsupported instead",
        "of guessing a provider-specific knowledge workflow.",
    ]


def _command_assignment_block(commands: dict[str, str]) -> list[str]:
    return [
        "```bash",
        *(f"{name}={value}" for name, value in commands.items()),
        "```",
    ]


def _provider_kind(config: Any, role: str) -> str | None:
    provider = getattr(config, role, None)
    kind = getattr(provider, "kind", None)
    if kind is None:
        return None
    text = str(kind).strip().lower()
    return text or None
