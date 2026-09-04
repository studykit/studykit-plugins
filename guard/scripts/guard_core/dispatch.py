"""The text guard hands the main agent.

Where each piece of text lives is decided by how often it is paid for, and that split must
hold. What this module builds reaches the main agent on every turn that has an answer file,
so it is one imperative plus a list of fields: paths, which agents are on, each one's mode.
``agents/turn-router.md`` is read once per AUDIT — and an audit happens only when the user
asks for one — so it carries the triage method and the dispatch per candidate.
``hooks/context/turn-closeout.md`` is read by the turn that has a file to deliver, so it
carries how the turn is delivered and what to do once an audit has reported. Nobody re-types
another home's text.
"""

from __future__ import annotations

from pathlib import Path

from .config import AgentMode
from .turnrec import _turn_record_file
from .agents import AUDIT_AGENTS


# The input line each file-reading agent's path list is introduced by. Worded as what the
# agent is being handed, not as what to look for: the criteria are the agent's own and live
# in its definition, so a lead that previewed them would be the caller telling it what to
# find. The `in place` on the corrector is the exception and is not a criterion — it warns
# the main agent that those files come back changed.
_FILE_INPUT_LABELS = {
    "files": "- files to audit (comments only, in place):",
    "agent-docs": "- agent instruction files to audit:",
}


def _agent_inputs(project_dir: Path, session_id: str, prompt_id: str, key: str,
                  files: dict[str, list[str]]) -> list[str]:
    """The dispatch inputs for one agent: ONLY what the main agent cannot supply itself.

    For a turn-reading agent that is the answer file — the same path for every agent in one
    dispatch, so they all read and correct the one document the user will be shown.

    For a file-reading agent it is instead the paths this turn edited that its own criteria
    apply to, recorded by PostToolUse and looked up here by the agent's ``reads`` value: a
    main agent asked to recall which files it wrote will approximate, and these are the
    agents pointed at the repository rather than at the answer.

    ``session_id`` / ``prompt_id`` are here to BUILD that path, never to be handed over: an
    agent working on one turn has no use for guard's identifiers, and an extra pointer is
    one more thing it can wander into instead of doing its job.
    """
    reads = AUDIT_AGENTS[key].reads
    if reads in _FILE_INPUT_LABELS:
        return [_FILE_INPUT_LABELS[reads]] + [f"    {p}" for p in files.get(reads, ())]
    return ["- answer file: "
            f"{_turn_record_file(project_dir, session_id, prompt_id).resolve()}"]


# The closeout file the main agent is sent to. Resolved from this file's own
# location rather than from `CLAUDE_PLUGIN_ROOT`: the same code is the Codex adapter's
# library and a plain CLI the settings skill calls over Bash, and only one of those three
# has the env var set.
CLOSEOUT_REL = "hooks/context/turn-closeout.md"
# The plugin root, found by looking for a directory that HAS the closeout file rather than by
# counting parents. A fixed `parent.parent` is a bet on this file's depth, and this module
# has already moved once — out of `scripts/guard_hook.py` and into `scripts/guard_core/`,
# which silently turned every closeout path guard printed into `scripts/hooks/context/…`.
# Walking up until the file is there costs a few `is_file()` calls once per process and
# cannot be wrong about a depth it never assumes.
_PLUGIN_ROOT_MAX_DEPTH = 5


def _plugin_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents[:_PLUGIN_ROOT_MAX_DEPTH]:
        if (parent / CLOSEOUT_REL).is_file():
            return parent
    # No closeout file on disk (a partial install, or a test tree). Fall back to the layout as
    # shipped — `<root>/scripts/guard_core/dispatch.py` — so the path printed is still the
    # one a correct install would have, rather than a path under `scripts/`.
    return here.parent.parent.parent


def _closeout_path() -> Path:
    return _plugin_root() / CLOSEOUT_REL


# The CLI behind guard's shell wrappers and the Codex adapter. Built from the same
# `_plugin_root` the closeout path is, so a moved install cannot leave one of the two
# pointing at nothing.
CLI_REL = "scripts/guard_hook.py"

# There is deliberately NO fallback for a tree whose `shell/bin/` wrappers are missing. One
# existed, testing `is_file()` on each wrapper and adding the long `uv run --script <cli>
# <verb>` form to the dispatch when it was absent. Measuring it found it caught nothing real:
#
# - A version mismatch cannot happen. `agents/turn-router.md` and `shell/bin/` install as one
#   tree, so a version whose router names `guard-candidates` is a version that ships it.
# - A lost exec bit, or a PATH the wrappers never reached, leaves the FILE in place — so
#   `is_file()` passes and the fallback never fires, which is every realistic failure.
# - Codex never builds a turn block at all (see `hooks/scripts/hook_codex.py`).
#
# So the test and the failure it was meant to cover were about different things, and the
# only state it caught was one produced by deleting the files by hand. It also had a real
# cost: the `candidates` half vanished silently in a refactor and nothing noticed until the
# paths were measured directly. If a wrapper is ever genuinely unreachable, the fix is for
# the router to distinguish "the command failed" from "nothing to audit" in its report —
# those two produce identical output today, which is the actual silent failure here.


