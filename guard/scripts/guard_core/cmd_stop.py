"""``stop`` (Stop) — the turn-end record, and the turn's closeout.

A turn == the transcript ``prompt_id``. guard reads ONE transcript record, for the turn's
kind only (``transcript._turn_identity``). It skips when ``stop_hook_active``, when the
prompt_id is absent, when the turn was opened by anything other than a person typing (a
background agent's completion, a subagent's ``SendMessage``: guard's own dispatch causes
those, so auditing them loops), when it was opened by one of guard's own control commands,
and when it was opened by a user ``!`` command (no ``UserPromptSubmit`` fired for it, so no
answer file was ever named).

Otherwise it records the turn as the pending on-demand target and fills in the answer
file if the turn left it empty — both regardless of the switches, because an on-demand audit
must work in a project that keeps everything off.

**No audit is recommended here.** The turn audit is the user's to ask for
(``/guard:audit-turn``, or one ``audit-turn-*`` skill by name), and this hook's turn block
says so: it carries the answer file — whose basename is the turn id the user's command
resolves to — the closeout path until this session has been told it once, and the prohibition
on routing the turn unasked. Recommending one on every finished
turn spent a router on turns that plainly had nothing in them, and a recommendation that
fires whether or not it is wanted is one the user learns to wave through.

Two blocks still name an agent, and neither is a triage question. The eligible file-reading
agents — ``comment-corrector`` (``reads="files"``) and ``agents-md-auditor``
(``reads="agent-docs"``) — are dispatched over the files this turn actually edited, and
``ext-docs-auditor`` over anything it wrote under the refs directory; in both cases the
condition is a file list rather than a judgment about the answer, so there is nothing for the
user to decide and nothing for a router to weigh. Either can be the only block a turn
produces. guard runs no model itself and never blocks here.
"""

from __future__ import annotations

