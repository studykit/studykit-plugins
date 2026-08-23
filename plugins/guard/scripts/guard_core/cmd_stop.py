"""``stop`` (Stop) — the turn-end recommendation.

A turn == the transcript ``prompt_id``. guard reads ONE transcript record, for the turn's
kind only (``transcript._turn_identity``). It skips when ``stop_hook_active``, when the
prompt_id is absent, when the turn was opened by anything other than a person typing (a
background agent's completion, a subagent's ``SendMessage``: guard's own dispatch causes
those, so auditing them loops), when it was opened by one of guard's own control commands,
and when it was opened by a user ``!`` command (no ``UserPromptSubmit`` fired for it, so no
answer file was ever named).

Otherwise it records the turn as the pending ``/guard:<agent>`` target and fills in the answer
file if the turn left it empty — both regardless of the switches, because the on-demand
commands must work in a project that keeps everything off. Then, when any agent is eligible,
it emits ``additionalContext`` of ONE line: invoke the ``guard:audit`` skill with this turn's
id. The dispatch itself — which agents, in which mode, over which paths — is built by the
``dispatch`` CLI verb inside that skill (``dispatch.turn_dispatch_text``), so the text a
routed turn costs in the context the user is talking to is one sentence instead of the whole
roster. This hook decides only WHETHER there is anything to audit; it still computes that
here, because eligibility is a fact about the turn that just ended and the skill's own
recomputation would be a second answer to the same question.

guard runs no model itself and never blocks here.
"""

from __future__ import annotations

from .config import _load_config
from .paths import _project_dir, _trace
from .turnrec import _write_turn_response
from .payload import _read_payload, _session_id
from .emit import _emit_stop_context
from .transcript import _is_control_command_name, _turn_identity
from .state import _audit_paused, _read_state, _write_state
from .dispatch import _skill_trigger, turn_dispatch_text


