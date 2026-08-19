#!/usr/bin/env python3
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

os.environ.setdefault("GUARD_HOST", "codex")
_SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import guard_hook as core  # noqa: E402

_APPROVAL = re.compile(
    r"\b(approve|approved|go ahead|proceed|implement it|do it|start implementation)\b|"
    r"(?:진행|수정해|수정해줘|구현해|구현해줘|해제해|해제해줘|시작해|시작해줘)",
    re.IGNORECASE,
)
_PATCH_PATH = re.compile(r"^\*\*\* (?:Add|Update|Delete) File: (.+)$", re.MULTILINE)


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
    return value if isinstance(value, str) and core._SESSION_ID_RE.match(value) and ".." not in value else ""


def _turn_id(payload: dict[str, Any]) -> str:
    value = payload.get("turn_id")
    return value if isinstance(value, str) and core._SESSION_ID_RE.match(value) and ".." not in value else ""


def _turn_path(project_dir: Path, session_id: str, turn_id: str) -> Path:
    return core._turn_slice_file(project_dir, session_id, turn_id)


def _load_turn(project_dir: Path, session_id: str, turn_id: str) -> dict[str, Any]:
    path = _turn_path(project_dir, session_id, turn_id)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        value = {}
    return value if isinstance(value, dict) else {}


def _save_turn(project_dir: Path, session_id: str, turn_id: str, turn: dict[str, Any]) -> None:
    core._write_turn_slice(project_dir, session_id, turn_id, turn)


def _emit(value: dict[str, Any]) -> None:
    json.dump(value, sys.stdout)


def _patch_targets(project_dir: Path, command: str) -> list[Path]:
    targets: list[Path] = []
    for raw in _PATCH_PATH.findall(command):
        path = Path(raw)
        try:
            targets.append((path if path.is_absolute() else project_dir / path).resolve())
        except OSError:
            continue
    return targets


def _is_exempt_target(project_dir: Path, target: Path, config: dict[str, Any]) -> bool:
    if core._is_guard_owned(project_dir, target):
        return False
    refs = core._refs_dir(project_dir, config)
    if target == refs or refs in target.parents:
        return True
    if core._is_outside_project(project_dir, target) or core._git_ignored(project_dir, target):
        return True
    return any(target == folder or folder in target.parents for folder in core._writable_dirs(project_dir, config))


def _handle_session_start(project_dir: Path) -> None:
    # The shared maintenance logic writes no Codex-specific state beyond the
    # host-selected paths and emits useful policy context on stdout.
    os.environ["GUARD_PROJECT_DIR"] = str(project_dir)
    core.cmd_session_start()


def _handle_prompt(project_dir: Path, payload: dict[str, Any], session_id: str, turn_id: str) -> None:
    prompt = payload.get("prompt")
    prompt = prompt if isinstance(prompt, str) else ""
    config = core._load_config(project_dir)
    state = core._read_state(project_dir, session_id, config)
    if _APPROVAL.search(prompt):
        state["approved"] = True
        core._write_state(project_dir, session_id, state)
    elif prompt.strip():
        state["approved"] = False
        core._write_state(project_dir, session_id, state)
    _save_turn(project_dir, session_id, turn_id, {"user": prompt, "tools": [], "assistant": ""})

    if prompt.strip().lower().startswith("/guard:audit-evidence"):
        pending = state.get("pending_verify_prompt_id")
        if isinstance(pending, str) and pending and _turn_path(project_dir, session_id, pending).is_file():
            _emit({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": (
                "guard: audit the saved turn before answering. Spawn the read-only "
                "guard_evidence_auditor named subagent in a fresh context, give it "
                f"the turn file {_turn_path(project_dir, session_id, pending)}, and have it verify the "
                "assistant claims against the repository. If that agent is unavailable, tell the user "
                "to run $guard:setup in this project."
            )}})