def _agent_pointer(project_dir: Path, session_id: str, prompt_id: str, keys: list[str],
                   files: dict[str, list[str]], modes: dict[str, AgentMode]) -> str:
    """Name these agents to the main agent and hand over their per-turn inputs.

The lead carries the one mechanical fact — these are agents, and the namespace they
    live in — because no router speaks on this path. Everything else the caller needs comes
    from the reports: each of these agents ends its findings in a disposition (apply, move,
    decide) because only the agent knows which one a finding is. Nothing here points at the
    closeout file: a turn dispatched this way wrote no answer file, so it has no closeout to
    run.

    The alternative, printing each agent's dispatch block here, costs the same text in the
    main agent's context on every routed turn, times every candidate, to be used by at
    most the ones the router picks and usually none. Having the ROUTER reproduce those
    blocks instead is no better: it makes an LLM re-type instructions it was handed, which
    is exactly where wording drifts.

    ``modes`` is passed in rather than re-read from config because the caller resolved it
    from session state, which can differ from the file for the live session.
    """
    lines = ["Dispatch these CONCURRENTLY, all in one message, with the Agent tool and "
             'subagent_type: "guard:<name>" — their file lists are disjoint, so none waits on '
             "another. Give each only the inputs named under it and no instructions of your "
             "own. Then apply what each reports — its findings say which of them you may apply "
             "and which are the user's call — and say in one line what changed:"]
    for key in keys:
        lines.append(f"- `{key}`={modes[key].value}")
        lines.extend("  " + line for line in _agent_inputs(
            project_dir, session_id, prompt_id, key, files))
    return "\n".join(lines)


def _dispatch_context(project_dir: Path, session_id: str, prompt_id: str, lead: str,
                      keys: list[str], modes: dict[str, AgentMode],
                      files: dict[str, list[str]] | None = None,
                      transcript: str = "") -> str:
    """``additionalContext`` asking the main agent to dispatch these agents directly.

    The no-router path: `cmd_stop` dispatching a file-reading agent, whose selection is not
    a question the router can answer — there is nothing to triage, so routing would only add
    a hop. It used to have a second caller, the per-agent `/guard:<agent>` command, which is
    gone; the signature is unchanged because the remaining caller needs all of it.
    """
    keys = list(keys)
    block = _agent_pointer(project_dir, session_id, prompt_id, keys, files or {}, modes)
    if transcript and any(AUDIT_AGENTS[k].needs_history for k in keys):
        block += f"\n- history: transcript {transcript}, turn {prompt_id}"
    return "\n\n".join([lead, block])


def _turn_context(project_dir: Path, session_id: str, prompt_id: str, lead: str,
                  with_closeout: bool) -> str:
    """``additionalContext`` for the Stop path: close the turn out, and audit nothing.

    Every line here is paid in the main agent's context at the end of EVERY turn that named
    an answer file, so the test each line has to pass is: could the closeout file have said
    this instead, or could the party that needs it derive it? If either, it is deleted from
    here.

    What survives that test is ONE path and one prohibition. The answer file, because it is
    the deliverable, this block is the last thing the turn reads, and it is the one value no
    reader here can work out for itself. The prohibition, because guard no longer asks for an
    audit here and a main agent that had been told to route every turn will keep routing on
    habit.

    Three lines were removed once the test was applied honestly rather than to the block as
    it stood:

    - The turn id, which is now the answer file's own basename (`turnrec._short`) and so is
      read off the path. It was kept for the audit command to resolve to, but
      ``/guard:audit-turn`` with no argument already resolves to the last recorded turn.
    - The translation file, which is the answer file with ``.ko`` before the extension. That
      rule is in the closeout, which is read on the turns that translate and by nobody else,
      so the derivation is paid for only when it is used. ``korean-translator`` is still
      forbidden from deriving its own target and is still handed an explicit path — by the
      caller, from that rule, rather than by this block on every turn including the ones that
      never translate.
    - The closeout path, on every turn after the one that first stated it (``with_closeout``).
      ``SessionStart`` names it when the session opens armed, and fires again on ``compact``
      on both hosts, so the line the compaction drops is re-stated by the event that dropped
      it rather than by a toll on every turn in between.

    No audit is named and no router is dispatched. **Auditing is the user's to ask for**
    (``/guard:audit-turn``, or one audit by name): a recommendation at the end of every turn
    spent a router on turns that plainly had nothing in them, and the recommendation that
    fires whether or not it is wanted is the one that gets waved through unread. What the
    hook still does is the part the user cannot do afterwards — recording the turn verbatim
    while it is fresh, and naming the file the answer was written to.

    Deliberately absent: any summary of the turn, from guard or from the main agent. Priming
    an audit with the author's account of the work is how an unexamined claim becomes an
    established one — every agent reads the turn itself and forms its own view, which is why
    the record is required to be verbatim.
    """
    lines = ["- answer file: "
             f"{_turn_record_file(project_dir, session_id, prompt_id).resolve()}"]
    if with_closeout:
        lines.append(f"- closeout: {_closeout_path()}")
    return "\n\n".join([lead, "\n".join(lines)])


