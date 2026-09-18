"""Bounded, atomic view snapshots keyed by canonical navigation root."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import tempfile


MAX_STATE_BYTES = 4 * 1024 * 1024
VERSION = 1


def normalize(value, root: Path):
    if not isinstance(value, dict) or not isinstance(value.get("root"), str):
        return None
    try:
        canonical = str(root.resolve())
        if not Path(value["root"]).is_absolute() or str(Path(value["root"]).resolve()) != canonical:
            return None
    except (OSError, ValueError, RuntimeError):
        return None
    result = {"root": canonical}
    for key in ("changes", "include_ignored", "preview_focus"):
        item = value.get(key, False)
        if type(item) is not bool:
            return None
        result[key] = item
    for key in ("query", "active", "selected"):
        item = value.get(key, "")
        if not isinstance(item, str) or len(item) > 4096 or "\0" in item:
            return None
        if key != "query" and item and not (key == "selected" and item == ".."):
            if Path(item).is_absolute() or ".." in Path(item).parts:
                return None
        result[key] = item
    expanded = value.get("expanded", [])
    if not isinstance(expanded, list) or len(expanded) > 50000:
        return None
    for item in expanded:
        if (not isinstance(item, str) or not item or len(item) > 4096 or "\0" in item
                or Path(item).is_absolute() or ".." in Path(item).parts):
            return None
    result["expanded"] = sorted(set(expanded))
    for key in ("scroll", "preview_scroll", "horizontal"):
        item = value.get(key, 0)
        if type(item) is not int or not 0 <= item <= 1_000_000_000:
            return None
        result[key] = item
    return result


def state_path(directory: Path, root: Path) -> Path:
    key = hashlib.sha256(os.fsencode(root.resolve())).hexdigest()
    return directory / "views" / f"{key}.json"


def load_view(directory: Path | None, root: Path):
    if directory is None:
        return None
    try:
        with state_path(directory, root).open("rb") as stream:
            raw = stream.read(MAX_STATE_BYTES + 1)
        if len(raw) > MAX_STATE_BYTES:
            return None
        payload = json.loads(raw)
        if (not isinstance(payload, dict) or type(payload.get("version")) is not int
                or payload["version"] != VERSION):
            return None
        return normalize(payload.get("view"), root)
    except (OSError, ValueError, RuntimeError, RecursionError):
        return None


def save_view(directory: Path, view: dict):
    root = Path(view["root"])
    normalized = normalize(view, root)
    if normalized is None:
        raise ValueError("Invalid navigator view state")
    data = json.dumps({"version": VERSION, "view": normalized}).encode("utf-8")
    if len(data) > MAX_STATE_BYTES:
        raise ValueError("Navigator view state exceeded the save limit")
    path = state_path(directory, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".view-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)
