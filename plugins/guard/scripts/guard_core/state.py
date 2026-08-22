"""The per-session state file, ``state/<sid>.json``.

Holds the agent modes as of this session, ``audit_paused``, the files this turn edited
(``edited_prompt_id`` / ``edited_files`` / ``edited_agent_docs`` / ``edited_refs``),
``last_audited_prompt_id``, ``pending_verify_prompt_id``, ``transcript_path`` and
``updated_at``.

Both the ``default`` dict and the ``keys`` tuple in ``_read_state`` are the schema, and a new
key must be added to BOTH. A key missing from ``keys`` is written by whoever set it and then
dropped on the very next read, which looks exactly like the writer never ran — that is how
``edited_refs`` behaved for its first hour of existence.
"""

from __future__ import annotations

import json

from pathlib import Path
from typing import Any

from .config import _agent_mode
from .paths import _now_iso, _state_file
from .agents import AUDIT_AGENTS


def _read_state(project_dir: Path, session_id: str, config: dict[str, Any]) -> dict[str, Any]:
    default = {
        **{k: str(_agent_mode(config, k)) for k in AUDIT_AGENTS},
        # Per-turn guards keyed by the transcript prompt_id (a turn == one promptId).
        "last_audited_prompt_id": "",
        # The most recent auditable turn's prompt_id — the target a `/guard:<agent>`
        # command dispatches its agent for. Recorded by every Stop, switches or not.
        "pending_verify_prompt_id": "",
        # The session's transcript, recorded at Stop so the on-demand `/guard:*` path can
        # hand it to an agent that needs history. That payload does not carry it, and the
        # path is a session-long fact, so remembering it is cheaper than making the agent
        # go looking for a file it has no reliable way to name.
        "transcript_path": "",
        # Files written during one turn, accumulated by PostToolUse and read back at Stop
        # to decide whether a file-reading agent has anything to look at. Stored WITH the
        # prompt_id they belong to: a bare list would outlive its turn and point an agent
        # at files the current turn never touched. Three lists, one marker — the split is by
        # which agent can judge the file (source code for `comment-corrector`, instruction
        # files for `agents-md-auditor`, saved references for `refs-auditor`), while "which
        # turn was this" is the same question for all of them and a second marker could only
        # drift from the first.
        "edited_prompt_id": "",
        "edited_files": [],
        "edited_agent_docs": [],
        "edited_refs": [],
        # Session-only mute, flipped by `/guard:toggle`. NOT a mode in front of the agent
        # switches the way the removed `audit_gate` was: it lives only in session state, so
        # it can never change what the project does by default, and the `status` subcommand
        # puts it in the user's status line so the muted state is visible rather than
        # remembered. A hidden mute is the failure that killed the old gate.
        "audit_paused": False,
        "updated_at": None,
    }
    path = _state_file(project_dir, session_id)
    if not path.is_file():
        return default
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return default
    if not isinstance(data, dict):
        return default
    keys = (*AUDIT_AGENTS, "last_audited_prompt_id", "pending_verify_prompt_id",
            "transcript_path", "audit_paused", "edited_prompt_id", "edited_files",
            "edited_agent_docs", "edited_refs", "updated_at")
    default.update({k: data[k] for k in keys if k in data})
    return default


def _write_state(project_dir: Path, session_id: str, state: dict[str, Any]) -> None:
    state["updated_at"] = _now_iso()
    path = _state_file(project_dir, session_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
        tmp.replace(path)
    except OSError:
        pass


def _edited_files(state: dict[str, Any], prompt_id: str, bucket: str) -> list[str]:
    """The files of one bucket THIS turn wrote, as recorded by PostToolUse.

    Empty unless the recorded list belongs to this prompt_id and the files still exist:
    a turn that edited a file and then deleted or moved it leaves nothing to audit, and
    handing an agent a missing path would spend it on a read failure.
    """
    if state.get("edited_prompt_id") != prompt_id:
        return []
    files = state.get(bucket)
    if not isinstance(files, list):
        return []
    return [f for f in files if isinstance(f, str) and f and Path(f).is_file()]


def _audit_paused(state: dict[str, Any]) -> bool:
    """Is the automatic audit muted for this session? Only ever True from `/guard:toggle`."""
    return state.get("audit_paused") is True
