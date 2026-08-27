"""``session-start`` (SessionStart) — the sweep, the exports, and the standing context.

Sweeps state files, ``trace.log``, and turns/ and extracts/ dirs older than retention;
exports ``GUARD_PROJECT_DIR`` and ``GUARD_REFS_DIR`` via ``$CLAUDE_ENV_FILE`` (append-once,
since this event also fires on every compaction); and states as session context the refs rule
always, and the turn closeout's path when any agent is on. Each is said ONCE here rather
than in every Stop, which is the
whole reason this hook prints anything.

There is deliberately no line naming ``ext-docs-fetcher``. That agent has no switch to
announce and nothing here forbids the session's own fetching; it is selected the way any agent
is, from its description, and the refs rule below is what tells the session that a cited page
has to end up saved.
"""

from __future__ import annotations

import json
import os
import shlex
import time

from pathlib import Path

from .config import (
    AUDIT_PLAN_KEY, AUDIT_TURN_KEY, CLEAR_INHERIT_MAX_AGE_SECONDS,
    ORPHAN_MAX_AGE_SECONDS, _HOST_IS_CODEX, _audit_on, _load_config, _switch_on
)
from .paths import (
    _clear_handoff_file, _project_dir, _refs_dir, _state_root, _trace, _trace_file
)
from .payload import _read_payload, _session_id
from .state import _audit_paused, _plan_audit_paused, _read_state, _write_state
from .agents import SETTABLE_AGENTS
from .dispatch import CLI_REL, _closeout_path, _plugin_root


def _session_muted(project_dir: Path, config: dict, payload: dict | None) -> bool:
    """Is the session this SessionStart opens muted? Claude only.

    At `startup` this is the project's `audit-turn` setting, armed unless the config says
    otherwise (`state._read_state`). It is not only that: SessionStart registers no matcher,
    so it also fires on `resume`, `clear`, `compact` and `fork`, where the session may already
    have been flipped by `guard` — or, on `clear`, by the handoff from the session it
    replaced — and the state file says so. Either way the line below reports what it finds
    rather than what the project configured, because the two can differ.

    The payload is passed in rather than read here: stdin can be read once, and the clear
    handoff needs the same payload's `source`. On Codex it is None (that adapter consumed
    stdin before calling this module), which costs nothing — Codex has no mute command
    and its Stop path never reads `audit_paused`, so a Codex session is never muted.
    """
    if _HOST_IS_CODEX:
        return False
    sid = _session_id(payload) if payload else None
    if sid is None:
        # No session id, no state file to read — so answer from the project setting, which is
        # what a session with no state of its own would have opened in anyway. Answering a
        # fixed `True` here would print "audits are OFF" to a project that configured them on.
        return not _audit_on(config, AUDIT_TURN_KEY)
    return _audit_paused(_read_state(project_dir, sid, config))


