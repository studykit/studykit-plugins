"""The per-session state file, ``state/<sid>.json``.

Holds the agent modes as of this session, the two audit mutes (``audit_paused`` /
``plan_audit_paused``, seeded from the project's ``audit-turn`` / ``audit-plan``), the files this turn edited
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

from .config import AUDIT_PLAN_KEY, AUDIT_TURN_KEY, _agent_mode, _audit_on
from .paths import _now_iso, _state_file
from .agents import AUDIT_AGENTS


def _read_state(project_dir: Path, session_id: str, config: dict[str, Any]) -> dict[str, Any]:
    default = {
        # Switchable agents only. A `fixed_mode` agent has no config key, so there is no
        # mode to seed and nothing the session could move it to — its mode is the roster's.
        # Seeding one here would also make it look settable in `settings show`.
        **{k: str(_agent_mode(config, k))
           for k, spec in AUDIT_AGENTS.items() if spec.fixed_mode is None},
        # Per-turn guards keyed by the transcript prompt_id (a turn == one promptId).
        "last_audited_prompt_id": "",
        # The most recent auditable turn's prompt_id, recorded by every Stop, switches or
        # not. Only the CODEX adapter reads it, for its `/guard:claims-auditor` prompt-prefix
        # path; Claude's per-agent commands were removed. Kept written on both hosts because
        # `cmd_stop` is shared core and because a marker maintained only from the day a host
        # gains an on-demand path back is a marker that is wrong on that day.
        "pending_verify_prompt_id": "",
        # The session's transcript, recorded at Stop. The Stop payload carries it and the
        # `UserPromptSubmit` one does not, and it is a session-long fact, so remembering it
        # here is cheaper than making an agent go looking for a file it has no reliable way
        # to name.
        "transcript_path": "",
        # Files written during one turn, accumulated by PostToolUse and read back at Stop
        # to decide whether a file-reading agent has anything to look at. Stored WITH the
        # prompt_id they belong to: a bare list would outlive its turn and point an agent
        # at files the current turn never touched. Three lists, one marker — the split is by
        # which agent can judge the file (source code for `comment-corrector`, instruction
        # files for `agents-md-auditor`, saved references for `ext-docs-auditor`), while "which
        # turn was this" is the same question for all of them and a second marker could only
        # drift from the first.
        "edited_prompt_id": "",
        "edited_files": [],
        "edited_agent_docs": [],
        "edited_refs": [],
        # Session-only mute, flipped by the `guard` shell command. The value a session OPENS
        # in is the project's `audit-turn` setting, armed when the file says nothing; from
        # then on this key is the session's own, and the toggle never writes back to the
        # config — so muting the session you are in cannot change what the next one does.
        # NOT a mode in front of the agent switches the way the removed `audit_gate` was:
        # it is two-valued, and the `status` subcommand puts it in the user's status line so
        # the muted state is visible rather than remembered. A hidden mute is the failure
        # that killed the old gate, which is why `session-start` says which state the session
        # opened in.
        "audit_paused": not _audit_on(config, AUDIT_TURN_KEY),
        # The plan audit reads its own config key, and is a SEPARATE key here, because the two
        # run at different moments on different material — one on a finished answer, one on a
        # plan awaiting approval — and a user who wants their turns audited has not thereby
        # asked for every plan to be.
        "plan_audit_paused": not _audit_on(config, AUDIT_PLAN_KEY),
        # Which plan this session has already audited, as a hash of the plan text. The
        # ExitPlanMode hook lets a plan through once its audit is recorded here and blocks
        # it otherwise; hashing the CONTENT rather than setting a flag is what makes a
        # revised plan a new plan — edit it after the audit and the hash no longer matches,
        # so the next ExitPlanMode is blocked again and the audit runs against what the user
        # will actually see.
        "plan_audited_hash": None,
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
            "transcript_path", "audit_paused", "plan_audit_paused", "plan_audited_hash",
            "edited_prompt_id", "edited_files",
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


def _plan_audit_paused(state: dict[str, Any]) -> bool:
    """Whether the plan audit is muted for this session.

    Mirrors ``_audit_paused``, including the absent case: ``_read_state`` seeds both keys from
    the config on every read, so a dict reaching here without one did not come from there, and
    the honest answer for a missing key is the config default — armed.
    """
    return state.get("plan_audit_paused") is True


def _audit_paused(state: dict[str, Any]) -> bool:
    """Is the automatic audit muted for this session?

    The session's own answer, not the project's: `_read_state` seeds it from `audit-turn` and
    `guard off` overrides it for the rest of the session.
    """
    return state.get("audit_paused") is True
