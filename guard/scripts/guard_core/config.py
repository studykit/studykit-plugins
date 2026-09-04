"""Host split, agent modes, and the project's configuration file.

Configuration is optional: a JSON object at ``${CLAUDE_PROJECT_DIR}/.claude/guard.local.json``
(``.codex/`` on Codex). One ``AgentMode`` per agent, keyed by that agent's own name —
``claims-auditor`` / ``deferrals-auditor`` / ``clarity-auditor`` / ``comment-corrector`` /
``agents-md-auditor``, each
``"off"`` (the default) or ``"on"`` — which together are the only control
over whether guard says anything unasked, and over which audits exist to be invoked. Plus
``audit-turn`` (``"off"`` by default) and ``audit-plan`` (``"on"`` by default), each ``"on"``
or ``"off"``: the state each session opens in — the shell toggles move the session
only and never write here. ``audit-turn`` no longer arms an automatic audit, because there is
none: it arms the turn discipline the audit needs — the answer file, the recorded turn — and
the user invokes the audit itself. And ``refs_dir`` (project-relative directory for saved copies of cited docs; empty
means the git-tracked default ``wiki/ref/``, and an unsafe value falls back to it — see
``paths._refs_dir``). There is no model key: every agent, the router included, brings its own
model from its own definition under ``agents/``.

Unknown keys are ignored; a missing or malformed file falls back to all defaults. The
``guard:settings`` skill changes these through the ``settings`` CLI, which writes this file
and, for the switches, the live session's state.

Requires Python 3.11+ (``enum.StrEnum``).
"""

from __future__ import annotations

import json
import os

from pathlib import Path
from enum import StrEnum
from typing import Any



# Codex adapters set GUARD_HOST before importing this module. Keep the historical
# Claude paths intact while preventing one host from interpreting the other's state.
# Read once into a constant: the Codex adapter imports this module, so anything below
# asking "which host" must get the same answer the paths were chosen from.
_HOST_IS_CODEX = os.environ.get("GUARD_HOST") == "codex"


if _HOST_IS_CODEX:
    STATE_DIR_REL = ".codex/guard"
    CONFIG_REL = ".codex/guard.local.json"
else:
    STATE_DIR_REL = ".claude/guard"
    CONFIG_REL = ".claude/guard.local.json"


TRACE_FILE_NAME = "trace.log"


TRACE_ENV_VAR = "GUARD_TRACE"


TRACE_TRUTHY = {"1", "true", "yes", "on"}


# Marker the `guard:settings` skill sets on the config-mutating CLI verbs. See
# _cli_write_allowed for what this does and does not buy.
CLI_WRITE_ENV_VAR = "GUARD_SETTINGS_SKILL"


ORPHAN_MAX_AGE_SECONDS = 7 * 24 * 60 * 60


# How long a `/clear` handoff record stays usable. The record is not a guess about which
# session preceded which — `SessionEnd` names the ending session outright, measured 55ms
# before the replacing `SessionStart` arrives — so this is not a confidence window. It is the
# expiry on a record that was never consumed: the new session's hook failing to run, or the
# process dying between the two events, leaves a file behind, and without an expiry that file
# would arm some unrelated `/clear` hours later. Five minutes is enormous next to 55ms and
# still far too short to become the persistent gate that was deleted.
CLEAR_INHERIT_MAX_AGE_SECONDS = 5 * 60


