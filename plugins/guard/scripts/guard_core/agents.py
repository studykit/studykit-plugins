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


class AuditAgent(NamedTuple):
    """One agent guard can recommend. Mechanical facts only — no prose.

    Keyed in ``AUDIT_AGENTS`` by the name of the AUDIT. That key is the config switch the
    user types and the key in the state file, and for most rows it is also the agent's own
    name — and, namespaced, its ``subagent_type``.

    Some audits are reached through a different ENTRY POINT per dispatch path
    (``turn_entry`` / ``report_entry``), and there the key names the audit while each entry
    has a name of its own. The key does NOT follow the entry: it is user-visible
    configuration, and ``_load_config`` honours only keys it already knows, so renaming one
    would silently downgrade a configured audit to its default and say nothing. What holds
    instead is that the translation happens in exactly one place — ``_path_entry``, which
    ``cmd_candidates`` calls — and downstream of it the entry name is the only string used.

    ``reads`` is what the agent is pointed at — ``"turn"`` for the turn record guard
    wrote, ``"files"`` for the source files the turn edited, ``"agent-docs"`` for the
    ``AGENTS.md`` / ``CLAUDE.md`` files it edited. It selects the paths the dispatch carries
    and gates eligibility, since a file-reading agent with no matching edit has no input at
    all.

    The two file values are separate rather than one "the turn's edits", because the agents
    behind them judge different things and a shared list would hand each one files it has
    nothing to say about. ``comment-corrector`` judges a comment against the code under it
    and a markdown file gives it none; the agent-doc auditor judges instruction files
    against what an instruction file is for and a ``.py`` is not one. Hence the buckets must
    stay DISJOINT (``_edited_bucket``): a name landing in two would be audited twice under
    criteria only one of which applies to it.

    ``fixed_mode`` marks an agent with NO config switch. ``None`` (the usual case) means the
    user's switch decides whether it runs and in which mode; a mode value means the agent is
    always eligible and always dispatched in that mode, and ``settings set <key>`` refuses the
    name because there is no key behind it. One agent is like this — ``korean-translator`` —
    because it does not audit: it writes the Korean the user reads, and a writer of the
    deliverable that a setting can switch off produces two tiers of Korean depending on a
    config nobody remembers. ``korean-corrector`` is the other, because it is the second half
    of that one step rather than an audit of its own. Neither makes guard speak on a turn it
    would otherwise be silent on; see ``_eligible_agents``.

    The mode is ``fresh`` for both, which is now the only mode there is.

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

    ``routed=False`` marks an audit the turn router must not be offered, because something
    else already hands it over: ``korean-corrector`` is named by ``korean-translator``'s own
    report, which is the only party that knows the translation now exists. Routing it as well
    would make two authorities for one step and give the router a name to judge from evidence
    that is not written yet.

    ``turn_entry`` and ``report_entry`` name what the caller INVOKES to run this audit on
    each dispatch path — the finished turn, and a standalone document such as an interview
    brief. ``turn_entry=None`` (the usual case) means the agent's name IS the key.
    ``report_entry=None`` means the audit is not offered on the document path at all, which
    is the right answer for part of the roster: the Korean pair writes and checks a
    translation that the document path never produces, and the file-reading agents are
    pointed at a turn's edits.

    An entry is a SKILL for every audit that runs on both paths and the agent's own name for
    the rest; the three shared audits are each one agent behind two `context: fork` skills.
    Which tool the caller reaches for is said by whoever dispatches — each router's report
    template, and ``_agent_pointer``'s lead on the direct path — not by this module; what this
    module guarantees is that the name it hands over is the name of a real entry point,
    checked by ``dev/check-entries.py`` against both ``agents/`` and ``skills/``.

    Entries are spelled out rather than derived as ``"turn-" + key``. A derived name that
    matches no file fails silently — the dispatch simply finds nothing — whereas a literal
    can be checked.

    What the agent DOES is its own definition, and what to do with its report is that
    report. Only where the caller has a judgment the report cannot make for it does a
    section exist, in ``hooks/context/turn-closeout.md``. None of it belongs here:
    every string guard prints is paid for in the main agent's context on the turn it
    prints it.
    """

    reads: str
    needs_history: bool
    fixed_mode: str | None = None
    turn_entry: str | None = None
    report_entry: str | None = None
    routed: bool = True


# No `subagent_type` is built here any more. `cmd_candidates` prints the bare entry name and
# the router copies it into its report, where its own template supplies the `guard:` prefix.
# The direct path has no router, so `_agent_pointer`'s lead supplies it there — once, as
# `guard:<name>`, not per agent. Building it per row here would put the namespace on every
# line of a list whose reader already has it from the lead.


