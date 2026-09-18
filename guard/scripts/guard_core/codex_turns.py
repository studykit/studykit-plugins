"""Codex adapter storage for documented hook turn payloads; not a transcript parser."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .paths import _state_root, _trace
from .turnrec import _short


def _turn_path(project_dir: Path, session_id: str, turn_id: str) -> Path:
    # Short ids, by the same rule as the Claude side (`turnrec._short`) and for the same
    # reason: this path is printed into the model's context when the user asks for an audit,
    # and two 36-char UUIDs in it are hex the tokenizer handles badly. The two hosts never
    # share a tree — `STATE_DIR_REL` differs — so the shape is a convention here, not a
    # coupling.
    return (_state_root(project_dir) / "turns" / _short(session_id)
            / f"{_short(turn_id)}.json")


def _load_turn(project_dir: Path, session_id: str, turn_id: str) -> dict[str, Any]:
    path = _turn_path(project_dir, session_id, turn_id)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        value = {}
    return value if isinstance(value, dict) else {}


def _save_turn(project_dir: Path, session_id: str, turn_id: str, turn: dict[str, Any]) -> None:
    """Write the turn record, atomically. Silent on failure — the caller fails open."""
    path = _turn_path(project_dir, session_id, turn_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(turn, ensure_ascii=False), encoding="utf-8")
        tmp.replace(path)
    except OSError:
        _trace(project_dir, session_id, "codex", "turn_write_failed", turn_id=turn_id)