class AgentMode(StrEnum):
    """How one audit agent runs. The value of that agent's config key.

    ``OFF`` — not offered to either router, and not runnable: the audit does not exist for
    this project. ``ON`` — a new instance per dispatch, which
    is the shape every agent definition is written for: judged in a fresh context, by a
    reader rather than the author.

    ``ON`` was spelled ``fresh`` until v0.116.0, when the one surviving mode stopped needing
    a name that only made sense beside a second one. ``fresh`` is still parsed, and never
    stops being: it is written into every config file this plugin has already touched, and a
    value that silently reads as its default is exactly the failure this file is careful
    about elsewhere. What changed is what gets WRITTEN and DISPLAYED.

    There used to be a third, ``REUSE``: one named instance per session, resumed on later
    turns with its full history. It bought continuity and cost independence — a verdict it
    got wrong sat in its own history as settled, and every later turn inherited that error
    where a fresh instance would have looked again. What made the trade survivable was one
    section in each agent's definition telling a resumed instance that a turn record it has
    not read is a NEW turn and that a remembered verdict is not a checked one. Those sections
    were removed, and a hazard whose only mitigation is gone is not a mode worth keeping. Do
    not add it back without them.

    Two things it took with it, both worth knowing before reviving it. Instance names were
    derived from the ROSTER KEY rather than from the agent name, so a renamed agent kept
    emitting its old instance name with nothing failing — a trap for every future rename,
    and one that is live again the moment anything derives a dispatchable identity from a
    key (see ``agents._path_entry``, which is now the only translation). And its two mode-transition notices existed only because guard
    cannot see or stop a running instance; that asymmetry comes back with it.
    """

    OFF = "off"
    ON = "on"


# The words that mean armed and muted, for BOTH ways a two-valued switch is written: the
# `audit-turn` / `audit-plan` values in guard.local.json and the argument to the `guard` /
# `guard-plan` shell commands. One vocabulary, because a word the config file accepts and the
# shell command rejects is a difference the user has no way to predict.
_ON_WORDS = frozenset({"on", "true", "yes", "1", "resume", "enable", "arm", "unmute"})


_OFF_WORDS = frozenset({"off", "false", "no", "0", "pause", "disable", "mute"})


# The two audit switches, keyed the way the agent switches are: the key is what the user
# reads, and each names the audit it opens. Values are `_ON_WORDS` / `_OFF_WORDS` words.
AUDIT_TURN_KEY = "audit-turn"


AUDIT_PLAN_KEY = "audit-plan"


AUDIT_SWITCHES = (AUDIT_TURN_KEY, AUDIT_PLAN_KEY)


# Spellings accepted for a mode, beyond the member values themselves. `fresh` heads the list
# because it is not a convenience: it is the value v0.115.0 and earlier WROTE into
# guard.local.json, so every config file already on disk says it. Drop it and those projects
# read as `off` — an agent switched on a year ago silently stops being recommended, which is
# the one failure shape this plugin must not have. It is an alias rather than a member so that
# nothing writes or prints it again.
#
# `keep` and `resume` used to alias the removed REUSE mode. They are NOT re-pointed at
# ON: a user who types one is asking for the thing that no longer exists, and silently
# giving them a fresh instance per turn would answer a different question. `_parse_mode`
# returns None and the CLI says the value is not a mode, which is the honest reply.
_MODE_ALIASES = {
    "fresh": AgentMode.ON,
    "true": AgentMode.ON, "yes": AgentMode.ON, "1": AgentMode.ON, "new": AgentMode.ON,
    "false": AgentMode.OFF, "no": AgentMode.OFF, "0": AgentMode.OFF,
}


