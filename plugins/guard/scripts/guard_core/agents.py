"""The agents guard can recommend, and mechanical eligibility.

The roster and the two gates in front of it. Everything that needs judgment about a
particular turn is the router's, not this module's: ``_eligible_agents`` checks only that the
switch is not ``off`` and that a file-reading agent has at least one file of its own kind
this turn wrote.
"""

from __future__ import annotations

from pathlib import Path
from collections.abc import Iterable
from typing import Any, NamedTuple

from .config import _switch_on


# --------------------------------------------------------------------------- #
# the agents guard can recommend
# --------------------------------------------------------------------------- #
class AuditAgent(NamedTuple):
    """One agent guard can recommend. Mechanical facts only — no prose.

    Keyed in ``AUDIT_AGENTS`` by the agent's own bare name, which is also its config
    switch key, its playbook section, and — namespaced — its ``subagent_type``. One string
    for one agent: the setting the user types, the key in the state file, the section that
    says how to dispatch it, and the agent that gets dispatched cannot drift apart because
    they are the same string.

    ``reads`` is what the agent is pointed at — ``"turn"`` for the turn record guard
    wrote, ``"files"`` for the source files the turn edited, ``"agent-docs"`` for the
    ``AGENTS.md`` / ``CLAUDE.md`` files it edited, ``"refs"`` for the saved reference files
    it wrote under the refs directory. It selects the paths the dispatch carries and gates
    eligibility, since a file-reading agent with no matching edit has no input at all.

    It governs the turn-end path and nothing else. ``docs-fetcher`` is also dispatched
    BEFORE an answer exists, off the standing policy ``cmd_session_start`` prints, and that
    entry point is not expressed here — there is no per-turn eligibility to compute for it
    and no path for guard to hand over, since guard keeps no copy of the prompt. A fourth
    ``reads`` value for "the question" existed for the agent that only did the lookup; when
    that agent merged into the fetcher it became a value with one member whose sole effect
    was an exclusion from a set it was never a candidate for, so it is gone.

    The three file values are separate rather than one "the turn's edits", because the
    agents behind them judge different things and a shared list would hand each one files it
    has nothing to say about. ``comment-corrector`` judges a comment against the code under
    it and a markdown file gives it none; the agent-doc auditor judges instruction files
    against what an instruction file is for and a ``.py`` is not one; the refs auditor judges
    a file against what a saved external excerpt may contain, which is a rule no source file
    is under. Hence the buckets must stay DISJOINT (``_edited_bucket``): a name landing in
    two would be audited twice under criteria only one of which applies to it. The one real
    collision is why ``_edited_bucket`` tests location first — the refs directory's own
    ``AGENTS.md`` is its index, and by name alone it would go to the agent-doc auditor and be
    faulted for not being a map of the project.

    ``verify_command`` marks the agents that also have their own ``/guard:*`` command over
    the last completed turn; it is what stops ``cmd_verify`` from dispatching an agent no
    command can reach.

    ``needs_history`` is whether this agent may need to look past the response — at the
    request, at what the turn ran, at what an earlier turn established. Those agents are
    given the transcript path and the turn id so they can extract what they need with the
    ``transcript`` subcommand; the others are not, because a pointer an agent has no use
    for is one it may chase anyway. Three need it: `claims-auditor`, since a claim made here
    is often grounded by a command run three turns ago; `deferrals-auditor`, since the
    request is what separates a deferral the assistant owed from a decision it correctly
    handed back; and `clarity-auditor`, since whether a term still needs explaining depends
    on whether an earlier turn already explained it. The correctors do not — Korean prose is
    judged as prose, and comments are judged against the code under them.

    What the agent DOES, how to dispatch it, and what to do with its report are all in
    ``hooks/context/dispatch-playbook.md``, under the section named by this key. None of
    it belongs here: every string guard prints is paid for in the main agent's context on
    the turn it prints it, and this text is the same on every turn — so it is stored once
    and read only when a turn is actually routed to that agent.
    """

    reads: str
    verify_command: bool
    needs_history: bool


# The plugin namespace every agent name is qualified with to become a `subagent_type`.
AGENT_NAMESPACE = "guard:"


def _agent_id(name: str) -> str:
    """The dispatchable `subagent_type` for an agent name (a plain AUDIT_AGENTS key)."""
    return AGENT_NAMESPACE + name


