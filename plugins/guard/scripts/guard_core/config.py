"""Host split, agent modes, and the project's configuration file.

Configuration is optional: a JSON object at ``${CLAUDE_PROJECT_DIR}/.claude/guard.local.json``
(``.codex/`` on Codex). One ``AgentMode`` per agent, keyed by that agent's own name —
``claims-auditor`` / ``deferrals-auditor`` / ``clarity-auditor`` / ``korean-corrector`` /
``comment-corrector`` / ``agents-md-auditor`` / ``ext-docs-fetcher`` / ``ext-docs-auditor``, each
``"off"`` (the default) / ``"fresh"`` / ``"reuse"`` — which together are the only control
over whether guard says anything unasked and over whether an agent is respawned per turn or
held open for the session. Plus ``refs_dir`` (project-relative directory for saved copies of cited docs; empty
means the git-tracked default ``wiki/ref/``, and an unsafe value falls back to it — see
``paths._refs_dir``) and ``router_model`` (a model override for the router alone; empty
leaves the choice to ``agents/router.md``, and every agent the router recommends brings its
own model from its own definition).

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


class AgentMode(StrEnum):
    """How one audit agent runs. The value of that agent's config key.

    ``OFF`` — never recommended unasked. ``FRESH`` — a new instance per dispatch, which
    is the shape every agent definition is written for: judged in a fresh context, by a
    reader rather than the author. ``REUSE`` — one named instance per session, resumed on
    later turns with its full history.

    ``REUSE`` is not strictly better and not strictly worse, which is why it is the
    user's call and not a default. It buys continuity: the instance already knows this
    repository and this session's conventions, it does not re-derive the same thing every
    turn, and the main agent can go back to it ("you cleared this claim two turns ago —
    does the change I just made break it?"). It costs independence: a verdict it got
    wrong is now in its own history as settled, and every later turn inherits that error,
    where a fresh instance would have looked again. Continuity is worth most where the
    judgment is about text and conventions (the correctors); independence is worth most
    where it is about whether something is true (the auditors).

    Reuse is per SESSION, not per project — subagent transcripts live under the session
    id, so a new session starts every agent fresh whatever this says
    (``wiki/ref/claude-code-subagent-resume.md``).
    """

    OFF = "off"
    FRESH = "fresh"
    REUSE = "reuse"


# CLI spellings accepted for a mode, beyond the member values themselves. The boolean
# words are kept because "on"/"off" is what a switch has always been set with here, and
# "on" has to mean something: it means the mode the agents were designed for.
_MODE_ALIASES = {
    "on": AgentMode.FRESH, "true": AgentMode.FRESH, "yes": AgentMode.FRESH,
    "1": AgentMode.FRESH, "new": AgentMode.FRESH,
    "false": AgentMode.OFF, "no": AgentMode.OFF, "0": AgentMode.OFF,
    "keep": AgentMode.REUSE, "resume": AgentMode.REUSE,
}


DEFAULT_CONFIG: dict[str, Any] = {
    # Model for the router agent, overriding whatever `agents/router.md` declares.
    # Empty (the default) means guard says nothing about the model and the agent's own
    # frontmatter governs — the normal way a subagent's model is chosen, and the one
    # that keeps working when a host has no way to override it at dispatch. This exists
    # for the project that wants the router cheaper or sharper than the plugin ships it:
    # a router that misses means the audit silently never happens, which is the exact
    # failure guard exists to prevent, and the other direction costs just as much — a
    # model that cannot tell a backed claim from one that merely sounds backed names
    # every agent every turn, which is the same as naming none, because the user stops
    # reading the recommendation.
    "router_model": "",
    # One key per agent, named after the agent it controls — the key IS the agent's name,
    # so `settings set korean-corrector reuse` and `guard:korean-corrector` are the same
    # string and there is no second vocabulary to learn or to keep in sync. The value is
    # an `AgentMode`, so how the agent runs is the same setting as whether it runs: there
    # is no separate reuse list that could name an agent that is off.
    #
    # These are the ONLY control over whether guard says anything unasked. All of them off
    # (the default) is guard silent at Stop: no router, no recommendation, nothing added
    # to the main agent's context. There is deliberately no separate mode setting in
    # front of them — switching one on IS switching guard on, and a project that wants
    # the claim check without the deferral check just switches the one it wants.
    #
    # None of them governs the on-demand `/guard:<agent>` commands: a switch that is off
    # still leaves the user free to ask for that audit now. That is why every switch
    # ships off — guard installed is guard available, not guard running.
    "claims-auditor": AgentMode.OFF,
    "deferrals-auditor": AgentMode.OFF,
    # Can the intended reader follow the answer? The only agent whose verdict depends on
    # who is reading, which is why it carries `memory: user` rather than `local` and why
    # it degrades loudly — with no reader profile it says so and checks less, instead of
    # guessing a level and flagging either every technical term or none of them.
    "clarity-auditor": AgentMode.OFF,
    # Does a Korean response read as natural Korean, or as translated English?
    # Switching it on in an English-answering project costs nothing on those turns: the
    # router reads the response and simply does not pick it.
    "korean-corrector": AgentMode.OFF,
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
    # Finds the documentation a question or an answer rests on — in `refs_dir` first, on the
    # network when nothing there covers it — and reports the local path either way. The only
    # switch here that puts an agent on the NETWORK, and the only one whose purpose is partly
    # to stop the main session doing something rather than to check what it did: with this on,
    # the session delegates its fetching, which is announced once at SessionStart. It is also
    # the only agent reached from BOTH ends of a turn — that announcement before an answer
    # exists, and the router afterwards when a finished answer rested on a document nobody
    # saved. And the only routed agent that writes to the repository, so its cost is a diff:
    # new files under `refs_dir` and rows in that directory's index.
    "ext-docs-fetcher": AgentMode.OFF,
    # The files under `refs_dir` THIS TURN wrote, judged as saved references: a trustworthy
    # source named, the content attributed to it rather than recalled, and — the rule that
    # actually gets broken — nothing in them about this repository. Reports only. Pairs with
    # `ext-docs-fetcher`, which is what usually writes those files, but is independent of it:
    # a hand-edited reference is audited the same way.
    "ext-docs-auditor": AgentMode.OFF,
    # Where guard saves local copies of cited docs, relative to
    # the project dir. Empty = the default git-tracked `wiki/ref/`, so the collected
    # references are committed with the repo. Point it at a different tracked path
    # (e.g. "docs/refs") to override. Values that resolve outside the project, at the
    # project root, or into guard's own config/state are ignored (fall back to the
    # default) — see _refs_dir for why.
    "refs_dir": "",
}


# --------------------------------------------------------------------------- #
# environment / paths
# --------------------------------------------------------------------------- #
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
    matches the default's JSON type (every key is a str: the agent modes,
    ``router_model``, ``refs_dir``), so a malformed value can never change a setting by
    accident.
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
        # ``isinstance("reuse", AgentMode)`` is False — so the accepted type has to be
        # widened for those keys or every mode in the file is silently dropped and only
        # the session state is ever honored. The accessor (``_agent_mode``) validates the
        # value; this only checks the shape.
        want = str if isinstance(default, StrEnum) else type(default)
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
    """
    try:
        return AgentMode(str(cfg.get(key, DEFAULT_CONFIG[key])).strip().lower())
    except ValueError:
        return AgentMode(DEFAULT_CONFIG[key])


def _switch_on(cfg: dict[str, Any], key: str) -> bool:
    """Whether this agent may be recommended at all."""
    return _agent_mode(cfg, key) is not AgentMode.OFF


def _router_model(cfg: dict[str, Any]) -> str:
    """The model override for the router agent, or "" to leave the choice to the agent.

    Never validated against a list of names — an alias, a full id, or a provider's own
    name are all legitimate and the set moves. An empty value is not a fallback to some
    default here: it means guard prints no model line at all, so `agents/router.md`
    decides, which is where a subagent's model normally comes from.
    """
    return str(cfg.get("router_model", "")).strip()
