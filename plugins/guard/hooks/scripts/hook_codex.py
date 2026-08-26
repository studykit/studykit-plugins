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
import subprocess
import sys
from pathlib import Path
from typing import Any

# Before importing anything from guard_core: `config` reads GUARD_HOST once, at import, and
# every path below it is chosen from that answer.
os.environ.setdefault("GUARD_HOST", "codex")


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
from guard_core import agents as core_agents  # noqa: E402
from guard_core import cmd_edit as core_edit  # noqa: E402
from guard_core import cmd_search as core_search  # noqa: E402
from guard_core import cmd_session as core_session  # noqa: E402
from guard_core import config as core_config  # noqa: E402
from guard_core import payload as core_payload  # noqa: E402
from guard_core import paths as core_paths  # noqa: E402
from guard_core import state as core_state  # noqa: E402

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


# Codex's turn record is JSON — `{user, tools, assistant}` — and the adapter owns both the
# format and these three accessors. Claude's side is a markdown file the main agent writes
# and the agents correct in place; there is nothing shared to factor out but the state root,
# and the two formats answer to different readers. Living in core once cost exactly this:
# the Claude side moved to markdown, its JSON helpers went away, and the adapter kept
# calling names that no longer existed — silently, because every hook here fails open.
def _turn_path(project_dir: Path, session_id: str, turn_id: str) -> Path:
    return core_paths._state_root(project_dir) / "turns" / session_id / f"{turn_id}.json"


def _load_turn(project_dir: Path, session_id: str, turn_id: str) -> dict[str, Any]:
    path = _turn_path(project_dir, session_id, turn_id)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        value = {}
    return value if isinstance(value, dict) else {}


def _save_turn(project_dir: Path, session_id: str, turn_id: str, turn: dict[str, Any]) -> None:
    """Write the turn record, atomically. Silent on failure — the caller fails open."""
    path = _turn_path(project_dir, session_id, turn_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(turn, ensure_ascii=False), encoding="utf-8")
        tmp.replace(path)
    except OSError:
        core_paths._trace(project_dir, session_id, "codex", "turn_write_failed", turn_id=turn_id)


def _emit(value: dict[str, Any]) -> None:
    json.dump(value, sys.stdout)


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
    config = core_config._load_config(project_dir)
    state = core_state._read_state(project_dir, session_id, config)
    _save_turn(project_dir, session_id, turn_id, {"user": prompt, "tools": [], "assistant": ""})

    if prompt.strip().lower().startswith("/guard:claims-auditor"):
        pending = state.get("pending_verify_prompt_id")
        if isinstance(pending, str) and pending and _turn_path(project_dir, session_id, pending).is_file():
            _emit({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": (
                "guard: audit the saved turn before answering. Spawn the read-only "
                "guard_claims_auditor named subagent in a fresh context, give it "
                f"the turn file {_turn_path(project_dir, session_id, pending)}, and have it verify the "
                "assistant claims against the repository. If that agent is unavailable, tell the user "
                "to run $guard:setup in this project."
            )}})


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

    # A reference saved into the refs dir must be listed in the index; same rule as
    # Claude's `post-edit` hook, applied here because Codex routes every event through
    # this one adapter. Claude's other `post-edit` job — recording the files the turn
    # edited — is deliberately not mirrored: it exists only to point `comment-corrector`,
    # `agents-md-auditor` at them, and Codex has none of those agents yet.
    # So the index rule below is enforced on Codex while the audit of what was saved is not.
    config = core_config._load_config(project_dir)
    if core_edit._targets_refs_dir(project_dir, tool_input, config):
        target = core_edit._tool_target_path(project_dir, tool_input)
        if target is not None and target.name not in core_edit._REFS_INDEX_SKIP:
            reason = core_edit.refs_index_gap(project_dir, target, config)
            if reason is not None:
                _emit({"decision": "block", "reason": reason})