def _instance_name(name: str) -> str:
    """The addressable instance name for an agent held open across turns.

    Hyphen rather than colon, and prefixed: it is a `name` on the Agent call, not a
    `subagent_type`, and the two must not be confusable in the dispatch text. One name
    per agent per session is the whole scheme — guard needs no registry of running
    instances, because the name is derived from the agent, so the main agent can look for
    it and guard can name it without either of them tracking anything.
    """
    return "guard-" + name


# Order here is the order the agents appear in a recommendation. The three read-only
# auditors come first: their findings may change what the correctors should be run on.
AUDIT_AGENTS: dict[str, AuditAgent] = {
    "claims-auditor": AuditAgent(reads="turn", verify_command=True, needs_history=True),
    "deferrals-auditor": AuditAgent(reads="turn", verify_command=True, needs_history=True),
    "clarity-auditor": AuditAgent(reads="turn", verify_command=True, needs_history=True),
    # Routed like the auditors above and for the same reason — whether the answer rests on
    # an external document is a reading of the answer — but it is the one routed agent that
    # is not auditing anything. It goes and gets what the answer should have cited.
    "docs-fetcher": AuditAgent(reads="turn", verify_command=False, needs_history=False),
    "korean-corrector": AuditAgent(reads="turn", verify_command=True, needs_history=False),
    "comment-corrector": AuditAgent(reads="files", verify_command=False, needs_history=False),
    "agents-md-auditor": AuditAgent(reads="agent-docs", verify_command=False,
                                    needs_history=False),
    # Deliberately AFTER `docs-fetcher` in this order, though the two never appear in the
    # same block: the fetcher is routed and the auditor is dispatched directly. The order
    # still says which way the pair runs — something saves a reference, then something else
    # checks what it saved — and a reader of this table should not have to infer that.
    "refs-auditor": AuditAgent(reads="refs", verify_command=False, needs_history=False),
}


# Source files whose comments `comment-corrector` can judge. Deliberately not "every
# file the turn touched": the agent judges comments against the code under them, and a
# markdown or JSON edit gives it nothing to judge. Extension-based rather than
# content-sniffing because this runs on every edit and must stay a dict lookup.
_SOURCE_SUFFIXES = frozenset({
    ".py", ".pyi", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".go", ".rs",
    ".java", ".kt", ".kts", ".c", ".h", ".cc", ".cpp", ".hpp", ".cs", ".rb", ".php",
    ".swift", ".scala", ".sh", ".bash", ".zsh", ".lua", ".sql", ".m", ".mm", ".dart",
    ".ex", ".exs", ".vue", ".svelte", ".zig",
})


# Filenames `agents-md-auditor` can judge. Matched on the name, not the suffix: what makes
# one of these auditable is that a coding agent loads it as standing instruction, and that
# is a property of the name the host looks for, not of it being markdown. Every other
# markdown file in a repository is prose nobody is instructed by, and auditing one against
# what an instruction file may contain would flag an ordinary document for having content.
#
# Lowercased before the lookup, since a repository may spell either one in any case and the
# host resolves them case-insensitively on macOS and Windows regardless.
_AGENT_DOC_NAMES = frozenset({"agents.md", "claude.md"})


# Which state list a PostToolUse target belongs in, if any.
#
# ORDER IS LOAD-BEARING here, unlike the two name-based tests below it, which are disjoint by
# construction (`_SOURCE_SUFFIXES` holds no `.md`). The refs test is by LOCATION and it comes
# first, because the refs directory's own index is named `AGENTS.md` and its shim `CLAUDE.md`:
# by name alone both go to the agent-doc auditor, which would fault the index of a reference
# library for not being a map of the project's deeper docs — a finding that is wrong about a
# file that is doing its job. Inside the refs directory, every markdown file is the refs
# auditor's, index included: a row describing local reasoning is the same violation as a
# section of it.
#
# `refs_dir` is passed in rather than resolved here so this stays a pure function of its
# arguments; the caller already has the project dir and the config it takes to resolve it.
def _edited_bucket(target: Path, refs_dir: Path | None = None) -> str | None:
    if refs_dir is not None and target.suffix.lower() == ".md" and (
            target.parent == refs_dir or refs_dir in target.parents):
        return "edited_refs"
    if target.suffix.lower() in _SOURCE_SUFFIXES:
        return "edited_files"
    if target.name.lower() in _AGENT_DOC_NAMES:
        return "edited_agent_docs"
    return None


