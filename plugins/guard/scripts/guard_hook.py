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
                 of ``audit_gate`` (``manual``|``headless`` — how the evidence judge
                 runs; ``manual`` is its practical off), the three axis switches
                 (``audit_claims``/``audit_deferrals``/``audit_korean``), ``model``,
                 ``effort``, or ``refs_dir``. ``audit_gate`` and the axis switches also
                 apply to the live session's ``state/<sid>.json`` when a session id is
                 available (``--session``, which the forked skill passes as
                 ``${CLAUDE_SESSION_ID}``, else the inherited ``CLAUDE_CODE_SESSION_ID``);
                 the rest are read from the config file at use. Preserves every other
                 key; ``exempt_skills`` is managed by the ``exempt`` CLI, not here.
                 Mutating verbs require the settings-skill marker — see
                 ``_cli_write_allowed``. Not a hook event.
- verify         UserPromptExpansion, one matcher per axis
                 (``^(guard:)?audit-{claims,deferrals}$``, ``^(guard:)?correct-korean$``).
                 On demand, emit the dispatch instruction for that ONE axis's agent
                 over the last completed turn (``pending_verify_prompt_id``, recorded by
                 manual-mode Stop). An
                 axis switched off is still auditable this way — the switch governs the
                 automatic audit, not what the user may ask for.
- exempt         CLI (argv), run by the ``guard:settings`` skill via Bash after the user
                 confirms an interactive selection. ``list``/``set``/``add``/
                 ``remove``/``clear`` the ``exempt_skills`` config key — that key ONLY,
                 never ``audit_gate``/state. Mutating verbs require the settings-skill
                 marker (``_cli_write_allowed``). Not a hook event.
- stop           Stop. A turn == the transcript ``prompt_id``; guard reads the whole
                 turn from Claude Code's transcript (``transcript_path`` +
                 ``prompt_id``, both in the payload) via ``_read_turn_from_transcript``
                 — user request, tool activity, and response. Skips when
                 ``stop_hook_active``, the prompt_id/transcript are absent, the slice
                 contains a user ``!`` command (its output arrives after the judged
                 response, so it is neither evidence nor auditable here), or the turn was
                 opened by guard's own ``/guard:settings`` / ``/guard:audit-*`` control
                 command or a user-configured ``exempt_skills`` entry (skill output / a
                 relay, not claims to ground). Otherwise branch on ``audit_gate``.
                 ``manual`` (default): do not audit — record the turn as the pending
                 ``/guard:audit-*`` target and emit nothing. ``headless``: spawn ONE
                 JUDGE PER ENABLED AXIS in parallel (see run_judges_parallel), block on
                 any axis's violation, and on a fully-audited PASS append the claims
                 judge's supported claims to the verified store.
- refs-index     PostToolUse (Write/Edit/MultiEdit/NotebookEdit). After a write inside
                 the refs directory, require the new file to be listed in that
                 directory's ``AGENTS.md`` index, blocking until it is. Independent of
                 the audit setting.
- session-start  SessionStart. Sweep state/sessions/verified files and turns/ dirs
                 older than retention, and export ``GUARD_REFS_DIR`` (the resolved
                 refs directory) via ``$CLAUDE_ENV_FILE`` for the session's Bash
                 environment.
- refs-dir       Print the resolved refs directory (absolute), applying the
                 ``refs_dir`` validation. Called via Bash (claims auditor fallback / the
                 output style), not a hook event.

State lives project-local under ``${CLAUDE_PROJECT_DIR}/.claude/guard/``:
- ``state/<sid>.json``       — {audit_gate, audit_claims, audit_deferrals, audit_korean, last_audited_prompt_id, pending_verify_prompt_id, updated_at}
- ``sessions/<sid>.jsonl``   — full session archive: one record per turn / verdict
- ``turns/<sid>/<pid>.json`` — manual mode: the turn slice guard hands a per-axis
                                auditor subagent ({user, tools[], assistant})
- ``verified/<sid>.jsonl``   — verified facts from PASSED turns: {turn, claim, evidence}
- ``trace.log``              — file-only debug trace (enabled by GUARD_TRACE)

State is retained across the end of a session so a resumed session
(``claude --resume``) keeps its judge flags; both state and logs are
expired only by the age-based sweep at SessionStart (see ORPHAN_MAX_AGE_SECONDS).

