#!/usr/bin/env python3
"""guard hook dispatcher.

stdlib-only, executed directly via its shebang (no ``uv run``). Every subcommand
exits 0; blocking is expressed through decision payloads on stdout, never through
a non-zero exit. Internal failures are silent and fail-open (guard never blocks
because its own machinery broke).

Subcommands
-----------
- user-prompt    UserPromptSubmit. Archive the user turn to the session log. That log is
                 the human-readable session record and the only place the user's own
                 wording is kept; the Stop audit reads the turn itself from the
                 transcript by ``prompt_id``, so nothing is derived here. guard's own
                 ``/guard:settings`` / ``/guard:audit-*`` commands are ignored (not
                 turns).
- settings       CLI (argv), run by the ``guard:settings`` skill (forked) via Bash.
                 ``show`` prints the current settings; ``set <key> <value>`` changes one
                 of the per-agent settings — each named after the agent it controls
                 (``claims-auditor`` / ``deferrals-auditor`` / ``korean-corrector`` /
                 ``comment-corrector``), valued ``off``/``fresh``/``reuse`` — or
                 ``router_model`` / ``refs_dir``. The agent settings also apply to the live
                 session's ``state/<sid>.json`` when a session id is available
                 (``--session``, which the forked skill passes as
                 ``${CLAUDE_SESSION_ID}``, else the inherited
                 ``CLAUDE_CODE_SESSION_ID``); the rest are read from the config file at
                 use. Preserves every other key; ``exempt_skills`` is managed by the
                 ``exempt`` CLI, not here. Mutating verbs require the settings-skill
                 marker — see ``_cli_write_allowed``. Not a hook event.
- verify         UserPromptExpansion, one matcher per axis
                 (``^(guard:)?{claims,deferrals}-auditor$``, ``^(guard:)?korean-corrector$``).
                 On demand, emit the dispatch instruction for that ONE axis's agent
                 over the last completed turn (``pending_verify_prompt_id``, recorded by
                 every Stop). A switch that is off is still auditable this way — the
                 switch governs what guard recommends unasked, not what the user may ask
                 for.
- exempt         CLI (argv), run by the ``guard:settings`` skill via Bash after the user
                 confirms an interactive selection. ``list``/``set``/``add``/
                 ``remove``/``clear`` the ``exempt_skills`` config key — that key ONLY,
                 never the switches/state. Mutating verbs require the settings-skill
                 marker (``_cli_write_allowed``). Not a hook event.
- stop           Stop. A turn == the transcript ``prompt_id``; guard reads the whole
                 turn from Claude Code's transcript (``transcript_path`` +
                 ``prompt_id``, both in the payload) via ``_read_turn_from_transcript``
                 — user request, tool activity, and response. Skips when
                 ``stop_hook_active``, the prompt_id/transcript are absent, the slice
                 contains a user ``!`` command (its output arrives after the response it
                 would have to support, so it is neither evidence nor auditable here),
                 or the turn was opened by guard's own ``/guard:settings`` /
                 ``/guard:audit-*`` control command or a user-configured
                 ``exempt_skills`` entry (skill output / a relay, not claims to ground).
                 Otherwise it archives the turn, writes its slice, and records it as the
                 pending ``/guard:audit-*`` target — in every gate mode. Then, unless
                 the gate is ``off``, it emits ``additionalContext`` asking the main
                 agent to dispatch THE ROUTER (``ROUTER_AGENT``) over the turn, choosing
                 from the eligible agents, and then to dispatch the ones it names,
                 concurrently — under ``ask`` after the user says yes, under ``auto``
                 straight away. guard runs no model itself and never blocks here.
- post-edit      PostToolUse (Write/Edit/MultiEdit/NotebookEdit). Records a source
                 file written this turn (the list a ``comment-corrector``
                 recommendation is built from), and requires a file saved inside the
                 refs directory to be listed in that directory's ``AGENTS.md``, blocking
                 until it is. Both are independent of the agent switches.
- session-start  SessionStart. Sweep state files and turns/ dirs
                 older than retention, and export ``GUARD_REFS_DIR`` (the resolved
                 refs directory) via ``$CLAUDE_ENV_FILE`` for the session's Bash
                 environment.
- refs-dir       Print the resolved refs directory (absolute), applying the
                 ``refs_dir`` validation. Called via Bash (claims auditor fallback / the
                 output style), not a hook event.

State lives project-local under ``${CLAUDE_PROJECT_DIR}/.claude/guard/``:
- ``state/<sid>.json``       — {<agent modes>, edited_prompt_id, edited_files, last_audited_prompt_id, pending_verify_prompt_id, updated_at}
- ``turns/<sid>/<pid>.md``   — the turn every agent in one recommendation reads; guard
                                names the path, the MAIN AGENT writes it (see
                                ``_turn_record_file``). ``<pid>.ko-fix.md`` beside it is
                                where the Korean corrector puts its rewrite.
- ``trace.log``              — file-only debug trace (enabled by GUARD_TRACE)

State is retained across the end of a session so a resumed session
(``claude --resume``) keeps its switch flags; both state and logs are
expired only by the age-based sweep at SessionStart (see ORPHAN_MAX_AGE_SECONDS).

Configuration (optional) is a JSON object at
``${CLAUDE_PROJECT_DIR}/.claude/guard.local.json``: one ``AgentMode`` per agent, keyed by
that agent's own name — ``claims-auditor`` / ``deferrals-auditor`` / ``korean-corrector``
/ ``comment-corrector``, each ``"off"`` (the default) / ``"fresh"`` / ``"reuse"`` — which
together are the only control over whether guard says anything unasked and over whether an
agent is respawned per turn or held open for the session; ``exempt_skills`` (list of strings, default
``[]``) — skills / slash commands whose turn Stop must not audit, named with their
plugin namespace (``plugin:skill``, e.g. ``guard:settings``) or bare for un-namespaced
skills; matched leading-``/``-stripped and case-insensitively (guard's own
``settings``/``audit-*`` control commands are always exempt regardless of this list),
and ``refs_dir`` (string, default ``""``) — project-relative directory where guard saves
local copies of cited docs; empty means the git-tracked default ``wiki/ref/``, so the
collected references are committed with the repo (point it at a different tracked path,
e.g. ``"docs/refs"``, to override; values resolving outside the project, at the project
root, or into guard's own config/state fall back to the default — see ``_refs_dir``).
``router_model`` (string, default ``""``) — a model override for the router
agent only; empty leaves the choice to ``agents/router.md``, and every agent the router
recommends brings its own model from its own definition.
Unknown keys are ignored; a missing or malformed file falls back to all defaults. The
``guard:settings`` skill changes these
through the ``settings`` CLI: it writes guard.local.json and, for the switches, the
live session's state.

Requires Python 3.11+ (uses ``enum.StrEnum``).
"""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
import time
from datetime import datetime, timezone
from enum import StrEnum
from pathlib import Path
from typing import Any, NamedTuple


# Codex adapters set GUARD_HOST before importing this module. Keep the historical
# Claude paths intact while preventing one host from interpreting the other's state.
if os.environ.get("GUARD_HOST") == "codex":
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
# List-CLI verbs that write the config; `list` and unknown verbs only report.
_CLI_MUTATING_VERBS = {"set", "add", "remove", "rm", "clear"}
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
    # These are the ONLY control over whether guard says anything unasked. All four off
    # (the default) is guard silent at Stop: no router, no recommendation, nothing added
    # to the main agent's context. There is deliberately no separate mode setting in
    # front of them — switching one on IS switching guard on, and a project that wants
    # the claim check without the deferral check just switches the one it wants.
    #
    # None of them governs the on-demand `/guard:audit-*` commands: a switch that is off
    # still leaves the user free to ask for that audit now. That is why every switch
    # ships off — guard installed is guard available, not guard running.
    "claims-auditor": AgentMode.OFF,
    "deferrals-auditor": AgentMode.OFF,
    # Does a Korean response read as natural Korean, or as translated English?
    # Switching it on in an English-answering project costs nothing on those turns: the
    # router reads the response and simply does not pick it.
    "korean-corrector": AgentMode.OFF,
    # Comments in the source files THIS TURN edited. Unlike the three above it is not
    # an audit of the response: it points a corrector at real files and that corrector
    # EDITS them, unattended, in the turn the user is still reading. That is why it is
    # the one switch whose cost is a diff rather than a report.
    "comment-corrector": AgentMode.OFF,
    # Skills / slash commands Stop must NOT recommend an audit for. A turn opened
    # by one of these is skill output or a relay, not a body of technical claims to
    # ground. Values are the name as it appears after the slash, INCLUDING the plugin
    # namespace (e.g. "guard:settings", "hindsight:review") or the bare name for an
    # un-namespaced skill ("deep-research"); matched leading-'/'-stripped and
    # case-insensitively. guard's own control commands are always exempt
    # regardless of this list.
    "exempt_skills": [],
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
    stops the automatic audit, and `exempt add <skill>` drops a skill's turns from
    it. The `guard:settings` skill is
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


