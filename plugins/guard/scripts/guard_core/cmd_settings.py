"""``settings`` and ``refs-dir`` — the CLI verbs, not hook events.

``settings`` is run by the ``guard:settings`` skill via Bash, in-session. ``show`` prints the
current settings; ``set <key> <value>`` changes one of the per-agent settings — each named
after the agent it controls, valued ``off``/``fresh``/``reuse`` — or ``refs_dir``; ``unset <key>`` removes a key from the file entirely, back to its default. The
agent settings also apply to the live session's ``state/<sid>.json`` when a session id is
available (``--session``, which the skill passes as ``${CLAUDE_SESSION_ID}``, else the
inherited ``CLAUDE_CODE_SESSION_ID``); the rest are read from the config file at use. Every
other key is preserved. Mutating verbs require the settings-skill marker — see
``config._cli_write_allowed``.

``refs-dir`` prints the resolved refs directory, absolute, applying the ``refs_dir``
validation. Called via Bash by an audit agent's fallback and by the output style.
"""

from __future__ import annotations

import os
import sys

from pathlib import Path
from typing import Any

from .config import (
    AgentMode, DEFAULT_CONFIG, _agent_mode, _cli_write_allowed, _load_config,
    _load_raw_config, _parse_mode, _write_config
)
from .paths import _cli_project_dir, _refs_dir, _trace
from .agents import AUDIT_AGENTS, _instance_name
from .state import _audit_paused, _read_state, _write_state


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
    # Read the state whenever there is a session, file or not. The defaults ARE the session's
    # state until something writes one, and the mute is the key where that distinction shows:
    # a session starts muted, so gating this on the file existing hid the muted line on
    # exactly the sessions that had never been armed. The switch lines are unaffected — their
    # defaults come from the same config `cfg` does, so they still report no difference.
    state = _read_state(project_dir, session_id, cfg) if session_id else None

    def switch_line(key: str) -> str:
        default = _agent_mode(cfg, key)
        live = _agent_mode(state, key) if state is not None else default
        suffix = " — one instance for the session" if live is AgentMode.REUSE else ""
        if live != default:
            return f"{key}: {live} (this session; default {default}){suffix}"
        return f"{key}: {default}{suffix}"

    refs_rel = raw.get("refs_dir") if isinstance(raw.get("refs_dir"), str) else ""
    # The mute is listed first and only when it is on: it overrides every line below it, so a
    # reader who sees the switches without it would read the wrong answer to "is guard
    # running". It is session state, so there is no default to show alongside.
    muted = ["audits: OFF for this session (/guard:toggle on to arm it)"] if (
        state is not None and _audit_paused(state)) else []
    return [
        *muted,
        *(switch_line(k) for k in AUDIT_AGENTS),
        "refs_dir: " + (refs_rel if refs_rel else "(default wiki/ref/)"),
    ]


def _live_agent_mode(project_dir: Path, session_id: str | None,
                     cfg: dict[str, Any], key: str) -> AgentMode:
    """The mode ``key`` is running under right now — session state when there is a
    session, the config file otherwise. Read BEFORE a write, so the change can be
    reported."""
    return _agent_mode(_read_state(project_dir, session_id, cfg) if session_id else cfg, key)


def _mode_transition_note(key: str, before: AgentMode, after: AgentMode) -> str:
    """The note a mode change owes the session, or "" when it owes none.

    A mode change is the one setting change that leaves something behind: an instance the
    main agent may still be addressing. Nothing in guard can see or stop that instance —
    this CLI has no channel to it — so the change has to be reported to the session that
    can, and this text is that report. It reaches the main agent because the skill relays
    what the CLI printed.
    """
    if before is AgentMode.REUSE and after is not AgentMode.REUSE:
        return (f"guard: {key} is no longer reused. Stop sending to "
                f"`{_instance_name(key)}` — shut it down if your session offers a way to "
                f"— and from the next turn dispatch a new instance each time.")
    if after is AgentMode.REUSE and before is not AgentMode.REUSE:
        return (f"guard: {key} now runs as one instance for the session, named "
                f"`{_instance_name(key)}`. Dispatch it under that name once, then "
                f"SendMessage it on later turns instead of dispatching again.")
    return ""