DEFAULT_CONFIG: dict[str, Any] = {
    # There is deliberately no key for the router's model. `agents/turn-router.md` pins `opus` and
    # that is the whole decision: every other agent in the set is paid for by one the router
    # makes, so the direction a project would tune this in — cheaper — is the direction whose
    # failure is invisible. A router that stops naming an agent looks exactly like a turn with
    # nothing in it, and the audit that never happened is the failure guard exists to prevent.
    #
    # One key per AUDIT, named after what it audits. For most of these the key is also the
    # agent's own name, so `settings set deferrals-auditor on` and
    # `guard:deferrals-auditor` are the same string and there is no second vocabulary. Where
    # one audit is reached through two entry points — `claims-auditor` through the
    # `audit-turn-claims` and `audit-report-claims` skills — the key stays the audit's,
    # because it is what a project has already written in its config file;
    # `agents._path_entry` is the one place it becomes an entry-point name, and the user
    # never types either of those. The value is
    # an `AgentMode`, so how the agent runs is the same setting as whether it runs: there
    # is no separate list of any kind that could name an agent that is off.
    #
    # These are the ONLY control over which audits exist for a project. All of them off
    # (the default) is guard silent at Stop and empty when an audit is invoked: no answer
    # file, no router roster, nothing added to the main agent's context. There is
    # deliberately no separate mode setting in front of them — switching one on IS switching
    # guard on, and a project that wants the claim check without the deferral check just
    # switches the one it wants.
    #
    # Every switch ships off: guard installed is guard available, not guard running. What
    # `off` costs is unchanged by the audit becoming on-demand — the user's own
    # `/guard:audit-turn` reads this same roster, so `off` still means the audit cannot
    # happen rather than merely that it is not offered. See `AGENTS.md`.
    # The state each session's two audits OPEN in — the project's answer to "audit by
    # default?". They part company when the file says nothing, and the split is the point:
    # the turn audit costs a router call plus whatever it names on EVERY finished turn, so it
    # opens muted and the user arms it (`guard on`) for the stretch of work that wants it. The
    # plan gate opens armed because it fires only at `ExitPlanMode` — rare, and at the one
    # moment where letting a deferral through is paid for by the whole implementation that
    # follows.
    #
    # These are the DEFAULT, not the live value: `guard` / `guard-plan` move `audit_paused` /
    # `plan_audit_paused` in `state/<sid>.json` for one session and never write here, so a
    # session muted at a shell prompt stays muted without changing what the next session does.
    # Two keys rather than one because the two audits run at different moments on different
    # material — a finished answer against a plan awaiting approval — and wanting one is not
    # wanting the other.
    #
    # A value that is neither an on-word nor an off-word falls back to this key's own default
    # (`_audit_on`), so an unreadable value lands wherever an absent one would. That is the
    # only guarantee worth making here: a project that mistypes a switch gets the behaviour it
    # would have had without the key at all, rather than a third answer it never wrote.
    AUDIT_TURN_KEY: "off",
    AUDIT_PLAN_KEY: "on",
    "claims-auditor": AgentMode.OFF,
    "deferrals-auditor": AgentMode.OFF,
    # Can the intended reader follow the answer? The only agent whose verdict depends on
    # who is reading, which is why it carries `memory: user` rather than `local` and why
    # it degrades loudly — with no reader profile it says so and checks less, instead of
    # guessing a level and flagging either every technical term or none of them.
    "clarity-auditor": AgentMode.OFF,
    # Comments in the source files THIS TURN edited. Unlike the three above it is not
    # an audit of the response: it points a corrector at real files and that corrector
    # EDITS them, unattended, in the turn the user is still reading. That is why it is
    # the one switch whose cost is a diff rather than a report.
    "comment-corrector": AgentMode.OFF,
    # The `AGENTS.md` / `CLAUDE.md` files THIS TURN edited, judged as instruction files:
    # a map pointing at the deeper docs, plus what a model gets wrong here — never the
    # implementation detail, the spec, or the thing every model already knows. Reports
    # only. Turning it on costs nothing on the many turns that touch no such file, since
    # eligibility needs one this turn actually wrote.
    "agents-md-auditor": AgentMode.OFF,
    # Where this project writes down what its DEPLOYED system looks like — topology,
    # environments, runbooks. Read by `design-environment` and by nothing else; guard never
    # writes here. Empty (the default) means the project has none, which is a normal state:
    # that agent then falls back to the repository's own deploy surface, to a read-only
    # probe, and finally to asking the user.
    #
    # Unlike `refs_dir` this is NOT confined to the project. The material it points at is
    # frequently a knowledge base kept outside the repository, and since nothing derives a
    # write from it, the containment rules that make `refs_dir` a hazard have nothing to
    # protect here. See `paths._knowledge_dirs`.
    #
    # A LIST — this knowledge is normally split across directories rather than centralized,
    # and order is precedence. A bare string is still accepted (one directory), since that
    # is what a user with one will write.
    "knowledge_dir": [],
    # No key for `docs-finder`, deliberately. It is not one of guard's recommended
    # agents any more: nothing routes it and no hook forces the session into it, so there is
    # no "says something unasked" for a switch to govern. The main agent picks it the way it
    # picks any agent — from its description — and an off-by-default switch in front of that
    # would only be a way to make a listed agent silently unusable.
    # Where guard saves local copies of cited docs, relative to
    # the project dir. Empty = the default git-tracked `wiki/ref/`, so the collected
    # references are committed with the repo. Point it at a different tracked path
    # (e.g. "docs/refs") to override. Values that resolve outside the project, at the
    # project root, or into guard's own config/state are ignored (fall back to the
    # default) — see _refs_dir for why.
    "refs_dir": "",
}