def _project_dir() -> Path | None:
    value = os.environ.get("GUARD_PROJECT_DIR") or os.environ.get("CLAUDE_PROJECT_DIR")
    return Path(value) if value else None


def _state_root(project_dir: Path) -> Path:
    return project_dir / STATE_DIR_REL


def _state_file(project_dir: Path, session_id: str) -> Path:
    return _state_root(project_dir) / "state" / f"{session_id}.json"


def _turn_record_file(project_dir: Path, session_id: str, prompt_id: str) -> Path:
    """The file the turn is passed between agents in. Written by guard, then extended.

    The turn goes through a file rather than through the dispatch text, and that is the
    whole coordination mechanism here. A routed turn has up to five readers — the router,
    then whichever agents it names — and pasting the turn into each dispatch means writing
    it out that many times, in a message the main agent composes itself, which is exactly
    where a turn quietly becomes a paraphrase of the turn. One file, read by everyone.

    Ownership is split, and the split is the point:

    - guard writes the RESPONSE section itself, at Stop, from ``last_assistant_message``
      in the payload. It is the text being audited, so it is the one part that must not
      pass through the author's hands — and guard is handed it for free.
    - the main agent appends everything else, because guard cannot see it: the request,
      the turn's tool activity, and whatever earlier evidence the response's claims rest
      on. guard has no transcript slice any more and no window past this turn.

    See ``_append_turn_instruction`` for why the second half is asked for as inclusion
    rather than selection.
    """
    return _state_root(project_dir) / "turns" / session_id / f"{prompt_id}.md"


# Section headings in the turn record. Fixed strings, because both the instruction that
# asks for a section and the agent definitions that say which section to read name them.
TURN_RESPONSE_HEADING = "## Assistant response (written by guard, verbatim)"
TURN_CONTEXT_HEADING = "## Request, tool activity, and prior evidence"


def _write_turn_response(project_dir: Path, session_id: str, prompt_id: str,
                         response: str) -> Path | None:
    """Write the record with the response section filled in. Returns the path, or None.

    Best-effort, and a failure is silent: the recommendation is emitted anyway, and the
    main agent is asked to create the file if it is not there. A guard that refused to
    recommend because it could not write a scratch file would be failing closed on its own
    plumbing.
    """
    path = _turn_record_file(project_dir, session_id, prompt_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"{TURN_RESPONSE_HEADING}\n\n{response.rstrip()}\n\n"
            f"{TURN_CONTEXT_HEADING}\n\n(to be appended by the main session)\n",
            encoding="utf-8")
    except OSError:
        return None
    return path


def _korean_rewrite_file(project_dir: Path, session_id: str, prompt_id: str) -> Path:
    """File the Korean corrector writes its rewritten response to.

    Beside the turn record, inside guard's own state: the rewrite is a proposal for the
    main agent to relay, not a user artifact, so it must not land in the user's tree.
    guard never reads it back — only the corrector writes it and only the main agent,
    told the path in its dispatch, reads it.
    """
    return _state_root(project_dir) / "turns" / session_id / f"{prompt_id}.ko-fix.md"


def _safe_project_subdir(project_dir: Path, raw: Any) -> Path | None:
    """Resolve a configured project-relative directory, or None if it is not safe.

    guard's self-neutering defense for a config key that names a directory guard
    treats specially (``refs_dir``). A value is honored only when it resolves:

    - inside the project, STRICTLY below it — ``project not in candidate.parents``
      rejects the project root itself, because a path is never in its own
      ``.parents`` and ``"."`` resolves to the project dir. A root-level exemption
      would exempt every project write and neuter the gate, so this strictness is
      load-bearing: do not relax it to a ``==``-tolerant containment test.
    - outside guard's OWN config/state — a value of ``.claude/guard`` would let the
      model write ``state/<sid>.json``, and ``.claude/guard.local.json`` would let it
      turn the audit off.

    Note what this does NOT catch: an ANCESTOR of guard's state (e.g. ``.claude``)
    is a legal value — it is neither the state root nor under it.

    Returns the resolved absolute Path, or None when the value is unusable (not a
    non-empty str, unresolvable, or failing either rule above); ``_refs_dir`` then
    falls back to its default.
    """
    if not isinstance(raw, str) or not raw.strip():
        return None
    try:
        candidate = (project_dir / raw.strip()).resolve()
        project = project_dir.resolve()
        state_root = _state_root(project_dir).resolve()
        config_path = (project_dir / CONFIG_REL).resolve()
    except OSError:
        return None
    if project not in candidate.parents:
        return None
    if candidate == state_root or state_root in candidate.parents or candidate == config_path:
        return None
    return candidate


def _refs_dir(project_dir: Path, config: dict[str, Any] | None = None) -> Path:
    """Directory where guard saves local copies of cited docs.

    Writes here are the assistant grounding its own claims (per the output style),
    not implementing the user's task.

    Default is ``wiki/ref/`` under the project, a git-tracked location so the
    collected references are committed with the repo; the ``refs_dir`` config key
    may point it at a different project path (e.g. ``docs/refs``). A configured
    value is honored only when ``_safe_project_subdir`` accepts it (strictly inside
    the project, outside guard's own config/state — see there for why); anything
    else falls back to the default, so ``refs_dir`` can never become a hole.
    """
    default = project_dir / "wiki" / "ref"
    return _safe_project_subdir(project_dir, (config or {}).get("refs_dir", "")) or default


def _project_rel(project_dir: Path, path: Path) -> str:
    """Project-relative form of an absolute path, for display. Falls back to the
    absolute path when it can't be made relative."""
    try:
        return str(path.resolve().relative_to(project_dir.resolve()))
    except (OSError, ValueError):
        return str(path)


def _trace_file(project_dir: Path) -> Path:
    return _state_root(project_dir) / TRACE_FILE_NAME


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _trace(project_dir: Path | None, session_id: str | None, cmd: str, event: str, **fields: Any) -> None:
    if not _trace_enabled() or project_dir is None:
        return
    try:
        path = _trace_file(project_dir)
        path.parent.mkdir(parents=True, exist_ok=True)
        record = {"ts": _now_iso(), "sid": session_id, "cmd": cmd, "event": event}
        record.update(fields)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass


# --------------------------------------------------------------------------- #
# payload / config / state
# --------------------------------------------------------------------------- #
def _read_payload() -> dict | None:
    try:
        raw = sys.stdin.read()
    except OSError:
        return None
    if not raw.strip():
        return None
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return None
    return payload if isinstance(payload, dict) else None


_SESSION_ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")
# guard's own control commands, e.g. "/guard:settings claims-auditor off", "/settings",
# "/guard:claims-auditor". `settings` is a forked skill and each per-agent command a
# UserPromptExpansion — either way the turn is a relay, not real work to log/judge. The
# name is `settings`, not `config`, precisely so the bare form does NOT match Claude Code's
# built-in `/config` command (which the optional `(guard:)?` would otherwise capture,
# making guard treat every `/config` as its own control command). `(?=\s|$)` rather than
# `\b`: the name must END here, not merely hit a word boundary — `\b` would also accept a
# longer hyphenated name from another plugin (`/settings-export` matching `settings`), and
# it is what keeps `claims-auditor` from matching a bare `/claims`.
# `comment-corrector` is deliberately ABSENT: that skill's relayed findings are claims about
# real files and about edits made to them, so its turn stays auditable like any other work.
_CONTROL_CMD_RE = re.compile(
    r"^/(guard:)?(settings|claims-auditor|deferrals-auditor|korean-corrector)(?=\s|$)",
    re.IGNORECASE)
