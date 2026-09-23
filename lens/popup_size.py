"""User-selected popup dimensions, independent of Herdr environment variables."""
from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import tempfile


@dataclass(frozen=True)
class PopupSize:
    width: int = 96
    height: int = 92

    def __post_init__(self):
        if any(type(value) is not int or not 40 <= value <= 100 for value in (self.width, self.height)):
            raise ValueError("Popup dimensions must be percentages between 40 and 100")

    def adjust(self, width=0, height=0):
        return PopupSize(max(40, min(100, self.width + width)),
                         max(40, min(100, self.height + height)))

    def as_dict(self):
        return {"width": self.width, "height": self.height}


PRESETS = (PopupSize(70, 65), PopupSize(85, 80), PopupSize(), PopupSize(100, 100))


def load_size(config_dir: Path | None) -> PopupSize:
    if config_dir is None:
        return PopupSize()
    try:
        value = json.loads((config_dir / "popup-size.json").read_text())
        return PopupSize(value["width"], value["height"])
    except (OSError, ValueError, KeyError, TypeError):
        return PopupSize()


def save_size(config_dir: Path, size: PopupSize):
    config_dir.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".popup-size-", dir=config_dir)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump(size.as_dict(), stream)
            stream.write("\n")
        os.replace(temporary, config_dir / "popup-size.json")
    finally:
        Path(temporary).unlink(missing_ok=True)