# --------------------------------------------------------------------------- #
# the router
#
# guard makes NO model call of its own. When a turn finishes, the Stop hook decides one
# mechanical thing — is any agent even eligible — and then asks the main agent to dispatch
# ONE subagent, the router. The router reads the finished response and answers with the
# INSTRUCTIONS: which of the eligible specialists would find something in it, why each,
# and the dispatch for each.
#
# It writes the dispatch rather than guard printing it because of where the cost falls.
# guard's context lands in the main agent on every routed turn; the router's own
# definition is read once, by the router, and only when a turn is actually routed. A
# per-candidate dispatch block in the hook's `additionalContext` is paid four times over
# on every turn to be used at most four times and usually zero — the router clearing a
# turn is the common case. So the hook carries only what the router cannot know (where the
# answer file is, which agents are on, their modes, the edited files, the transcript
# pointer) and `agents/router.md` carries everything that describes an agent.
#
# That the router is an agent and not a `claude -p` child guard spawns itself is the
# design. A spawned child made the Stop hook block for the router's whole runtime at
# the end of every turn the user was waiting on, and it dragged in a set of problems
# that exist only because it was a child: it had to carry `--safe-mode` or guard's own
# Stop hook would fire inside it and recurse, it needed an explicit tool denylist
# because omitting `--allowedTools` leaves a child fully tooled, `--bare` was
# unusable because it takes auth down to `ANTHROPIC_API_KEY` only, and every one of
# spawn / timeout / exit code / envelope parsing was a failure path guard had to tell
# apart from a clean verdict. As a subagent none of that exists: it runs in the host's
# own dispatch machinery, its model lives in its definition, and the hook returns
# immediately.
#
# What travels as a FILE and what travels as PROSE is a per-case choice, not a policy.
# A file earns its place when the text has several readers who must all see the same
# thing (the turn record: the router plus every agent it names), or when it is long
# enough that carrying it in a message would crowd out the message (the Korean rewrite).
# Everything short and single-hop stays prose in the dispatch or the report: the roster,
# the edited-file list, the router's picks and its reason per pick. Routing a two-line
# verdict through a file would only add a read.
#
# The roster is built HERE, not in `agents/router.md`, because eligibility is per turn
# and per project: which switches are on, and which files this turn wrote. The router's
# definition holds everything that is the same every turn — the method, and the dispatch
# template per agent. An agent absent from the roster cannot be picked, which beats
# describing a disabled agent and appending "but this one is off".
#
# The result-handling line for an agent lives in exactly one place: its section of
# `hooks/context/dispatch-playbook.md`. Both paths read it from there — the on-demand
# `/guard:<agent>` path via `_agent_pointer`, the routed path via the router's own
# report — so there is nothing in Python to keep in sync with the markdown, and no
# duplicated guidance that could drift between the two.
# --------------------------------------------------------------------------- #
ROUTER_AGENT = "guard:router"


def _reads_turn(keys: Iterable[str]) -> bool:
    """Does any of ``keys`` read the turn's answer file?

    The gate on everything the answer file costs. That file exists for the agents whose
    input it IS (``reads="turn"``); ``comment-corrector`` reads the source files the turn
    wrote and never opens it. So a configuration with only ``comment-corrector`` on must
    not pay for it — neither the per-prompt instruction telling the session to write into
    it, nor the dispatch line naming it.
    """
    return any(AUDIT_AGENTS[k].reads == "turn" for k in keys if k in AUDIT_AGENTS)


def _eligible_agents(state: dict[str, Any], edited: list[str],
                     agent_docs: list[str] | None = None,
                     refs: list[str] | None = None) -> list[str]:
    """The agents the router may choose from, in ``AUDIT_AGENTS`` order.

    Two mechanical gates, and only mechanical ones — everything that needs judgment is
    the router's call:

    - the switch, which is the user saying they are willing to have this agent run;
    - for a file-reading agent, at least one file of its own kind this turn wrote,
      because that list is the agent's whole input and nobody downstream can invent one.

    ``agent_docs`` and ``refs`` default to none rather than being required, for the Codex
    adapter: it shares this function but mirrors no edited-file recording of its own, so
    every file-reading agent is ineligible there and passing empty lists is the honest
    answer.

    Notably absent: any language test for ``korean-corrector``. Deciding whether a
    response is Korean enough to audit is a reading task, and the router does it better
    than a Hangul ratio that has to guess how many English identifiers a Korean answer
    may carry before it stops being Korean.
    """
    inputs = {"files": edited, "agent-docs": agent_docs or [], "refs": refs or []}
    out: list[str] = []
    for key, spec in AUDIT_AGENTS.items():
        if not _switch_on(state, key):
            continue
        if spec.reads in inputs and not inputs[spec.reads]:
            continue
        out.append(key)
    return out
