"""The text guard hands the main agent.

Where each piece of text lives is decided by how often it is paid for, and that split must
hold. What this module builds reaches the main agent on every routed turn, so it is one
imperative plus a list of fields: paths, which agents are on, each one's mode.
``agents/turn-router.md`` is read once per routed turn by the router alone, so it carries the
triage method and the dispatch per candidate. ``hooks/context/dispatch-playbook.md`` is read
only by whoever is sent to a section, so it carries how to dispatch an agent and what to do
with its report. Nobody re-types another home's text.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

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


# The playbook the main agent is sent to by section name. Resolved from this file's own
# location rather than from `CLAUDE_PLUGIN_ROOT`: the same code is the Codex adapter's
# library and a plain CLI the settings skill calls over Bash, and only one of those three
# has the env var set.
PLAYBOOK_REL = "hooks/context/dispatch-playbook.md"
# The plugin root, found by looking for a directory that HAS the playbook rather than by
# counting parents. A fixed `parent.parent` is a bet on this file's depth, and this module
# has already moved once — out of `scripts/guard_hook.py` and into `scripts/guard_core/`,
# which silently turned every playbook path guard printed into `scripts/hooks/context/…`.
# Walking up until the file is there costs a few `is_file()` calls once per process and
# cannot be wrong about a depth it never assumes.
_PLUGIN_ROOT_MAX_DEPTH = 5


def _plugin_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents[:_PLUGIN_ROOT_MAX_DEPTH]:
        if (parent / PLAYBOOK_REL).is_file():
            return parent
    # No playbook on disk (a partial install, or a test tree). Fall back to the layout as
    # shipped — `<root>/scripts/guard_core/dispatch.py` — so the path printed is still the
    # one a correct install would have, rather than a path under `scripts/`.
    return here.parent.parent.parent


def _playbook_path() -> Path:
    return _plugin_root() / PLAYBOOK_REL


# The CLI behind guard's shell wrappers and the Codex adapter. Built from the same
# `_plugin_root` the playbook path is, so a moved install cannot leave one of the two
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
# - Codex never calls `_router_context` at all (see `hooks/scripts/hook_codex.py`).
#
# So the test and the failure it was meant to cover were about different things, and the
# only state it caught was one produced by deleting the files by hand. It also had a real
# cost: the `candidates` half vanished silently in a refactor and nothing noticed until the
# paths were measured directly. If a wrapper is ever genuinely unreachable, the fix is for
# the router to distinguish "the command failed" from "nothing to audit" in its report —
# those two produce identical output today, which is the actual silent failure here.


def _agent_pointer(project_dir: Path, session_id: str, prompt_id: str, keys: list[str],
                   files: dict[str, list[str]], modes: dict[str, AgentMode]) -> str:
    """Name the playbook sections for these agents and hand over their per-turn inputs.

    This is the whole dispatch instruction, and what is NOT in it is the point: how to
    dispatch an agent, what its report means, and what to do about it are the same on every
    turn, so they are stored once in the playbook and read only when a turn is actually
    routed. What guard prints is only what the playbook cannot know — which agents, in
    which mode, and the paths for this turn.

    The alternative, printing each agent's dispatch block here, costs the same text in the
    main agent's context on every routed turn, times every candidate, to be used by at
    most the ones the router picks and usually none. Having the ROUTER reproduce those
    blocks instead is no better: it makes an LLM re-type instructions it was handed, which
    is exactly where wording drifts.

    ``modes`` is passed in rather than re-read from config because the caller resolved it
    from session state, which can differ from the file for the live session.
    """
    lines = [f"Follow {_playbook_path()}, these sections in this order:"]
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


def _router_context(prompt_id: str, lead: str) -> str:
    """``additionalContext`` for the Stop path: one imperative and the turn id.

    Every line here is paid in the main agent's context at the end of EVERY routed turn,
    including the many the router then clears, so the test each line has to pass is: could
    the playbook have said this instead, or could the party that needs it derive it? If
    either, it is deleted from here.

    Everything else failed that test. The procedure went to the playbook, read once by
    whoever is sent to a section. The roster and the per-turn paths went to `guard-candidates`
    and `guard-inputs`, run by the agents that use them — the main agent opens none of those
    files, so relaying their paths only gave it text to carry and a copy step to get wrong.
    The ROUTER returns the next instruction itself, naming the playbook and the sections, so
    the main agent never reads a section about routing.

    The turn id is what remains because it is the one thing nothing downstream can work out
    for itself.

    Deliberately absent: any summary of the turn, from guard or from the main agent. Priming
    an audit with the author's account of the work is how an unexamined claim becomes an
    established one — every agent reads the turn itself and forms its own view, which is why
    the record is required to be verbatim.

    The ROUTER is always a fresh instance, whatever the agents are set to. Its question is
    about this turn, and an instance carrying the last five turns is one that can answer it
    from the wrong one — the failure would be silent, and routing is the step nothing else
    checks. Cheapness is not what it is tuned for: a router that misreads the turn either
    ships the defect or spends a subagent for every agent it named for nothing, and both cost
    more than the routing call itself ever will. Hence `agents/turn-router.md` pins `opus`, and
    there is no per-project override: the one setting that could make routing cheaper is the
    one setting whose failure is invisible, since a router that stops naming an agent looks
    exactly like a turn with nothing in it.
    """
    # ONE field: the turn id. Everything else the agent needs — the playbook, the answer
    # file, the request file beside it, the transcript and the turn to look up in it — is
    # derivable from that id plus the session, so `guard-inputs` derives them and the agent
    # runs it. What this replaces is the main agent relaying four absolute paths it never
    # opens: text paid for in its context on every routed turn, and a copy step whose only
    # possible contribution is to get one wrong.
    #
    # It also puts the layout back with the code that owns it. A dispatch that spelled the
    # turn directory out was a second copy of `turnrec`'s layout, in prose, and a drifted
    # copy reads nothing and clears every turn silently.
    return lead + "\n\n" + f"- turn: {prompt_id}"


# The lead for a routed turn. There is no second mode: a switch the user turned on is
# the user saying they want this audit, so asking again every turn would be a formality
# that trains them to wave it through. What the main agent must not do is quietly swallow
# the result — the report is the point.
_ROUTE_LEAD = (
    "guard: audit the turn you just finished. Dispatch `guard:turn-router` (subagent_type: "
    "\"guard:turn-router\") with the inputs below and follow its report."
)


# The lead for the file-reading agents, which never go through the router. It says what the
# turn did rather than what to look for: each agent's criteria are its own, and a lead that
# previewed them would be the caller telling it what to find. One lead covers however many
# of them are eligible, because the per-agent input lines below it already say which files
# each one gets — a lead per agent would be the same sentence twice.
_DIRECT_LEAD = (
    "guard: this turn edited files in the repository. Audit them."
)


# Same dispatch, when a router block precedes it. The one thing the main agent could
# plausibly get wrong here is sequencing — the router block above it ends in "follow its
# report", which reads as something to finish first — so the concurrency is spelled out.
# Waiting would cost a round trip for agents that share no input with the routed ones.
_DIRECT_LEAD_WITH_ROUTER = (
    "guard: this turn also edited files in the repository. Audit them. Dispatch these in "
    "the SAME message as the router above — they read neither the answer file nor the "
    "router's report, so they wait for nothing."
)


# `ext-docs-auditor`, which has no switch and is not routed. It is named here rather than
# through `AUDIT_AGENTS` because the condition for it is not a judgment and not a setting: the
# turn either wrote a file under the refs directory or it did not, and `edited_refs` already
# answers that. Routing it could only restate what the file list says, and a switch in front
# of it would be a way to save a saved reference from ever being checked.
#
# The section is named the same way the other file-reading agents' sections are, so what to
# do with its report stays in the playbook and is read only when a turn actually wrote one of
# these files. Worded as what the turn did, not as what to look for — the criteria are the
# agent's own.
_REFS_LEAD = (
    "guard: this turn wrote saved reference files. Dispatch `guard:ext-docs-auditor` "
    "(subagent_type: \"guard:ext-docs-auditor\") over them and follow the "
    "`ext-docs-auditor` section of {playbook}."
)


def _refs_context(refs: list[str]) -> str:
    """``additionalContext`` naming ``ext-docs-auditor`` for the refs files this turn wrote."""
    lines = [_REFS_LEAD.format(playbook=_playbook_path()),
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
# matters: a compressed restatement of the answer obeys it and still puts the unaudited text
# in front of the user, which is the one thing this lead exists to prevent. So the reply is
# specified by CONTENT — a headline and the path — rather than by length. The two named
# exclusions are the shapes that were observed slipping through as "short": a bullet summary
# of the file, and a preview of its opening.
_DRAFT_LEAD = (
    "guard: put your answer's substance in {path}, written in ENGLISH. Until the audits have "
    "run, the user should be reading that file and not a copy of it in the transcript: your "
    "reply is ONE headline sentence plus that path — no summary of what the file says, no "
    "excerpt from it, no findings list. guard audits that file when the turn ends. When you "
    "will answer the user in another language, the version they read is translated from this "
    "file after the audits have run — the playbook says how."
)