def _trace_enabled() -> bool:
    return os.environ.get(TRACE_ENV_VAR, "").strip().lower() in TRACE_TRUTHY


def _cli_write_allowed() -> bool:
    """True when a config-mutating CLI verb may write.

    guard never gates Bash, so the model can invoke this script directly — and the
    config-mutating verbs can weaken guard itself: `settings set claims-auditor off`
    stops the automatic audit. The `guard:settings` skill is
    `disable-model-invocation: true` (user-invoked only) and sets this marker; a bare
    model-issued Bash call does not have it.

    This is a SPEED BUMP, NOT A SECURITY BOUNDARY: the variable name is in this file,
    which the model can read, so a model that decides to defeat guard can set it. What
    it buys is (a) the unreflective path — "this gate is in my way, let me widen it" —
    fails closed, (b) the refusal names the user as the only legitimate widener, and
    (c) the attempt lands in the trace as `refused_no_skill_marker`. A model that
    deliberately sets the marker is outside guard's threat model, and either way the
    Bash call is visible to the user in the transcript.
    """
    return os.environ.get(CLI_WRITE_ENV_VAR, "").strip().lower() in TRACE_TRUTHY


def _load_config(project_dir: Path) -> dict[str, Any]:
    """Load the JSON config at guard.local.json, if present. Fail-open to defaults.

    Only keys present in DEFAULT_CONFIG are honored, and only when the supplied value
    matches the default's JSON type — a str for the agent modes and ``refs_dir``, a list
    (or a bare str) for ``knowledge_dir`` — so a malformed value can never change a setting
    by accident.
    """
    config = dict(DEFAULT_CONFIG)
    path = project_dir / CONFIG_REL
    if not path.is_file():
        return config
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return config
    if not isinstance(data, dict):
        return config
    for key, default in DEFAULT_CONFIG.items():
        # An ``AgentMode`` default round-trips through JSON as a plain str, and
        # ``isinstance("on", AgentMode)`` is False — so the accepted type has to be
        # widened for those keys or every mode in the file is silently dropped and only
        # the session state is ever honored. The accessor (``_agent_mode``) validates the
        # value; this only checks the shape.
        want: type | tuple[type, ...]
        if key in AUDIT_SWITCHES:
            # `"off"` and `false` are the same instruction written two ways, and a two-valued
            # switch is the one setting a user reasonably writes as a JSON boolean. Rejecting
            # one of the two spellings would silently ignore an intention that is not
            # ambiguous; `_audit_on` reads both.
            want = (str, bool)
        elif isinstance(default, StrEnum):
            want = str
        elif isinstance(default, list):
            # A list default accepts a bare string too — `knowledge_dir` takes one
            # directory written plainly. The resolver normalizes; this only checks shape.
            want = (list, str)
        else:
            want = type(default)
        if key in data and isinstance(data[key], want):
            config[key] = data[key]
    return config