def _add_shell_command_to_path() -> bool:
    """Put guard's shell commands on the session's ``PATH``. True if written.

    Two of them share the directory and are reached the same way, by parties that never
    meet: ``guard`` is the user's, typed at a shell prompt, and ``guard-candidates`` is the
    router's, run from a subagent's Bash. Adding the directory serves both, which is why
    this is one export rather than two.

    ``CLAUDE_ENV_FILE`` is not a list of ``export`` lines — it is a shell script Claude Code
    SOURCES before each Bash command, so it can prepend a directory as readily as it can set
    a variable. That is what makes ``guard on`` work with nothing to install: no startup
    file is edited, and nothing is left behind when the session ends, because the file
    belongs to one session.

    A real executable on ``PATH``, not a shell function. A function exists only in the shell
    that sourced it, so anything one level down — a subprocess, a Makefile recipe, a script
    the agent writes — would not find ``guard``; an executable is inherited the way every
    other command is. It also behaves like a command in the ways people expect: ``command -v
    guard`` locates it, and ``guard`` inside ``$(...)`` works.

    Only guard's own ``bin`` is added, and only ever once (``_append_env_file`` matches on
    the directory). Prepending is not "reordering the user's PATH": it adds one directory
    holding one command. A user who already has a ``guard`` can set ``GUARD_TOGGLE_NAME``,
    which is the name guard's own messages then suggest — though note that variable renames
    only the SUGGESTION, not this file, so a genuine collision is theirs to resolve.

    Added unconditionally, for every project. Gating it on "guard is configured here" would
    be gating on nothing: a project with no ``guard.local.json`` loads the defaults and is an
    ordinary guard project whose switches are all ``off`` — so the condition would not
    separate the case it appears to, and the command would be missing exactly where a user
    might reach for it first.

    Best-effort and silent, like the exports: the CLI verb is reachable by path regardless,
    and a session without it is merely less convenient.
    """
    bin_dir = _plugin_root() / "shell" / "bin"
    if not (bin_dir / "guard").is_file():
        return False
    quoted = shlex.quote(str(bin_dir))
    return _append_env_file(f"export PATH={quoted}:$PATH", marker=f"export PATH={quoted}:")


def _export_to_bash_env(name: str, value: str) -> bool:
    """Persist one ``export`` into the session's Bash environment. True if written.

    SessionStart is handed ``CLAUDE_ENV_FILE``, a path whose ``export`` lines reach every
    later Bash command Claude Code runs (`wiki/ref/claude-code-hooks-session-env.md`). It is
    the only channel by which a Bash-invoked verb learns something the HOST decided rather
    than inferring it, and guard uses it for two values: the project root and the resolved
    refs directory.

    ``GUARD_``-prefixed names only, never ``CLAUDE_PROJECT_DIR``: the host owns that name,
    other tooling reads its presence as "running inside a hook", and guard exporting it into
    every shell in the session would be guard answering for the host.

    Appended only when the identical line is not already present. SessionStart registers no
    matcher, so it fires on `startup`, `resume`, `clear`, `compact` and `fork` alike, and a
    blind append added the same export once per compaction for the life of the session —
    which is what `GUARD_REFS_DIR` did before this became shared.

    Best-effort, silent on failure: everything that reads these has a fallback, and the
    session's context lines go out either way.
    """
    return _append_env_file(f"export {name}={shlex.quote(value)}")


def _append_env_file(text: str, marker: str | None = None) -> bool:
    """Append to ``$CLAUDE_ENV_FILE`` unless it already carries this. True if written.

    ``marker`` is the line that identifies a multi-line block already being present; for a
    single line the text is its own marker. SessionStart registers no matcher, so it fires
    on `startup`, `resume`, `clear`, `compact` and `fork` alike — a blind append added the
    same content once per compaction for the life of the session, which is what
    ``GUARD_REFS_DIR`` did before this check existed.
    """
    env_file = os.environ.get("CLAUDE_ENV_FILE", "").strip()
    if not env_file:
        return False
    needle = marker if marker is not None else text
    try:
        path = Path(env_file)
        if path.is_file() and needle in path.read_text(encoding="utf-8"):
            return False
        with path.open("a", encoding="utf-8") as fh:
            fh.write(text + "\n")
    except OSError:
        return False
    return True


def _default_paused(config: dict) -> tuple[bool, bool]:
    """The two mutes a session with no state of its own opens in, as ``(turn, plan)``.

    The baseline the `/clear` handoff is judged against: a session sitting on exactly these
    has nothing to hand over, because its replacement reads the same config and lands on the
    same pair without being told.
    """
    return (not _audit_on(config, AUDIT_TURN_KEY), not _audit_on(config, AUDIT_PLAN_KEY))