def cmd_stop() -> int:
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0

    # Recursion / re-entry guard: never continue twice in a row.
    if payload.get("stop_hook_active") is True:
        _trace(project_dir, session_id, "stop", "skip_active")
        return 0

    response = payload.get("last_assistant_message")
    if not (isinstance(response, str) and response.strip()):
        return 0

    # The turn is the transcript prompt_id. Without it there is no per-turn marker to
    # write and no way to tell a real turn from a background completion — fail open.
    prompt_id = payload.get("prompt_id")
    if not (isinstance(prompt_id, str) and prompt_id):
        _trace(project_dir, session_id, "stop", "skip_no_prompt_id")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    # How the turn was opened decides whether guard says anything at all. Three skips, and
    # the first is not politeness: guard audits an answer to the USER, so a turn opened by
    # anything other than a person typing is machinery reporting in — a background agent's
    # completion, a subagent's `SendMessage` — and auditing it puts guard in a loop with
    # itself, since guard's own dispatch is what produced it. The turn also gets no record
    # file and does not become the `/guard:<agent>` target, so the main agent is left
    # holding exactly one answer file per question: the user's.
    #
    # Every named non-human kind is skipped rather than a list of the two seen so far, so a
    # kind added later cannot reopen the loop. An ABSENT kind still audits: if `origin`
    # stops being emitted, guard staying noisy is recoverable and guard going silently
    # dormant is not.
    identity = _turn_identity(payload.get("transcript_path"), prompt_id)
    if identity is not None:
        origin_kind = identity["origin_kind"]
        if origin_kind and origin_kind != "human":
            _trace(project_dir, session_id, "stop", "skip_nonhuman_turn",
                   prompt_id=prompt_id, origin_kind=origin_kind)
            return 0
        # A turn opened by one of guard's own control commands is guard reporting on
        # guard: the response is a relay of an audit, not an answer to a question the
        # user asked. Skipping it BEFORE the record write below is the load-bearing
        # part — were such a turn to become the pending target, the next
        # `/guard:<agent>` would audit the previous audit's relay instead of the answer
        # the user actually wants checked.
        cmd_name = identity["command_name"]
        if cmd_name and _is_control_command_name(cmd_name):
            _trace(project_dir, session_id, "stop", "skip_control_cmd",
                   prompt_id=prompt_id, command=cmd_name)
            return 0
        # A turn opened by a user `!` command. `UserPromptSubmit` does not fire for one —
        # a `!` command is not a prompt — so no answer file was ever named, and guard's
        # whole premise is audit-then-CORRECT: the answer has to exist somewhere editable
        # while the turn is still running. What Stop would hand an auditor here is the
        # fallback copy it just made of an answer already printed, which no correction can
        # reach. (Verified in 2.1.239, session 6bc60bbf: every turn in the transcript got
        # the draft path except the `!` one.) This skip was removed in v0.45.0 on a
        # different rationale — that guard cut the turn slice itself and the `!` output
        # landed after the response, so evidence trailed the claims. That reason is indeed
        # gone; this one replaces it, and is about the record, not the evidence.
        #
        # Before the record write, like the control-command skip above: a `!` turn must not
        # displace the user's actual question as the `/guard:<agent>` target.
        if identity.get("bash_input"):
            _trace(project_dir, session_id, "stop", "skip_bash_input", prompt_id=prompt_id)
            return 0

    # Both of these happen whether or not any switch is on. They are what the on-demand
    # `/guard:<agent>` commands target, and those are the user asking for an audit now —
    # refusing them because the automatic recommendation is off would take away the very
    # thing switching everything off is meant to leave in place.
    #
    # Writing the response here rather than in the recommendation path is deliberate: it
    # is the one part of the record guard is handed for free, and it is the part that must
    # not pass through the author's hands. An hour-old turn the user asks about is still
    # quoted exactly.
    state["pending_verify_prompt_id"] = prompt_id
    if isinstance(payload.get("transcript_path"), str):
        state["transcript_path"] = payload["transcript_path"]
    _write_turn_response(project_dir, session_id, prompt_id, response)

    # Muted by `/guard:toggle`. Checked AFTER the two lines above, on purpose: the pending
    # target and the response still get recorded, so `/guard:claims-auditor` on the turn the
    # user just muted still has something to audit. Muting stops the recommendation, not the
    # user's ability to ask for one.
    if _audit_paused(state):
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "skip_paused", prompt_id=prompt_id)
        return 0

    # Once per turn. `stop_hook_active` already covers the normal path, but the
    # recommendation asks the main agent to dispatch background agents, and each of
    # those completions opens a transcript turn of its own; a marker keyed on the
    # prompt_id does not depend on the payload flag surviving that.
    if state.get("last_audited_prompt_id") == prompt_id:
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "skip_already_recommended",
               prompt_id=prompt_id)
        return 0

    # Eligibility is decided HERE and the dispatch text is thrown away. The skill rebuilds
    # it from the same state a moment later, which sounds like waste and is the cheaper half
    # of the trade: this hook must know whether to say anything at all, and that question is
    # `_eligible_agents` either way. What it must NOT do is print the answer — every line it
    # prints is paid for in the main agent's context on every audited turn, and the roster,
    # the paths and the modes are exactly the lines only the audit needs.
    transcript = payload.get("transcript_path")
    transcript = transcript if isinstance(transcript, str) else ""
    _, outcome, eligible = turn_dispatch_text(project_dir, session_id, prompt_id, state,
                                              config, transcript)
    if not eligible:
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "none_eligible", prompt_id=prompt_id)
        return 0

    # The marker is spent before the recommendation goes out, not after. One
    # recommendation per turn, whatever the main agent does with it: the alternative is
    # a turn that gets re-recommended because the first dispatch is still in flight.
    state["last_audited_prompt_id"] = prompt_id
    _write_state(project_dir, session_id, state)

    # `additionalContext`, not `decision: "block"`. Per the official hooks docs
    # (https://code.claude.com/docs/en/hooks, "Stop decision control"; excerpt saved at
    # wiki/ref/claude-code-stop-hook-decision-control.md) the two continue the
    # conversation identically and share the same loop protections, but block is
    # reported as a hook ERROR while this shows as `Stop hook feedback`. A
    # recommendation is guard working as designed, so it must not look like a failure.
    _emit_stop_context(_skill_trigger(prompt_id))
    _trace(project_dir, session_id, "stop", outcome, prompt_id=prompt_id,
           eligible=",".join(eligible))
    return 0
