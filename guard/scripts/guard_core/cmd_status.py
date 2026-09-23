"""Pending-file status plus compatibility output for the retired session mute.

``status`` prints ``guard N pending`` and the independent plan-gate flag. ``toggle-cli`` is
kept so an existing `guard on|off` shell command explains the checkpoint replacement instead
of failing silently.
"""

from __future__ import annotations

import json
import os
import sys

from pathlib import Path

from .config import _HOST_IS_CODEX, _load_config, _parse_switch
from .cmd_checkpoint import reconcile_queue
from .payload import _session_id
from .state import _plan_audit_paused, _read_state


# Status-line colours. Green means pending work or an armed plan gate; dim means empty or
# muted. Kept as constants because a stray escape sequence garbles the terminal row.
_ANSI_RESET = "\033[0m"


_ANSI_ARMED = "\033[32m"


_ANSI_IDLE = "\033[2m"


def _parse_toggle_arg(arg: str) -> str | None:
    """Shared on/off vocabulary for the still-active plan-gate command."""
    arg = arg.strip().lower()
    if arg in ("", "flip", "toggle"):
        return "flip"
    parsed = _parse_switch(arg)
    if parsed is None:
        return None
    return "on" if parsed else "off"


def cmd_toggle_cli() -> int:
    """Explain the retired automatic-audit mute to existing shell-command users."""
    print("guard: `guard on|off` is retired — edited files are queued without automatic "
          "Stop audits. Run `/guard:audit-files` at a checkpoint.")
    return 0


def cmd_status() -> int:
    """Print the pending-file count and plan-gate state for a composed status line.

    A plugin cannot install the MAIN status line — only `agent` and `subagentStatusLine` are
    honored in a plugin's settings.json — so this prints a segment the user composes into
    whatever status line they already run (`wiki/ref/claude-code-statusline.md`).

    The trailing plan flag is filled (`⚑`) when armed and outline (`⚐`) when muted.

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

    pending, _ = reconcile_queue(project_dir, state,
                                 "codex" if _HOST_IS_CODEX else "claude")
    # Always show one of the two same-width glyphs; absence would be indistinguishable from a
    # status integration that does not report the plan gate at all.
    if _plan_audit_paused(state):
        flag = f"{_ANSI_IDLE} · ⚐{_ANSI_RESET}"
    else:
        flag = f"{_ANSI_IDLE} · {_ANSI_RESET}{_ANSI_ARMED}⚑{_ANSI_RESET}"
    colour = _ANSI_ARMED if pending else _ANSI_IDLE
    turn = f"{colour}guard {len(pending)} pending{_ANSI_RESET}"
    print(f"{turn}{flag}")
    return 0
