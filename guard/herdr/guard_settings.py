"""Editor and diff-tool settings for the Herdr pending-files popup."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import tomllib
from typing import Any, Mapping


@dataclass
class Settings:
    editor: str = ""
    diff: str = ""
    diff_pause: bool = False
    errors: list[str] = field(default_factory=list)


def location(env: Mapping[str, str]) -> Path:
    """GUARD_HERDR_CONFIG, else herdr.toml under $XDG_CONFIG_HOME/guard (~/.config/guard)."""
    if env.get("GUARD_HERDR_CONFIG"):
        return Path(env["GUARD_HERDR_CONFIG"]).expanduser()
    base = Path(env["XDG_CONFIG_HOME"]) if env.get("XDG_CONFIG_HOME") else Path.home() / ".config"
    return base / "guard" / "herdr.toml"


def load(file: Path) -> Settings:
    """Read the settings; a mistake is reported and the rest still applies, as in Lens."""
    settings = Settings()
    try:
        with file.open("rb") as stream:
            data = tomllib.load(stream)
    except FileNotFoundError:
        return settings
    except (OSError, ValueError) as error:
        settings.errors.append(f"{file.name}: {error}")
        return settings

    def section(name: str) -> dict[str, Any]:
        value = data.get(name, {})
        if isinstance(value, dict):
            return value
        settings.errors.append(f"{file.name}: [{name}] must be a table")
        return {}

    editor = section("editor").get("command", "")
    if isinstance(editor, str):
        settings.editor = editor.strip()
    else:
        settings.errors.append(f"{file.name}: editor.command must be a string")
    diff = section("diff")
    command = diff.get("command", "")
    if isinstance(command, str):
        settings.diff = command.strip()
    else:
        settings.errors.append(f"{file.name}: diff.command must be a string")
    pause = diff.get("pause", False)
    if isinstance(pause, bool):
        settings.diff_pause = pause
    else:
        settings.errors.append(f"{file.name}: diff.pause must be true or false")
    return settings