# Order here is the order the agents appear in a recommendation, and on the routed path it is
# the order they RUN in, one at a time. Each one's findings are applied before the next is
# dispatched, so each reads a file the one before it changed: fixing an unsupported claim is
# often how a deferral gets written ("I could not establish this"), and both kinds of repair add
# prose that is then the likeliest thing in the file to be hard to follow. `korean-translator`
# is last, translating what all of them settled. No agent here waits on another directly — every
# dependency runs through an edit the CALLER makes in between, which is why the router's
# template has to state it rather than leaving an agent to notice.
#
# One pass, in this order, and the cycle is real but not chased: a deferral resolved in step 2
# introduces facts nothing re-audits for evidence. Running the list twice would cost double for
# a second round that is empty on almost every turn.
AUDIT_AGENTS: dict[str, AuditAgent] = {
    # Every audit that runs on both dispatch paths splits at the ENTRY, not at the agent: one
    # agent judges, and a `context: fork` skill per path carries the input-gathering. What
    # settles it is memory — a memory directory is named after the AGENT, so two definitions
    # are two memories, and what one learned about this repository is invisible to the other.
    #
    # A judgment that genuinely differs by path is stated in the skill, and the agent says
    # which one that is rather than picking a side. Here it is the documentation rule: the
    # turn path requires a local saved copy under the refs directory, because the session that
    # wrote the turn was told to save one. On the document path that same rule would fail
    # every citation in every brief.
    "claims-auditor": AuditAgent(reads="turn", needs_history=True,
                                 turn_entry="audit-turn-claims",
                                 report_entry="audit-report-claims"),
    # Same shape, and the reversal it carries is the sharper one: on a turn, "the assistant
    # handed this back to the user" is legitimate because the user was there to be asked. In a
    # document nobody was, so the same sentence is the author deferring on their own behalf
    # unless the text records the question actually being put to someone. That is stated in
    # each skill, and the agent says in so many words that the ruling is the skill's — which
    # is what lets one definition hold a rule that comes out opposite on the two paths.
    "deferrals-auditor": AuditAgent(reads="turn", needs_history=True,
                                    turn_entry="audit-turn-deferrals",
                                    report_entry="audit-report-deferrals"),
    # Same shape, and here the memory argument is sharpest: what lives in this agent's
    # `memory: user` directory is the READER PROFILE. Two definitions would be two
    # `user`-scoped directories drifting apart and neither would be the reader's. Nothing
    # about what makes an explanation followable differs by path, so neither skill overrides
    # a judgment; they carry only the gathering.
    "clarity-auditor": AuditAgent(reads="turn", needs_history=True,
                                  turn_entry="audit-turn-clarity",
                                  report_entry="audit-report-clarity"),
    # Before the corrector, and that order is the point: the translator writes the Korean
    # the user reads, and the corrector then judges what it wrote. Reversed, the corrector
    # would be repairing a draft that is about to be replaced.
    #
    # No switch (`fixed_mode`): the answer the user reads is not an audit to opt into. What
    # decides whether it runs is the router, on the language of the turn — so an
    # English-answering project never pays for it, and a Korean-answering one cannot end up
    # with the main session translating its own text because a config key was left off.
    "korean-translator": AuditAgent(reads="turn", needs_history=False, fixed_mode="fresh"),
    # Switch-free for the same reason, and it has to be the same reason: these two are one
    # step. A corrector the user can switch off behind a translator they cannot is a Korean
    # deliverable nothing reads — and the pair is what makes the writer/reader split hold.
    #
    # `routed=False` because being one step is enough: the translator's report ends in a `next`
    # line naming this agent and the file it wrote, so the hand-off happens where the fact it
    # depends on — the translation exists — is actually known. The router, reading before either
    # ran, could only have guessed at it from the request.
    "korean-corrector": AuditAgent(reads="turn", needs_history=False, fixed_mode="fresh",
                                   routed=False),
    "comment-corrector": AuditAgent(reads="files", needs_history=False),
    "agents-md-auditor": AuditAgent(reads="agent-docs", needs_history=False),
}


# The agents that HAVE a config switch, in roster order — the only names `settings set` and
# `settings show` may touch. A `fixed_mode` agent has no key behind it, so writing one would
# record a setting nothing reads and showing one would offer a switch that does not exist.
SETTABLE_AGENTS: tuple[str, ...] = tuple(
    k for k, spec in AUDIT_AGENTS.items() if spec.fixed_mode is None)


# The dispatch paths an audit can run on. `"turn"` is the routed Stop path; `"report"` is a
# standalone document, routed by `report-router` with no hook in front of it.
TURN_PATH = "turn"
REPORT_PATH = "report"