# The lead at the end of a turn that has an answer file. It asks for delivery and forbids
# the audit, and the second half is the load-bearing one: the turn audit used to be dispatched
# from here on every turn, so this is where a main agent reaches for it out of habit.
#
# The command is named because the session cannot invoke it — `audit-turn` is
# `disable-model-invocation: true`, so it is not even in the session's skill list — and a user
# who asks for an audit in prose has to be told what to type. That is a different thing from
# offering one every turn, which is the noise this replaced.
_TURN_LEAD = (
    "guard: the turn is finished. Its answer file is the deliverable — close the turn out per "
    "guard's turn closeout. NO audit runs unless the user asks for one, and the audit is "
    "theirs to start: do not dispatch an audit, an auditor or a router yourself, and do not "
    "ask whether to run one. When the user does ask for one in prose, tell them to run "
    "`/guard:audit-turn` (or `/guard:audit-turn-claims`, `-clarity`, `-deferrals` for a single "
    "audit) — you cannot invoke it for them."
)


# The lead for the file-reading agents, which never go through the router. It says what the
# turn did rather than what to look for: each agent's criteria are its own, and a lead that
# previewed them would be the caller telling it what to find. One lead covers however many
# of them are eligible, because the per-agent input lines below it already say which files
# each one gets — a lead per agent would be the same sentence twice.
_DIRECT_LEAD = (
    "guard: this turn edited files in the repository. Audit them."
)


# Same dispatch, when the turn block precedes it. The one thing the main agent could
# plausibly get wrong here is sequencing — the block above it ends in closing the turn out,
# which reads as something to finish first — so the concurrency is spelled out. Waiting would
# cost a round trip for agents that share no input with the turn's own delivery.
_DIRECT_LEAD_WITH_TURN = (
    "guard: this turn also edited files in the repository. Audit them. Dispatch these BEFORE "
    "you close the turn out above, in one message — they read neither the answer file nor "
    "anything the closeout produces, so they wait for nothing and nothing waits on them."
)


# `ext-docs-auditor`, which has no switch and is not routed. It is named here rather than
# through `AUDIT_AGENTS` because the condition for it is not a judgment and not a setting: the
# turn either wrote a file under the refs directory or it did not, and `edited_refs` already
# answers that. Routing it could only restate what the file list says, and a switch in front
# of it would be a way to save a saved reference from ever being checked.
#
# Worded as what the turn did, not as what to look for — the criteria are the agent's own, and
# so is what its findings need: each one ends in a disposition saying whether the caller may
# apply it, must only relay it, or has a decision to make. Nothing here names the closeout file;
# a turn that only wrote refs files has no answer file and so no closeout to run.
_REFS_LEAD = (
    "guard: this turn wrote saved reference files. Dispatch `guard:ext-docs-auditor` "
    "(subagent_type: \"guard:ext-docs-auditor\") over them, then act on what it reports — "
    "its findings say which are yours to apply and which are the user's call."
)


def _refs_context(refs: list[str]) -> str:
    """``additionalContext`` naming ``ext-docs-auditor`` for the refs files this turn wrote."""
    lines = [_REFS_LEAD,
             "- saved reference files to audit:"]
    lines.extend(f"    {p}" for p in refs)
    return "\n".join(lines)


# What the main agent is told at the START of a turn, when guard has anything switched on.
# It fires on EVERY prompt, including the many that are never audited, so it is one sentence
# and a path.
#
# The substance goes in the FILE and the reply stays short, and that ordering is the whole
# point: it makes the full text cross the wire once. Answer in the reply and the audited
# version has to be printed a second time; answer in the file and a correction is a small
# edit to it, with the reply carrying only what changed. The file is also the only version
# that CAN be corrected — a reply that has already been printed cannot be, and the earlier
# shape left the user reading the flawed text with a list of fixes underneath it.
#
# "Keep the reply short" was the whole instruction once, and short is not the property that
# matters: a compressed restatement of the answer obeys it and still puts a second copy of the
# answer in the transcript, which is the one thing this lead exists to prevent. So the reply is
# specified by CONTENT — a headline and the path — rather than by length. The two named
# exclusions are the shapes that were observed slipping through as "short": a bullet summary
# of the file, and a preview of its opening.
#
# The audit is no longer what the file is for — it is asked for afterwards, if at all — and the
# file still is. It is the one copy of the answer, so an audit the user asks for an hour later
# corrects the document they have rather than a transcript nothing can reach, and it is the
# English source a translation is written from.
_DRAFT_LEAD = (
    "guard: put your answer's substance in {path}, written in ENGLISH. That file IS the answer, "
    "not a record of one: your reply is ONE headline sentence plus the path — no summary of "
    "what the file says, no excerpt from it, no findings list. Nothing audits it unless the "
    "user asks; when they do, the audit corrects that file in place, which is why the answer "
    "lives there rather than in the transcript. It stays ENGLISH whatever language you reply "
    "in: a Korean version is written only when the user runs `/guard:translate-turn`, so do "
    "not translate it yourself and do not offer to."
)