def _settings_unset(project_dir: Path, session_id: str | None,
                    positional: list[str]) -> int:
    """``settings unset <key>`` — delete one key from guard.local.json.

    Deleting an agent switch is a change to what guard does, not just to the file, so it
    goes through the same two steps a ``set`` does: the session's cached mode is reset to
    the default and any reuse transition is reported. Deleting a key guard does not
    honor touches neither.
    """
    if not positional:
        print("guard settings: usage: settings unset <key>", file=sys.stderr)
        return 0
    key = positional[0]
    raw = _load_raw_config(project_dir)
    # Case-sensitive on purpose: this removes a key by its literal name in the file, and
    # a lowercased guess would miss the misspelled or foreign-cased key that is exactly
    # what someone reaches for this verb to clear.
    if key not in raw:
        print(f"guard settings: no key {key!r} in .claude/guard.local.json — nothing to "
              f"remove. Keys present: " + (", ".join(raw) if raw else "(none)"))
        _trace(project_dir, session_id, "settings", "unset_absent", key=key)
        return 0

    cfg = _load_config(project_dir)
    transition = ""
    if key in AUDIT_AGENTS:
        before = _live_agent_mode(project_dir, session_id, cfg, key)
        after = AgentMode(DEFAULT_CONFIG[key])
        _apply_session_scalar(project_dir, session_id, key, after.value)
        transition = _mode_transition_note(key, before, after)
    del raw[key]

    if not _write_config(project_dir, raw):
        print("guard settings: failed to write .claude/guard.local.json", file=sys.stderr)
        return 0

    known = key in DEFAULT_CONFIG
    # `str()` first: an `AgentMode` default would otherwise print as `<AgentMode.OFF: 'off'>`.
    print(f"guard: removed {key!r} — "
          + (f"back to the default ({str(DEFAULT_CONFIG[key])!r})." if known
             else "guard does not honor that key, so nothing changes."))
    print()
    for line in _config_show_lines(project_dir, session_id):
        print(line)
    if transition:
        print()
        print(transition)
    _trace(project_dir, session_id, "settings", "unset", key=key, known=known)
    return 0


def cmd_settings() -> int:
    """View/change guard.local.json settings — the CLI behind the ``guard:settings`` skill.

        settings [show]                      — print the current settings
        settings set <key> <value>           — change one setting
        settings unset <key>                 — delete one key from the file

    Settable keys: the agent switches (the keys of ``AUDIT_AGENTS`` — each is the name
    of the agent it admits) and ``refs_dir``. The switches
    also apply to the live session's ``state/<sid>.json`` when a session id is available
    (``--session <id>``, which the forked skill passes as ``${CLAUDE_SESSION_ID}``, else
    the inherited ``CLAUDE_CODE_SESSION_ID``) so the change takes effect at once and
    persists as the new default; the rest are read from the config file at use.
    ``set`` preserves every other key in the file. ``unset`` is the one way to remove a
    key, and it exists because that preservation has no other exit: a key guard stopped
    honoring (``exempt_skills``, ``audit_gate``) is invisible to ``show`` and survives
    every ``set`` forever, and the file may only be written through this CLI, so without
    this verb the only way to clear one is the hand-edit the skill forbids. It deletes
    any key, live or dead, rather than only the dead ones — guard cannot know which keys
    a newer version owns, so pruning on its own judgment would silently discard a
    downgraded user's config. Project dir from ``_cli_project_dir`` — the git root, not the
    cwd, or a `set` run from a subdirectory would write a second config file the session
    never reads."""
    positional, session_arg = _parse_settings_argv(sys.argv[2:])
    op = positional[0].lower() if positional else "show"

    project_dir = _cli_project_dir()
    session_id = session_arg or (os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip() or None)

    if op not in ("set", "unset"):
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

    if op == "unset":
        return _settings_unset(project_dir, session_id, positional[1:])

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
        before = _live_agent_mode(project_dir, session_id, cfg, key)
        raw[key] = v.value
        _apply_session_scalar(project_dir, session_id, key, v.value)
        transition = _mode_transition_note(key, before, v)
    elif key == "refs_dir":
        raw["refs_dir"] = value  # "" resets to the default; _refs_dir validates at use
    else:
        print(f"guard settings: unknown or unsettable key {key!r}. Settable: "
              + ", ".join(AUDIT_AGENTS)
              + ", refs_dir.",
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

    A CLI verb, so `_cli_project_dir`. On `_project_dir` it printed NOTHING to every caller
    it has — the Bash environment has no `CLAUDE_PROJECT_DIR` to find — which is not a
    fail-open, since the whole verb is the answer it was asked for.
    """
    project_dir = _cli_project_dir()
    print(_refs_dir(project_dir, _load_config(project_dir)))
    return 0
