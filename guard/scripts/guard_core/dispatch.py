"""The text guard hands the main agent.

Where each piece of text lives is decided by how often it is paid for, and that split must
hold. What this module builds reaches the main agent on every turn that has an answer file,
so it is one imperative plus a list of fields: paths, which agents are on, each one's mode.
``agents/turn-router.md`` is read once per AUDIT — and an audit happens only when the user
asks for one — so it carries the triage method and the dispatch per candidate.
Nobody re-types another home's text.
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


# A file that is present in every install and nowhere else, used to find the plugin root.
CLOSEOUT_REL = "hooks/context/answer-lane.md"
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


# The lead for the file-reading agents, which never go through the router. It says what the
# turn did rather than what to look for: each agent's criteria are its own, and a lead that
# previewed them would be the caller telling it what to find. One lead covers however many
# of them are eligible, because the per-agent input lines below it already say which files
# each one gets — a lead per agent would be the same sentence twice.
_DIRECT_LEAD = (
    "guard: this turn edited files in the repository. Audit them."
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
