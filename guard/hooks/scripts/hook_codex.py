#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Codex hook adapter for guard.

This module owns Codex payload parsing and output.  It intentionally builds a
guard-owned turn record from documented payload fields instead of parsing
``transcript_path``, whose format is not a stable Codex hook interface.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

# Before importing anything from guard_core: `config` reads GUARD_HOST once, at import, and
# every path below it is chosen from that answer.
os.environ["GUARD_HOST"] = "codex"


def _guard_core_dir() -> Path:
    """The directory holding the ``guard_core`` package, found by looking rather than counting.

    A fixed ``parents[2]`` is a bet on this file's depth in the plugin tree, and the bet on
    the other side of this import is what broke when the implementation moved into a package.
    """
    here = Path(__file__).resolve()
    for parent in here.parents[:5]:
        if (parent / "scripts" / "guard_core" / "__init__.py").is_file():
            return parent / "scripts"
    return here.parents[2] / "scripts"


sys.path.insert(0, str(_guard_core_dir()))
# Imported by module rather than through one façade, so these lines say which layers the
# adapter leans on and a layering violation is visible here. It also means a name that moves
# or goes away breaks at import instead of at the call: the façade version of this file spent
# releases calling two turn-record helpers that no longer existed, and every hook here fails
# open, so it failed silently.
from guard_core import cmd_edit as core_edit  # noqa: E402
from guard_core import cmd_search as core_search  # noqa: E402
from guard_core import cmd_session as core_session  # noqa: E402
from guard_core import config as core_config  # noqa: E402
from guard_core import payload as core_payload  # noqa: E402
from guard_core import paths as core_paths  # noqa: E402
from guard_core import state as core_state  # noqa: E402
from guard_core.codex_turns import _load_turn, _save_turn  # noqa: E402
from guard_core.transcript import _is_control_command_name, _turn_command_name  # noqa: E402