def _path_entry(key: str, path: str) -> str | None:
    """What runs audit ``key`` on ``path``, or None if it does not run there.

    The ONE place a roster key becomes an entry-point name. Everything downstream of
    ``cmd_candidates`` — the router's report, and the skill or ``subagent_type`` its caller
    then runs — carries the name this returns, so the key and the name cannot drift apart
    anywhere else by construction: nowhere else translates.

    ``None`` on the report path is the normal answer, not an error. Most of the roster has
    nothing to do with a document, and returning the key as a fallback would offer the
    document router a turn agent whose whole body is about a transcript it will not get.
    """
    spec = AUDIT_AGENTS[key]
    if path == REPORT_PATH:
        return spec.report_entry
    return spec.turn_entry or key


# Source files whose comments `comment-corrector` can judge. Deliberately not "every
# file the turn touched": the agent judges comments against the code under them, and a
# markdown or JSON edit gives it nothing to judge. Extension-based rather than
# content-sniffing because this runs on every edit and must stay a set lookup.
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
# `edited_refs` is the one bucket with no `AUDIT_AGENTS` entry behind it. `ext-docs-auditor`
# has no switch and is not routed, so nothing computes eligibility for it; the Stop hook reads
# this list directly and names the agent when it is non-empty.
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
# pointer) and `agents/turn-router.md` carries everything that describes an agent.
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
# The roster is built HERE, not in `agents/turn-router.md`, because eligibility is per turn
# and per project: which switches are on, and which files this turn wrote. The router's
# definition holds everything that is the same every turn — the method, and the dispatch
# template per agent. An agent absent from the roster cannot be picked, which beats
# describing a disabled agent and appending "but this one is off".
#
# How to dispatch an agent is said by whoever dispatches it, once per path: the router's own
# report template on the routed path, `_agent_pointer`'s lead on the direct one. It used to be
# a section per agent in the closeout file, reached from both — which gave that file a place
# to state, and then to contradict, decisions the router had already made. What is left in it
# is the part no report can carry: the turn's closeout, and the two file-writing audits whose
# findings must not be applied on autopilot.
# --------------------------------------------------------------------------- #
ROUTER_AGENT = "guard:turn-router"


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
                     agent_docs: list[str] | None = None) -> list[str]:
    """The agents the router may choose from, in ``AUDIT_AGENTS`` order.

    Two mechanical gates, and only mechanical ones — everything that needs judgment is
    the router's call:

    - the switch, which is the user saying they are willing to have this agent run;
    - for a file-reading agent, at least one file of its own kind this turn wrote,
      because that list is the agent's whole input and nobody downstream can invent one.

    ``agent_docs`` defaults to none rather than being required, for the Codex adapter: it
    shares this function but mirrors no edited-file recording of its own, so every
    file-reading agent is ineligible there and passing empty lists is the honest answer.

    A third gate, in the other direction: an agent with a ``fixed_mode`` has no switch and so
    passes the first one always — but it is dropped again unless some SWITCHABLE turn-reading
    agent also got through, so it can only ever join a turn that was already being routed and
    already has an answer file. Only those riders are dropped; the rest of the result stands,
    which is what keeps a ``comment-corrector``-only project working.

    Notably absent: any language test for ``korean-translator``. Deciding whether a turn
    will be delivered in Korean is a reading task, and the router does it better than a
    Hangul ratio that has to guess how many English identifiers a Korean answer may carry
    before it stops being Korean. ``korean-corrector`` needs no test at all — it is not
    routed, and the translator's report is what reaches it.
    """
    inputs = {"files": edited, "agent-docs": agent_docs or []}
    out: list[str] = []
    carries_the_turn = False
    for key, spec in AUDIT_AGENTS.items():
        switchable = spec.fixed_mode is None
        if switchable and not _switch_on(state, key):
            continue
        if spec.reads in inputs and not inputs[spec.reads]:
            continue
        if switchable and spec.reads == "turn":
            carries_the_turn = True
        out.append(key)
    # The switch-free agents ride along; they never make a turn routed on their own. What
    # they ride on is a switchable TURN-reading agent that got through both gates above —
    # nothing weaker works. With no switch on at all, guard must add nothing to the main
    # agent's context, which is what "every switch ships off" buys. And with only a
    # file-reading agent on, there is no answer file (`_reads_turn` decides that off this
    # list) and so nothing for a translator to translate: letting the pair through there
    # would conjure the answer file that configuration exists to avoid paying for.
    #
    # Only the riders are dropped, never the list. A `comment-corrector`-only project is a
    # working configuration — it is dispatched around the router on the files the turn wrote —
    # and emptying its result here would silence guard for it entirely.
    if carries_the_turn:
        return out
    return [k for k in out if AUDIT_AGENTS[k].fixed_mode is None]
