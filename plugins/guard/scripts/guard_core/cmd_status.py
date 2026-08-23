"""``toggle`` and ``status`` — the session mute, and the indicator that makes it visible.

``toggle`` (UserPromptExpansion, for ``/guard:toggle [on|off]``) arms or mutes the automatic
audit for THIS SESSION — ``audit_paused`` in the session state, never guard.local.json, so it
cannot change what the project does by default. A session STARTS muted
(``state._read_state``), which makes ``on`` the common direction: it clears the pause and is
the only thing that ever does. An empty argument flips. While muted, ``stop`` recommends
nothing and ``user-prompt`` names no answer file, but the pending target and the answer file
are still recorded — the Codex adapter reads that marker. The hook does the work and prints
the resulting state; the command file only relays it.

``status`` (CLI, stdin JSON) is the other half, and starting muted is what makes it
load-bearing rather than a convenience: the mute is a feature only because it is visible, and
now it is the state every session opens in. It prints one short field — ``guard <n>`` armed / ``guard off`` muted / ``guard ·``
nothing switched on — or NOTHING on any failure, because its stdout goes straight into the
user's status bar. A plugin cannot own the main ``statusLine``, so the user composes this
segment into theirs (``/guard:statusline`` offers to do it). It reads only the small config
and state files, nothing else: it runs on every assistant message. Not a hook event.
"""

from __future__ import annotations

import json
import os
import sys

from pathlib import Path

from .config import _load_config, _switch_on
from .paths import _project_dir, _trace
from .payload import _read_payload, _session_id
from .emit import _emit_expansion
from .agents import AUDIT_AGENTS
from .state import _audit_paused, _read_state, _write_state


# Status-line colours. Dim for the state guard chose not to shout about, green for armed,
# yellow for muted — the one state the user set and can forget. Kept as constants because a
# status line that emits a stray escape sequence garbles the user's terminal row.
_ANSI_RESET = "\033[0m"


_ANSI_ARMED = "\033[32m"


_ANSI_MUTED = "\033[33m"


_ANSI_IDLE = "\033[2m"


def cmd_toggle() -> int:
    """UserPromptExpansion for `/guard:toggle [on|off]`. Mute or unmute this session.

    The hook does the work rather than telling the model to: `command_args` carries the
    argument (hooks docs, excerpt in the refs dir as `claude-code-statusline.md`), so no
    argument means flip, `on`/`off` set it outright, and the outcome does not depend on a
    model reading a procedure correctly.

    Session state only. It cannot touch guard.local.json, which is what makes this safe to
    reach for mid-conversation: it cannot change what any other session does. And since every
    session starts muted, an `off` here is not undone by the next session either — there is
    nothing this can leave behind. `on` means auditing on, so it CLEARS the pause — the
    user's vocabulary is about guard, not about the flag's name.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None:
        return 0
    # Not silent, unlike every other guard failure. A hook that prints nothing lets the model
    # report the mute it was asked for and never got — the same shape as the crashed toggle
    # this project has already seen narrated as success. The two neighbouring branches (no
    # session id, unrecognised argument) say so out loud for the same reason.
    if project_dir is None:
        _emit_expansion(
            "guard: no project directory resolved, so there is no session state to write. "
            "Nothing changed — say so in one line rather than reporting the mute."
        )
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        _emit_expansion("guard: no usable session id, so there is no session to mute.")
        return 0

    arg = payload.get("command_args")
    arg = arg.strip().lower() if isinstance(arg, str) else ""
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    if arg in ("", "flip", "toggle"):
        paused = not _audit_paused(state)
    elif arg in ("on", "resume", "enable"):
        paused = False
    elif arg in ("off", "pause", "disable", "mute"):
        paused = True
    else:
        _emit_expansion(
            f"guard: `{arg}` is not an argument for /guard:toggle — use `on`, `off`, or "
            "nothing to flip. Nothing changed; say so in one line."
        )
        return 0

    state["audit_paused"] = paused
    _write_state(project_dir, session_id, state)
    armed = [k for k in AUDIT_AGENTS if _switch_on(state, k)]

    if paused:
        msg = ("guard: audits are OFF for this session. Nothing is recommended when a turn "
               "ends, and answers are no longer written to a file. `/guard:toggle on` arms "
               "it again and the project's own settings are untouched.")
    elif armed:
        msg = ("guard: audits are ON for this session — "
               + ", ".join(f"`{k}`" for k in armed) + ". They stay on until this session "
               "ends; the next one starts muted again. Nothing else changed.")
    else:
        # Not "nothing will run": `ext-docs-auditor` has no switch, so a turn that writes a
        # saved reference is still named at Stop with every agent off. Overstating the silence
        # here is how a user reads that dispatch as guard ignoring their settings.
        msg = ("guard: no longer muted, but every agent switch is `off` for this project, so "
               "no audit of the turn itself will run — only a saved reference the turn writes "
               "is still checked. `/guard:settings` is where you switch one on.")
    _emit_expansion(msg + " Relay this in one line and do nothing else.")
    _trace(project_dir, session_id, "toggle", "set", arg=arg or "flip", paused=paused)
    return 0


def cmd_status() -> int:
    """Status-line segment: is guard auditing this session? Reads stdin, prints one field.

    A plugin cannot install the MAIN status line — only `agent` and `subagentStatusLine` are
    honored in a plugin's settings.json — so this prints a segment the user composes into
    whatever status line they already run. The excerpt is saved in the refs dir as
    `claude-code-statusline.md`.

    Two documented constraints shape the body. It runs on every assistant message, debounced
    at 300ms, and a newer update cancels the one in flight: so it reads only the small
    config and state JSON files and does nothing else — no git, no transcript, no subprocess.
    And its stdout goes
    straight into the user's status bar: so every failure prints NOTHING rather than an
    error message, because a status line is the one place guard must never shout from.
    """
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError, OSError, UnicodeDecodeError):
        return 0
    if not isinstance(payload, dict):
        return 0

    # The status-line payload names the launch directory, which is where guard's state hangs
    # off. `CLAUDE_PROJECT_DIR` is the fallback so the same command works when a user wires
    # it into a script that does not forward the JSON.
    ws = payload.get("workspace")
    root = ws.get("project_dir") if isinstance(ws, dict) else None
    for cand in (root, payload.get("cwd"), os.environ.get("CLAUDE_PROJECT_DIR")):
        if isinstance(cand, str) and cand.strip():
            root = cand.strip()
            break
    else:
        return 0
    session_id = _session_id(payload)
    if not isinstance(root, str) or session_id is None:
        return 0

    try:
        project_dir = Path(root)
        state = _read_state(project_dir, session_id, _load_config(project_dir))
    except Exception:
        return 0

    armed = [k for k in AUDIT_AGENTS if _switch_on(state, k)]
    if _audit_paused(state):
        # Muted is the state worth a colour: the user chose it and can forget it.
        print(f"{_ANSI_MUTED}guard off{_ANSI_RESET}")
    elif armed:
        print(f"{_ANSI_ARMED}guard {len(armed)}{_ANSI_RESET}")
    else:
        # Nothing switched on for this project: not an error and not something the user did
        # this session, so it gets a dot rather than a word — "installed, idle" without
        # asking for attention on every redraw.
        print(f"{_ANSI_IDLE}guard ·{_ANSI_RESET}")
    return 0
