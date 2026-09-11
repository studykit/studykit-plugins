#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Lifecycle adapter for one-time handover transfer across ``/clear``."""

from __future__ import annotations

import hashlib
import json
import os
import shlex
import sys
import time
from pathlib import Path
from typing import Any


MAX_AGE_SECONDS = 300


def payload() -> dict[str, Any]:
    try:
        value = json.load(sys.stdin)
    except (OSError, ValueError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def project_dir(data: dict[str, Any]) -> Path | None:
    value = os.environ.get("CLAUDE_PROJECT_DIR")
    if not isinstance(value, str) or not value:
        return None
    try:
        return Path(value).resolve()
    except OSError:
        return None


def session_id(data: dict[str, Any]) -> str:
    value = data.get("session_id")
    return value if isinstance(value, str) and value and "/" not in value else ""


def state_dir(project: Path) -> Path:
    digest = hashlib.sha256(str(project).encode("utf-8")).hexdigest()[:24]
    base = Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local" / "state"))
    return base / "studykit-handover" / digest


def handoff_path(project: Path) -> Path:
    return state_dir(project) / "clear-handoff.json"


def session_path(project: Path, sid: str) -> Path:
    return state_dir(project) / f"session-{sid}.json"


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
    temp.replace(path)


def add_shell_command() -> None:
    env_file = os.environ.get("CLAUDE_ENV_FILE", "").strip()
    if not env_file:
        return
    command_dir = Path(__file__).resolve().parent.parent / "shell" / "bin"
    project = os.environ.get("CLAUDE_PROJECT_DIR", "")
    line = f'export PATH={shlex.quote(str(command_dir))}:$PATH\nexport HANDOVER_PROJECT_DIR={shlex.quote(project)}'
    try:
        path = Path(env_file)
        if not path.is_file() or line not in path.read_text(encoding="utf-8"):
            with path.open("a", encoding="utf-8") as stream:
                stream.write(line + "\n")
    except OSError:
        return


def on_end(data: dict[str, Any]) -> None:
    if data.get("reason") != "clear":
        return
    project, sid = project_dir(data), session_id(data)
    if project is None or not sid:
        return
    try:
        record = json.loads(session_path(project, sid).read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            return
        path = record.get("handover_file")
        if not isinstance(path, str) or not Path(path).is_file():
            return
        write_json(handoff_path(project), {"from_session": sid, "handover_file": path, "written_at": time.time()})
        session_path(project, sid).unlink()
    except (OSError, ValueError, json.JSONDecodeError):
        return


def on_start(data: dict[str, Any]) -> None:
    add_shell_command()
    if data.get("source") != "clear":
        return
    project, sid = project_dir(data), session_id(data)
    if project is None or not sid:
        return
    path = handoff_path(project)
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
        path.unlink()
    except (OSError, ValueError, json.JSONDecodeError):
        return
    handover = record.get("handover_file") if isinstance(record, dict) else None
    written = record.get("written_at") if isinstance(record, dict) else None
    if not isinstance(handover, str) or not isinstance(written, (int, float)):
        return
    if time.time() - written > MAX_AGE_SECONDS or not Path(handover).is_file():
        return
    print(json.dumps({"systemMessage": f"handover: the session cleared before this one left {handover}.", "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": f"handover: read {handover} before answering. Treat it as the prior session's state; do not ask whether to read it."}}))


def record_session(sid: str, path_arg: str) -> None:
    if not sid or "/" in sid or "\\" in sid:
        raise SystemExit("handover-record: missing or invalid session ID")
    try:
        handover = Path(path_arg).expanduser().resolve()
    except OSError:
        return
    if not handover.is_file():
        raise SystemExit("handover-record: handover file does not exist")
    project = Path.cwd().resolve()
    write_json(session_path(project, sid), {"handover_file": str(handover)})
    print(f"handover: recorded {handover} for this session.")


def main() -> None:
    if len(sys.argv) == 4 and sys.argv[1] == "record":
        record_session(sys.argv[2], sys.argv[3])
        return
    data = payload()
    event = data.get("hook_event_name")
    if event == "SessionEnd":
        on_end(data)
    elif event == "SessionStart":
        on_start(data)


if __name__ == "__main__":
    main()
