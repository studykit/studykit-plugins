"""``settings`` and ``refs-dir`` — the CLI verbs, not hook events.

``settings`` is run by the ``guard:settings`` skill via Bash, in-session. ``show`` prints the
current settings; ``set <key> <value>`` changes one of the per-agent settings — each named
after the agent it controls, valued ``off``/``fresh`` — one of the two audit
switches (``audit-turn`` / ``audit-plan``, ``on``/``off``) or ``refs_dir``; ``unset <key>`` removes a key from the file entirely, back to its default. The
agent settings and the audit switches also apply to the live session's ``state/<sid>.json``
when a session id is
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
    AUDIT_PLAN_KEY, AUDIT_SWITCHES, AUDIT_TURN_KEY, AgentMode, DEFAULT_CONFIG, _agent_mode,
    _audit_on, _cli_write_allowed, _load_config, _load_raw_config, _parse_mode, _parse_switch,
    _write_config
)
from .paths import _cli_project_dir, _refs_dir, _trace
from .agents import AUDIT_AGENTS, SETTABLE_AGENTS
from .state import _audit_paused, _plan_audit_paused, _read_state, _write_state


# Which session-state key each audit switch seeds, and the shell command that moves it for one
# session. The state key is the switch INVERTED — the config says armed, the state says paused —
# and that inversion is why this mapping is written down once rather than open-coded per call
# site: a `set audit-turn off` that wrote `audit_paused = False` would report the change the
# user asked for and apply its opposite.
_SWITCH_STATE_KEY = {AUDIT_TURN_KEY: "audit_paused", AUDIT_PLAN_KEY: "plan_audit_paused"}


_SWITCH_COMMAND = {AUDIT_TURN_KEY: "guard", AUDIT_PLAN_KEY: "guard-plan"}


# And how each one is read back out of a state dict, since the two accessors are what hold the
# "missing key means armed" rule.
_SWITCH_PAUSED = {AUDIT_TURN_KEY: _audit_paused, AUDIT_PLAN_KEY: _plan_audit_paused}


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
    for them. No-op without a session id.

    ``key`` is the STATE key, which for the two audit switches is not the config key and is
    inverted from it — see ``_SWITCH_STATE_KEY``."""
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
    # state until something writes one, so `_read_state` on a session with no file yet returns
    # the config-seeded values — which is exactly what the audit lines below want to compare
    # against. Gating this on the file existing would have made every never-toggled session
    # report no session value at all.
    state = _read_state(project_dir, session_id, cfg) if session_id else None

    def switch_line(key: str) -> str:
        default = _agent_mode(cfg, key)
        live = _agent_mode(state, key) if state is not None else default
        if live != default:
            return f"{key}: {live} (this session; default {default})"
        return f"{key}: {default}"

    def audit_line(key: str) -> str:
        """One audit switch: the project's setting, and the live session's value when it
        differs. Both halves are needed and neither substitutes for the other — the setting is
        what a `set` here changes, the session value is what the user is actually getting, and
        the shell toggle can put them out of step for the rest of the session."""
        default = _audit_on(cfg, key)
        live = default if state is None else not _SWITCH_PAUSED[key](state)
        cmd = _SWITCH_COMMAND[key]
        if live != default:
            return (f"{key}: {'on' if live else 'off'} (this session; project setting "
                    f"{'on' if default else 'off'}) — `{cmd} {'off' if live else 'on'}` in a "
                    f"shell undoes that")
        if not live:
            return (f"{key}: off — `{cmd} on` arms this session without changing the "
                    f"setting")
        return f"{key}: on"

    refs_rel = raw.get("refs_dir") if isinstance(raw.get("refs_dir"), str) else ""
    # The two audit switches are listed FIRST: each overrides every agent line below it, so a
    # reader who sees the switches without them would read the wrong answer to "is guard
    # running". Always listed, unlike the old mute line, which appeared only while muted —
    # armed is now the default, and a state that is never printed is a state the reader has no
    # way to tell from a guard that does not have it.
    return [
        *(audit_line(k) for k in AUDIT_SWITCHES),
        *(switch_line(k) for k in SETTABLE_AGENTS),
        "refs_dir: " + (refs_rel if refs_rel else "(default wiki/ref/)"),
    ]


def _settings_unset(project_dir: Path, session_id: str | None,
                    positional: list[str]) -> int:
    """``settings unset <key>`` — delete one key from guard.local.json.

    Deleting an agent switch is a change to what guard does, not just to the file, so it
    goes through the same step a ``set`` does: the session's cached mode is reset to the
    default. Deleting a key guard does not honor touches neither.
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

    if key in SETTABLE_AGENTS:
        after = AgentMode(DEFAULT_CONFIG[key])
        _apply_session_scalar(project_dir, session_id, key, after.value)
    elif key in AUDIT_SWITCHES:
        # Same as a `set` to the default: removing the key changes what guard does now, not
        # only what the next session opens in, so the live session follows it back.
        on = _parse_switch(str(DEFAULT_CONFIG[key])) is True
        _apply_session_scalar(project_dir, session_id, _SWITCH_STATE_KEY[key], not on)
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
    _trace(project_dir, session_id, "settings", "unset", key=key, known=known)
    return 0


def cmd_settings() -> int:
    """View/change guard.local.json settings — the CLI behind the ``guard:settings`` skill.

        settings [show]                      — print the current settings
        settings set <key> <value>           — change one setting
        settings unset <key>                 — delete one key from the file

    Settable keys: the two audit switches (``AUDIT_SWITCHES``), the agent switches (the keys
    of ``SETTABLE_AGENTS`` — each is the name of the agent it admits) and ``refs_dir``. The
    switches
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

    if key in SETTABLE_AGENTS:
        v = _parse_mode(value)
        if v is None:
            print(f"guard settings: {key} must be one of "
                  f"{[m.value for m in AgentMode]} (got {value!r})", file=sys.stderr)
            return 0
        raw[key] = v.value
        _apply_session_scalar(project_dir, session_id, key, v.value)
    elif key in AUDIT_SWITCHES:
        on = _parse_switch(value)
        if on is None:
            print(f"guard settings: {key} must be `on` or `off` (got {value!r})",
                  file=sys.stderr)
            return 0
        raw[key] = "on" if on else "off"
        # The live session moves with it, inverted into the state's paused key. Without this a
        # user who just turned auditing off would keep being audited for the rest of the
        # session, having been shown a line that says it is off.
        _apply_session_scalar(project_dir, session_id, _SWITCH_STATE_KEY[key], not on)
    elif key == "refs_dir":
        raw["refs_dir"] = value  # "" resets to the default; _refs_dir validates at use
    else:
        print(f"guard settings: unknown or unsettable key {key!r}. Settable: "
              + ", ".join((*AUDIT_SWITCHES, *SETTABLE_AGENTS))
              + ", refs_dir.",
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

    A CLI verb, so `_cli_project_dir`. On `_project_dir` it printed NOTHING to every caller
    it has — the Bash environment has no `CLAUDE_PROJECT_DIR` to find — which is not a
    fail-open, since the whole verb is the answer it was asked for.
    """
    project_dir = _cli_project_dir()
    print(_refs_dir(project_dir, _load_config(project_dir)))
    return 0
