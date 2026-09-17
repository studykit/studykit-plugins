#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Herdr presentation and actions for Guard's file checkpoint queue."""

from __future__ import annotations

import curses
import json
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def _context() -> dict[str, Any]:
    try:
        value = json.loads(os.environ.get("HERDR_PLUGIN_CONTEXT_JSON", "{}"))
    except (TypeError, ValueError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _herdr(*args: str) -> dict[str, Any]:
    binary = os.environ.get("HERDR_BIN_PATH") or "herdr"
    try:
        result = subprocess.run([binary, *args], capture_output=True, check=True,
                                text=True, timeout=10)
        value = json.loads(result.stdout)
    except (OSError, subprocess.SubprocessError, ValueError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _target_pane() -> str:
    context = _context()
    return (os.environ.get("GUARD_TARGET_PANE_ID")
            or str(context.get("focused_pane_id") or "")
            or os.environ.get("HERDR_PANE_ID", ""))


def _pane() -> dict[str, Any]:
    pane_id = _target_pane()
    result = _herdr("pane", "get", pane_id) if pane_id else {}
    pane = result.get("result", {}).get("pane", {}) if isinstance(result.get("result"), dict) else {}
    return pane if isinstance(pane, dict) else {}


def _checkpoint_script() -> Path:
    return (Path(os.environ["HERDR_PLUGIN_ROOT"]) / "skills" / "audit-files" /
            "scripts" / "checkpoint.py")


def _checkpoint(pane: dict[str, Any], *args: str) -> dict[str, Any]:
    session = pane.get("agent_session")
    session_id = session.get("value") if isinstance(session, dict) else ""
    host = pane.get("agent")
    cwd = pane.get("foreground_cwd") or pane.get("cwd")
    if host not in ("claude", "codex") or not isinstance(session_id, str) or not session_id:
        return {"error": "The focused pane has no Guard-compatible agent session."}
    if not isinstance(cwd, str) or not cwd:
        return {"error": "Herdr could not resolve the focused pane's project directory."}
    env = dict(os.environ)
    env["GUARD_PROJECT_DIR"] = cwd
    try:
        result = subprocess.run(
            [str(_checkpoint_script()), *args, "--host", host, "--session", session_id],
            capture_output=True, check=True, text=True, timeout=15, cwd=cwd, env=env,
        )
        value = json.loads(result.stdout)
    except (OSError, subprocess.SubprocessError, ValueError, json.JSONDecodeError):
        return {"error": "Guard's pending queue could not be updated."}
    return value if isinstance(value, dict) else {}


def _pending() -> tuple[dict[str, Any], dict[str, Any]]:
    pane = _pane()
    return pane, _checkpoint(pane, "show")


def _prompt_audit(pane: dict[str, Any], token: str | None = None) -> bool:
    pane_id = pane.get("pane_id")
    host = pane.get("agent")
    if not isinstance(pane_id, str) or host not in ("claude", "codex"):
        return False
    prompt = "/guard:audit-files" if host == "claude" else "$guard:audit-files"
    if token:
        prompt += f" --token {token}"
    result = _herdr("agent", "prompt", pane_id, prompt)
    return bool(result.get("result"))


def show_action() -> int:
    pane = _pane()
    pane_id = pane.get("pane_id")
    cwd = pane.get("foreground_cwd") or pane.get("cwd")
    if not isinstance(pane_id, str) or not pane_id:
        return 1
    # Popup placement and dimensions belong to the manifest. Herdr 0.9.1 rejects a popup
    # override through this CLI and requires modal panes to target the active pane implicitly.
    args = ["plugin", "pane", "open", "--plugin", os.environ["HERDR_PLUGIN_ID"],
            "--entrypoint", "pending-files",
            "--env", f"GUARD_TARGET_PANE_ID={pane_id}", "--focus"]
    if isinstance(cwd, str) and cwd:
        args.extend(["--cwd", cwd])
    return 0 if _herdr(*args).get("result") else 1


def audit_action() -> int:
    return 0 if _prompt_audit(_pane()) else 1


def _editor_command(path: str) -> list[str] | None:
    """Resolve a terminal editor without involving a shell."""
    configured = os.environ.get("VISUAL") or os.environ.get("EDITOR")
    if configured:
        try:
            command = shlex.split(configured)
        except ValueError:
            command = []
        if command and shutil.which(command[0]):
            return [*command, path]
    for candidate in ("nvim", "vim", "vi"):
        if shutil.which(candidate):
            return [candidate, path]
    return None


def _file_rows(pane: dict[str, Any], pending: dict[str, Any]
               ) -> tuple[Path, list[tuple[str, str, str]]]:
    """Return ``(absolute path, display path, reviewer)`` rows."""
    project = Path(str(pane.get("foreground_cwd") or pane.get("cwd") or "."))
    reviewers: dict[str, list[str]] = {}
    groups = pending.get("groups")
    if isinstance(groups, list):
        for group in groups:
            if not isinstance(group, dict):
                continue
            name = group.get("name")
            paths = group.get("paths")
            if not isinstance(name, str) or not isinstance(paths, list):
                continue
            for path in paths:
                if isinstance(path, str):
                    reviewers.setdefault(path, []).append(name)
    files = pending.get("files")
    rows: list[tuple[str, str, str]] = []
    if isinstance(files, dict):
        for raw in files:
            try:
                label = Path(raw).relative_to(project).as_posix()
            except ValueError:
                label = raw
            rows.append((raw, label, ", ".join(reviewers.get(raw, ()))))
    return project, rows


def _put(screen: Any, y: int, x: int, text: str, style: int = 0) -> None:
    """Draw within the terminal; tiny popups should degrade rather than crash."""
    height, width = screen.getmaxyx()
    if y < 0 or y >= height or x < 0 or x >= width:
        return
    try:
        screen.addnstr(y, x, text, max(0, width - x - 1), style)
    except curses.error:
        pass


def _open_editor(screen: Any, path: str) -> str:
    command = _editor_command(path)
    if command is None:
        return "No terminal editor found. Set $VISUAL or $EDITOR."
    if not Path(path).is_file():
        return "That file no longer exists; refresh the queue."
    try:
        curses.def_prog_mode()
        curses.endwin()
        result = subprocess.run(command, cwd=str(Path(path).parent), check=False)
        message = ("Returned from editor." if result.returncode == 0 else
                   f"Editor exited with status {result.returncode}.")
    except OSError as error:
        message = f"Could not start editor: {error}."
    finally:
        try:
            curses.reset_prog_mode()
            screen.keypad(True)
            curses.curs_set(0)
            screen.clear()
            screen.refresh()
        except curses.error:
            pass
    return message


def _confirm_clear(screen: Any, count: int) -> bool:
    height, width = screen.getmaxyx()
    noun = "file" if count == 1 else "files"
    prompt = f" Clear {count} selected {noun}?  y confirm · any other key cancel "
    _put(screen, height - 2, 0, prompt.ljust(max(0, width - 1)),
         curses.color_pair(4) | curses.A_REVERSE | curses.A_BOLD)
    screen.refresh()
    try:
        return screen.get_wch() in ("y", "Y")
    except (curses.error, KeyboardInterrupt):
        return False


def _panel(screen: Any) -> int:
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    screen.keypad(True)
    try:
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_CYAN, -1)
        curses.init_pair(2, curses.COLOR_GREEN, -1)
        curses.init_pair(3, curses.COLOR_YELLOW, -1)
        curses.init_pair(4, curses.COLOR_RED, -1)
    except curses.error:
        pass

    selected = 0
    scroll = 0
    marked: set[str] = set()
    message = ""
    pane, pending = _pending()
    while True:
        project, rows = _file_rows(pane, pending)
        row_paths = {row[0] for row in rows}
        marked.intersection_update(row_paths)
        selected = min(selected, max(0, len(rows) - 1))
        height, width = screen.getmaxyx()
        visible = max(1, height - 8)
        if selected < scroll:
            scroll = selected
        elif selected >= scroll + visible:
            scroll = selected - visible + 1

        screen.erase()
        title = " Guard  ·  Pending audits "
        _put(screen, 0, 0, title.ljust(max(0, width - 1)), curses.A_REVERSE | curses.A_BOLD)
        agent = str(pane.get("agent") or "no agent")
        _put(screen, 2, 2, f"{project}  ·  {agent}", curses.A_DIM)
        status = f"{len(rows)} pending  ·  {len(marked)} selected"
        _put(screen, 3, 2, status,
             curses.color_pair(2) | curses.A_BOLD)

        error = pending.get("error")
        if isinstance(error, str):
            _put(screen, 5, 4, "! " + error, curses.color_pair(4) | curses.A_BOLD)
        elif not rows:
            _put(screen, 5, 4, "✓ Nothing is waiting for an audit checkpoint.",
                 curses.color_pair(2))
        else:
            for offset, (path, label, reviewer) in enumerate(rows[scroll:scroll + visible]):
                index = scroll + offset
                cursor = "›" if index == selected else " "
                checkbox = "[x]" if path in marked else "[ ]"
                reviewer_text = f"  ·  {reviewer}" if reviewer else ""
                line = f" {cursor} {checkbox} {label}{reviewer_text}"
                style = (curses.A_REVERSE | curses.A_BOLD if index == selected
                         else (curses.color_pair(3) if path in marked
                               else curses.color_pair(1)))
                _put(screen, 5 + offset, 1, line.ljust(max(0, width - 3)), style)

        if message:
            _put(screen, height - 2, 2, message, curses.color_pair(3))
        footer = " ↑/↓ move   Space select   Enter open   a audit selected/all   c clear selected   r refresh   q close "
        _put(screen, height - 1, 0, footer.ljust(max(0, width - 1)), curses.A_REVERSE)
        screen.refresh()

        try:
            key = screen.get_wch()
        except (curses.error, KeyboardInterrupt):
            return 0
        if key in ("q", "Q", "\x1b"):
            return 0
        if key in (curses.KEY_UP, "k", "K") and rows:
            selected = (selected - 1) % len(rows)
            message = ""
        elif key in (curses.KEY_DOWN, "j", "J") and rows:
            selected = (selected + 1) % len(rows)
            message = ""
        elif key in (curses.KEY_HOME, "g") and rows:
            selected = 0
            message = ""
        elif key in (curses.KEY_END, "G") and rows:
            selected = len(rows) - 1
            message = ""
        elif key == " " and rows:
            path = rows[selected][0]
            if path in marked:
                marked.remove(path)
            else:
                marked.add(path)
            message = f"{len(marked)} file{'s' if len(marked) != 1 else ''} selected."
        elif key in (curses.KEY_ENTER, "\n", "\r") and rows:
            message = _open_editor(screen, rows[selected][0])
            pane, pending = _pending()
        elif key in ("a", "A"):
            token: str | None = None
            audit_count = len(rows)
            if marked:
                prepared = _checkpoint(
                    pane, "show", "--paths-json",
                    json.dumps(sorted(marked), ensure_ascii=False, separators=(",", ":")),
                )
                files = prepared.get("files")
                prepared_token = prepared.get("token")
                if prepared.get("error"):
                    message = str(prepared["error"])
                    continue
                if not isinstance(files, dict) or not files:
                    pane, pending = _pending()
                    message = "The selected files are no longer pending."
                    continue
                if not isinstance(prepared_token, str) or not prepared_token:
                    message = "Guard could not prepare the selected checkpoint."
                    continue
                token = prepared_token
                audit_count = len(files)
            if _prompt_audit(pane, token):
                scope = "selected" if token else "pending"
                message = (f"Requested an audit for {audit_count} {scope} "
                           f"file{'s' if audit_count != 1 else ''}.")
            else:
                message = "Could not prompt the agent; wait until it is idle and try again."
        elif key in ("c", "C"):
            if not rows:
                message = "The queue is already empty."
            elif not marked:
                message = "Select one or more files with Space first."
            elif not _confirm_clear(screen, len(marked)):
                message = "Clear cancelled."
            else:
                result = _checkpoint(
                    pane, "clear", "--paths-json",
                    json.dumps(sorted(marked), ensure_ascii=False, separators=(",", ":")),
                )
                if result.get("error"):
                    message = str(result["error"])
                else:
                    cleared = result.get("cleared", len(marked))
                    message = f"Cleared {cleared} pending file{'s' if cleared != 1 else ''}."
                    marked.clear()
                    scroll = 0
                    pane, pending = _pending()
        elif key in ("r", "R", curses.KEY_RESIZE):
            pane, pending = _pending()
            message = ("Queue refreshed." if not pending.get("error") else
                       "Refresh failed; see the message above.")
        else:
            message = "Use Space to select files, then a to audit or c to clear them."


def panel() -> int:
    if not (sys.stdin.isatty() and sys.stdout.isatty()):
        print("Guard's pending-files panel needs an interactive terminal.", file=sys.stderr)
        return 1
    return curses.wrapper(_panel)


if __name__ == "__main__":
    handlers = {"show-action": show_action, "audit-action": audit_action, "panel": panel}
    handler = handlers.get(sys.argv[1] if len(sys.argv) > 1 else "")
    raise SystemExit(handler() if handler else 2)