def _payload() -> dict[str, Any]:
    try:
        value = json.load(sys.stdin)
    except (OSError, ValueError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _project_dir(payload: dict[str, Any]) -> Path | None:
    cwd = payload.get("cwd")
    if not isinstance(cwd, str) or not cwd:
        return None
    path = Path(cwd).expanduser().resolve()
    try:
        result = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--show-toplevel"],
            capture_output=True, check=True, text=True, timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return path
    return Path(result.stdout.strip()).resolve() if result.stdout.strip() else path


def _session_id(payload: dict[str, Any]) -> str:
    value = payload.get("session_id")
    return value if isinstance(value, str) and core_payload._SESSION_ID_RE.match(value) and ".." not in value else ""


def _turn_id(payload: dict[str, Any]) -> str:
    value = payload.get("turn_id")
    return value if isinstance(value, str) and core_payload._SESSION_ID_RE.match(value) and ".." not in value else ""


def _handle_session_start(project_dir: Path) -> None:
    # The shared maintenance logic writes no Codex-specific state beyond the
    # host-selected paths and emits useful policy context on stdout.
    os.environ["GUARD_PROJECT_DIR"] = str(project_dir)
    core_session.cmd_session_start()


# Caps on what one tool call contributes to Codex's turn record. Codex keeps a record of
# its own because its transcript is not a stable hook interface; Claude no longer keeps
# one at all (its main agent writes the turn), so these live here rather than in core.
TOOL_CONTEXT_MAX_CHARS = 12000
TOOL_RESULT_MAX_CHARS = 2000


def _handle_prompt(project_dir: Path, payload: dict[str, Any], session_id: str, turn_id: str) -> None:
    prompt = payload.get("prompt")
    prompt = prompt if isinstance(prompt, str) else ""
    _save_turn(project_dir, session_id, turn_id, {"user": prompt, "tools": [], "assistant": ""})
    # The explicit audit-turn skill owns dispatch; a hook must not launch a second review.


def _handle_post_tool(project_dir: Path, payload: dict[str, Any], session_id: str, turn_id: str) -> None:
    turn = _load_turn(project_dir, session_id, turn_id)
    if not turn:
        return
    tool_input, tool_response = payload.get("tool_input"), payload.get("tool_response")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    tool_name = payload.get("tool_name") if isinstance(payload.get("tool_name"), str) else "tool"
    if not isinstance(command, str):
        command = f"[{tool_name}] {json.dumps(tool_input, ensure_ascii=False)[:TOOL_CONTEXT_MAX_CHARS]}"
    output = json.dumps(tool_response, ensure_ascii=False) if not isinstance(tool_response, str) else tool_response
    turn.setdefault("tools", []).append({"command": command[:TOOL_CONTEXT_MAX_CHARS], "output": output[:TOOL_RESULT_MAX_CHARS]})
    _save_turn(project_dir, session_id, turn_id, turn)

    config = core_config._load_config(project_dir)
    if core_search.is_shell_tool(payload.get("tool_name")):
        normalized = dict(payload)
        normalized["prompt_id"] = turn_id
        normalized["session_id"] = session_id
        core_edit.record_shell_writes(project_dir, normalized, config)
    edited_paths = _edited_paths(payload)
    for edited_path in edited_paths:
        normalized = dict(payload)
        normalized["prompt_id"] = turn_id
        normalized["session_id"] = session_id
        synthetic_input = {"file_path": edited_path}
        core_edit._record_edited_source(project_dir, normalized, synthetic_input, config)


def _edited_paths(payload: dict[str, Any]) -> list[str]:
    """Extract Codex write targets from a native file input or an apply_patch body."""

    tool_input = payload.get("tool_input")
    if isinstance(tool_input, dict):
        direct = tool_input.get("file_path") or tool_input.get("notebook_path")
        if isinstance(direct, str) and direct:
            return [direct]
        patch = tool_input.get("patch") or tool_input.get("input")
    else:
        patch = tool_input
    if not isinstance(patch, str):
        return []
    out: list[str] = []
    for match in re.finditer(r"^\*\*\* (?:Add|Update|Delete) File: (.+)$", patch, re.MULTILINE):
        path = match.group(1).strip()
        if path and path not in out:
            out.append(path)
    return out


def _handle_stop(project_dir: Path, payload: dict[str, Any], session_id: str, turn_id: str) -> None:
    turn = _load_turn(project_dir, session_id, turn_id)
    response = payload.get("last_assistant_message")
    response = response if isinstance(response, str) else ""
    if not turn or not response.strip():
        return
    turn["assistant"] = response
    _save_turn(project_dir, session_id, turn_id, turn)
    config = core_config._load_config(project_dir)
    normalized = dict(payload)
    normalized["prompt_id"] = turn_id
    normalized["session_id"] = session_id
    core_edit.recover_shell_writes(project_dir, normalized, config)
    state = core_state._read_state(project_dir, session_id, config)
    # Audit/control replies must not replace the target of the next explicit review.
    prompt = turn.get("user", "")
    if isinstance(prompt, str) and not _is_control_command_name(_turn_command_name(prompt)):
        state["pending_verify_prompt_id"] = turn_id
        core_state._write_state(project_dir, session_id, state)
    # Stop records evidence and recovers edits; it never requests a review.


def main() -> int:
    payload = _payload()
    project_dir, session_id, turn_id = _project_dir(payload), _session_id(payload), _turn_id(payload)
    if project_dir is None:
        return 0
    os.environ["GUARD_PROJECT_DIR"] = str(project_dir)
    event = payload.get("hook_event_name")
    if event == "SessionStart":
        _handle_session_start(project_dir)
    elif event == "PreToolUse":
        # Before the turn-id guard below, deliberately. Every other handler here writes or
        # reads a turn record and is meaningless without one; this rule reads `tool_name`
        # and `tool_input` only, both of which Codex documents on this event
        # (`wiki/ref/openai-codex-pretooluse-payload.md`), and a missing turn id must not
        # quietly disarm a prohibition.
        #
        # This is the one guard rule Codex CAN express. The removed `pre-write` hook could
        # not port because it classified the CALLER and this payload carries no
        # `agent_type`; this one classifies the tool ARGUMENT, which is present on both
        # hosts. The deny shape is the same `hookSpecificOutput.permissionDecision` Claude
        # uses — Codex documents it, alongside a legacy `decision: "block"` it still accepts
        # (`wiki/ref/openai-codex-pretooluse-deny-output-shape.md`), so `_emit_pre_tool_deny`
        # is shared rather than reimplemented.
        if core_search.is_shell_tool(payload.get("tool_name")) and session_id:
            core_edit.snapshot_shell_write_candidates(project_dir, payload)
        core_search.cmd_pre_search_payload(payload, project_dir, session_id)
    elif not session_id or not turn_id:
        return 0
    elif event == "UserPromptSubmit":
        _handle_prompt(project_dir, payload, session_id, turn_id)
    elif event == "PostToolUse":
        _handle_post_tool(project_dir, payload, session_id, turn_id)
    elif event == "Stop":
        _handle_stop(project_dir, payload, session_id, turn_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