Configuration (optional) is a JSON object at
``${CLAUDE_PROJECT_DIR}/.claude/guard.local.json``: ``model`` (string, default
``"haiku"``), ``effort`` (one of low/medium/high/xhigh/max, default ``"medium"``
— reasoning effort of the HEADLESS judges only; an auditor subagent's model/effort come
from the per-axis auditor agent's own frontmatter, not these keys), ``audit_gate``
(``"manual"``|``"headless"``, default ``"manual"``) — how the Stop-time
evidence judge runs (manual: no auto-audit — the judge's practical off — audit on
demand via the per-axis ``/guard:audit-*`` commands; headless: one in-hook judge per
enabled axis, blocking on a violation), the three axis switches ``audit_claims`` /
``audit_deferrals`` (both default ``true``) and ``audit_korean`` (default ``false``),
``exempt_skills`` (list of strings, default ``[]``) — skills / slash
commands whose turn the Stop judge must not audit, named with their plugin namespace
(``plugin:skill``, e.g. ``guard:settings``) or bare for un-namespaced skills; matched
leading-``/``-stripped and case-insensitively (guard's own ``settings``/``audit-*``
control commands are always exempt regardless of this
list), and ``refs_dir`` (string, default ``""``) — project-relative directory where
guard saves local copies of cited docs; empty means the
git-tracked default ``wiki/ref/``, so the collected references are committed with the
repo (point it at a different tracked path, e.g. ``"docs/refs"``, to override; values
resolving outside the project, at the project root, or into guard's own config/state
fall back to the default — see ``_refs_dir``). Unknown keys are ignored; a missing or
malformed file falls back to all defaults. The claims judge always reads the repo
(Read/Grep/Glob/Bash) to verify claims. The ``guard:settings`` skill changes these
through the ``settings`` CLI: it writes guard.local.json and, for ``audit_gate`` and the
axis switches, the live session's state.

Requires Python 3.11+ (uses ``enum.StrEnum``).
"""

from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from enum import StrEnum
from pathlib import Path
from typing import Any, NamedTuple


class AuditGate(StrEnum):
    """How the Stop-time evidence judge runs (see DEFAULT_CONFIG["audit_gate"])."""

    MANUAL = "manual"
    HEADLESS = "headless"

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
JUDGE_TIMEOUT_SECONDS = 90

DEFAULT_CONFIG: dict[str, Any] = {
    "model": "haiku",
    "effort": "medium",
    "audit_gate": AuditGate.MANUAL,
    # The two axes the evidence judge checks, switched independently. `audit_gate`
    # picks HOW/WHEN the audit runs; these pick WHAT it looks for within that one run.
    # Split so a project can keep the claim check while dropping the deferral check (or
    # the reverse) without giving up the judge entirely. With both off the audit is
    # skipped outright — a run that can report nothing is pure cost.
    "audit_claims": True,
    "audit_deferrals": True,
    # Third axis: does a Korean response read as natural Korean, or as translated
    # English? Governed by `audit_gate` with the other two — it is an audit of the
    # finished turn, so HOW/WHEN it runs is the same one question. Defaults OFF, unlike
    # the other two axes: most projects answer in English, where this axis reports
    # nothing, so making it opt-in keeps it from being pure cost. The axis self-skips on
    # a non-Korean response (see KOREAN_SYSTEM).
    "audit_korean": False,
    # Skills / slash commands whose turn the Stop judge must NOT audit. A turn opened
    # by one of these is skill output or a relay, not a body of technical claims to
    # ground. Values are the name as it appears after the slash, INCLUDING the plugin
    # namespace (e.g. "guard:settings", "hindsight:review") or the bare name for an
    # un-namespaced skill ("deep-research"); matched leading-'/'-stripped and
    # case-insensitively. guard's own config/judge control commands are always exempt
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

VALID_EFFORTS = {"low", "medium", "high", "xhigh", "max"}
# Accepted spellings for the boolean axis switches. The CLI takes a string argument, so
# "off"/"no"/"0" must map to False rather than land in the config as a truthy string.
_BOOL_TRUE = {"true", "on", "yes", "1"}
_BOOL_FALSE = {"false", "off", "no", "0"}

# The evidence-judge settings live on AuditGate:
# AuditGate.MANUAL (default): the hook does NOT audit at Stop — it archives the turn and
#   records it as the pending verify target; verification runs only on demand via
#   `/guard:audit-claims`, which dispatches the claims auditor. This is the judge's practical off.
# AuditGate.HEADLESS: spawn an isolated `claude` inside the hook and block the turn (the
#   original path).


# --------------------------------------------------------------------------- #
# environment / paths
# --------------------------------------------------------------------------- #
def _trace_enabled() -> bool:
    return os.environ.get(TRACE_ENV_VAR, "").strip().lower() in TRACE_TRUTHY


def _cli_write_allowed() -> bool:
    """True when a config-mutating CLI verb may write.

    guard never gates Bash, so the model can invoke this script directly — and the
    config-mutating verbs can weaken guard itself: `settings set audit_gate manual`
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


def _log_file(project_dir: Path, session_id: str) -> Path:
    return _state_root(project_dir) / "sessions" / f"{session_id}.jsonl"


def _verified_file(project_dir: Path, session_id: str) -> Path:
    """Per-session accumulation of VERIFIED facts (claims from passed turns)."""
    return _state_root(project_dir) / "verified" / f"{session_id}.jsonl"


def _turn_slice_file(project_dir: Path, session_id: str, prompt_id: str) -> Path:
    """File holding one turn's transcript slice, handed to the claims auditor subagent.

    guard slices the transcript itself (single slice implementation) and writes just
    that turn here, so the auditor reads one turn — not the whole transcript.
    """
    return _state_root(project_dir) / "turns" / session_id / f"{prompt_id}.json"


def _korean_rewrite_file(project_dir: Path, session_id: str, prompt_id: str) -> Path:
    """File the Korean corrector writes its rewritten response to.

    Beside the turn slice, inside guard's own state: the rewrite is a proposal for the
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
      turn the judge off.

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


def _refs_rel(project_dir: Path, config: dict[str, Any]) -> str:
    """Project-relative refs path (with trailing slash) for prompts and messages."""
    refs = _refs_dir(project_dir, config)
    try:
        return str(refs.resolve().relative_to(project_dir.resolve())) + "/"
    except (OSError, ValueError):
        return str(refs) + "/"


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
# guard's own control commands, e.g. "/guard:settings audit_gate manual", "/settings",
# "/guard:audit-claims". `settings` is a forked skill and each per-axis command a
# UserPromptExpansion — either way the turn is a relay, not real work to log/judge. The
# name is `settings`, not `config`, precisely so the bare form does NOT match Claude Code's
# built-in `/config` command (which the optional `(guard:)?` would otherwise capture,
# making guard treat every `/config` as its own control command). `(?=\s|$)` rather than
# `\b`: the name must END here, not merely hit a word boundary — `\b` would also accept a
# longer hyphenated name from another plugin (`/settings-export` matching `settings`), and
# it is what keeps `audit-claims` from matching a bare `/audit`.
# `correct-comment` is deliberately ABSENT: that skill's relayed findings are claims about
# real files and about edits made to them, so its turn stays auditable like any other work.
_CONTROL_CMD_RE = re.compile(
    r"^/(guard:)?(settings|audit-claims|audit-deferrals|correct-korean)(?=\s|$)",
    re.IGNORECASE)
# In the transcript, a slash command is expanded to
# "<command-name>/guard:settings</command-name>" (see session b30dbaec). Pull the command
# name out of that tag; a raw typed form ("/guard:settings audit_gate manual") is handled by
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


TOOL_CONTEXT_MAX_CHARS = 12000
TOOL_RESULT_MAX_CHARS = 2000


# A turn is the transcript's promptId: the typed user prompt plus everything derived
# from it (assistant text, tool calls). The Stop payload gives us prompt_id +
# transcript_path, so we read the turn from Claude Code's own transcript rather than
# maintaining a parallel buffer.
#
# A user `!` command does NOT open its own promptId — it inherits the preceding typed
# prompt's id, and its <bash-input>/<bash-stdout> records are appended to that turn's
# slice AFTER the responses guard already judged (evidence arriving later than the
# claims it would support). guard therefore does not treat `!` output as evidence and
# does not judge a turn whose slice contains one; we only need to detect the tag.
_BASH_TAG = "<bash-input>"


def _message_of(record: Any) -> dict[str, Any]:
    msg = record.get("message") if isinstance(record, dict) else None
    return msg if isinstance(msg, dict) else {}


def _turn_command_name(user_text: str) -> str:
    """The slash command that opened the turn, normalized (leading '/' stripped,
    lowercased), or '' when the turn was not opened by a slash command.

    Slash commands reach the transcript expanded as
    ``<command-name>/guard:settings</command-name>``; a raw typed form
    (``/guard:settings audit_gate manual``) is handled by the fallback.
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
    (``settings``/``judge``, with or without the ``guard:`` prefix)."""
    return bool(name) and bool(_CONTROL_CMD_RE.match("/" + name))


def _norm_skill(name: Any) -> str:
    """Normalize a skill / command name for storage and matching: leading '/' stripped,
    lowercased, plugin namespace (``plugin:skill``) preserved. '' if not a usable str."""
    if not isinstance(name, str):
        return ""
    return name.strip().lstrip("/").lower()


def _exempt_skills(config: dict[str, Any]) -> set[str]:
    """Normalized set of skill / command names whose turn the Stop judge must not audit
    (from the ``exempt_skills`` config key). Values keep their plugin namespace
    (``plugin:skill``); compared leading-'/'-stripped and lowercased, matching
    ``_turn_command_name``."""
    raw = config.get("exempt_skills", [])
    if not isinstance(raw, list):
        return set()
    return {n for n in (_norm_skill(c) for c in raw) if n}


def _read_turn_from_transcript(transcript_path: Any, prompt_id: Any) -> dict[str, Any] | None:
    """Reconstruct a turn from Claude Code's transcript, sliced by ``prompt_id``.

    Returns ``{user, tools[], has_user_command, origin_kind, command_name}`` or None
    (fail-open) when the transcript is unreadable or the prompt_id is not found.
    ``command_name`` is the slash command that opened the turn (normalized, '' if none)
    — used by the Stop path to skip auditing guard's own control turns and user-exempted
    commands. ``origin_kind`` is the anchor's ``origin.kind`` ('' if absent) — the Stop
    path skips turns opened by a ``task-notification`` (a background-agent completion,
    not a user request).

    A turn is anchored on the FIRST record whose top-level ``promptId == prompt_id``
    (origin-agnostic — a turn opened by a typed prompt has ``origin.kind=human`` and
    str content; both typed and `!`-command records carry the turn's promptId,
    verified). The turn's derived records (assistant text, tool_use/tool_result) carry
    ``promptId=None`` and stay in the slice; the slice ends at the first record whose
    non-empty ``promptId`` differs (the next turn). ``isMeta`` records (guard's own
    injected feedback) are skipped.

    ``!`` command records (``<bash-input>``…) are not evidence and are not rendered;
    we only set ``has_user_command`` so the Stop path can skip judging that turn (the
    `!` output arrives in the slice after the responses guard would judge).
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

    user = ""
    tools: list[dict[str, str]] = []
    has_user_command = False
    origin_kind = ""
    in_turn = False

    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except (json.JSONDecodeError, ValueError):
            continue
        if not isinstance(rec, dict):
            continue
        rec_pid = rec.get("promptId")

        if not in_turn:
            if rec_pid == prompt_id:
                in_turn = True
                # The anchor is either the typed prompt (str) or a `!` command
                # (str with <bash-input>); classify it like any in-turn record below.
                # Capture how the turn was opened. A typed prompt has
                # ``origin.kind == "human"``; a background-agent completion opens a turn
                # whose anchor is a ``<task-notification>`` with
                # ``origin.kind == "task-notification"`` (promptSource "system", NOT
                # isMeta) — the Stop path uses this to skip auditing such relay turns.
                origin = rec.get("origin")
                if isinstance(origin, dict):
                    origin_kind = str(origin.get("kind") or "")
            else:
                continue
        else:
            # End the slice at the next turn's anchor (a different non-empty id).
            if isinstance(rec_pid, str) and rec_pid and rec_pid != prompt_id:
                break

        if rec.get("isMeta") is True:
            continue

        msg = _message_of(rec)
        content = msg.get("content")
        if isinstance(content, str):
            if _BASH_TAG in content or "<bash-stdout>" in content or "<bash-stderr>" in content:
                # A user `!` command (input or output record). Not evidence; flag the
                # turn so Stop skips judging it, and do not collect it.
                has_user_command = True
            elif not user:
                # The turn's typed human prompt (first non-bash str user record).
                user = content
            continue
        if not isinstance(content, list):
            continue
        for part in content:
            if not isinstance(part, dict):
                continue
            ptype = part.get("type")
            if ptype == "tool_use":
                name = part.get("name", "tool")
                inp = part.get("input")
                cmd = inp.get("command") if isinstance(inp, dict) else None
                if not isinstance(cmd, str) or not cmd:
                    cmd = f"[{name}] {json.dumps(inp, ensure_ascii=False)[:200]}"
                tools.append({"command": cmd, "output": ""})
            elif ptype == "tool_result":
                res = part.get("content")
                if isinstance(res, list):
                    res = " ".join(
                        str(x.get("text", "")) for x in res if isinstance(x, dict)
                    )
                out = str(res if res is not None else "")
                # Attach to the most recent tool call lacking output, else append.
                for t in reversed(tools):
                    if not t["output"]:
                        t["output"] = out
                        break
                else:
                    tools.append({"command": "[tool_result]", "output": out})
    if not in_turn:
        return None
    return {
        "user": user,
        "tools": tools,
        "has_user_command": has_user_command,
        "origin_kind": origin_kind,
        "command_name": _turn_command_name(user),
    }


def _render_turn_for_judge(turn: dict[str, Any]) -> str:
    """Render a whole turn (user request + tool activity + response) for the judge."""
    tool_parts: list[str] = []
    for t in turn.get("tools", []):
        if not isinstance(t, dict):
            continue
        out = str(t.get("output", ""))
        if len(out) > TOOL_RESULT_MAX_CHARS:
            out = out[:TOOL_RESULT_MAX_CHARS] + "\n…(truncated)"
        tool_parts.append(f"$ {t.get('command', '')}\n→ {out}")
    tools_text = "\n\n".join(tool_parts).strip() or "(none)"
    if len(tools_text) > TOOL_CONTEXT_MAX_CHARS:
        tools_text = "…(earlier tool activity omitted)\n" + tools_text[-TOOL_CONTEXT_MAX_CHARS:]

    return "\n\n".join([
        "<<<USER_REQUEST\n" + str(turn.get("user", "")) + "\nUSER_REQUEST",
        "<<<TOOL_ACTIVITY\n" + tools_text + "\nTOOL_ACTIVITY",
        "<<<ASSISTANT_RESPONSE\n" + str(turn.get("assistant", "")) + "\nASSISTANT_RESPONSE",
    ])


def _load_config(project_dir: Path) -> dict[str, Any]:
    """Load the JSON config at guard.local.json, if present. Fail-open to defaults.

    Only keys present in DEFAULT_CONFIG are honored, and only when the supplied value
    matches the default's JSON type (str for ``model`` and the StrEnum-backed gate
    fields, list for ``exempt_skills``), so a malformed value can never change a setting
    by accident. ``audit_gate`` persists as a plain string, so it is validated as
    ``str`` here and coerced to a valid enum member downstream (``_audit_gate``); a
    bad-but-string value is dropped there, not here.
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
        # A StrEnum default round-trips through JSON as a plain str, so widen the
        # accepted type to str for those keys (the enum accessor validates the value).
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
        "audit_gate": _audit_gate(config),
        "audit_claims": _audit_claims(config),
        "audit_deferrals": _audit_deferrals(config),
        "audit_korean": _audit_korean(config),
        # Per-turn guards keyed by the transcript prompt_id (a turn == one promptId).
        "last_audited_prompt_id": "",
        # Manual mode: the most recent auditable turn's prompt_id, the target that
        # `/guard:audit-claims` dispatches the claims auditor for.
        "pending_verify_prompt_id": "",
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
    keys = ("audit_gate", "audit_claims", "audit_deferrals", "audit_korean",
            "last_audited_prompt_id", "pending_verify_prompt_id", "updated_at")
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


def _append_log(project_dir: Path, session_id: str, record: dict[str, Any]) -> None:
    record = {"ts": _now_iso(), **record}
    path = _log_file(project_dir, session_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass


VERIFIED_MAX_FACTS = 200
VERIFIED_CONTEXT_MAX = 40


def _append_verified(project_dir: Path, session_id: str, turn_ref: Any, verdict: dict[str, Any]) -> None:
    """Record the supported claims of a PASSED turn as verified facts.

    Only called when the turn passed (no unsupported claim, no resolvable
    deferral). Each supported claim + its evidence becomes a reusable fact that
    later turns' judging can rely on without re-deriving it. ``turn_ref`` is a
    provenance label (the transcript prompt_id) stored alongside each fact.
    """
    facts = [
        {"claim": c.get("claim", "").strip(), "evidence": c.get("evidence", "").strip()}
        for c in verdict.get("claims", [])
        if isinstance(c, dict) and c.get("supported") is True and c.get("claim")
    ]
    if not facts:
        return
    path = _verified_file(project_dir, session_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            for fact in facts:
                f.write(json.dumps({"ts": _now_iso(), "turn": turn_ref, **fact}, ensure_ascii=False) + "\n")
    except OSError:
        pass


def _read_verified_facts(project_dir: Path, session_id: str) -> list[dict[str, str]]:
    """Load previously verified facts (most recent first, capped)."""
    path = _verified_file(project_dir, session_id)
    if not path.is_file():
        return []
    facts: list[dict[str, str]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    for line in lines[-VERIFIED_MAX_FACTS:]:
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except (json.JSONDecodeError, ValueError):
            continue
        if isinstance(rec, dict) and rec.get("claim"):
            facts.append({"claim": rec.get("claim", ""), "evidence": rec.get("evidence", "")})
    return facts


# --------------------------------------------------------------------------- #
# headless judge
# --------------------------------------------------------------------------- #
def _parse_bool(value: str) -> bool | None:
    """Parse a CLI boolean; None when the spelling is not recognized (the caller
    reports the error rather than guessing a default)."""
    v = value.strip().lower()
    if v in _BOOL_TRUE:
        return True
    if v in _BOOL_FALSE:
        return False
    return None


def _effort(config: dict[str, Any]) -> str:
    value = str(config.get("effort", "medium")).lower()
    return value if value in VALID_EFFORTS else "medium"


def _audit_gate(cfg: dict[str, Any]) -> AuditGate:
    """The evidence-judge setting from a config or session-state dict, coerced to a
    valid AuditGate member (defaults on anything unrecognized)."""
    try:
        return AuditGate(str(cfg.get("audit_gate", DEFAULT_CONFIG["audit_gate"])).lower())
    except ValueError:
        return AuditGate(DEFAULT_CONFIG["audit_gate"])


def _audit_claims(cfg: dict[str, Any]) -> bool:
    """Whether the judge checks axis 1 (unsupported claims). Non-bool values fall back
    to the default rather than Python truthiness, so a stray "false" string cannot
    silently disable an axis."""
    v = cfg.get("audit_claims", DEFAULT_CONFIG["audit_claims"])
    return v if isinstance(v, bool) else bool(DEFAULT_CONFIG["audit_claims"])


def _audit_deferrals(cfg: dict[str, Any]) -> bool:
    """Whether the judge checks axis 2 (unjustified deferrals). Same coercion rule as
    _audit_claims."""
    v = cfg.get("audit_deferrals", DEFAULT_CONFIG["audit_deferrals"])
    return v if isinstance(v, bool) else bool(DEFAULT_CONFIG["audit_deferrals"])


def _audit_korean(cfg: dict[str, Any]) -> bool:
    """Whether the judge checks axis 3 (Korean naturalness). Same coercion rule as
    _audit_claims, but the default is False — see DEFAULT_CONFIG["audit_korean"]."""
    v = cfg.get("audit_korean", DEFAULT_CONFIG["audit_korean"])
    return v if isinstance(v, bool) else bool(DEFAULT_CONFIG["audit_korean"])


def _judge_argv(project_dir: Path, system_prompt: str, user_prompt: str, schema: dict,
                config: dict[str, str], tools: str | None) -> list[str] | None:
    """The ``claude`` argv for one judge, or None when the binary is missing.

    ``tools`` None means the child gets NO tool access. An axis that judges the response
    text alone (Korean naturalness) must not be handed the repository: it cannot use it,
    and withholding it is what keeps that judge to a few seconds instead of ~30.
    """
    claude = shutil.which("claude")
    if claude is None:
        _trace(project_dir, None, "judge", "no_claude_binary")
        return None
    cmd = [
        claude, "-p", user_prompt,
        "--safe-mode",
        "--model", config.get("model", "haiku"),
        "--effort", _effort(config),
        "--output-format", "json",
        "--system-prompt", system_prompt,
        "--json-schema", json.dumps(schema),
        "--no-session-persistence",
    ]
    if tools is not None:
        cmd += ["--allowedTools", tools]
    return cmd


def run_judges_parallel(
    project_dir: Path,
    jobs: list[tuple[str, str, str, dict, str | None]],
    config: dict[str, str],
) -> dict[str, dict | None]:
    """Spawn every judge at once and collect them against ONE shared deadline.

    ``jobs`` is a list of (key, system_prompt, user_prompt, schema, tools). Returns
    {key: verdict-or-None}: a key maps to None when its judge failed, timed out, or
    could not be spawned, so the caller sees PARTIAL results instead of losing every
    axis to one bad child. Callers must decide what a missing axis means — silence is
    not a pass.

    The deadline covers the GROUP, not each child: they run concurrently, so the wall
    clock is the slowest one. Giving each its own full ``JUDGE_TIMEOUT_SECONDS`` would
    let a slow set outlive the Stop hook's own timeout and be killed mid-write.
    """
    results: dict[str, dict | None] = {key: None for key, _, _, _, _ in jobs}
    procs: list[tuple[str, subprocess.Popen]] = []
    for key, system_prompt, user_prompt, schema, tools in jobs:
        argv = _judge_argv(project_dir, system_prompt, user_prompt, schema, config, tools)
        if argv is None:
            continue
        try:
            procs.append((key, subprocess.Popen(
                argv, cwd=str(project_dir), stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, text=True)))
        except OSError as e:
            _trace(project_dir, None, "judge", "spawn_failed", axis=key, error=repr(e))
    deadline = time.monotonic() + JUDGE_TIMEOUT_SECONDS
    for key, proc in procs:
        try:
            out, err = proc.communicate(timeout=max(0.1, deadline - time.monotonic()))
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.communicate()
            _trace(project_dir, None, "judge", "timeout", axis=key)
            continue
        if proc.returncode != 0:
            _trace(project_dir, None, "judge", "nonzero_exit", axis=key,
                   code=proc.returncode, stderr=err[:300])
            continue
        results[key] = _parse_judge_output(project_dir, out)
    return results


def _parse_judge_output(project_dir: Path, stdout: str) -> dict | None:
    """Extract the model's JSON verdict from the ``--output-format json`` envelope.

    Prefer the pre-parsed ``structured_output`` field (populated when
    ``--json-schema`` is passed); fall back to parsing the ``result`` string.
    """
    try:
        envelope = json.loads(stdout)
    except (json.JSONDecodeError, ValueError):
        _trace(project_dir, None, "judge", "envelope_unparseable")
        return None
    if not isinstance(envelope, dict):
        return None
    structured = envelope.get("structured_output")
    if isinstance(structured, dict):
        return structured
    result = envelope.get("result")
    if isinstance(result, dict):
        return result
    if not isinstance(result, str):
        return None
    # result is a string that should contain JSON; strip optional code fences.
    text = result.strip()
    fence = re.match(r"^```(?:json)?\s*\n(.*?)\n```\s*$", text, re.DOTALL)
    if fence:
        text = fence.group(1)
    try:
        parsed = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        _trace(project_dir, None, "judge", "result_unparseable", sample=text[:200])
        return None
    return parsed if isinstance(parsed, dict) else None


# --------------------------------------------------------------------------- #
# judge prompts + schemas
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
# per-axis judges
#
# One judge per axis, each carrying its axis text VERBATIM. The text is NOT
# shortened for the split: a trimmed Korean prompt was measured flagging
# `prompt_id`, 커밋, 리팩토링 and `git rebase` as unnatural, so the loanword and
# identifier protections are load-bearing rather than padding. Each judge gets
# only the tools its axis needs (AXIS_JUDGES below) — the Korean axis needs none,
# which is what makes it ~10s against ~30s for a repo-reading judge.
# --------------------------------------------------------------------------- #
_EVIDENCE_PREAMBLE = (
    'A TOOL_ACTIVITY block may precede the response: it is the commands the '
    'assistant actually ran this turn and their output. Treat that output as '
    'first-class evidence — a claim that restates or directly follows from a '
    "command's output in TOOL_ACTIVITY is SUPPORTED even if the response does not "
    're-cite it.\n\nA VERIFIED_FACTS block may also precede the response: these are '
    'claims already confirmed (with their evidence) in earlier turns of this '
    'session. Treat them as established — a claim consistent with a verified fact '
    'is SUPPORTED and need not be re-derived.'
)

_TRIAGE = (
    'TRIAGE FIRST — before reading anything. Scan the response for something to '
    'verify on your axis. If it has NOTHING, return an EMPTY array IMMEDIATELY, '
    'without reading the repository or calling any tool. Do not spend tool calls '
    'on a turn that asserts nothing verifiable.'
)

CLAIMS_SYSTEM = (
    "You audit an assistant's turn from a coding session on ONE axis, defined "
    "below. Judge nothing else. Return only JSON with a `claims` array.\n\n"
    + _TRIAGE + "\n\n"
    + _EVIDENCE_PREAMBLE + "\n\n"
    +
    'AXIS 1 — unsupported or shallowly-supported claims. A claim is ANY statement '
    'the reader could check and find wrong, not only technical behavior. '
    'Technical claims are the obvious case (how a system, tool, library, API, '
    'algorithm, configuration, or codebase behaves or performs), but the same bar '
    "applies to what a file contains or lacks, history and process ('added for "
    "X', 'tests passed before'), what a tool or subagent reported, counts and "
    "comparisons ('the only place', 'most of'), what the user decided earlier, "
    'and attributions of cause. A genuine preference or aesthetic judgment is NOT '
    "a claim: 'cleaner' is a preference, 'allocates less' is a claim. For each "
    'load-bearing claim, decide if it is backed by adequate evidence: output of a '
    'command in TOOL_ACTIVITY, a specific code reference (file:line or symbol), a '
    'named doc/spec, a measurement, or a sound derivation. Evidence may sit '
    'anywhere in the response — including a References section closing the '
    'answer, with a short mark on the claim. Judge whether a mark RESOLVES, never '
    'whether it matches any particular syntax. Resolve whatever marks you find '
    'against that section before judging: a claim whose mark is backed by an '
    "adequate entry is SUPPORTED, and the mark's presence is not itself a missing "
    'citation — but a mark resolving to NOTHING, or to an entry that does not '
    'establish the claim, is UNSUPPORTED exactly as an uncited claim would be. '
    'Follow the link; never credit a claim for merely carrying a mark. Judge the '
    'QUALITY of the evidence, not just its presence — mark the claim UNSUPPORTED '
    'when the assistant reasoned from a SURFACE SIGNAL instead of the actual '
    'behavior: inferring what a function does from its NAME, a comment, a '
    'variable/type name, a filename, or a docstring without reading the body; '
    "assuming a caller's or dependency's behavior without opening it; or building "
    'a conclusion on an earlier UNVERIFIED ASSUMPTION. Open the real definition '
    'and confirm. A cited file:line that does not actually establish the claim '
    'counts as unsupported. When a claim cites OFFICIAL DOCUMENTATION, the '
    'response must also point to a local saved copy under `__REFS_DIR__`; verify '
    'that file actually exists (Read/Glob) and supports the claim — a docs claim '
    'with no existing local copy, or a path that is missing, is UNSUPPORTED. '
    'Statements explicitly flagged as unverified assumptions are NOT violations; '
    'genuine preferences and hedged suggestions are NOT claims.'
)

DEFERRALS_SYSTEM = (
    "You audit an assistant's turn from a coding session on ONE axis, defined "
    "below. Judge nothing else. Return only JSON with a `deferrals` array.\n\n"
    + _TRIAGE + "\n\n"
    + _EVIDENCE_PREAMBLE + "\n\n"
    +
    'AXIS 2 — unjustified deferrals. The assistant must not punt on something it '
    'could resolve by reading the code. Flag every place it defers, postpones, or '
    'declares uncertainty about a matter of FACT that the repository would answer '
    "— phrased as an 'open question', 'TBD', 'to be decided', 'deferred', 'needs "
    "investigation', 'unclear', 'would need to check', 'left for later', or an "
    "equivalent in any language (including Korean: '미정', '추후', '확인 필요', '결정 안 "
    "됨'). For each, actually look in the repo. A deferral is RESOLVABLE (a "
    'violation) when the answer is discoverable from the code, config, tests, or '
    'docs in this repository — the assistant should have looked instead of '
    'deferring. A deferral is LEGITIMATE (not a violation) only when it genuinely '
    'requires a human product/policy/taste decision, external input the repo '
    'cannot contain, or runtime data not yet available. A question the assistant '
    'explicitly hands to the user as their decision ("your call", "email vs log — '
    'up to you") is LEGITIMATE unless the repo already fixes the answer. Do NOT '
    'flag a genuine product/UX/policy choice as resolvable. Only flag a deferral '
    'resolvable when you can name the concrete file/symbol that answers it.'
)

KOREAN_SYSTEM = (
    "You audit an assistant's turn from a coding session on ONE axis, defined "
    "below. Judge nothing else. Return only JSON with a `korean` array.\n\n"
    + _TRIAGE + "\n\n"
    +
    'AXIS 3 — unnatural Korean. FIRST, decide the language of the assistant '
    'response. If it is not substantially in Korean, return `korean` as an EMPTY '
    'ARRAY immediately and audit nothing on this axis — an English (or any '
    'non-Korean) response is never a violation here, no matter how it is phrased. '
    'Judge the PROSE only: code, identifiers, paths, commands, log output, quoted '
    'English terms, and established loanwords that Korean developers actually say '
    "('커밋', '파일', '후킹', '리팩토링') are all fine and must NOT be flagged. Do not ask "
    'for a pure-Korean rewrite of a technical term; a translated identifier is '
    'worse than the English one. Flag a phrase ONLY when it reads as '
    'machine-translated English rather than something a Korean developer would '
    "write: English word order forced into Korean, a chain of '~에 대한' / '~를 위한' "
    "noun stacks where a verb is natural ('~에 대한 처리를 수행합니다' → '~를 처리합니다'), "
    "redundant '해당/상기/동일한' where a plain demonstrative works, literal calques "
    "('존재하지 않습니다' → '없습니다'), mismatched particles (은/는, 이/가, 을/를), or a "
    'sentence so long its subject and verb no longer agree. SEPARATELY, the register '
    "must be 존댓말: a Korean response holds the -습니다/-입니다 form throughout. Flag "
    "반말, bare 해체 endings, and a drift out of 존댓말 partway through (it usually "
    "starts once the writing turns technical). The user writing in 반말 does not "
    "license a 반말 answer. This is not a translationese test — a sentence can be "
    'natural Korean and still be the wrong register. For each finding give the '
    'offending `phrase` verbatim from the response and a `suggestion` that a Korean '
    'developer would actually write. Report only phrases you would genuinely '
    'rewrite — style you merely dislike is not a violation.'
)

# One narrow schema per axis. Each judge returns only its own array, so a judge
# cannot report on an axis it was not asked about.
CLAIMS_SCHEMA = {
    "type": "object",
    "properties": {
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string"},
                    "supported": {"type": "boolean"},
                    "evidence": {"type": "string"},
                    "reasoning": {"type": "string"},
                },
                "required": ["claim", "supported", "evidence", "reasoning"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["claims"],
    "additionalProperties": False,
}

DEFERRALS_SCHEMA = {
    "type": "object",
    "properties": {
        "deferrals": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "item": {"type": "string"},
                    "resolvable_from_repo": {"type": "boolean"},
                    "how_to_resolve": {"type": "string"},
                    "reasoning": {"type": "string"},
                },
                "required": ["item", "resolvable_from_repo", "how_to_resolve", "reasoning"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["deferrals"],
    "additionalProperties": False,
}

KOREAN_SCHEMA = {
    "type": "object",
    "properties": {
        "korean": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "phrase": {"type": "string"},
                    "unnatural": {"type": "boolean"},
                    "suggestion": {"type": "string"},
                    "reasoning": {"type": "string"},
                },
                "required": ["phrase", "unnatural", "suggestion", "reasoning"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["korean"],
    "additionalProperties": False,
}

# Field order is the order findings appear in the block message.
_AXIS_FIELDS = ("claims", "deferrals", "korean")


class AxisJudge(NamedTuple):
    """Everything needed to spawn one axis's judge and read its answer back.

    ``tools`` is the ``--allowedTools`` value, or None for a judge that gets no tool
    access at all. The Korean axis is None deliberately: it judges prose and never
    needs the repository, and withholding the tools is what keeps it fast.
    ``violates`` picks the finding records that count as violations for that axis.
    """

    field: str
    system: str
    schema: dict
    tools: str | None
    violates: Any
    label: str


AXIS_JUDGES: dict[str, AxisJudge] = {
    "claims": AxisJudge(
        "claims", CLAIMS_SYSTEM, CLAIMS_SCHEMA, "Read,Grep,Glob,Bash",
        lambda r: r.get("supported") is False, "unsupported claims"),
    "deferrals": AxisJudge(
        "deferrals", DEFERRALS_SYSTEM, DEFERRALS_SCHEMA, "Read,Grep,Glob",
        lambda r: r.get("resolvable_from_repo") is True, "resolvable deferrals"),
    "korean": AxisJudge(
        "korean", KOREAN_SYSTEM, KOREAN_SCHEMA, None,
        lambda r: r.get("unnatural") is True, "unnatural Korean"),
}


def _enabled_axes(state: dict[str, Any]) -> list[str]:
    """The axis fields switched on, in _AXIS_FIELDS order."""
    on = {"claims": _audit_claims(state), "deferrals": _audit_deferrals(state),
          "korean": _audit_korean(state)}
    return [f for f in _AXIS_FIELDS if on[f]]


# --------------------------------------------------------------------------- #
# subcommands
# --------------------------------------------------------------------------- #
def cmd_user_prompt() -> int:
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0

    prompt = payload.get("prompt")
    prompt = prompt if isinstance(prompt, str) else ""

    # guard's own control commands (`/guard:settings ...`, `/guard:audit-claims`) are not
    # real turns — the forked `config` skill / the `verify` expansion handle them. Don't
    # log, don't start a turn, don't judge.
    if _CONTROL_CMD_RE.match(prompt.strip()):
        _trace(project_dir, session_id, "user-prompt", "skip_control_cmd")
        return 0

    # The log is the human-readable session record and the only place the user's own
    # wording is kept; the Stop audit reads the turn itself from the transcript by
    # prompt_id, so nothing else is derived here.
    _append_log(project_dir, session_id, {"role": "user", "text": prompt})
    _trace(project_dir, session_id, "user-prompt", "logged")
    return 0


def _emit_expansion(msg: str) -> None:
    output = {"hookSpecificOutput": {"hookEventName": "UserPromptExpansion", "additionalContext": msg}}
    json.dump(output, sys.stdout)


def cmd_verify() -> int:
    """UserPromptExpansion for the per-axis ``/guard:audit-*`` commands.

    The axis comes from argv (``verify claims`` | ``deferrals`` | ``korean``), one per
    command, so each skill audits exactly its own axis. Targets
    ``pending_verify_prompt_id`` (set by manual-mode Stop) and reads no transcript — the
    Stop hook already wrote the slice. Works in any ``audit_gate`` mode.

    An axis switched off is still auditable here: the switch governs the AUTOMATIC
    Stop-time audit, while running the command is the user asking for this one audit
    now. Refusing it would leave the user no way to check an axis they keep off by
    default, which is the main reason to keep the axis off in the first place.
    """
    axis = sys.argv[2].strip().lower() if len(sys.argv) > 2 else "claims"
    if axis not in AXIS_AGENTS:
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
    turn_path = _turn_slice_file(project_dir, session_id, pid) if pid else None
    if not pid or turn_path is None or not turn_path.is_file():
        _emit_expansion("guard: no completed turn is available to audit yet. "
                        f"Ask something first, then run `/guard:audit-{axis}`.")
        _trace(project_dir, session_id, "verify", "no_pending", axis=axis, prompt_id=pid)
        return 0

    context = _axis_dispatch_context(
        project_dir, session_id, pid, turn_path,
        "guard: audit the last completed turn on request.", axis)
    _emit_expansion(context)
    _trace(project_dir, session_id, "verify", "dispatch", axis=axis, prompt_id=pid)
    return 0


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


def _write_turn_slice(project_dir: Path, session_id: str, prompt_id: str,
                      turn: dict[str, Any]) -> Path | None:
    """Write this turn's slice ({user, tools, assistant}) to its ``turn_file``.

    The single slice-writer, shared by manual-mode Stop (whose slice the on-demand
    claims auditor) and manual-mode Stop (which records it as the pending on-demand target).
    Internal flags (has_user_command / origin_kind / command_name — all handled before
    this point) are not part of the claims auditor's schema, so drop them. Returns the path,
    or None on a write failure (caller fails open).
    """
    slice_out = {k: v for k, v in turn.items()
                 if k not in ("has_user_command", "origin_kind", "command_name")}
    turn_path = _turn_slice_file(project_dir, session_id, prompt_id)
    try:
        turn_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = turn_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(slice_out, ensure_ascii=False), encoding="utf-8")
        tmp.replace(turn_path)
    except OSError:
        _trace(project_dir, session_id, "stop", "slice_write_failed", prompt_id=prompt_id)
        return None
    return turn_path


# The subagent handling one axis on demand, per axis. Each has its own agent
# definition because the tool grant lives in that file's frontmatter, and the grants
# differ: claims and deferrals read the repository, while the Korean axis needs no
# repository access and instead needs `Write` to emit its corrected text. The headless
# judges express the Korean axis's zero-tool need as a missing --allowedTools flag
# (AXIS_JUDGES); a subagent frontmatter cannot express it at all.
AXIS_AGENTS = {
    "claims": ("guard:claims-auditor", "unsupported claims"),
    "deferrals": ("guard:deferrals-auditor", "deferrals the repository could resolve"),
    "korean": ("guard:korean-corrector", "Korean prose that reads as translated English"),
}

# What the main agent does with each axis's report. Only the Korean axis produces a
# corrected artifact, so only it needs the main agent told where to find one.
_AXIS_DISPATCH_TAIL = {
    "claims": "It writes nothing. If it reports violations, address them; otherwise continue.",
    "deferrals": "It writes nothing. If it reports violations, address them; otherwise continue.",
    "korean": ("On violations it also writes the corrected response to the rewrite path "
               "and names it in its report; read that file and use its text as the "
               "corrected wording, keeping any phrase it listed as unfixed for yourself "
               "to resolve. On a pass it writes nothing and there is nothing to do."),
}


def _axis_dispatch_context(project_dir: Path, session_id: str, prompt_id: str,
                           turn_path: Path, lead: str, axis: str) -> str:
    """Build the additionalContext asking the main agent to dispatch one axis's agent.

    One axis per dispatch: each per-axis command owns a single axis, so the agent is told
    what to audit by WHICH agent is dispatched rather than by an argument it has to be
    trusted to honor.

    Pass ONLY what the agent cannot get for itself. That is the turn record — guard sliced
    it, so nothing else knows the path — and, for Korean, somewhere to write. Everything
    else the agent resolves on its own or asks the main agent for: the refs directory
    comes from the `refs-dir` subcommand, and the repository it audits against is simply
    the working tree. `session_id` / `prompt_id` are here to BUILD those two paths, never
    to be handed over: an agent auditing one turn has no use for guard's identifiers, and
    an extra pointer is one more thing it can wander into instead of auditing.

    The verified-facts store is deliberately NOT passed. Only `cmd_stop`'s headless branch
    writes it, so on the manual path that dispatches these agents it is either absent or a
    leftover from an earlier headless stretch of the same session — and priming an audit
    with facts this run never established is how an unexamined claim becomes an
    established one.
    """
    agent, what = AXIS_AGENTS[axis]
    # The turn record is the whole input: `_write_turn_slice` dumps the tool outputs
    # uncut (only the headless judge's `_render_turn_for_judge` truncates, and it never
    # reads this file), so there is nothing for a transcript fallback to recover.
    inputs = [f"- turn record: {turn_path.resolve()}"]
    if axis == "korean":
        inputs.append(f"- rewrite path (write the corrected text here): "
                      f"{_korean_rewrite_file(project_dir, session_id, prompt_id).resolve()}")
    return (
        lead + " "
        f"Dispatch the {agent} subagent with the Agent tool "
        f"(subagent_type: \"{agent}\"), passing it these inputs verbatim:\n"
        + "\n".join(inputs) + "\n"
        f"It audits the turn for {what} and reports back. {_AXIS_DISPATCH_TAIL[axis]}"
    )


def _stop_manual(project_dir: Path, session_id: str, state: dict[str, Any],
                 prompt_id: str, turn: dict[str, Any]) -> int:
    """Manual mode Stop: record the turn as the pending verify target; do NOT audit.

    The turn is already in the session archive; here we persist just its slice and
    remember its prompt_id so ``/guard:audit-claims`` can dispatch the claims auditor for it
    without any transcript access. The hook emits nothing and never blocks.
    """
    turn_path = _write_turn_slice(project_dir, session_id, prompt_id, turn)
    if turn_path is None:
        return 0  # fail open
    state["pending_verify_prompt_id"] = prompt_id
    _write_state(project_dir, session_id, state)
    _trace(project_dir, session_id, "stop", "manual_pending", prompt_id=prompt_id)
    return 0


def cmd_stop() -> int:
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0

    response = payload.get("last_assistant_message")
    response = response if isinstance(response, str) else ""

    # Read the finished turn up front: it is needed both to keep the session archive and
    # to judge, and a `<task-notification>` turn must be excluded from BOTH, so the check
    # precedes the archive write. When a background subagent finishes, Claude Code opens
    # a NEW transcript turn (fresh promptId) whose anchor is a `<task-notification>`
    # record (`origin.kind == "task-notification"`, promptSource "system", NOT isMeta —
    # otherwise indistinguishable from a typed prompt). It is not the assistant answering
    # a user, so it does not belong in the archive; and in subagent mode auditing it is
    # self-perpetuating (the auditor dispatch is itself a background task whose
    # completion is another task-notification → claims auditor re-dispatched ad infinitum,
    # verified 2.1.197). (older CC / no prompt yet → turn is None; nothing to skip here,
    # the judge path below still fails open on skip_no_prompt_id.)
    prompt_id = payload.get("prompt_id")
    transcript_path = payload.get("transcript_path")
    has_prompt = isinstance(prompt_id, str) and bool(prompt_id) and isinstance(transcript_path, str)
    turn = _read_turn_from_transcript(transcript_path, prompt_id) if has_prompt else None
    if turn is not None and turn.get("origin_kind") == "task-notification":
        _trace(project_dir, session_id, "stop", "skip_task_notification", prompt_id=prompt_id)
        return 0

    _append_log(project_dir, session_id, {"role": "assistant", "text": response})

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    # Recursion / re-entry guard: never block twice in a row.
    if payload.get("stop_hook_active") is True:
        _trace(project_dir, session_id, "stop", "skip_active")
        return 0

    if not response.strip():
        return 0

    # The turn is identified by the transcript prompt_id; guard reads the whole turn
    # from Claude Code's transcript. Without them (older CC / no prompt yet) there is
    # nothing to audit — fail open.
    if not has_prompt:
        _trace(project_dir, session_id, "stop", "skip_no_prompt_id")
        return 0
    if turn is None:
        _trace(project_dir, session_id, "stop", "skip_no_turn", prompt_id=prompt_id)
        return 0

    # Skip judging a turn whose slice contains a user `!` command. A `!` command
    # inherits the preceding typed prompt's promptId (verified on 2.1.197: `!git push`
    # ran after a reply carried that reply's promptId), and its <bash-input>/
    # <bash-stdout> records land in the slice AFTER the responses guard already judged
    # — the `!` output is evidence that arrives later than the claims it would support,
    # so it cannot be judged coherently within this turn. Do not treat `!` as evidence
    # and do not audit the turn it appears in.
    if turn.get("has_user_command"):
        _trace(project_dir, session_id, "stop", "skip_user_command", prompt_id=prompt_id)
        return 0

    # Skip judging a turn opened by guard's own control command (`/guard:settings`,
    # `/guard:audit-claims`) or by a user-configured exempt skill/command. Such a turn's
    # response is a relay or skill output, not a body of technical claims to ground —
    # e.g. relaying "guard on" has no evidence to cite and would be falsely blocked
    # (session b30dbaec). The approval classifier already skips control commands at
    # UserPromptSubmit; this is the matching skip at Stop. Applies to both modes.
    cmd_name = turn.get("command_name", "")
    if cmd_name and (_is_control_command_name(cmd_name) or cmd_name in _exempt_skills(config)):
        _trace(project_dir, session_id, "stop", "skip_exempt_skill",
               prompt_id=prompt_id, command=cmd_name)
        return 0

    turn["assistant"] = response

    # No axis enabled: nothing for any judge to report, so run none of them — no spawn,
    # no dispatch, and no pending target for `/guard:audit-*` to pick up.
    axes = _enabled_axes(state)
    if not axes:
        _trace(project_dir, session_id, "stop", "skip_axes_off", prompt_id=prompt_id)
        return 0

    # Manual mode (default): the hook never audits or blocks at Stop. It records the
    # turn as the pending on-demand target; the user runs one of the per-axis
    # `/guard:audit-*` commands to audit it.
    if state["audit_gate"] == AuditGate.MANUAL:
        return _stop_manual(project_dir, session_id, state, prompt_id, turn)

    turn["assistant"] = response

    # Facts verified in earlier passed turns are reusable evidence: a claim that
    # matches one need not be re-derived. Only the claims judge can use them.
    verified = _read_verified_facts(project_dir, session_id)
    verified_block = ""
    if verified:
        lines_v = [f"- {v['claim']}" + (f"  [evidence: {v['evidence']}]" if v.get("evidence") else "")
                   for v in verified[-VERIFIED_CONTEXT_MAX:]]
        verified_block = (
            "<<<VERIFIED_FACTS (already confirmed earlier this session — treat as "
            "established; a claim consistent with these is supported)\n"
            + "\n".join(lines_v) + "\nVERIFIED_FACTS\n\n"
        )

    rendered = _render_turn_for_judge(turn)
    refs_rel = _refs_rel(project_dir, config)
    jobs: list[tuple[str, str, str, dict, str | None]] = []
    for field in axes:
        j = AXIS_JUDGES[field]
        # The Korean axis judges prose alone: it gets the response without the evidence
        # blocks it cannot use, which is also most of the token saving from the split.
        if field == "korean":
            user = ("Audit the assistant's response below on your single axis. Return "
                    "only the JSON verdict.\n\n<<<ASSISTANT_RESPONSE\n"
                    + str(turn.get("assistant", "")) + "\nASSISTANT_RESPONSE")
        else:
            user = ("Audit the assistant's turn below on your single axis. Treat the "
                    "commands in TOOL_ACTIVITY and their output as first-class evidence, "
                    "alongside VERIFIED_FACTS and what you can read from the repository. "
                    "USER_REQUEST is context (e.g. facts the user already confirmed). "
                    "Return only the JSON verdict.\n\n" + verified_block + rendered)
        jobs.append((field, j.system.replace("__REFS_DIR__", refs_rel), user, j.schema, j.tools))

    verdicts = run_judges_parallel(project_dir, jobs, config)

    # Every axis failed: fail open, exactly as the single judge did on a None verdict.
    if all(v is None for v in verdicts.values()):
        _trace(project_dir, session_id, "stop", "all_judges_failed", axes=",".join(axes))
        return 0

    # A judge that did not report is NOT a pass. Name the axis in the block reason so
    # its silence is never read as a clean result, and never record verified facts for
    # a turn whose audit was incomplete.
    missing = [f for f in axes if verdicts.get(f) is None]

    _append_log(project_dir, session_id, {
        "role": "judge",
        "axes": axes,
        "missing": missing,
        **{f: (verdicts[f] or {}).get(f, []) for f in axes},
    })

    # Violations come from the concrete finding records, not from any judge's own
    # verdict field — a judge sometimes calls a turn blocked while every item it listed
    # is actually fine. Each axis has its own predicate (AXIS_JUDGES[...].violates), and
    # only ENABLED axes are in `axes` at all, so a disabled axis cannot contribute here.
    found: dict[str, list[dict]] = {}
    for field in axes:
        v = verdicts.get(field)
        if v is None:
            continue
        items = v.get(field, [])
        pred = AXIS_JUDGES[field].violates
        found[field] = [r for r in items if isinstance(r, dict) and pred(r)]

    if not any(found.values()) and not missing:
        # Passed turn, fully audited: collect its supported claims as verified facts.
        cv = verdicts.get("claims")
        if cv is not None:
            _append_verified(project_dir, session_id, prompt_id, cv)
        _trace(project_dir, session_id, "stop", "pass", axes=",".join(axes))
        return 0

    sections: list[str] = []
    if found.get("claims"):
        lines_c = [f"- {c.get('claim', '').strip()}" for c in found["claims"][:6] if c.get("claim")]
        sections.append(
            "Claims stated as fact without adequate evidence — ground each "
            "(cite file:line, a command's output, a named doc/spec, or a measurement) "
            "or explicitly mark it as an unverified assumption:\n" + "\n".join(lines_c)
        )
    if found.get("deferrals"):
        lines_d = []
        for d in found["deferrals"][:6]:
            item = d.get("item", "").strip()
            how = d.get("how_to_resolve", "").strip()
            lines_d.append(f"- {item}" + (f" — resolve by: {how}" if how else ""))
        sections.append(
            "Questions you deferred that the repository can answer — do NOT punt "
            "these as 'open question', 'TBD', 'deferred', or 'needs investigation'. "
            "Read the code and resolve them now:\n" + "\n".join(lines_d)
        )
    if found.get("korean"):
        lines_k = []
        for k in found["korean"][:6]:
            phrase = k.get("phrase", "").strip()
            fix = k.get("suggestion", "").strip()
            lines_k.append(f"- {phrase}" + (f" → {fix}" if fix else ""))
        sections.append(
            "Korean phrasing that reads as translated rather than written. Rewrite "
            "these the way a Korean developer would say them, then finish (leave code, "
            "identifiers, paths, and established loanwords as they are):\n" + "\n".join(lines_k)
        )
    if missing:
        sections.append(
            "guard could not audit these axes this turn (the judge failed or timed "
            "out), so treat them as UNCHECKED rather than clean: " + ", ".join(missing)
        )
    if not sections:
        return 0

    reason = "guard: finish the work before stopping.\n\n" + "\n\n".join(sections)
    json.dump({"decision": "block", "reason": reason}, sys.stdout)
    _trace(project_dir, session_id, "stop", "block",
           **{f: len(found.get(f, [])) for f in axes}, missing=",".join(missing))
    return 0


def cmd_session_start() -> int:
    # Sweep both state and logs on the same age policy. State is intentionally NOT
    # cleared at SessionEnd: a session can be resumed later (`claude --resume`), and
    # its audit_gate / axis flags must survive the gap. Age-based expiry is the
    # only reaper, so a resumed session keeps its state as long as it is touched
    # within the retention window.
    project_dir = _project_dir()
    if project_dir is None:
        return 0
    root = _state_root(project_dir)
    cutoff = time.time() - ORPHAN_MAX_AGE_SECONDS
    # File-per-session dirs.
    for sub in ("state", "sessions", "verified"):
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
    # turns/ holds one dir per session of claims auditor turn-slice files; sweep stale dirs.
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

    Edits ONLY the ``exempt_skills`` key — never ``audit_gate`` / state — so it can
    change which skills' turns the Stop judge skips but cannot disable guard
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
    """Mirror an ``audit_gate`` / axis-switch change into the live session's
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
    guard.local.json defaults; for ``audit_gate`` and the axis switches it also shows the
    live session value when it differs from the default (the session may have been changed
    after)."""
    raw = _load_raw_config(project_dir)
    cfg = _load_config(project_dir)
    state = None
    if session_id and _state_file(project_dir, session_id).is_file():
        state = _read_state(project_dir, session_id, cfg)

    judge_default = _audit_gate(cfg)
    if state is not None and _audit_gate(state) != judge_default:
        judge_line = f"audit_gate: {_audit_gate(state)} (this session; default {judge_default})"
    else:
        judge_line = f"audit_gate: {judge_default}"

    def axis_line(key: str, reader) -> str:
        default = reader(cfg)
        shown = "on" if default else "off"
        if state is not None and reader(state) != default:
            return f"{key}: {'on' if reader(state) else 'off'} (this session; default {shown})"
        return f"{key}: {shown}"

    claims_line = axis_line("audit_claims", _audit_claims)
    deferrals_line = axis_line("audit_deferrals", _audit_deferrals)
    korean_line = axis_line("audit_korean", _audit_korean)

    exempt = _exempt_skills(cfg)
    refs_rel = raw.get("refs_dir") if isinstance(raw.get("refs_dir"), str) else ""
    return [
        f"model: {cfg['model']}",
        f"effort: {_effort(cfg)}",
        judge_line,
        claims_line,
        deferrals_line,
        korean_line,
        "exempt_skills: " + (", ".join(sorted(exempt)) if exempt else "(none)"),
        "refs_dir: " + (refs_rel if refs_rel else "(default wiki/ref/)"),
    ]


def cmd_settings() -> int:
    """View/change guard.local.json settings — the CLI behind the ``guard:settings`` skill.

        settings [show]                      — print the current settings
        settings set <key> <value>           — change one setting

    Settable keys: ``audit_gate`` (manual|headless — how the evidence judge runs), the
    axis switches ``audit_claims`` / ``audit_deferrals`` / ``audit_korean``, ``model``,
    ``effort`` (low|medium|high|xhigh|max), ``refs_dir``.
    ``audit_gate`` and the axis switches
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

    if key == "audit_gate":
        try:
            v = AuditGate(value.strip().lower())
        except ValueError:
            print(f"guard settings: audit_gate must be one of {[e.value for e in AuditGate]} "
                  f"(got {value!r})", file=sys.stderr)
            return 0
        raw["audit_gate"] = v.value
        _apply_session_scalar(project_dir, session_id, "audit_gate", v.value)
    elif key in ("audit_claims", "audit_deferrals", "audit_korean"):
        v = _parse_bool(value)
        if v is None:
            print(f"guard settings: {key} must be one of "
                  f"{sorted(_BOOL_TRUE | _BOOL_FALSE)} (got {value!r})", file=sys.stderr)
            return 0
        raw[key] = v
        _apply_session_scalar(project_dir, session_id, key, v)
    elif key == "effort":
        v = value.lower()
        if v not in VALID_EFFORTS:
            print(f"guard settings: effort must be one of {sorted(VALID_EFFORTS)} (got {value!r})", file=sys.stderr)
            return 0
        raw["effort"] = v
    elif key == "model":
        v = value.strip()
        if not v:
            print("guard settings: model must be a non-empty string", file=sys.stderr)
            return 0
        raw["model"] = v
    elif key == "refs_dir":
        raw["refs_dir"] = value  # "" resets to the default; _refs_dir validates at use
    else:
        print(f"guard settings: unknown or unsettable key {key!r}. Settable: "
              "audit_gate, audit_claims, audit_deferrals, audit_korean, model, effort, "
              "refs_dir (exempt_skills via the exempt CLI).",
              file=sys.stderr)
        return 0

    if not _write_config(project_dir, raw):
        print("guard settings: failed to write .claude/guard.local.json", file=sys.stderr)
        return 0

    for line in _config_show_lines(project_dir, session_id):
        print(line)
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


def cmd_refs_index() -> int:
    """PostToolUse: after a write inside the refs dir, require the new file to be
    listed in the refs index (``AGENTS.md``).

    A saved reference nothing points at is a file the next reader never finds, so the
    index is the deliverable, not a courtesy. This fires *after* the write (PostToolUse)
    rather than blocking it: the natural order is save-then-index, and blocking the save
    would force the index entry to be written first, for a file that does not exist yet.

    Blocks with ``decision: "block"`` so the reason returns to the model as work to
    finish, and stays silent in every other case — a write outside the refs dir, the
    index itself, or a file already listed.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0

    config = _load_config(project_dir)
    tool_input = payload.get("tool_input")
    if not _targets_refs_dir(project_dir, tool_input, config):
        return 0
    target = _tool_target_path(project_dir, tool_input)
    if target is None or target.name in _REFS_INDEX_SKIP:
        return 0

    reason = refs_index_gap(project_dir, target, config)
    if reason is None:
        _trace(project_dir, None, "refs-index", "listed", file=target.name)
        return 0

    json.dump({"decision": "block", "reason": reason}, sys.stdout)
    _trace(project_dir, None, "refs-index", "missing", file=target.name)
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
    "refs-index": cmd_refs_index,
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