def _handle_pre_tool(project_dir: Path, payload: dict[str, Any], session_id: str) -> None:
    config = core._load_config(project_dir)
    state = core._read_state(project_dir, session_id, config)
    if state["edit_gate"] == core.EditGate.OFF or state.get("approved"):
        return
    tool_input = payload.get("tool_input")
    command = tool_input.get("command") if isinstance(tool_input, dict) else ""
    targets = _patch_targets(project_dir, command) if isinstance(command, str) else []
    if targets and all(_is_exempt_target(project_dir, target, config) for target in targets):
        return
    turn_id = _turn_id(payload)
    if turn_id:
        state["gated_prompt_id"] = turn_id
        core._write_state(project_dir, session_id, state)
    _emit({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": (
        "guard: file edits are blocked until the user explicitly approves implementation. "
        "Present a plan and wait for the user's approval, then retry."
    )}})


def _handle_post_tool(project_dir: Path, payload: dict[str, Any], session_id: str, turn_id: str) -> None:
    turn = _load_turn(project_dir, session_id, turn_id)
    if not turn:
        return
    tool_input, tool_response = payload.get("tool_input"), payload.get("tool_response")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    tool_name = payload.get("tool_name") if isinstance(payload.get("tool_name"), str) else "tool"
    if not isinstance(command, str):
        command = f"[{tool_name}] {json.dumps(tool_input, ensure_ascii=False)[:core.TOOL_CONTEXT_MAX_CHARS]}"
    output = json.dumps(tool_response, ensure_ascii=False) if not isinstance(tool_response, str) else tool_response
    turn.setdefault("tools", []).append({"command": command[:core.TOOL_CONTEXT_MAX_CHARS], "output": output[:core.TOOL_RESULT_MAX_CHARS]})
    _save_turn(project_dir, session_id, turn_id, turn)


def _handle_stop(project_dir: Path, payload: dict[str, Any], session_id: str, turn_id: str) -> None:
    if payload.get("stop_hook_active") is True:
        return
    turn = _load_turn(project_dir, session_id, turn_id)
    response = payload.get("last_assistant_message")
    response = response if isinstance(response, str) else ""
    if not turn or not response.strip():
        return
    turn["assistant"] = response
    _save_turn(project_dir, session_id, turn_id, turn)
    config = core._load_config(project_dir)
    state = core._read_state(project_dir, session_id, config)
    if state.get("gated_prompt_id") == turn_id:
        return
    want_claims, want_deferrals = core._audit_claims(state), core._audit_deferrals(state)
    # Both axes off: nothing for the auditor to report, so do not block for one.
    if not want_claims and not want_deferrals:
        return
    if state["audit_gate"] == core.AuditGate.MANUAL:
        state["pending_verify_prompt_id"] = turn_id
        core._write_state(project_dir, session_id, state)
        return
    # Codex command hooks cannot launch an agent themselves.  A Stop block creates
    # one continuation prompt, where the main agent can dispatch the auditor.
    state["last_audited_prompt_id"] = turn_id
    core._write_state(project_dir, session_id, state)
    if want_claims and want_deferrals:
        scope = "the response's claims and deferrals"
    elif want_claims:
        scope = "the response's claims ONLY (skip the deferral axis; report no deferrals)"
    else:
        scope = "the response's deferrals ONLY (skip the claim axis; report no claims)"
    _emit({"decision": "block", "reason": (
        "guard: before completing, spawn the read-only guard_evidence_auditor named subagent in a fresh "
        "context. Give it "
        f"the saved turn record at {_turn_path(project_dir, session_id, turn_id)} and have it check "
        f"{scope} against the repository; then address any violations. If that agent is unavailable, "
        "tell the user to run $guard:setup in this project."
    )})


def main() -> int:
    payload = _payload()
    project_dir, session_id, turn_id = _project_dir(payload), _session_id(payload), _turn_id(payload)
    if project_dir is None:
        return 0
    os.environ["GUARD_PROJECT_DIR"] = str(project_dir)
    event = payload.get("hook_event_name")
    if event == "SessionStart":
        _handle_session_start(project_dir)
    elif not session_id or not turn_id:
        return 0
    elif event == "UserPromptSubmit":
        _handle_prompt(project_dir, payload, session_id, turn_id)
    elif event == "PreToolUse":
        _handle_pre_tool(project_dir, payload, session_id)
    elif event == "PostToolUse":
        _handle_post_tool(project_dir, payload, session_id, turn_id)
    elif event == "Stop":
        _handle_stop(project_dir, payload, session_id, turn_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