# In the transcript, a slash command is expanded to
# "<command-name>/guard:settings</command-name>" (see session b30dbaec). Pull the command
# name out of that tag; a raw typed form ("/guard:settings claims-auditor off") is handled by
# the fallback in _turn_command_name.
_COMMAND_NAME_RE = re.compile(r"<command-name>\s*(/?[^<\n]+?)\s*</command-name>", re.IGNORECASE)


def _session_id(payload: dict) -> str | None:
    sid = payload.get("session_id")
    if not isinstance(sid, str) or not sid:
        return None
    # Defensive: session_id is interpolated into state/log filenames. Reject any
    # value that could escape the state directory (path separators, `..`). Note
    # the charclass alone still admits "..", so exclude that explicitly.
    if ".." in sid or not _SESSION_ID_RE.match(sid):
        return None
    return sid


def _message_of(record: Any) -> dict[str, Any]:
    msg = record.get("message") if isinstance(record, dict) else None
    return msg if isinstance(msg, dict) else {}


def _turn_command_name(user_text: str) -> str:
    """The slash command that opened the turn, normalized (leading '/' stripped,
    lowercased), or '' when the turn was not opened by a slash command.

    Slash commands reach the transcript expanded as
    ``<command-name>/guard:settings</command-name>``; a raw typed form
    (``/guard:settings claims-auditor off``) is handled by the fallback.
    """
    text = user_text.strip()
    m = _COMMAND_NAME_RE.search(text)
    if m:
        name = m.group(1).strip()
    elif text.startswith("/"):
        name = text.split()[0]
    else:
        return ""
    return name.lstrip("/").lower()


def _is_control_command_name(name: str) -> bool:
    """True when a normalized command name is one of guard's own control commands
    (``settings``/``*-auditor``/``korean-corrector``, with or without the ``guard:``
    prefix)."""
    return bool(name) and bool(_CONTROL_CMD_RE.match("/" + name))


def _norm_skill(name: Any) -> str:
    """Normalize a skill / command name for storage and matching: leading '/' stripped,
    lowercased, plugin namespace (``plugin:skill``) preserved. '' if not a usable str."""
    if not isinstance(name, str):
        return ""
    return name.strip().lstrip("/").lower()


def _exempt_skills(config: dict[str, Any]) -> set[str]:
    """Normalized set of skill / command names whose turn Stop must not audit
    (from the ``exempt_skills`` config key). Values keep their plugin namespace
    (``plugin:skill``); compared leading-'/'-stripped and lowercased, matching
    ``_turn_command_name``."""
    raw = config.get("exempt_skills", [])
    if not isinstance(raw, list):
        return set()
    return {n for n in (_norm_skill(c) for c in raw) if n}


def _turn_identity(transcript_path: Any, prompt_id: Any) -> dict[str, str] | None:
    """What KIND of turn this is, read from the transcript anchor. Never its content.

    Returns ``{origin_kind, command_name}``, or None (fail-open) when the transcript is
    unreadable or the prompt_id is not in it.

    guard used to reconstruct the whole turn here — request, tool activity, response —
    and hand it to the agents as a file. It no longer does: the main agent already holds
    the turn it just produced, so it can pass the text to the router and to the agents
    itself, and a second copy cut by guard was work and storage for nothing.

    What guard still cannot get from the payload is how the turn was OPENED, and both
    users of it are skips, not audits:

    - ``origin_kind`` — a typed prompt is ``"human"``; a background subagent's
      completion opens a NEW turn (fresh promptId) anchored on a ``<task-notification>``
      record (``origin.kind == "task-notification"``, promptSource "system", NOT
      ``isMeta``, so otherwise indistinguishable from a typed prompt). Recommending an
      audit there is self-perpetuating: the audit dispatch is itself a background task
      whose completion is another task-notification (verified 2.1.197).
    - ``command_name`` — the slash command that opened the turn, so a turn that is
      guard's own control command or a user-exempted skill can be skipped.

    Only the ANCHOR record is examined. Records derived from the turn carry
    ``promptId=None``, and nothing about them changes the turn's kind.
    """
    if not isinstance(transcript_path, str) or not isinstance(prompt_id, str) or not prompt_id:
        return None
    path = Path(transcript_path)
    if not path.is_file():
        return None
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except (json.JSONDecodeError, ValueError):
            continue
        if not isinstance(rec, dict) or rec.get("promptId") != prompt_id:
            continue
        origin = rec.get("origin")
        content = _message_of(rec).get("content")
        return {
            "origin_kind": str(origin.get("kind") or "") if isinstance(origin, dict) else "",
            "command_name": _turn_command_name(content if isinstance(content, str) else ""),
        }
    return None


def _load_config(project_dir: Path) -> dict[str, Any]:
    """Load the JSON config at guard.local.json, if present. Fail-open to defaults.

    Only keys present in DEFAULT_CONFIG are honored, and only when the supplied value
    matches the default's JSON type (str for the agent modes and for ``router_model`` /
    ``refs_dir``, list for ``exempt_skills``), so a malformed value can never change a
    setting by accident.
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
    missing/malformed. Used by the exempt CLI so it can edit ``exempt_skills`` in place
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


def _read_state(project_dir: Path, session_id: str, config: dict[str, Any]) -> dict[str, Any]:
    default = {
        **{k: str(_agent_mode(config, k)) for k in AUDIT_AGENTS},
        # Per-turn guards keyed by the transcript prompt_id (a turn == one promptId).
        "last_audited_prompt_id": "",
        # The most recent auditable turn's prompt_id — the target a `/guard:audit-*`
        # command dispatches its agent for. Recorded by every Stop, switches or not.
        "pending_verify_prompt_id": "",
        # Source files written during one turn, accumulated by PostToolUse and read back
        # at Stop to decide whether `comment-corrector` has anything to look at. Stored
        # WITH the prompt_id it belongs to: a bare list would outlive its turn and point
        # the corrector at files the current turn never touched.
        "edited_prompt_id": "",
        "edited_files": [],
        "updated_at": None,
    }
    path = _state_file(project_dir, session_id)
    if not path.is_file():
        return default
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return default
    if not isinstance(data, dict):
        return default
    keys = (*AUDIT_AGENTS, "last_audited_prompt_id", "pending_verify_prompt_id",
            "edited_prompt_id", "edited_files", "updated_at")
    default.update({k: data[k] for k in keys if k in data})
    return default


def _write_state(project_dir: Path, session_id: str, state: dict[str, Any]) -> None:
    state["updated_at"] = _now_iso()
    path = _state_file(project_dir, session_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
        tmp.replace(path)
    except OSError:
        pass


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


# --------------------------------------------------------------------------- #
# the agents guard can recommend
# --------------------------------------------------------------------------- #
class AuditAgent(NamedTuple):
    """One agent guard can recommend, plus everything its dispatch text needs.

    Keyed in ``AUDIT_AGENTS`` by the agent's own bare name, which is also its config
    switch key and, namespaced, its ``subagent_type``. One string for one agent: the
    setting the user types, the key in the state file, and the agent that gets
    dispatched cannot drift apart because they are the same string.

    ``reads`` is what the agent is pointed at — ``"turn"`` for the turn record guard
    sliced, ``"files"`` for the source files the turn edited — and it selects the inputs
    the dispatch carries. ``verify_command`` marks the agents that also have their own
    ``/guard:*`` command over the last completed turn; it is what stops ``cmd_verify``
    from dispatching an agent no command can reach.

    No cue for the router here: the router's cue per agent is its own instruction, and it
    lives in ``agents/router.md``. Keeping it out of this table is what keeps the Stop
    hook's ``additionalContext`` small — that text enters the main agent's context on
    every routed turn, so a paragraph per candidate would be paid for every turn.
    """

    what: str
    reads: str
    verify_command: bool
    tail: str

    @property
    def summary(self) -> str:
        """The agent's one-line job, phrased for what it was actually handed."""
        subject = "the turn" if self.reads == "turn" else "the files it is given"
        return f"audits {subject} for {self.what}"


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


