"""``exit-plan`` and ``plan-toggle-cli`` — the gate in front of an unaudited plan.

``exit-plan`` is a PostToolUse hook on ``ExitPlanMode``: the audit is required at the moment
the user APPROVES a plan, before it is built. A skill the model chooses to invoke is a skill it
can also forget, and a plan reaches approval either way.

PostToolUse rather than PreToolUse, and the difference is the whole design. ``ExitPlanMode``
presents a plan and the user answers it three ways: approve (two variants) or "tell Claude what
to change". Only the approvals execute the tool — choosing to give feedback runs no tool at all,
so PostToolUse never fires for it (measured, not assumed). PreToolUse fires before that choice
exists and therefore cannot tell them apart, which made it demand a full review of plans the
user was about to send back for revision anyway.

It also decides WHEN the audit runs. The audit used to be invoked from inside plan mode, before
the plan was presented, which works and makes plan mode unusable while it runs: the review takes
minutes and holds the turn, so the user cannot talk to the session about the plan they are in the
middle of shaping — which is what plan mode is for. Gating on approval moves the review after
that conversation has finished, and blocking after the tool ran is not too late: approval ends
plan mode, it does not build anything.

The gate is content-addressed, not a flag. ``plan_audited_hash`` records the hash of the plan
text that was audited, and an approval passes only while the plan still hashes to it. Revise the
plan after its audit and the next approval is held again — which is the behaviour worth having,
because the audited plan and the approved plan are then the same document. A boolean would let an
edit ride through on the previous plan's clearance.

``plan-toggle-cli`` is the session switch, the same shape as ``toggle-cli`` for the turn audit
(``cmd_status``) and reached from the shell the same way, through ``guard-plan``. It writes
``plan_audit_paused`` and nothing else, so muting the plan audit cannot alter the turn audit or
touch guard.local.json — the project's own default for it is the ``audit-plan`` setting, which
seeds this at session start and which only ``/guard:settings`` writes.
"""

from __future__ import annotations

import hashlib
import os
import sys

from pathlib import Path

from .config import _load_config
from .emit import _emit_post_tool_block
from .paths import _cli_project_dir, _project_dir, _trace
from .payload import _read_payload, _session_id
from .state import _plan_audit_paused, _read_state, _write_state
from .cmd_status import _parse_toggle_arg


def _plan_hash(plan: str) -> str:
    """Identify a plan by its text, so a revised plan is a different plan.

    Whitespace at the edges is stripped; nothing else is normalised. A plan that differs only
    in trailing newlines is the same plan, and any other edit — a reordered step, a softened
    caveat — is not, which is the conservative direction: re-auditing a plan that did not
    really change costs time, while letting a changed one through costs the guarantee.
    """
    return hashlib.sha256(plan.strip().encode("utf-8")).hexdigest()


def cmd_exit_plan() -> int:
    """PostToolUse on ``ExitPlanMode``: require the plan audit once a plan is approved.

    Silent when the session has the plan audit muted, when there is no session id or plan text
    to work with, or when the plan already hashes to the audited one. Blocks otherwise, with a
    reason that tells the model to audit the plan before building it.

    Fail-OPEN in every failure branch. A hook that cannot read its own state must not be able
    to wedge an approved plan — the audit is worth having, and it is not worth stalling a
    session over.
    """
    payload = _read_payload()
    if payload is None:
        return 0
    project_dir = _project_dir()
    session_id = _session_id(payload)
    if not session_id:
        return 0

    # The RESPONSE carries the plan as approved, alongside the plan file's path; the request
    # carries it too, and reading the response keeps this reading the same object the user just
    # said yes to.
    response = payload.get("tool_response")
    request = payload.get("tool_input") or {}
    source = response if isinstance(response, dict) else request
    plan = (source.get("plan") or request.get("plan") or "")
    if not isinstance(plan, str) or not plan.strip():
        # No plan text to identify. Auditing an empty string proves nothing, and blocking on
        # it would block every ExitPlanMode whose payload shape we did not anticipate.
        _trace(project_dir, session_id, "exit-plan", "no_plan_text")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    if _plan_audit_paused(state):
        _trace(project_dir, session_id, "exit-plan", "muted")
        return 0

    if state.get("plan_audited_hash") == _plan_hash(plan):
        _trace(project_dir, session_id, "exit-plan", "audited")
        return 0

    revised = state.get("plan_audited_hash") is not None
    what = ("This approved plan has changed since it was audited"
            if revised else "This plan was approved without being audited")
    _emit_post_tool_block(
        f"{what}. Do not start building it. Run the `guard:audit-plan` skill over the plan "
        "file first, then act on what comes back: fold in what the critics found, and put "
        "anything that changes the approach to the user before you build it. "
        "`guard-plan off` in Bash turns this off for the session if the user asks for it."
    )
    _trace(project_dir, session_id, "exit-plan", "revised" if revised else "unaudited")
    return 0


