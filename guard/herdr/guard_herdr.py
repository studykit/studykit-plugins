#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Herdr presentation and actions for Guard's file checkpoint queue."""

from __future__ import annotations

import json
import os
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


def _pending() -> tuple[dict[str, Any], dict[str, Any]]:
    pane = _pane()
    session = pane.get("agent_session")
    session_id = session.get("value") if isinstance(session, dict) else ""
    host = pane.get("agent")
    cwd = pane.get("foreground_cwd") or pane.get("cwd")
    if host not in ("claude", "codex") or not isinstance(session_id, str) or not session_id:
        return pane, {"error": "The focused pane has no Guard-compatible agent session."}
    if not isinstance(cwd, str) or not cwd:
        return pane, {"error": "Herdr could not resolve the focused pane's project directory."}
    env = dict(os.environ)
    env["GUARD_PROJECT_DIR"] = cwd
    try:
        result = subprocess.run(
            [str(_checkpoint_script()), "show", "--host", host, "--session", session_id],
            capture_output=True, check=True, text=True, timeout=15, cwd=cwd, env=env,
        )
        value = json.loads(result.stdout)
    except (OSError, subprocess.SubprocessError, ValueError, json.JSONDecodeError):
        return pane, {"error": "Guard's pending queue could not be read."}
    return pane, value if isinstance(value, dict) else {}


def _prompt_audit(pane: dict[str, Any]) -> bool:
    pane_id = pane.get("pane_id")
    host = pane.get("agent")
    if not isinstance(pane_id, str) or host not in ("claude", "codex"):
        return False
    prompt = "/guard:audit-files" if host == "claude" else "$guard:audit-files"
    result = _herdr("agent", "prompt", pane_id, prompt)
    return bool(result.get("result"))


def show_action() -> int:
    pane = _pane()
    pane_id = pane.get("pane_id")
    cwd = pane.get("foreground_cwd") or pane.get("cwd")
    if not isinstance(pane_id, str) or not pane_id:
        return 1
    args = ["plugin", "pane", "open", "--plugin", os.environ["HERDR_PLUGIN_ID"],
            "--entrypoint", "pending-files", "--placement", "popup",
            "--width", "80%", "--height", "70%", "--target-pane", pane_id,
            "--env", f"GUARD_TARGET_PANE_ID={pane_id}", "--focus"]
    if isinstance(cwd, str) and cwd:
        args.extend(["--cwd", cwd])
    return 0 if _herdr(*args).get("result") else 1


def audit_action() -> int:
    return 0 if _prompt_audit(_pane()) else 1


def panel() -> int:
    message = ""
    while True:
        pane, pending = _pending()
        print("\033[2J\033[H", end="")
        print("Guard pending files")
        print("=" * 60)
        if pending.get("error"):
            print(pending["error"])
        else:
            project = Path(str(pane.get("foreground_cwd") or pane.get("cwd") or "."))
            files = pending.get("files", {})
            groups = pending.get("groups", [])
            if not files:
                print("No edited files are waiting for a checkpoint.")
            else:
                reviewed = {path for group in groups for path in group.get("paths", [])}
                for raw in files:
                    try:
                        label = Path(raw).relative_to(project).as_posix()
                    except ValueError:
                        label = raw
                    marker = "audit" if raw in reviewed else "tracked"
                    print(f"  [{marker:7}] {label}")
                print(f"\n{len(files)} pending · {len(reviewed)} selected by audit rules")
        if message:
            print(f"\n{message}")
        print("\n[a] audit checkpoint   [r] refresh   [q] close")
        try:
            choice = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return 0
        if choice == "q":
            return 0
        if choice == "a":
            message = ("Checkpoint requested in the agent pane."
                       if _prompt_audit(pane) else
                       "Could not prompt the agent; wait until it is idle and try again.")
        else:
            message = ""


if __name__ == "__main__":
    handlers = {"show-action": show_action, "audit-action": audit_action, "panel": panel}
    handler = handlers.get(sys.argv[1] if len(sys.argv) > 1 else "")
    raise SystemExit(handler() if handler else 2)