from .config import _agent_mode, _load_config
from .paths import _project_dir, _trace
from .turnrec import _write_turn_response
from .payload import _read_payload, _session_id
from .emit import _emit_stop_context
from .transcript import _is_control_command_name, _turn_identity
from .agents import AUDIT_AGENTS, _eligible_agents
from .state import _audit_paused, _edited_files, _read_state, _write_state
from .dispatch import (
    _DIRECT_LEAD, _DIRECT_LEAD_WITH_TURN, _TURN_LEAD, _dispatch_context, _refs_context,
    _turn_context
)


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
    # file and does not become the on-demand target, so the main agent is left
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
        # on-demand audit would audit the previous audit's relay instead of the answer
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
        # displace the user's actual question as the on-demand target.
        if identity.get("bash_input"):
            _trace(project_dir, session_id, "stop", "skip_bash_input", prompt_id=prompt_id)
            return 0

    # Both of these happen whether or not any switch is on. They are what an on-demand audit
    # targets — the user asking for one now — and refusing that because a switch is off would
    # take away the very thing switching everything off is meant to leave in place. The marker
    # is load-bearing on both hosts now: `guard-inputs` with no turn id resolves it, which is
    # how `/guard:audit-turn` finds the turn the user means without the caller having to
    # remember an id, and the Codex adapter reads the same key.
    #
    # Writing the response here rather than in the recommendation path is deliberate: it
    # is the one part of the record guard is handed for free, and it is the part that must
    # not pass through the author's hands. An hour-old turn the user asks about is still
    # quoted exactly.
    state["pending_verify_prompt_id"] = prompt_id
    if isinstance(payload.get("transcript_path"), str):
        state["transcript_path"] = payload["transcript_path"]
    _write_turn_response(project_dir, session_id, prompt_id, response)

    # Muted by `guard off`. Checked AFTER the two lines above, on purpose: the pending
    # target and the response still get recorded, so the turn is still there to work on if
    # the user arms guard and asks. `guard off` means guard says nothing unasked — the
    # closeout block, the file audits, the answer file — and `guard-candidates` keeps the
    # other half of it, so an audit invoked while muted is told the session is muted rather
    # than quietly running against switches the user turned off.
    if _audit_paused(state):
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "skip_paused", prompt_id=prompt_id)
        return 0

    # Once per turn. `stop_hook_active` already covers the normal path, but the block below
    # asks the main agent to dispatch background agents, and each of those completions opens
    # a transcript turn of its own; a marker keyed on the prompt_id does not depend on the
    # payload flag surviving that.
    if state.get("last_audited_prompt_id") == prompt_id:
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "skip_already_recommended",
               prompt_id=prompt_id)
        return 0

    edited = _edited_files(state, prompt_id, "edited_files")
    agent_docs = _edited_files(state, prompt_id, "edited_agent_docs")
    # No switch and no eligibility computation: `ext-docs-auditor` is named whenever this turn
    # wrote a file under the refs directory. That list is the whole condition, so this is
    # independent of `_eligible_agents` and of every switch — a project can have all of them
    # off and still be told to check a reference it just saved.
    refs = _edited_files(state, prompt_id, "edited_refs")
    eligible = _eligible_agents(state, edited, agent_docs)
    modes = {k: _agent_mode(state, k) for k in eligible}
    if not eligible and not refs:
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "none_eligible", prompt_id=prompt_id)
        return 0

    # The marker is spent before the context goes out, not after. One block per turn,
    # whatever the main agent does with it: the alternative is a turn that gets its closeout
    # named twice because the first dispatch is still in flight. `closeout_stated` is spent in
    # the same write and for the same reason — it is the record that this session has been
    # told where the closeout file is, and a block that went out without the write landing
    # would state the path on every turn thereafter.
    state["last_audited_prompt_id"] = prompt_id
    # Spent only when a turn block is actually going out. A turn with nothing but file audits
    # names no closeout, so marking the path as stated there would consume the one turn that
    # was going to print it.
    turn_agents = [k for k in eligible if AUDIT_AGENTS[k].reads == "turn"]
    with_closeout = bool(turn_agents) and not state.get("closeout_stated")
    if with_closeout:
        state["closeout_stated"] = True
    _write_state(project_dir, session_id, state)

    transcript = payload.get("transcript_path")
    transcript = transcript if isinstance(transcript, str) else ""
    # Split by what each agent reads, because only one of the two groups is a question at
    # all. Whether the ANSWER is worth auditing is a judgment about this turn, so it is the
    # user's to make and nothing is dispatched for it here. For a file-reading agent there is
    # no such judgment to make: the turn either edited a file of its kind or it did not, the
    # list is the agent's whole input, and `_eligible_agents` has already answered it. So
    # these go out as they always did — asking the user to confirm a file list would be asking
    # them to re-decide what the switch already decided.
    #
    # The two blocks need no ordering between them either. The file-reading agents never open
    # the answer file, so they share no input with the turn's own delivery and none of the
    # closeout's ordering applies to them. They need no ordering among themselves: their file
    # lists are disjoint by construction (`_edited_bucket`), so the one that edits cannot
    # touch what the one that only reports is reading.
    direct = [k for k in eligible
              if AUDIT_AGENTS[k].reads in ("files", "agent-docs")]
    blocks: list[str] = []
    if turn_agents:
        blocks.append(_turn_context(project_dir, session_id, prompt_id, _TURN_LEAD,
                                    with_closeout))
    if direct:
        lead = _DIRECT_LEAD_WITH_TURN if turn_agents else _DIRECT_LEAD
        blocks.append(_dispatch_context(
            project_dir, session_id, prompt_id, lead, direct, modes,
            {"files": edited, "agent-docs": agent_docs}, transcript))
    if refs:
        blocks.append(_refs_context(refs))
    context = "\n\n".join(blocks)
    parts = [n for n, on in (("turn", turn_agents), ("direct", direct), ("refs", refs)) if on]
    outcome = "+".join(parts)
    # `additionalContext`, not `decision: "block"`. Per the official hooks docs
    # (https://code.claude.com/docs/en/hooks, "Stop decision control"; excerpt saved at
    # wiki/ref/claude-code-stop-hook-decision-control.md) the two continue the
    # conversation identically and share the same loop protections, but block is
    # reported as a hook ERROR while this shows as `Stop hook feedback`. Naming a turn's
    # closeout is guard working as designed, so it must not look like a failure.
    _emit_stop_context(context)
    _trace(project_dir, session_id, "stop", outcome, prompt_id=prompt_id,
           eligible=",".join(eligible))
    return 0
