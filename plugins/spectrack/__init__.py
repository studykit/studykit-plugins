"""Hermes plugin adapter for SpecTrack.

Hermes does not consume Claude/Codex plugin manifests or hook JSON. This module
registers the portable pieces of SpecTrack through Hermes' Python plugin API:
first-turn workflow context injection and bundled skills.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

_PLUGIN_ROOT = Path(__file__).resolve().parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
_SKILLS_DIR = _PLUGIN_ROOT / "skills"
_injected_sessions: set[str] = set()


def _ensure_scripts_path() -> None:
    scripts_path = str(_SCRIPTS_DIR)
    if scripts_path not in sys.path:
        sys.path.insert(0, scripts_path)


def _project_dir() -> Path:
    value = os.environ.get("SPECTRACK_PROJECT_DIR")
    if value:
        return Path(value).expanduser().resolve()
    return Path.cwd().resolve()


def _workflow_context(
    *,
    session_id: str = "",
    is_first_turn: bool = False,
    **_: Any,
) -> dict[str, str] | None:
    """Inject SpecTrack session policy once for configured Hermes sessions."""

    key = session_id or ""
    if key:
        if key in _injected_sessions:
            return None
    elif not is_first_turn:
        return None

    _ensure_scripts_path()
    from config import load_workflow_config  # type: ignore
    from main_context import build_session_policy_context  # type: ignore

    config = load_workflow_config(_project_dir())
    if config is None:
        return None

    if key:
        _injected_sessions.add(key)
    return {
        "context": build_session_policy_context(
            config,
            plugin_root=_PLUGIN_ROOT,
            runtime="hermes",
        )
    }


def _register_skills(ctx: Any) -> None:
    if not _SKILLS_DIR.exists():
        return
    for child in sorted(_SKILLS_DIR.iterdir()):
        skill_md = child / "SKILL.md"
        if child.is_dir() and skill_md.exists():
            ctx.register_skill(child.name, skill_md)


def register(ctx: Any) -> None:
    """Register SpecTrack with Hermes."""

    ctx.register_hook("pre_llm_call", _workflow_context)
    _register_skills(ctx)