def _dispatch_line(key: str, mode: AgentMode, cont: str) -> str:
    """How to get this agent working, given its mode.

    Under ``FRESH`` this is a plain dispatch. Under ``REUSE`` it is "resume the named
    instance if it exists, else dispatch under that name", which is the documented shape:
    a completed subagent that receives a ``SendMessage`` auto-resumes with its full
    history, and no agent-teams setting is needed for a plain message
    (``wiki/ref/claude-code-subagent-resume.md``).

    The order matters — resume first, dispatch second. Written the other way round the
    main agent spawns a second instance under a name that is already taken, and then
    there are two of them with divergent histories and no way to tell which one answered.
    """
    agent_id = _agent_id(key)
    if mode is not AgentMode.REUSE:
        return (f"{cont}Dispatch it with the Agent tool (subagent_type: \"{agent_id}\"), "
                f"passing these inputs:")
    inst = _instance_name(key)
    return (f"{cont}This agent is in REUSE mode. If `{inst}` already exists in this "
            f"session, SendMessage it (to: \"{inst}\") — it resumes with everything it "
            f"has already read and judged. Only if it does not exist, dispatch it with "
            f"the Agent tool (subagent_type: \"{agent_id}\", name: \"{inst}\"). Either "
            f"way, give it these inputs:")