def cmd_session_end() -> int:
    """SessionEnd, matched on ``clear`` — hand this session's switches to its replacement.

    `/clear` starts a NEW session with a new id, so `state/<sid>.json` no longer applies and
    both switches would go back to the project's `audit-turn` / `audit-plan` defaults: the user
    who muted guard a minute ago has to mute it again, with nothing saying why. This is the one
    boundary where that is worth fixing, because it is the one boundary where a new session is
    not a new intention — the conversation was cleared, the work was not.

    **Why this event, and not an inference in SessionStart.** `SessionStart` with
    `source: "clear"` says the session was born from a clear but names no predecessor (measured
    payload keys: `cwd`, `hook_event_name`, `session_id`, `source`, `transcript_path`). Picking
    the predecessor by recency instead is wrong the moment two sessions run in one project. So
    the ENDING session writes the record and names itself; `SessionEnd` carries `reason:
    "clear"` and the old `session_id`, and fires 55ms before the replacing `SessionStart`
    (measured 2026-08-26 in a live session; ordering is not documented, which is why it was
    measured and why this fails silent if it ever reverses).

    Nothing is written unless a switch differs from what this project configures — a session
    still sitting on its defaults has nothing to hand over, since the replacement reads the
    same config and arrives at the same two values on its own. That comparison, not "is
    anything armed", is what makes the record carry a MUTE as readily as it carries an arming:
    with `audit-turn` defaulting to on, a `guard off` before a `/clear` is precisely the
    intention most likely to be lost. A stale record from a previous clear is removed when
    there is nothing to carry, rather than left to be read later.

    NOT handed over: `plan_audited_hash`. The plan a cleared session had audited is gone from
    the conversation that approved it, so the gate should audit again rather than wave through
    a plan on the strength of a review nobody in this session saw.
    """
    if _HOST_IS_CODEX:
        return 0
    project_dir = _project_dir()
    if project_dir is None:
        return 0
    payload = _read_payload()
    if payload is None:
        return 0
    # The matcher already filters this, so the test is defence against a future registration
    # without one: every other reason (`logout`, `prompt_input_exit`, `resume`, `other`) ends
    # a session that is not being replaced, and inheriting into the next unrelated session is
    # exactly the persistent gate this must not become.
    if payload.get("reason") != "clear":
        return 0
    sid = _session_id(payload)
    if sid is None:
        return 0

    handoff = _clear_handoff_file(project_dir)
    config = _load_config(project_dir)
    state = _read_state(project_dir, sid, config)
    audit_paused = _audit_paused(state)
    plan_paused = _plan_audit_paused(state)
    if (audit_paused, plan_paused) == _default_paused(config):
        try:
            handoff.unlink()
        except OSError:
            pass
        _trace(project_dir, sid, "session-end", "clear_nothing_to_carry")
        return 0

    record = {
        "from_session": sid,
        "audit_paused": audit_paused,
        "plan_audit_paused": plan_paused,
        "written_at": time.time(),
    }
    try:
        handoff.parent.mkdir(parents=True, exist_ok=True)
        tmp = handoff.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
        tmp.replace(handoff)
    except OSError:
        return 0
    _trace(project_dir, sid, "session-end", "clear_handoff_written",
           audit_paused=audit_paused, plan_audit_paused=plan_paused)
    return 0


