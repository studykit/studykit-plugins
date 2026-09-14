"""``stop`` (Stop) — the edited-file audits, and nothing else.

A turn == the transcript ``prompt_id``, and this hook now uses it only as the key the
``PostToolUse`` hook filed this turn's edits under. It records nothing about the turn, names
no answer file, and reads none of the response.

Everything it used to do about the turn's TEXT is gone as of v0.122.0. The answer file moved
to ``/guard:answer``, which writes its own; the turn audit resolves its target by walking the
transcript when the user asks for one (``transcript._last_auditable_prompt_id``), so there is
no marker to keep and no copy to make. The three skips that protected that marker — non-human
origin, guard's own control commands, a user ``!`` command — moved with it.

What is left is the file-reading audits, and none of them is a triage question. The eligible
ones — ``comment-corrector`` (``reads="files"``) and ``agents-md-auditor``
(``reads="agent-docs"``) — are dispatched over the files this turn actually edited,
``ext-docs-auditor`` over anything it wrote under the refs directory, and ``doc-auditor`` over
the ordinary documents it changed; in each case the condition is a file list rather than a
judgment about the answer, so there is nothing for the user to decide and nothing for a router
to weigh. guard runs no model itself and never blocks here.

Three of the four are named as AGENTS and the fourth as a SKILL — see ``dispatch._DOCS_LEAD``
for why that difference is in the document audit and not in the others.
"""

from __future__ import annotations

from .config import _agent_mode, _load_config
from .paths import _project_dir, _trace
from .payload import _read_payload, _session_id
from .emit import _emit_stop_context
from .agents import AUDIT_AGENTS, EDIT_PATH, _eligible_agents, _path_entry
from .state import _audit_paused, _edited_files, _read_state, _write_state
from .dispatch import _DIRECT_LEAD, _dispatch_context, _docs_context, _refs_context


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

    # The turn is the transcript prompt_id, and here it is only the key `post-edit` filed
    # this turn's edits under. Without it there is nothing to look up — fail open.
    prompt_id = payload.get("prompt_id")
    if not (isinstance(prompt_id, str) and prompt_id):
        _trace(project_dir, session_id, "stop", "skip_no_prompt_id")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    # Muted by `guard off`: guard says nothing unasked. `guard-candidates` keeps the other
    # half of it, so an audit the user invokes while muted is told the session is muted
    # rather than quietly running against switches they turned off.
    if _audit_paused(state):
        _trace(project_dir, session_id, "stop", "skip_paused", prompt_id=prompt_id)
        return 0

    # Once per turn. `stop_hook_active` already covers the normal path, but the block below
    # asks the main agent to dispatch background agents, and each of those completions opens
    # a transcript turn of its own; a marker keyed on the prompt_id does not depend on the
    # payload flag surviving that.
    if state.get("last_audited_prompt_id") == prompt_id:
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
    # Filtered to what reads FILES. `_eligible_agents` still answers for the whole roster,
    # and the turn-reading audits are in it — but nothing dispatches them from here any more,
    # so letting one through would put a turn audit back on the automatic path.
    docs = _edited_files(state, prompt_id, "edited_docs")
    passed = _eligible_agents(state, edited, agent_docs, docs)
    eligible = [k for k in passed if AUDIT_AGENTS[k].reads in ("files", "agent-docs")]
    # Split out of `eligible` because it is named as a SKILL, not dispatched as an agent:
    # `_agent_pointer` builds one block for however many agents came through, and a skill
    # cannot ride in it. Eligibility is still `_eligible_agents`' answer — the switch and a
    # non-empty list, same two gates as the rest — so nothing about WHEN it runs is decided
    # here.
    docs_entry = _path_entry("doc-auditor", EDIT_PATH) if "doc-auditor" in passed else None
    modes = {k: _agent_mode(state, k) for k in eligible}
    if not eligible and not refs and docs_entry is None:
        _trace(project_dir, session_id, "stop", "none_eligible", prompt_id=prompt_id)
        return 0

    # The marker is spent before the context goes out, not after. One block per turn,
    # whatever the main agent does with it: the alternative is a turn that gets its block
    # emitted twice because the first dispatch is still in flight.
    state["last_audited_prompt_id"] = prompt_id
    _write_state(project_dir, session_id, state)

    # The three blocks need no ordering between them. They need none among themselves either:
    # their file lists are disjoint by construction (`_edited_bucket`), so the one that edits
    # cannot touch what the ones that only report are reading.
    blocks: list[str] = []
    if eligible:
        blocks.append(_dispatch_context(
            project_dir, session_id, prompt_id, _DIRECT_LEAD, eligible, modes,
            {"files": edited, "agent-docs": agent_docs}, ""))
    if refs:
        blocks.append(_refs_context(refs))
    if docs_entry is not None:
        blocks.append(_docs_context(docs_entry, docs))
    context = "\n\n".join(blocks)
    outcome = "+".join(n for n, on in (("direct", eligible), ("refs", refs),
                                       ("docs", docs_entry)) if on)
    # `additionalContext`, not `decision: "block"`. Per the official hooks docs
    # (https://code.claude.com/docs/en/hooks, "Stop decision control"; excerpt saved at
    # wiki/ref/claude-code-stop-hook-decision-control.md) the two continue the
    # conversation identically and share the same loop protections, but block is
    # reported as a hook ERROR while this shows as `Stop hook feedback`. Naming an audit
    # over files the turn edited is guard working as designed, so it must not look like a
    # failure.
    _emit_stop_context(context)
    _trace(project_dir, session_id, "stop", outcome, prompt_id=prompt_id,
           eligible=",".join(eligible))
    return 0