def cmd_plan_audited() -> int:
    """Record that the plan at ``<path>`` has been audited.

        plan-audited <plan-file-path>

    Run by the ``guard:audit-plan`` skill when its review is finished. It hashes the file as
    it stands at that moment, which is deliberately AFTER the skill has folded the findings
    in: the audited plan is the revised one, and recording the pre-revision text would make
    the very edits the audit asked for look like tampering.

    Fail-open and quiet: on a missing session, an unreadable file or an unwritable state
    directory it says so on stderr and exits 0. The cost is one more ExitPlanMode denial,
    which the skill can answer by running again.
    """
    session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    project_dir = _cli_project_dir()
    if not session_id:
        print("guard plan-audited: no CLAUDE_CODE_SESSION_ID in this environment.",
              file=sys.stderr)
        return 0
    if len(sys.argv) < 3 or not sys.argv[2].strip():
        print("guard plan-audited: needs the plan file path.", file=sys.stderr)
        return 0

    path = Path(sys.argv[2].strip()).expanduser()
    try:
        plan = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"guard plan-audited: cannot read {path} ({exc}).", file=sys.stderr)
        _trace(project_dir, session_id, "plan-audited", "unreadable")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    state["plan_audited_hash"] = _plan_hash(plan)
    _write_state(project_dir, session_id, state)
    print("guard: plan audit recorded — approval passes while the plan is unchanged.")
    _trace(project_dir, session_id, "plan-audited", "recorded")
    return 0


def _plan_sentence(paused: bool) -> str:
    """The one description of the plan-audit switch, for setting it and for reporting it."""
    if paused:
        return ("guard: plan audits OFF for this session. `guard-plan on` to arm — an "
                "approved plan then gets audited before it is built.")
    return ("guard: plan audits ON for this session. An approved plan is held before it is "
            "built until it has been through `guard:audit-plan`.")


def cmd_plan_toggle_cli() -> int:
    """Arm or mute the plan audit for this session, from the shell.

        plan-toggle-cli [on|off|status]

    Session-scoped like the turn audit's mute, and separate from it: the two audits run at
    different moments on different material, so one switch for both would arm a review the
    user did not ask for. The state a session opens in is the project's ``audit-plan``
    setting, armed when the config says nothing (``state._read_state``).
    """
    session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    project_dir = _cli_project_dir()
    if not session_id:
        print("guard-plan: no CLAUDE_CODE_SESSION_ID — this command works inside a Claude "
              "Code session.", file=sys.stderr)
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    raw = sys.argv[2] if len(sys.argv) > 2 else ""

    if raw.strip().lower() == "status":
        print(_plan_sentence(_plan_audit_paused(state)))
        return 0

    action = _parse_toggle_arg(raw)
    if action is None:
        print(f"guard-plan: don't know '{raw.strip()}' — use on, off, or status.",
              file=sys.stderr)
        return 0

    paused = (not _plan_audit_paused(state)) if action == "flip" else (action == "off")
    state["plan_audit_paused"] = paused
    # Arming mid-session must not clear a hash the user has already earned, and muting must
    # not keep one that would let a later, unrelated plan through: only the switch moves here.
    _write_state(project_dir, session_id, state)
    print(_plan_sentence(paused))
    _trace(project_dir, session_id, "plan-toggle", "off" if paused else "on")
    return 0