def _consume_clear_handoff(project_dir: Path, config: dict, payload: dict | None) -> dict | None:
    """On a `source: "clear"` SessionStart, adopt the ended session's switches. Once.

    Returns what was carried, for the line that says so out loud — an inheritance nobody is
    told about is the invisible gate, and being told is the whole difference. Returns None when
    there is nothing to carry, which is the ordinary case.

    The record is deleted whether or not it is used: single use is what stops one clear's
    choice from reaching a second clear, and the expiry
    (``CLEAR_INHERIT_MAX_AGE_SECONDS``) covers a record whose reader never ran.
    """
    if _HOST_IS_CODEX or payload is None:
        return None
    if payload.get("source") != "clear":
        return None
    sid = _session_id(payload)
    if sid is None:
        return None
    handoff = _clear_handoff_file(project_dir)
    try:
        raw = handoff.read_text(encoding="utf-8")
    except OSError:
        return None
    # Read once, then gone, regardless of what happens below.
    try:
        handoff.unlink()
    except OSError:
        pass
    try:
        record = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return None
    if not isinstance(record, dict):
        return None
    if record.get("from_session") == sid:
        # The session cannot inherit from itself; a record naming this id means the id was
        # reused, and applying it would be a no-op at best.
        return None
    written = record.get("written_at")
    if not isinstance(written, (int, float)):
        return None
    if time.time() - written > CLEAR_INHERIT_MAX_AGE_SECONDS:
        _trace(project_dir, sid, "session-start", "clear_handoff_expired")
        return None
    audit_paused = record.get("audit_paused")
    plan_paused = record.get("plan_audit_paused")
    if not isinstance(audit_paused, bool) or not isinstance(plan_paused, bool):
        return None
    if (audit_paused, plan_paused) == _default_paused(config):
        # The record says exactly what this session would have opened in anyway — either the
        # config changed between the two sessions, or the writer's check and this one
        # disagree. Nothing to apply, and nothing to announce.
        return None

    state = _read_state(project_dir, sid, config)
    state["audit_paused"] = audit_paused
    state["plan_audit_paused"] = plan_paused
    _write_state(project_dir, sid, state)
    # Confirm by reading back: `_write_state` swallows OSError by design, and a line saying
    # the switches were carried over a write that failed is worse than no line at all.
    check = _read_state(project_dir, sid, config)
    if _audit_paused(check) != audit_paused or _plan_audit_paused(check) != plan_paused:
        _trace(project_dir, sid, "session-start", "clear_handoff_write_failed")
        return None
    _trace(project_dir, sid, "session-start", "clear_handoff_applied",
           audit_paused=audit_paused, plan_audit_paused=plan_paused)
    return {"audit_paused": audit_paused, "plan_audit_paused": plan_paused}