# Order here is the order the agents appear in a recommendation. The two read-only
# auditors come first: their findings may change what the correctors should be run on.
AUDIT_AGENTS: dict[str, AuditAgent] = {
    "claims-auditor": AuditAgent(
        what="claims asserted without adequate evidence",
        reads="turn",
        verify_command=True,
        tail="It writes nothing. If it reports violations, address them; otherwise continue.",
    ),
    "deferrals-auditor": AuditAgent(
        what="work punted as TBD / 확인 필요 that the repository could have answered",
        reads="turn",
        verify_command=True,
        tail="It writes nothing. If it reports violations, address them; otherwise continue.",
    ),
    "korean-corrector": AuditAgent(
        what="Korean prose that reads as translated English rather than written",
        reads="turn",
        verify_command=True,
        tail=("On violations it also writes the corrected response to the rewrite path "
              "and names it in its report; read that file and use its text as the "
              "corrected wording, keeping any phrase it listed as unfixed for yourself "
              "to resolve. On a pass it writes nothing and there is nothing to do."),
    ),
    "comment-corrector": AuditAgent(
        what=("comments that are false, that only restate the code, or that are missing "
              "where the intent is not obvious"),
        reads="files",
        verify_command=False,
        tail=("It EDITS the comments in place, so its changes are already in the files "
              "when it reports. Relay what it changed AND what it left unfixed — an "
              "unfixed finding needs the user — and do not re-edit its work."),
    ),
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

# --------------------------------------------------------------------------- #
# the router
#
# guard makes NO model call of its own. When a turn finishes and the gate is open,
# the Stop hook decides one mechanical thing — is any agent even eligible — and then
# asks the main agent to dispatch ONE subagent, the router, whose whole job is to read
# the finished response and say which of the eligible specialists would find something
# in it.
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
# The roster is built HERE, not in `agents/router.md`, and it lists only the agents
# this turn is eligible for. The router's definition holds the method — triage, not
# adjudication — while the per-agent cue stays next to the agent table it belongs to.
# An agent absent from the roster cannot be picked, which beats describing a disabled
# agent and appending "but this one is off".
# --------------------------------------------------------------------------- #
ROUTER_AGENT = "guard:router"


def _router_roster(keys: list[str], edited: list[str]) -> str:
    """The candidate list handed to the router: the eligible keys, one per line.

    Keys only. What each key means, and the cue for picking it, is in the router's own
    definition — repeating it here would put a paragraph per candidate into the main
    agent's context on every routed turn.

    Only eligible keys are listed, and the dispatch blocks printed below the roster cover
    exactly the same set, so a key the router invents has nothing to dispatch. That is the
    real bound on the answer; the roster is what stops it being reached for in the first
    place.
    """
    lines = []
    for key in keys:
        line = f"- `{key}`"
        if AUDIT_AGENTS[key].reads == "files":
            line += " (this turn wrote: " + ", ".join(Path(f).name for f in edited) + ")"
        lines.append(line)
    return "\n".join(lines)


def _eligible_agents(state: dict[str, Any], edited: list[str]) -> list[str]:
    """The agents the router may choose from, in ``AUDIT_AGENTS`` order.

    Two mechanical gates, and only mechanical ones — everything that needs judgment is
    the router's call:

    - the switch, which is the user saying they are willing to have this agent run;
    - for a ``reads="files"`` agent, at least one source file this turn wrote, because
      that list is the agent's whole input and the router cannot invent one.

    Notably absent: any language test for ``korean-corrector``. Deciding whether a
    response is Korean enough to audit is a reading task, and the router does it better
    than a Hangul ratio that has to guess how many English identifiers a Korean answer
    may carry before it stops being Korean.
    """
    out: list[str] = []
    for key, spec in AUDIT_AGENTS.items():
        if not _switch_on(state, key):
            continue
        if spec.reads == "files" and not edited:
            continue
        out.append(key)
    return out


# --------------------------------------------------------------------------- #
# dispatch text
# --------------------------------------------------------------------------- #
def _agent_inputs(project_dir: Path, session_id: str, prompt_id: str, key: str,
                  edited: list[str]) -> list[str]:
    """The dispatch inputs for one agent: ONLY what the main agent cannot supply itself.

    For a turn-reading agent that is the path to the turn record — the same path for
    every agent in one recommendation, so they all read the identical text — plus, for
    the Korean corrector, somewhere to put a long rewrite. The main agent writes the
    record; see ``_turn_record_file`` for why the turn travels as a file.

    For ``comment-corrector`` it is instead the source files this turn edited, recorded
    by PostToolUse: a main agent asked to recall which files it wrote will approximate,
    and this is the one agent that EDITS what it is pointed at.

    ``session_id`` / ``prompt_id`` are here to BUILD the rewrite path, never to be handed
    over: an agent auditing one turn has no use for guard's identifiers, and an extra
    pointer is one more thing it can wander into instead of auditing.
    """
    if AUDIT_AGENTS[key].reads == "files":
        return ["- files to audit (comments only, in place):"] + [f"    {p}" for p in edited]
    inputs = ["- turn record: "
              f"{_turn_record_file(project_dir, session_id, prompt_id).resolve()}"]
    if key == "korean-corrector":
        inputs.append("- rewrite path (write the corrected text here): "
                      f"{_korean_rewrite_file(project_dir, session_id, prompt_id).resolve()}")
    return inputs


def _agent_blocks(project_dir: Path, session_id: str, prompt_id: str, keys: list[str],
                  edited: list[str], numbered: bool,
                  modes: dict[str, AgentMode]) -> list[str]:
    """One dispatch block per agent: its name, its job, and the inputs it needs.

    The agents are named individually and each carries its own inputs, so an agent
    learns what to audit from WHICH agent was dispatched rather than from a scope
    argument it has to be trusted to honor. That is why a multi-agent recommendation is
    a list of separate dispatches and never one agent told to cover several axes.

    Guard names the AGENTS here, never its own `/guard:*` skills. Those skills are
    `disable-model-invocation: true` — the user's own entry point, not something a hook
    may reach through — and the Agent tool is the only path guard asks the main agent to
    take.

    ``modes`` carries each key's ``AgentMode``; it is passed in rather than re-read from
    config because the caller has already resolved it from session state, which can differ
    from the file for the live session.
    """
    blocks: list[str] = []
    for n, key in enumerate(keys, 1):
        spec = AUDIT_AGENTS[key]
        # Continuation lines are indented only under a number, where the indent is what
        # keeps one agent's inputs from reading as the next agent's.
        head, cont = (f"{n}. ", "   ") if numbered else ("", "")
        blocks.append(
            f"{head}`{key}` — {spec.summary}.\n"
            + _dispatch_line(key, modes[key], cont) + "\n"
            + "\n".join(cont + line for line in _agent_inputs(
                project_dir, session_id, prompt_id, key, edited))
            + f"\n{cont}{spec.tail}"
        )
    return blocks


def _append_turn_instruction(project_dir: Path, session_id: str, prompt_id: str,
                             which: str) -> str:
    """The step asking the MAIN AGENT to complete the record guard started.

    guard has already written the response. What it asks for is the half it cannot see —
    and the shape of the ask matters more than the wording, because two different failures
    are possible here.

    The first is a paraphrase. An agent writing out its own turn tends to tidy it, and a
    tidied turn is one where the claim actually made is no longer the claim being audited.
    That is why the response is guard's to write and why this asks for a copy, stated as a
    prohibition.

    The second is curation, and it only appears once earlier evidence is in scope — which
    it must be: a claim in this turn is often grounded by a command run three turns ago,
    and an auditor that never sees it reports a backed claim as unbacked. False positives
    are the failure that teaches the user to stop reading guard. But "include what is
    relevant" asked of the claim's own author invites picking exactly the evidence that
    supports it. So this asks for INCLUSION, never selection: err toward including, and
    keep your reasoning about why the claim holds out of it. The auditor has the
    repository and can check what the record does not cover; what it cannot do is
    un-see a curated case for the defence.
    """
    path = _turn_record_file(project_dir, session_id, prompt_id).resolve()
    return (
        f"STEP 0 — complete the turn record at {path}. guard has already written "
        f"{which} into it verbatim; do not edit that section. Under "
        f"\"{TURN_CONTEXT_HEADING.lstrip('# ')}\", append:\n"
        "   - the user's request for this turn, copied;\n"
        "   - the tool activity this turn ran — what you ran and what came back, copied, "
        "not described;\n"
        "   - anything from EARLIER in the session that the response's statements rest "
        "on: a command whose output a claim is repeating, a file you read, a number you "
        "are carrying forward. Include it rather than judging it relevant — if you are "
        "unsure whether something is load-bearing, put it in. What must NOT go in is your "
        "own case for why the response is right; the agents form their own view, and an "
        "argument in the record is the one thing that can bias every one of them at once."
        "\n   Create the file if it is missing (write both sections, response first). "
        "Every agent below reads this one file."
    )


def _dispatch_context(project_dir: Path, session_id: str, prompt_id: str, lead: str,
                      keys: list[str], modes: dict[str, AgentMode],
                      edited: list[str] | None = None) -> str:
    """``additionalContext`` asking the main agent to dispatch these agents directly.

    The no-router path: the user named the audit themselves with a `/guard:audit-*`
    command, so there is nothing to triage and routing it would only add a hop.
    """
    keys = list(keys)
    blocks = _agent_blocks(project_dir, session_id, prompt_id, keys, edited or [],
                           len(keys) > 1, modes)
    parts = [lead]
    if any(AUDIT_AGENTS[k].reads == "turn" for k in keys):
        parts.append(_append_turn_instruction(project_dir, session_id, prompt_id,
                                              "the response being audited"))
    return "\n\n".join(parts + blocks)


def _router_context(project_dir: Path, session_id: str, prompt_id: str, lead: str,
                    eligible: list[str], edited: list[str], modes: dict[str, AgentMode],
                    config: dict[str, Any]) -> str:
    """``additionalContext`` for the Stop path: route first, then dispatch what it names.

    Everything both steps need is in this one message, on purpose. The alternative — the
    router reports back and a second hook builds the real dispatch — would put a round
    trip between "which agents" and "how to dispatch them", and guard has nothing to add
    in between: it knows every candidate's inputs already.

    So the turn is written once to a file, the router is told what it may choose from,
    and each candidate's dispatch block is printed below it in advance. The main agent
    writes the record, routes, then dispatches the subset the router names — all of them
    reading that same file. The roster carries the ELIGIBLE agents only, and the blocks cover
    exactly the same set: a switch the user turned off is not offered and has no block, so
    it cannot be reached even if the router names it anyway.

    Deliberately absent: any summary of the turn, from guard or from the main agent.
    Priming an audit with the author's account of the work is how an unexamined claim
    becomes an established one — every agent here reads the turn itself and forms its own
    view, which is also why the record is required to be verbatim.

    The ROUTER is always a fresh instance, whatever the agents are set to. Its question is
    about this turn, and an instance carrying the last five turns is one that can answer it
    from the wrong one — the failure would be silent, and routing is the step nothing else
    checks. It is also the cheapest agent here, so continuity buys the least.
    """
    model = _router_model(config)
    model_line = (f"\n   Dispatch it with model: {model}." if model else "")
    blocks = _agent_blocks(project_dir, session_id, prompt_id, eligible, edited, True,
                           modes)
    return (
        lead
        + "\n\n"
        + _append_turn_instruction(project_dir, session_id, prompt_id,
                                   "the response you just finished")
        + "\n\nSTEP 1 — route. Dispatch `" + ROUTER_AGENT + "` with the Agent tool "
        "(subagent_type: \"" + ROUTER_AGENT + "\"), passing these inputs:"
        + f"\n   - turn record: {_turn_record_file(project_dir, session_id, prompt_id).resolve()}"
        + "\n   - candidate agents (it may name only these, by their `key`):\n"
        + "\n".join("     " + line for line in _router_roster(eligible, edited).splitlines())
        + model_line
        + "\n   It reports which candidates are worth running, with a reason for each. An "
        "empty answer is a normal result: it means the turn has nothing for any of them, "
        "and then you say nothing about auditing and continue.\n\n"
        "STEP 2 — dispatch what it named, and only that, in ONE message so they run "
        "concurrently. The blocks below are every candidate; use the ones it picked. "
        "Relay each agent's own reason from the router's report when you report back — a "
        "pick that plainly misread the turn is worth saying so about rather than working "
        "around.\n\n"
        + "\n\n".join(blocks)
    )


# The lead for a routed turn. There is no second mode: a switch the user turned on is
# the user saying they want this audit, so asking again every turn would be a formality
# that trains them to wave it through. What the main agent must not do is quietly swallow
# the result — the report is the point.
_ROUTE_LEAD = (
    "guard: audit the turn you just finished, then act on what the agents report. Route "
    "it first to find which agents are worth running, dispatch those, and report what "
    "they found; a clean result is one line."
)


# --------------------------------------------------------------------------- #
# subcommands
# --------------------------------------------------------------------------- #
def cmd_user_prompt() -> int:
    """UserPromptSubmit. Trace only.

    guard keeps no record of the user's prompt. It used to archive one, as the other half
    of a turn store the audit agents read from; now the main agent supplies the turn to
    whoever needs it, and an archive nothing reads is just a copy of the user's words
    sitting in the repository.

    The hook stays registered because the trace is how a "guard said nothing" report gets
    diagnosed: without it there is no way to tell a turn guard skipped from a hook that
    never ran.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0
    prompt = payload.get("prompt")
    prompt = prompt if isinstance(prompt, str) else ""
    if _CONTROL_CMD_RE.match(prompt.strip()):
        _trace(project_dir, session_id, "user-prompt", "skip_control_cmd")
        return 0
    _trace(project_dir, session_id, "user-prompt", "seen")
    return 0


def _emit_expansion(msg: str) -> None:
    output = {"hookSpecificOutput": {"hookEventName": "UserPromptExpansion", "additionalContext": msg}}
    json.dump(output, sys.stdout)


def _emit_stop_context(msg: str) -> None:
    """Emit a Stop hook's ``additionalContext``.

    Not ``decision: "block"``. Per the official hooks docs
    (https://code.claude.com/docs/en/hooks, "Stop decision control"; excerpt at
    ``wiki/ref/claude-code-stop-hook-decision-control.md``) both keep the conversation
    going so Claude can act on the text, and both run under the same loop protections
    (``stop_hook_active`` and the 8-consecutive-continuation cap). The difference is how
    it reads: block surfaces as a hook error, while this is labelled ``Stop hook
    feedback``. guard's recommendation is guard working, not guard failing.
    """
    output = {"hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": msg}}
    json.dump(output, sys.stdout)


def cmd_verify() -> int:
    """UserPromptExpansion for the per-agent ``/guard:audit-*`` commands.

    The agent comes from argv (``verify claims-auditor`` | ``deferrals-auditor`` |
    ``korean-corrector``), one per command, so each skill dispatches exactly its own
    agent and the choice is not a dispatch input the model has to be trusted to honor.

    Works regardless of the switches: a switch governs what guard recommends UNASKED,
    while running the command is the user asking for this one audit now. Refusing it
    would leave the user no way to check the very agent they keep switched off, which is
    the main reason to keep it off in the first place.

    ``pending_verify_prompt_id`` names the turn, and the record for it already holds that
    turn's response — every Stop writes that section, whatever the switches say, which is
    what makes this command work in a project that keeps all four off. The main agent
    still appends the request, the tool activity, and the earlier evidence, exactly as on
    a routed turn.
    """
    key = sys.argv[2].strip().lower() if len(sys.argv) > 2 else ""
    spec = AUDIT_AGENTS.get(key)
    if spec is None or not spec.verify_command:
        return 0
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    pid = state.get("pending_verify_prompt_id") or ""
    if not pid:
        _emit_expansion("guard: no completed turn is available to audit yet. "
                        f"Ask something first, then run `/guard:{key}`.")
        _trace(project_dir, session_id, "verify", "no_pending", agent=key)
        return 0

    context = _dispatch_context(
        project_dir, session_id, pid,
        "guard: audit the last completed turn, on request.", [key],
        {key: _agent_mode(state, key)})
    _emit_expansion(context)
    _trace(project_dir, session_id, "verify", "dispatch", agent=key, prompt_id=pid)
    return 0


# Cap on the source files one turn may hand `comment-corrector`. Past this the list
# stops being an audit target and becomes a sweep of the whole change: the agent must
# read every file in full to judge a comment against the code under it, and the skill
# that dispatches it by hand asks the user to narrow at roughly this size for the same
# reason. Recording stops at the cap rather than dropping the oldest entries — the
# earliest edits of a turn are as worth auditing as the last, and a stable prefix keeps
# the recommendation reproducible.
EDITED_FILES_MAX = 20


def _record_edited_source(project_dir: Path, payload: dict, tool_input: Any,
                          config: dict[str, Any]) -> None:
    """Note a source file this turn wrote, for a later `comment-corrector` recommendation.

    Only source files (`_SOURCE_SUFFIXES`) and only inside the project: a comment audit
    of a file outside the working tree is not this turn's work to fix. Files under
    guard's own state are excluded too — a turn slice is a record, not code.

    Silent and best-effort. A miss here costs one skipped recommendation; a raise here
    would surface as a hook failure on an ordinary edit, which is far worse.
    """
    prompt_id = payload.get("prompt_id")
    session_id = _session_id(payload)
    if not isinstance(prompt_id, str) or not prompt_id or session_id is None:
        return
    target = _tool_target_path(project_dir, tool_input)
    if target is None or target.suffix.lower() not in _SOURCE_SUFFIXES:
        return
    try:
        project = project_dir.resolve()
        state_root = _state_root(project_dir).resolve()
    except OSError:
        return
    if project not in target.parents or state_root in target.parents:
        return

    state = _read_state(project_dir, session_id, config)
    # A new turn resets the list; without this, files from the previous turn would ride
    # along into this turn's recommendation.
    if state.get("edited_prompt_id") != prompt_id:
        state["edited_prompt_id"] = prompt_id
        state["edited_files"] = []
    files = state["edited_files"]
    if not isinstance(files, list):
        files = []
    path = str(target)
    if path in files or len(files) >= EDITED_FILES_MAX:
        return
    files.append(path)
    state["edited_files"] = files
    _write_state(project_dir, session_id, state)
    _trace(project_dir, session_id, "post-edit", "edited_recorded",
           prompt_id=prompt_id, file=target.name, count=len(files))


def _edited_source_files(state: dict[str, Any], prompt_id: str) -> list[str]:
    """The source files THIS turn wrote, as recorded by PostToolUse.

    Empty unless the recorded list belongs to this prompt_id and the files still exist:
    a turn that edited a file and then deleted or moved it leaves nothing to audit, and
    handing the corrector a missing path would spend an agent on a read failure.
    """
    if state.get("edited_prompt_id") != prompt_id:
        return []
    files = state.get("edited_files")
    if not isinstance(files, list):
        return []
    return [f for f in files if isinstance(f, str) and f and Path(f).is_file()]


def _tool_target_path(project_dir: Path, tool_input: Any) -> Path | None:
    """Absolute, resolved target path of a mutating tool call, or None.

    Reads the path from the PreToolUse `tool_input` (`file_path` for
    Write/Edit/MultiEdit, `notebook_path` for NotebookEdit). Resolving means a
    relative path or `..` cannot smuggle a write past the path-based checks below.
    """
    if not isinstance(tool_input, dict):
        return None
    raw = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not isinstance(raw, str) or not raw:
        return None
    try:
        target = Path(raw)
        if not target.is_absolute():
            target = project_dir / target
        return target.resolve()
    except OSError:
        return None


def _targets_refs_dir(project_dir: Path, tool_input: Any, config: dict[str, Any]) -> bool:
    """True when a mutating tool's target path is inside the refs directory
    (`wiki/ref/` by default, or the validated `refs_dir` config path)."""
    target = _tool_target_path(project_dir, tool_input)
    if target is None:
        return False
    try:
        refs = _refs_dir(project_dir, config).resolve()
    except OSError:
        return False
    return target == refs or refs in target.parents


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

    # How the turn was opened decides whether guard says anything at all. Two skips, and
    # the first is not politeness: a `task-notification` turn is a background agent
    # reporting in, and recommending an audit of it puts guard in a loop with itself,
    # since the audit it recommends is another background agent.
    identity = _turn_identity(payload.get("transcript_path"), prompt_id)
    if identity is not None:
        if identity["origin_kind"] == "task-notification":
            _trace(project_dir, session_id, "stop", "skip_task_notification",
                   prompt_id=prompt_id)
            return 0
        # A turn opened by guard's own control command (`/guard:settings`,
        # `/guard:audit-*`) or by a user-configured exempt skill is skill output or a
        # relay, not the assistant's own prose — there is nothing in it to audit, and
        # recommending one turns the user's own guard command into an audit of guard.
        cmd_name = identity["command_name"]
        if cmd_name and (_is_control_command_name(cmd_name)
                         or cmd_name in _exempt_skills(config)):
            _trace(project_dir, session_id, "stop", "skip_exempt_skill",
                   prompt_id=prompt_id, command=cmd_name)
            return 0

    # Both of these happen whether or not any switch is on. They are what the on-demand
    # `/guard:audit-*` commands target, and those are the user asking for an audit now —
    # refusing them because the automatic recommendation is off would take away the very
    # thing switching everything off is meant to leave in place.
    #
    # Writing the response here rather than in the recommendation path is deliberate: it
    # is the one part of the record guard is handed for free, and it is the part that must
    # not pass through the author's hands. An hour-old turn the user asks about is still
    # quoted exactly.
    state["pending_verify_prompt_id"] = prompt_id
    _write_turn_response(project_dir, session_id, prompt_id, response)

    # Once per turn. `stop_hook_active` already covers the normal path, but the
    # recommendation asks the main agent to dispatch background agents, and each of
    # those completions opens a transcript turn of its own; a marker keyed on the
    # prompt_id does not depend on the payload flag surviving that.
    if state.get("last_audited_prompt_id") == prompt_id:
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "skip_already_recommended",
               prompt_id=prompt_id)
        return 0

    edited = _edited_source_files(state, prompt_id)
    eligible = _eligible_agents(state, edited)
    modes = {k: _agent_mode(state, k) for k in eligible}
    if not eligible:
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "none_eligible", prompt_id=prompt_id)
        return 0

    # The marker is spent before the recommendation goes out, not after. One
    # recommendation per turn, whatever the main agent does with it: the alternative is
    # a turn that gets re-recommended because the first dispatch is still in flight.
    state["last_audited_prompt_id"] = prompt_id
    _write_state(project_dir, session_id, state)

    context = _router_context(project_dir, session_id, prompt_id, _ROUTE_LEAD,
                              eligible, edited, modes, config)
    # `additionalContext`, not `decision: "block"`. Per the official hooks docs
    # (https://code.claude.com/docs/en/hooks, "Stop decision control"; excerpt saved at
    # wiki/ref/claude-code-stop-hook-decision-control.md) the two continue the
    # conversation identically and share the same loop protections, but block is
    # reported as a hook ERROR while this shows as `Stop hook feedback`. A
    # recommendation is guard working as designed, so it must not look like a failure.
    _emit_stop_context(context)
    _trace(project_dir, session_id, "stop", "routed", prompt_id=prompt_id,
           eligible=",".join(eligible))
    return 0


def cmd_session_start() -> int:
    # Sweep both state and logs on the same age policy. State is intentionally NOT
    # cleared at SessionEnd: a session can be resumed later (`claude --resume`), and
    # its switch flags must survive the gap. Age-based expiry is the
    # only reaper, so a resumed session keeps its state as long as it is touched
    # within the retention window.
    project_dir = _project_dir()
    if project_dir is None:
        return 0
    root = _state_root(project_dir)
    cutoff = time.time() - ORPHAN_MAX_AGE_SECONDS
    # File-per-session dirs.
    for sub in ("state",):
        d = root / sub
        if not d.is_dir():
            continue
        try:
            entries = list(d.iterdir())
        except OSError:
            continue
        for entry in entries:
            try:
                if entry.is_file() and entry.stat().st_mtime < cutoff:
                    entry.unlink()
            except OSError:
                pass
    # turns/ holds one dir per session of turn records and rewrites; sweep stale dirs.
    turns_root = root / "turns"
    if turns_root.is_dir():
        try:
            sess_dirs = list(turns_root.iterdir())
        except OSError:
            sess_dirs = []
        for d in sess_dirs:
            try:
                if d.is_dir() and d.stat().st_mtime < cutoff:
                    for child in d.iterdir():
                        try:
                            child.unlink()
                        except OSError:
                            pass
                    d.rmdir()
            except OSError:
                pass
    # Persist the resolved refs directory into the session's Bash environment
    # (GUARD_REFS_DIR) so a Bash caller resolves it with one `echo`
    # instead of re-deriving the `refs_dir` validation from the raw config. Docs:
    # a SessionStart hook may append `export` lines to $CLAUDE_ENV_FILE and the
    # variables reach all subsequent Bash commands
    # (https://code.claude.com/docs/en/hooks, "CLAUDE_ENV_FILE").
    session_cfg = _load_config(project_dir)
    refs = _refs_dir(project_dir, session_cfg)
    env_file = os.environ.get("CLAUDE_ENV_FILE")
    if env_file:
        try:
            with open(env_file, "a", encoding="utf-8") as fh:
                fh.write(f"export GUARD_REFS_DIR={shlex.quote(str(refs))}\n")
        except OSError:
            pass

    # The injected contract states the general rule — a doc-based claim cites the source
    # URL and a local saved copy — but not where this project keeps that copy, which
    # is per-project config (`refs_dir`). Inject the resolved path here instead: for
    # SessionStart, plain stdout becomes context the model can act on (docs:
    # https://code.claude.com/docs/en/hooks, "Exit code 0"). Without it the judge
    # would fail a docs claim for a missing refs copy that nothing told the model
    # where to write.
    print(
        "guard: when a claim rests on official documentation, save the cited content "
        f"to this project's refs directory — {refs} — and cite both the source URL "
        "and that local path. The same path is in $GUARD_REFS_DIR for Bash."
    )

    # The standing reuse policy is stated ONCE, here, rather than in every Stop
    # recommendation. Reuse is a session-long fact — the instance lives under the session
    # id — so the session's opening is where it belongs, and repeating it per turn would
    # pay for it on every turn. The per-turn text still carries the mechanic (resume this
    # name, or dispatch under it), because that is what changes with which agents were
    # picked; what it does not carry is the explanation.
    #
    # A mode changed mid-session leaves this line stale, which is exactly why
    # `cmd_settings` prints its own transition note: the two together are how the main
    # agent learns the policy and then learns it changed.
    reused = [k for k in AUDIT_AGENTS if _agent_mode(session_cfg, k) is AgentMode.REUSE]
    if reused:
        named = ", ".join(f"{_agent_id(k)} as `{_instance_name(k)}`" for k in reused)
        print(
            "guard: these audit agents run as ONE instance for this session, not a fresh "
            f"one per turn — {named}. Dispatch each under that name the first time it is "
            "needed, then SendMessage the name on later turns so it keeps what it has "
            "already read and judged. They can also message each other and you by name. "
            "Every other guard agent, the router included, is a fresh instance each time."
        )
    _trace(project_dir, None, "session-start", "swept")
    return 0


def cmd_exempt() -> int:
    """Manage the ``exempt_skills`` list in guard.local.json. Invoked by the
    ``guard:settings`` skill via Bash, AFTER the user has confirmed a selection
    interactively (the skill drives the listing + AskUserQuestion; this only records
    the confirmed result). Argv:

        exempt list                — print the current exempt_skills
        exempt set   NAME [NAME…]  — replace the list with exactly these
        exempt add   NAME [NAME…]  — add
        exempt remove NAME [NAME…] — remove
        exempt clear               — empty the list

    Edits ONLY the ``exempt_skills`` key — never a switch or session state — so it can
    change which skills' turns Stop skips but cannot disable guard
    outright. Project dir from ``CLAUDE_PROJECT_DIR`` (Bash env), else
    the current working directory. Prints the resulting list for the skill to relay.
    """
    argv = sys.argv[2:]
    op = argv[0].lower() if argv else "list"
    names = [n for n in (_norm_skill(a) for a in argv[1:]) if n]

    pd_env = os.environ.get("CLAUDE_PROJECT_DIR")
    project_dir = Path(pd_env) if pd_env else Path.cwd()

    if op in _CLI_MUTATING_VERBS and not _cli_write_allowed():
        print("guard exempt: refusing to change settings outside /guard:settings. "
              "Ask the user to run `/guard:settings` — only the user changes guard's "
              "own configuration.", file=sys.stderr)
        _trace(project_dir, None, "exempt", "refused_no_skill_marker", op=op)
        return 0

    raw = _load_raw_config(project_dir)
    cur_raw = raw.get("exempt_skills")
    current: list[str] = []
    if isinstance(cur_raw, list):
        for c in cur_raw:
            n = _norm_skill(c)
            if n and n not in current:
                current.append(n)

    changed = False
    if op == "set":
        new: list[str] = []
        for n in names:
            if n not in new:
                new.append(n)
        changed = new != current
        current = new
    elif op == "add":
        for n in names:
            if n not in current:
                current.append(n)
                changed = True
    elif op in ("remove", "rm"):
        for n in names:
            if n in current:
                current.remove(n)
                changed = True
    elif op == "clear":
        changed = bool(current)
        current = []
    # "list" / unknown → report only

    if changed:
        raw["exempt_skills"] = current
        if not _write_config(project_dir, raw):
            print("guard exempt: failed to write .claude/guard.local.json", file=sys.stderr)
            return 0

    print("exempt_skills: " + (", ".join(current) if current else "(none)"))
    _trace(project_dir, None, "exempt", op, n=len(current), changed=changed)
    return 0


def _parse_settings_argv(argv: list[str]) -> tuple[list[str], str | None]:
    """Split a ``settings`` CLI argv into positionals and the ``--session <id>`` value."""
    positional: list[str] = []
    session: str | None = None
    i = 0
    while i < len(argv):
        tok = argv[i]
        if tok == "--session":
            if i + 1 < len(argv):
                session = argv[i + 1].strip() or None
                i += 2
                continue
            i += 1
            continue
        positional.append(tok)
        i += 1
    return positional, session


def _apply_session_scalar(project_dir: Path, session_id: str | None, key: str, value: Any) -> None:
    """Mirror a switch change into the live session's
    ``state/<sid>.json`` so it takes effect at once, not only for sessions started later.
    These are the only settings cached in session state (seeded from config at session
    start); the rest are read from the config file at use, so writing the file is enough
    for them. No-op without a session id."""
    if not session_id:
        return
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    state[key] = value
    _write_state(project_dir, session_id, state)


def _config_show_lines(project_dir: Path, session_id: str | None) -> list[str]:
    """Render current guard settings for the ``guard:settings`` skill to display. Shows the
    guard.local.json defaults; for the switches it also shows the live session value when
    it differs from the default (the session may have been changed after)."""
    raw = _load_raw_config(project_dir)
    cfg = _load_config(project_dir)
    state = None
    if session_id and _state_file(project_dir, session_id).is_file():
        state = _read_state(project_dir, session_id, cfg)

    def switch_line(key: str) -> str:
        default = _agent_mode(cfg, key)
        live = _agent_mode(state, key) if state is not None else default
        suffix = " — one instance for the session" if live is AgentMode.REUSE else ""
        if live != default:
            return f"{key}: {live} (this session; default {default}){suffix}"
        return f"{key}: {default}{suffix}"

    exempt = _exempt_skills(cfg)
    refs_rel = raw.get("refs_dir") if isinstance(raw.get("refs_dir"), str) else ""
    return [
        *(switch_line(k) for k in AUDIT_AGENTS),
        "router_model: " + (_router_model(cfg) or "(agents/router.md)"),
        "exempt_skills: " + (", ".join(sorted(exempt)) if exempt else "(none)"),
        "refs_dir: " + (refs_rel if refs_rel else "(default wiki/ref/)"),
    ]


def cmd_settings() -> int:
    """View/change guard.local.json settings — the CLI behind the ``guard:settings`` skill.

        settings [show]                      — print the current settings
        settings set <key> <value>           — change one setting

    Settable keys: the agent switches (the keys of ``AUDIT_AGENTS`` — each is the name
    of the agent it admits), ``router_model`` (the router agent's model, and nothing
    else's), and ``refs_dir``. The switches
    also apply to the live session's ``state/<sid>.json`` when a session id is available
    (``--session <id>``, which the forked skill passes as ``${CLAUDE_SESSION_ID}``, else
    the inherited ``CLAUDE_CODE_SESSION_ID``) so the change takes effect at once and
    persists as the new default; the rest are read from the config file at use.
    ``exempt_skills`` is managed by the ``exempt`` CLI, not here, and
    every other key in the file is preserved. Project dir from ``CLAUDE_PROJECT_DIR``
    (Bash env), else the current directory."""
    positional, session_arg = _parse_settings_argv(sys.argv[2:])
    op = positional[0].lower() if positional else "show"

    pd_env = os.environ.get("CLAUDE_PROJECT_DIR")
    project_dir = Path(pd_env) if pd_env else Path.cwd()
    session_id = session_arg or (os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip() or None)

    if op != "set":
        for line in _config_show_lines(project_dir, session_id):
            print(line)
        _trace(project_dir, session_id, "settings", "show")
        return 0

    if not _cli_write_allowed():
        print("guard settings: refusing to change settings outside /guard:settings. "
              "Ask the user to run `/guard:settings` — only the user changes guard's "
              "own configuration.", file=sys.stderr)
        _trace(project_dir, session_id, "settings", "refused_no_skill_marker")
        return 0

    if len(positional) < 3:
        print("guard settings: usage: settings set <key> <value>", file=sys.stderr)
        return 0
    key = positional[1].lower()
    value = positional[2]

    raw = _load_raw_config(project_dir)
    cfg = _load_config(project_dir)
    transition = ""

    if key in AUDIT_AGENTS:
        v = _parse_mode(value)
        if v is None:
            print(f"guard settings: {key} must be one of "
                  f"{[m.value for m in AgentMode]} (got {value!r})", file=sys.stderr)
            return 0
        # Read the mode this replaces BEFORE writing, so the transition can be reported.
        # A mode change is the one setting change that leaves something behind: an
        # instance the main agent may still be addressing. Nothing in guard can see or
        # stop that instance — the settings CLI runs in a forked skill with no channel to
        # it — so the change has to be reported to the session that CAN, and this print
        # is that report. It reaches the main agent because the skill relays what the CLI
        # printed.
        before = _agent_mode(_read_state(project_dir, session_id, cfg) if session_id
                             else cfg, key)
        raw[key] = v.value
        _apply_session_scalar(project_dir, session_id, key, v.value)
        if before is AgentMode.REUSE and v is not AgentMode.REUSE:
            transition = (
                f"guard: {key} is no longer reused. Stop sending to "
                f"`{_instance_name(key)}` — shut it down if your session offers a way to "
                f"— and from the next turn dispatch a new instance each time.")
        elif v is AgentMode.REUSE and before is not AgentMode.REUSE:
            transition = (
                f"guard: {key} now runs as one instance for the session, named "
                f"`{_instance_name(key)}`. Dispatch it under that name once, then "
                f"SendMessage it on later turns instead of dispatching again.")
        else:
            transition = ""
    elif key == "router_model":
        # "" is a legitimate value here, not an error: it hands the choice back to
        # `agents/router.md`, which is how a router model is normally set.
        raw["router_model"] = value.strip()
    elif key == "refs_dir":
        raw["refs_dir"] = value  # "" resets to the default; _refs_dir validates at use
    else:
        print(f"guard settings: unknown or unsettable key {key!r}. Settable: "
              + ", ".join(AUDIT_AGENTS)
              + ", router_model, refs_dir (exempt_skills via the exempt CLI).",
              file=sys.stderr)
        return 0

    if not _write_config(project_dir, raw):
        print("guard settings: failed to write .claude/guard.local.json", file=sys.stderr)
        return 0

    for line in _config_show_lines(project_dir, session_id):
        print(line)
    if transition:
        print()
        print(transition)
    _trace(project_dir, session_id, "settings", "set", key=key)
    return 0


def cmd_refs_dir() -> int:
    """Print the resolved refs directory (absolute), applying `refs_dir` validation.

    The single query point for "where do cited-doc copies go": the claims auditor falls
    back to it when its dispatch omits `refs_dir`, and anything with the script
    path can use it instead of re-implementing _refs_dir's fallback rules.
    """
    project_dir = _project_dir()
    if project_dir is None:
        return 0
    print(_refs_dir(project_dir, _load_config(project_dir)))
    return 0


REFS_INDEX_NAME = "AGENTS.md"
# Files in the refs dir that are the index machinery itself, never indexed entries.
_REFS_INDEX_SKIP = {REFS_INDEX_NAME, "CLAUDE.md"}


def cmd_post_edit() -> int:
    """PostToolUse on the file-writing tools. Two jobs on the one payload.

    1. Record the source file, if that is what was written, against this turn — the
       list `comment-corrector` is pointed at when Stop recommends it. This is the event
       that actually sees the path, so nothing has to be reconstructed from a transcript
       later; Stop only reads back what accumulated here.
    2. Require a file saved inside the refs dir to be listed in the refs index
       (``AGENTS.md``). A saved reference nothing points at is a file the next reader
       never finds, so the index is the deliverable, not a courtesy. This fires *after*
       the write rather than blocking it: the natural order is save-then-index, and
       blocking the save would force an index entry for a file that does not exist yet.

    Job 2 blocks with ``decision: "block"`` so the reason returns to the model as work
    to finish; job 1 never emits anything. Silent in every other case — a write outside
    the refs dir, the index itself, or a file already listed.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0

    config = _load_config(project_dir)
    tool_input = payload.get("tool_input")
    _record_edited_source(project_dir, payload, tool_input, config)
    if not _targets_refs_dir(project_dir, tool_input, config):
        return 0
    target = _tool_target_path(project_dir, tool_input)
    if target is None or target.name in _REFS_INDEX_SKIP:
        return 0

    reason = refs_index_gap(project_dir, target, config)
    if reason is None:
        _trace(project_dir, None, "post-edit", "refs_listed", file=target.name)
        return 0

    json.dump({"decision": "block", "reason": reason}, sys.stdout)
    _trace(project_dir, None, "post-edit", "refs_missing", file=target.name)
    return 0


def refs_index_gap(project_dir: Path, target: Path, config: dict[str, Any]) -> str | None:
    """The block reason when ``target`` is missing from the refs index, else None.

    Host-neutral so both adapters enforce one rule. Matching is by file name anywhere
    in the index text rather than by table structure: the index is prose a human
    maintains, and pinning the check to a column layout would fail the moment someone
    reformats it.
    """
    index = _refs_dir(project_dir, config) / REFS_INDEX_NAME
    try:
        if target.name in index.read_text(encoding="utf-8"):
            return None
    except OSError:
        pass  # No index yet: the first saved reference is what creates it.
    return (
        f"guard: `{target.name}` is saved but not listed in the reference index. "
        f"Add a row for it to `{_project_rel(project_dir, index)}` — file name, what "
        "it covers, and the source — so the next reader finds it without opening "
        "every file. Then continue."
    )


SUBCOMMANDS = {
    "user-prompt": cmd_user_prompt,
    "post-edit": cmd_post_edit,
    "verify": cmd_verify,
    "settings": cmd_settings,
    "stop": cmd_stop,
    "session-start": cmd_session_start,
    "exempt": cmd_exempt,
    "refs-dir": cmd_refs_dir,
}


def main() -> int:
    if len(sys.argv) < 2:
        return 0
    handler = SUBCOMMANDS.get(sys.argv[1])
    if handler is None:
        return 0
    try:
        return handler()
    except Exception as e:  # never let guard's own failure surface as a hook error
        _trace(_project_dir(), None, sys.argv[1] if len(sys.argv) > 1 else "?", "exception", error=repr(e))
        return 0


if __name__ == "__main__":
    sys.exit(main())