def _load_raw_config(project_dir: Path) -> dict[str, Any]:
    """Read guard.local.json as a raw dict (unmerged, no defaults applied), or {} if
    missing/malformed. Used by the ``settings`` CLI so it can edit one key in place
    while preserving every other key the user has set."""
    path = project_dir / CONFIG_REL
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def _write_config(project_dir: Path, data: dict[str, Any]) -> bool:
    """Atomically write guard.local.json. Returns True on success."""
    path = project_dir / CONFIG_REL
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.parent / (path.name + ".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        tmp.replace(path)
        return True
    except OSError:
        return False


def _parse_mode(value: str) -> AgentMode | None:
    """Parse a CLI mode word; None when the spelling is not recognized (the caller
    reports the error rather than guessing, since guessing here could silently turn an
    agent off or leave a stale instance in charge)."""
    v = value.strip().lower()
    if v in _MODE_ALIASES:
        return _MODE_ALIASES[v]
    try:
        return AgentMode(v)
    except ValueError:
        return None


def _agent_mode(cfg: dict[str, Any], key: str) -> AgentMode:
    """One agent's mode from a config or session-state dict, coerced to a valid member.

    Anything unrecognized lands on the default rather than raising: a hand-edited config
    must not be able to break the hook, and the ``settings`` CLI is where a bad value
    gets rejected out loud. A stringy value that is not a mode word therefore reads as
    ``off`` — the safe direction, since the alternative is guard acting on a setting the
    user did not write.

    It reads through ``_parse_mode``, so the aliases apply HERE and not only at the CLI. That
    is what makes a config file written before v0.116.0 — every one of which spells the on
    mode ``fresh`` — keep working: the hooks read this function, never the CLI, so an alias
    the CLI alone honoured would leave those projects silently unaudited.
    """
    # A key with no default is an agent with no switch (`AuditAgent.fixed_mode`). Callers
    # are meant to consult the roster for those, so reaching here is a bug — but it must not
    # be a crash: this runs inside hooks, and an exception here took `settings show` down to
    # silent-and-exit-0 once, which is the shape guard must never fail into.
    default = DEFAULT_CONFIG.get(key, AgentMode.OFF)
    parsed = _parse_mode(str(cfg.get(key, default)))
    if parsed is not None:
        return parsed
    return _parse_mode(str(default)) or AgentMode.OFF


def _switch_on(cfg: dict[str, Any], key: str) -> bool:
    """Whether this agent may be recommended at all."""
    return _agent_mode(cfg, key) is not AgentMode.OFF


def _parse_switch(value: str) -> bool | None:
    """Parse an on/off word: True armed, False muted, None when it is neither.

    The caller reports the error rather than guessing — this is what the ``settings`` CLI
    validates a written value with, and guessing there would record a switch the user did not
    ask for in a file that outlives the session.
    """
    v = value.strip().lower()
    if v in _ON_WORDS:
        return True
    if v in _OFF_WORDS:
        return False
    return None


def _audit_on(cfg: dict[str, Any], key: str) -> bool:
    """Does this project's config open a session with ``key``'s audit armed?

    A CONFIG reader, never a state reader: the live answer for a session is
    ``state._audit_paused`` / ``state._plan_audit_paused``, which this seeds and the shell
    toggle then overrides. Absent, malformed, or written as a JSON boolean all resolve here —
    and anything unrecognized resolves to THAT KEY's own default, which is muted for
    ``audit-turn`` and armed for ``audit-plan`` (see ``DEFAULT_CONFIG``). Per-key rather than one
    direction for both: a mistyped switch then lands where an absent one would, which is the
    only fallback a project can predict once the two keys disagree.
    """
    raw = cfg.get(key, DEFAULT_CONFIG[key])
    if isinstance(raw, bool):
        return raw
    parsed = _parse_switch(str(raw))
    if parsed is None:
        return _parse_switch(str(DEFAULT_CONFIG[key])) is True
    return parsed