def cmd_session_start() -> int:
    # Sweep both state and logs on the same age policy. State is intentionally NOT
    # cleared at SessionEnd: a session can be resumed later (`claude --resume`), and
    # its switch flags must survive the gap. Age-based expiry is the
    # only reaper, so a resumed session keeps its state as long as it is touched
    # within the retention window.
    project_dir = _project_dir()
    if project_dir is None:
        return 0
    # Once, here: stdin is readable one time, and two things below need this payload — the
    # mute line and the `/clear` handoff, which keys off `source`.
    payload = _read_payload()
    # Before the sweep: the sweep can fail on a filesystem error, and this export is what
    # keeps the CLI verbs off their inferred fallback for the rest of the session.
    exported = _export_to_bash_env("GUARD_PROJECT_DIR", str(project_dir))
    root = _state_root(project_dir)
    cutoff = time.time() - ORPHAN_MAX_AGE_SECONDS
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
    # `trace.log` sits at the root, not under `state/`, so the loop above never reached it
    # and the log grew without bound — the same way `extracts` did, and found the same way.
    # What the age policy buys here is narrower than it looks: every trace write refreshes
    # the mtime, so this reaps a log left behind by a project that has stopped tracing, and
    # never one being actively written. Bounding a live log needs a size check, which this
    # is not.
    trace = _trace_file(project_dir)
    try:
        if trace.is_file() and trace.stat().st_mtime < cutoff:
            trace.unlink()
    except OSError:
        pass
    # Dir-per-session trees. Swept on the directory's own mtime, never on its name: an
    # extract directory is named from `--session` when the caller passes one and from the
    # transcript's filename when it does not, so nothing here may assume the name is a
    # session id. `extracts` was missing from this sweep and grew without bound — the
    # agents that extract history write there on every audit, and guard runs in other
    # people's repositories, where a directory nothing reaps is a directory nobody asked
    # for.
    for sub in ("turns", "extracts"):
        sub_root = root / sub
        if not sub_root.is_dir():
            continue
        try:
            sess_dirs = list(sub_root.iterdir())
        except OSError:
            continue
        for d in sess_dirs:
            try:
                if not (d.is_dir() and d.stat().st_mtime < cutoff):
                    continue
                # One level of children only, which is all either tree has. rmdir then
                # fails on a dir holding anything deeper rather than deleting blind.
                for child in d.iterdir():
                    try:
                        child.unlink()
                    except OSError:
                        pass
                d.rmdir()
            except OSError:
                pass
    # The resolved refs directory, so a Bash caller gets it with one `echo` instead of
    # re-deriving the `refs_dir` validation from the raw config.
    session_cfg = _load_config(project_dir)
    refs = _refs_dir(project_dir, session_cfg)
    _export_to_bash_env("GUARD_REFS_DIR", str(refs))

    # The CLI behind the shell toggle. `CLAUDE_PLUGIN_ROOT` is given to hook processes and
    # substituted into command bodies, but it is NOT in the Bash tool's environment, so a
    # shell wrapper has no way to find this script — and its path is not guessable: the
    # marketplace installs the plugin under a versioned cache directory. Exporting the
    # resolved path is what makes `guard on` from a prompt possible at all.
    #
    # The shell commands go on PATH beside it, appended once per session to the same file.
    _export_to_bash_env("GUARD_TOGGLE_CLI", str(_plugin_root() / CLI_REL))
    _add_shell_command_to_path()

    # A `/clear` is the one boundary where a new session is not a new intention, so the
    # switches the ended session was carrying are adopted here — before the lines below,
    # which read the state this may have just written. Said out loud, because an inheritance
    # nobody is told about is the invisible gate that was deleted.
    carried = _consume_clear_handoff(project_dir, session_cfg, payload)
    if carried:
        # Both switches, in both directions. The record only exists because one of them
        # differs from this project's setting, and that difference can be either way now that
        # the settings default to on — so a line naming only the armed ones would go silent on
        # exactly the case it was added for, a mute carried across a `/clear`.
        parts = [
            "audits are " + ("OFF" if carried["audit_paused"] else "ON"),
            "plan audits are " + ("OFF" if carried["plan_audit_paused"] else "ON"),
        ]
        print(
            "guard: carried the previous session's switches across the /clear — "
            f"{' and '.join(parts)} for this session, whatever this project's settings say. "
            "`guard` / `guard-plan` in a shell change either. Do not mention this unless the "
            "user asks."
        )

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

    # Name the closeout file once, at the session's opening, when guard has anything switched
    # on. The Stop hook repeats the path on each routed turn — one line, and it must,
    # because context compaction can drop this one — but stating it here is what lets that
    # line stay a path instead of an explanation of what the file is for.
    if any(_switch_on(session_cfg, k) for k in SETTABLE_AGENTS):
        # Which of the two lines goes out is the mute, not the switches. Saying "audits are
        # on" to a muted session would be false in the one place a false line is most
        # expensive: nothing later in the session contradicts it, so the model spends the
        # session expecting a recommendation that never comes.
        if _session_muted(project_dir, session_cfg, payload):
            print(
                "guard: agents are configured for this project, but audits are OFF for this "
                "session — nothing is recommended when a turn ends and no answer file is "
                "named. Running `guard on` in a shell arms it for this session only. Do not "
                "mention this unless the user asks."
            )
        else:
            print(
                "guard: audits are on for this session. When a turn finishes, guard names the "
                "agents to consider; how to dispatch each one comes with that naming, and what "
                f"its findings mean comes from its own report. {_closeout_path()} says how a "
                "routed turn is closed out afterwards — do not read it until a turn sends you "
                "there."
            )

    _trace(project_dir, None, "session-start", "swept", exported_project_dir=exported)
    return 0
