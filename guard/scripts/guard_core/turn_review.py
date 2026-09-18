"""Configured turn-review selection and a stable input contract for either host."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from uuid import uuid4

from .config import ReviewAction, _load_config, _turn_review_action
from .turnrec import _turn_dir


def configured_reviewer(project_dir: Path) -> ReviewAction | None:
    action, configured = _turn_review_action(_load_config(project_dir))
    if configured and action is None:
        raise ValueError("turn_review must specify an agent or skill other than audit-turn")
    return action


def prepare_review(project_dir: Path, session_id: str, reviewer: ReviewAction,
                   turn_id: str, turn: dict[str, Any], source_path: Path) -> dict[str, Any]:
    response = turn.get("assistant")
    if not isinstance(response, str) or not response.strip():
        raise ValueError("The selected turn has no recorded assistant response")
    # A separate snapshot prevents a later request or hook update from changing the
    # evidence a reviewer already received. Session retention sweeps these with turns.
    directory = _turn_dir(project_dir, session_id)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"review-{uuid4().hex}.json"
    record = {
        "turn_id": turn_id,
        "user": turn.get("user", ""),
        "assistant": response,
        "tools": turn.get("tools", []),
        "source_path": str(source_path),
    }
    with path.open("x", encoding="utf-8") as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return {
        "status": "review",
        "turn_id": turn_id,
        "input_path": str(path.resolve()),
        "reviewer": {"kind": reviewer.kind, "name": reviewer.name},
    }
