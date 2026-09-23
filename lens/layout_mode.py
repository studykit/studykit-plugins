"""Remember the last successfully selected navigator layout."""
from __future__ import annotations

import json
import os
from pathlib import Path
import tempfile

MODES = ("popup", "overlay", "left", "right")
# Split placements share the tab with the source pane instead of covering it.
SPLITS = ("left", "right")


def load_layout(config_dir: Path | None) -> str:
    if config_dir is not None:
        try:
            value = json.loads((config_dir / "layout.json").read_text())
            if isinstance(value, dict) and value.get("placement") in MODES:
                return value["placement"]
        except (OSError, ValueError):
            pass
    return "popup"


def save_layout(config_dir: Path, placement: str):
    if placement not in MODES:
        raise ValueError("Unknown navigator layout")
    config_dir.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".layout-", dir=config_dir)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump({"placement": placement}, stream)
            stream.write("\n")
        os.replace(temporary, config_dir / "layout.json")
    finally:
        Path(temporary).unlink(missing_ok=True)
