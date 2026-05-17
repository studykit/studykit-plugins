#!/usr/bin/env python3
"""Workflow main-assistant context helpers.

Main-session prompt fragments live in Markdown files under
``agents/workflow-main-context/`` so injected wording can be maintained without
editing hook logic.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

_PLUGIN_ROOT = Path(__file__).resolve().parents[1]
_CONTEXT_ROOT = _PLUGIN_ROOT / "agents" / "workflow-main-context"


def build_commit_prefix_context() -> str:
    """Return commit-prefix guidance injected into main assistant prompts."""

    return _read_fragment("commit-prefix.md").strip()


def build_session_policy_context(config: Any) -> str:
    """Return SessionStart policy guidance injected into main assistant sessions."""

    fragments = [_read_fragment("session-policy.md").strip()]
    if _provider_kind(config, "knowledge") == "github":
        fragments.append(_read_fragment("knowledge/github.md").strip())
    return "\n".join(fragment for fragment in fragments if fragment)


def build_codex_operator_reuse_context() -> str:
    """Return Codex-specific main-session operator reuse guidance."""

    return _read_fragment("codex-operator-reuse.md").strip()


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
