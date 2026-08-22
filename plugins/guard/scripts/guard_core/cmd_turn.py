"""``user-prompt`` and ``verify`` — the two hooks that run before an answer exists.

``user-prompt`` (UserPromptSubmit) names the file this turn's answer is to be written to, so
the answer exists somewhere editable while the turn is still running. It has to be this hook:
by Stop the answer is already printed, and a printed answer cannot be corrected. Silent when
no agent that reads the turn (``agents._reads_turn``) is on — which includes "every agent off"
but also a project running only ``comment-corrector`` — and for guard's own control commands.
It also saves the user's request verbatim, for the router alone.

``verify`` (UserPromptExpansion, one matcher per agent) emits the dispatch instruction for
that ONE agent over the last completed turn (``pending_verify_prompt_id``, recorded by every
Stop). A switch that is off is still auditable this way — the switch governs what guard
recommends unasked, not what the user may ask for.
"""

from __future__ import annotations

import sys

from .config import _agent_mode, _load_config, _switch_on
from .paths import _project_dir, _trace
from .turnrec import _turn_record_file, _write_turn_request
from .payload import _read_payload, _session_id
from .emit import _emit_expansion
from .transcript import _CONTROL_CMD_RE
from .agents import AUDIT_AGENTS, _reads_turn
from .state import _audit_paused, _read_state
from .dispatch import _DRAFT_LEAD, _dispatch_context


def cmd_user_prompt() -> int:
    """UserPromptSubmit. Names the file the turn's answer is written to, and saves the request.

    It has to be this hook, for both jobs. The draft path, because a Stop hook is too late:
    by the time Stop runs the answer has already been printed to the user, and a printed
    answer cannot be corrected — audit-then-correct only works if the answer also exists
    somewhere editable, and only the main agent can put it there while the turn is running.
    The request, because this is the only event that carries it; guard's turn store holds the
    answer and nothing else, and the router cannot go to the transcript for it.

    guard keeps no general copy of the user's prompt — it used to, as half of a turn store
    nothing reads any more. What `_write_turn_request` restores is narrower than what was
    removed: one reader, the router, and one question, how much of the answer the user
    actually asked for.

    Silent when no on agent reads the turn (``_reads_turn``) — an unconfigured guard, or one
    running only ``comment-corrector``, adds nothing to any prompt. Also silent for guard's
    own control commands, whose turns are never audited.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0
    prompt = payload.get("prompt")
    prompt = prompt if isinstance(prompt, str) else ""
    if _CONTROL_CMD_RE.match(prompt.strip()):
        _trace(project_dir, session_id, "user-prompt", "skip_control_cmd")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    # Muted by `/guard:toggle`: no audit is coming, so naming a file for the answer would
    # ask the user to read a file nothing is going to correct.
    if _audit_paused(state):
        _trace(project_dir, session_id, "user-prompt", "skip_paused")
        return 0
    prompt_id = payload.get("prompt_id")
    # Gated on the agents that READ the answer file, not on every switch: see `_reads_turn`.
    on = [k for k in AUDIT_AGENTS if _switch_on(state, k)]
    if not _reads_turn(on) or not (isinstance(prompt_id, str) and prompt_id):
        _trace(project_dir, session_id, "user-prompt", "seen")
        return 0

    # Before the lead, so a write that fails cannot be mistaken for the turn being
    # unroutable: the lead goes out either way and the router adapts to the file's absence.
    if prompt.strip():
        _write_turn_request(project_dir, session_id, prompt_id, prompt)
    path = _turn_record_file(project_dir, session_id, prompt_id).resolve()
    print(_DRAFT_LEAD.format(path=path))
    _trace(project_dir, session_id, "user-prompt", "draft_path", prompt_id=prompt_id)
    return 0


def cmd_verify() -> int:
    """UserPromptExpansion for the per-agent ``/guard:<agent>`` commands.

    The agent comes from argv (``verify claims-auditor`` | ``deferrals-auditor`` |
    ``clarity-auditor`` | ``korean-corrector``), one per command, so each skill dispatches
    exactly its own agent and the choice is not a dispatch input the model has to be
    trusted to honor.

    Works regardless of the switches: a switch governs what guard recommends UNASKED,
    while running the command is the user asking for this one audit now. Refusing it
    would leave the user no way to check the very agent they keep switched off, which is
    the main reason to keep it off in the first place.

    ``pending_verify_prompt_id`` names the turn, and the record for it already holds that
    turn's response — every Stop writes that section, whatever the switches say, which is
    what makes this command work in a project that keeps every switch off. The main agent
    still appends the request, the tool activity, and the earlier evidence, exactly as on
    a routed turn.
    """
    key = sys.argv[2].strip().lower() if len(sys.argv) > 2 else ""
    spec = AUDIT_AGENTS.get(key)
    if spec is None or not spec.verify_command:
        return 0
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    pid = state.get("pending_verify_prompt_id") or ""
    if not pid:
        _emit_expansion("guard: no completed turn is available to audit yet. "
                        f"Ask something first, then run `/guard:{key}`.")
        _trace(project_dir, session_id, "verify", "no_pending", agent=key)
        return 0

    context = _dispatch_context(
        project_dir, session_id, pid,
        "guard: audit the last completed turn, on request.", [key],
        {key: _agent_mode(state, key)},
        transcript=str(state.get("transcript_path") or ""))
    _emit_expansion(context)
    _trace(project_dir, session_id, "verify", "dispatch", agent=key, prompt_id=pid)
    return 0
