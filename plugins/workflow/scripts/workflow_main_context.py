#!/usr/bin/env python3
"""Workflow main-assistant context helpers.

Main-session prompt fragments live in Markdown files under
``agents/workflow-main-context/`` so injected wording can be maintained without
editing hook logic. The always-loaded entry point at ``session-policy.md`` uses
``$WORKFLOW_POLICY_DIR``, ``$WORKFLOW_ISSUE_PROVIDER``,
``$WORKFLOW_KNOWLEDGE_PROVIDER``, and ``$WORKFLOW_ISSUE_FETCH_BLOCK``
placeholders that this module substitutes at SessionStart based on the active
workflow configuration. Provider-specific inline snippets live under
``agents/workflow-main-context/snippets/<group>/<provider>.md``.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

_PLUGIN_ROOT = Path(__file__).resolve().parents[1]
_CONTEXT_ROOT = _PLUGIN_ROOT / "agents" / "workflow-main-context"
_KNOWN_ISSUE_PROVIDERS = {"github", "jira", "filesystem"}
_KNOWN_KNOWLEDGE_PROVIDERS = {"github", "confluence", "filesystem"}


def build_commit_prefix_context() -> str:
    """Return commit-prefix guidance injected into main assistant prompts."""

    return _read_fragment("commit-prefix.md").strip()


def build_session_policy_context(config: Any, *, plugin_root: Path | None = None) -> str:
    """Return SessionStart policy guidance injected into main assistant sessions."""

    text = _read_fragment("session-policy.md").strip()
    if plugin_root is None:
        return text
    policy_dir = plugin_root.expanduser().resolve() / "agents" / "workflow-main-context" / "policy"
    issue_provider = _provider_segment(config, "issues", _KNOWN_ISSUE_PROVIDERS)
    knowledge_provider = _provider_segment(config, "knowledge", _KNOWN_KNOWLEDGE_PROVIDERS)
    issue_fetch_block = _read_snippet("issue-fetch", issue_provider)
    return (
        text
        .replace("$WORKFLOW_ISSUE_FETCH_BLOCK", issue_fetch_block)
        .replace("$WORKFLOW_POLICY_DIR", str(policy_dir))
        .replace("$WORKFLOW_ISSUE_PROVIDER", issue_provider)
        .replace("$WORKFLOW_KNOWLEDGE_PROVIDER", knowledge_provider)
    )


def _read_snippet(group: str, provider: str) -> str:
    path = _CONTEXT_ROOT / "snippets" / group / f"{provider}.md"
    return path.read_text(encoding="utf-8").strip()


def _provider_segment(config: Any, role: str, known: set[str]) -> str:
    kind = _provider_kind(config, role)
    return kind if kind in known else "unsupported"


def _read_fragment(name: str) -> str:
    try:
        return (_CONTEXT_ROOT / name).read_text(encoding="utf-8")
    except OSError:
        return ""


def _provider_kind(config: Any, role: str) -> str | None:
    provider = getattr(config, role, None)
    kind = getattr(provider, "kind", None)
    if kind is None:
        return None
    text = str(kind).strip().lower()
    return text or None
