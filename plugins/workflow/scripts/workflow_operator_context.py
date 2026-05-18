#!/usr/bin/env python3
"""Workflow operator subagent context helpers.

Operator-specific detection and bootstrap context generation are shared by hook
adapters. Host adapters pass concrete project configuration and launcher paths
so this module never reads runtime-specific environment variables directly.

Provider-specific operator instructions live in Markdown context fragments under
``agents/workflow-operator-context/``. This module selects only the fragments
that match the active workflow configuration and renders small placeholders.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

WORKFLOW_OPERATOR_AGENT_NAME = "workflow-operator"

_PLUGIN_ROOT = Path(__file__).resolve().parents[1]
_CONTEXT_ROOT = _PLUGIN_ROOT / "agents" / "workflow-operator-context"
_SUPPORTED_PROVIDER_FRAGMENTS = {
    "issues": {"github", "jira", "filesystem"},
    "knowledge": {"github", "confluence", "filesystem"},
}


class WorkflowOperatorContextError(RuntimeError):
    """Raised when an operator context fragment cannot be loaded."""


def agent_name_matches_operator(name: str | None) -> bool:
    return bool(name) and name.strip() == WORKFLOW_OPERATOR_AGENT_NAME


def build_operator_session_context(config: Any) -> str:
    """Build project-specific operator bootstrap context for SessionStart."""

    issue_kind = _provider_kind(config, "issues")
    knowledge_kind = _provider_kind(config, "knowledge")
    fragments = [
        _render_fragment("bootstrap.md", {}),
        _render_fragment(
            "configured-providers.md",
            {
                "ISSUE_KIND": issue_kind or "unknown",
                "KNOWLEDGE_KIND": knowledge_kind or "unknown",
            },
        ),
        _provider_fragment("issues", issue_kind),
        _provider_fragment("knowledge", knowledge_kind),
        _render_fragment("response-boundary.md", {}),
    ]
    return "\n\n".join(fragment.strip() for fragment in fragments if fragment.strip())


def _provider_fragment(section: str, provider_kind: str | None) -> str:
    supported = _SUPPORTED_PROVIDER_FRAGMENTS[section]
    fragment_name = provider_kind if provider_kind in supported else "unsupported"
    return _render_fragment(f"{section}/{fragment_name}.md", {})


def _render_fragment(relative_path: str, values: dict[str, str]) -> str:
    text = _read_fragment(relative_path)
    for key, value in values.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    unresolved = [
        token
        for token in ("{{ISSUE_KIND}}", "{{KNOWLEDGE_KIND}}")
        if token in text
    ]
    if unresolved:
        raise WorkflowOperatorContextError(
            f"operator context fragment {relative_path} has unresolved placeholders: {', '.join(unresolved)}"
        )
    return text


def _read_fragment(relative_path: str) -> str:
    path = (_CONTEXT_ROOT / relative_path).resolve()
    try:
        path.relative_to(_CONTEXT_ROOT.resolve())
    except ValueError as exc:
        raise WorkflowOperatorContextError(
            f"operator context fragment escapes context root: {relative_path}"
        ) from exc
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise WorkflowOperatorContextError(f"cannot read operator context fragment: {relative_path}") from exc


def _provider_kind(config: Any, role: str) -> str | None:
    provider = getattr(config, role, None)
    kind = getattr(provider, "kind", None)
    if kind is None:
        return None
    text = str(kind).strip().lower()
    return text or None
