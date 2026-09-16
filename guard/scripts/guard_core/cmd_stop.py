"""``stop`` (Stop) — the edited-file audits, and nothing else.

A turn == the transcript ``prompt_id``, and this hook now uses it only as the key the
``PostToolUse`` hook filed this turn's edits under. It records nothing about the turn, names
no answer file, and reads none of the response.

Everything it used to do about the turn's TEXT is gone as of v0.122.0. The answer file moved
to ``/guard:answer``, which writes its own; the turn audit resolves its target by walking the
transcript when the user asks for one (``transcript._last_auditable_prompt_id``), so there is
no marker to keep and no copy to make. The three skips that protected that marker — non-human
origin, guard's own control commands, a user ``!`` command — moved with it.

What is left is the file-reading audits. Native write targets are exact; Bash candidates are
conditional because a shared-worktree diff may include another session's write. The Stop
context tells the main session to use its own tool activity to discard those foreign paths
before dispatch. ``comment-corrector`` covers source files, while configured document-review
actions cover ordinary, agent-instruction and reference Markdown files. Nothing routes on the
answer text, guard runs no model itself, and it never blocks here.

The fixed source bucket names an AGENT. All project Markdown is matched against
project-configured review actions, which may name either an agent or a skill.
"""

from __future__ import annotations

from pathlib import Path

from .config import _agent_mode, _doc_review_rule, _doc_review_rules, _load_config
from .paths import _project_dir, _project_rel, _trace
from .payload import _read_payload, _session_id
from .emit import _emit_stop_context
from .agents import AUDIT_AGENTS, _eligible_agents
from .state import (_audit_paused, _edit_source, _edited_files, _edited_fingerprint,
                    _read_state, _write_state)
from .dispatch import (_DIRECT_LEAD, _REVIEW_TIMING, _SHELL_DIRECT_LEAD,
                       _dispatch_context, _docs_context)
from .cmd_edit import EDITED_FILES_MAX, recover_shell_writes


def cmd_stop() -> int:
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0

    # The turn is the transcript prompt_id, and here it is only the key `post-edit` filed
    # this turn's edits under. Without it there is nothing to look up — fail open.
    prompt_id = payload.get("prompt_id")
    if not (isinstance(prompt_id, str) and prompt_id):
        _trace(project_dir, session_id, "stop", "skip_no_prompt_id")
        return 0

    config = _load_config(project_dir)
    # A cancelled Bash call has no post-tool event. Its pre-snapshot still lets Stop
    # recover any writes completed before the interruption.
    recover_shell_writes(project_dir, payload, config)
    state = _read_state(project_dir, session_id, config)

    # Muted by `guard off`: guard says nothing unasked. This is the ONLY reader of that mute
    # — `guard-candidates` deliberately does not read it, so an audit the user types while
    # muted still runs. The mute governs what guard volunteers, not what it is asked for.
    if _audit_paused(state):
        _trace(project_dir, session_id, "stop", "skip_paused", prompt_id=prompt_id)
        return 0

    fingerprint = _edited_fingerprint(state, prompt_id)
    # Re-entry with identical contents is the ordinary Stop-hook continuation and is skipped.
    # If applying review findings changed a retained file, its fingerprint differs and the
    # corrected document gets one more pass in the same turn.
    if (state.get("last_audited_prompt_id") == prompt_id
            and state.get("last_audited_fingerprint") == fingerprint):
        _trace(project_dir, session_id, "stop", "skip_already_recommended",
               prompt_id=prompt_id)
        return 0

    edited = _edited_files(state, prompt_id, "edited_files")
    agent_docs = _edited_files(state, prompt_id, "edited_agent_docs")
    refs = _edited_files(state, prompt_id, "edited_refs")
    # Filtered to what reads FILES. `_eligible_agents` still answers for the whole roster,
    # and the turn-reading audits are in it — but nothing dispatches them from here any more,
    # so letting one through would put a turn audit back on the automatic path.
    docs = [*refs, *agent_docs, *_edited_files(state, prompt_id, "edited_docs")]
    passed = _eligible_agents(state, edited, [], docs)
    eligible = [k for k in passed if AUDIT_AGENTS[k].reads == "files"]
    # Split out of `eligible`: document review rules may name either a skill or a direct
    # agent. Eligibility remains `_eligible_agents`' answer — the switch and a non-empty
    # list, same two gates as the rest — so nothing about WHEN it runs is decided here.
    docs_enabled = "doc-auditor" in passed
    docs_review_rules = _doc_review_rules(config)
    # The most-specific matching per-file rule wins. An unmatched document has no dispatch;
    # grouping keeps one action to one dispatch across several documents.
    doc_groups: dict[tuple[str, str, bool], list[str]] = {}
    if docs_enabled:
        for path in docs:
            rule = _doc_review_rule(_project_rel(project_dir, Path(path)), docs_review_rules)
            if rule is None:
                continue
            conditional = _edit_source(state, path) != "native"
            doc_groups.setdefault((rule.kind, rule.name, conditional), []).append(path)
    modes = {k: _agent_mode(state, k) for k in eligible}
    if not eligible and not doc_groups:
        _trace(project_dir, session_id, "stop", "none_eligible", prompt_id=prompt_id)
        return 0

    # The marker is spent before the context goes out, not after. One block per turn,
    # whatever the main agent does with it: the alternative is a turn that gets its block
    # emitted twice because the first dispatch is still in flight.
    state["last_audited_prompt_id"] = prompt_id
    state["last_audited_fingerprint"] = fingerprint
    _write_state(project_dir, session_id, state)

    # The three blocks need no ordering between them. They need none among themselves either:
    # their file lists are disjoint by construction (`_edited_bucket`), so the one that edits
    # cannot touch what the ones that only report are reading.
    blocks: list[str] = []
    if eligible:
        lead = (_SHELL_DIRECT_LEAD
                if any(_edit_source(state, path) != "native" for path in edited)
                else _DIRECT_LEAD)
        blocks.append(_dispatch_context(
            project_dir, session_id, prompt_id, lead, eligible, modes,
            {"files": edited}, ""))
    if doc_groups:
        for (action_kind, action_name, conditional), group in doc_groups.items():
            blocks.append(_docs_context(group, action_kind=action_kind,
                                        action_name=action_name,
                                        conditional=conditional))
    truncated = state.get("edited_truncated")
    if isinstance(truncated, dict) and truncated:
        omitted = sum(v for v in truncated.values() if isinstance(v, int) and v > 0)
        if omitted:
            blocks.append(
                f"guard: the per-turn review list reached its {EDITED_FILES_MAX}-file-per-category limit; "
                f"{omitted} additional changed file(s) are not listed. Tell the user the "
                "review was partial instead of implying that every changed file was checked."
            )
    context = "\n\n".join([_REVIEW_TIMING, *blocks])
    outcome = "+".join(n for n, on in (("direct", eligible), ("docs", doc_groups)) if on)
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