# How each shared recommendation key reads in the sentence handed to Codex's single
# named agent. Keys absent here have no Codex agent and are dropped.
#
# `clarity-auditor` is absent on purpose, and this is not an omission to fix. It needs two
# things Codex does not have: the session's transcript, to tell a term this session already
# explained from one it never did (Codex's transcript is not a stable hook interface, which
# is why this adapter keeps its own turn record), and agent memory, to hold the reader
# profile it calibrates against. Without either it would have nothing to audit against and
# would report `profile: MISSING` on every turn.
#
# `ext-docs-fetcher` and `ext-docs-auditor` are absent, and neither could reach this table:
# they have no `AUDIT_AGENTS` entry, so `core_agents._eligible_agents` never offers them. On
# Claude the fetcher is selected from its description and the auditor is named by the Stop hook
# off the turn's refs edits; Codex ships one named agent from `$guard:setup` and this adapter
# mirrors no edited-file recording (see `_handle_post_tool`), so neither route exists here.
# Giving Codex the agent set is what unblocks both, same as above.
_SCOPE = {"claims-auditor": "the response's claims",
          "deferrals-auditor": "deferrals the repository could resolve",
          "korean-corrector": "whether the Korean reads as translated English"}


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
    config = core_config._load_config(project_dir)
    state = core_state._read_state(project_dir, session_id, config)
    # Recorded whether or not a switch is on: it is what `$guard:claims-auditor` is
    # pointed at, and switching the automatic recommendation off is not meant to take
    # away the user's own command.
    state["pending_verify_prompt_id"] = turn_id
    # `audit-turn: off` in this project's config, read through the state it seeds. Codex has no
    # `guard` command, so on this host the switch is only ever the config's value — but it IS a
    # config key, and a project that writes one and gets audited anyway has been told nothing.
    # Placed after the line above for the same reason Claude's Stop places it there: the pending
    # target is still recorded, so `$guard:claims-auditor` still works on the turn.
    if core_state._audit_paused(state):
        core_state._write_state(project_dir, session_id, state)
        return
    # Codex command hooks cannot launch an agent themselves, and unlike Claude's Stop
    # there is no continuation to piggyback on — so the once-guard cannot lean on
    # `stop_hook_active` and keys on the turn id instead.
    if state.get("last_audited_prompt_id") == turn_id:
        core_state._write_state(project_dir, session_id, state)
        return
    # Neither reuse nor routing exists here. `reuse` is a named instance addressed with
    # `SendMessage`, and this adapter has neither — `core_agents._eligible_agents` only asks
    # whether a mode is `off`, so the value costs nothing and means nothing on Codex.
    #
    # No router here either. Claude's Stop asks its main agent to dispatch `guard:router`, a
    # subagent that reads the turn and names which of the eligible agents would find
    # something in it. Codex ships one named agent, installed by `$guard:setup`, and a
    # router that can only forward to that same agent decides nothing — so Codex
    # recommends the whole ELIGIBLE set, unrouted, and is correspondingly noisier.
    # Fixing that means giving Codex the agent set first, not adding a router.
    #
    # `_SCOPE` filters before the once-guard is spent, not after: a turn whose only
    # recommendation is one Codex cannot act on must stay eligible for the next event
    # rather than be marked audited on the strength of a message never sent.
    keys = [k for k in core_agents._eligible_agents(state, []) if k in _SCOPE]
    if not keys:
        core_state._write_state(project_dir, session_id, state)
        return
    state["last_audited_prompt_id"] = turn_id
    core_state._write_state(project_dir, session_id, state)

    # Codex has ONE named agent (`guard_claims_auditor`, installed by `$guard:setup`),
    # so the per-agent fan-out Claude gets is expressed here as a scope sentence handed
    # to that single agent. The eligibility rules are shared (`core_agents._eligible_agents`);
    # what Claude adds on top is the router.
    scope = ", ".join(_SCOPE[k] for k in keys)
    _emit({"decision": "block", "reason": (
        "guard: before completing, audit the turn you just finished. Spawn the "
        "read-only guard_claims_auditor named subagent in a fresh context, give it the "
        f"saved turn record at {_turn_path(project_dir, session_id, turn_id)}, and have "
        f"it check {scope} against the repository; then address what it reports. If that "
        "agent is unavailable, tell the user to run $guard:setup in this project."
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
