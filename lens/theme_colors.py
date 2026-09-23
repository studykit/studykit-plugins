"""Resolve Herdr-compatible theme tokens without accessing host state."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import json
from pathlib import Path
import re


# Palette data adapted from Herdr v0.9.1 (Apache-2.0); see licenses/ and dev/testing.md.
BUILTINS = json.loads(Path(__file__).with_name("herdr_palettes.json").read_text())
NAMED = dict(zip(("black", "red", "green", "yellow", "blue", "magenta", "cyan", "gray",
                  "darkgray", "lightred", "lightgreen", "lightyellow", "lightblue",
                  "lightmagenta", "lightcyan", "white"), range(16)))
NAMED.update(purple=5, grey=7, darkgrey=8, reset=-1, default=-1, none=-1, transparent=-1)
ANSI_RGB = ((0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128),
            (128, 0, 128), (0, 128, 128), (192, 192, 192), (128, 128, 128),
            (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255),
            (255, 0, 255), (0, 255, 255), (255, 255, 255))
CUBE = (0, 95, 135, 175, 215, 255)
RGB = ANSI_RGB + tuple((r, g, b) for r in CUBE for g in CUBE for b in CUBE) + tuple((v, v, v) for v in range(8, 239, 10))
ALIASES = {
    "catppuccin-mocha": "catppuccin", "latte": "catppuccin-latte", "light": "catppuccin-latte",
    "tokyonight": "tokyo-night", "tokyo-day": "tokyo-night-day", "tokyonight-day": "tokyo-night-day",
    "gruvbox-dark": "gruvbox", "onedark": "one-dark", "onelight": "one-light",
    "solarized-dark": "solarized", "lotus": "kanagawa-lotus", "rosepine": "rose-pine",
    "rosepine-dawn": "rose-pine-dawn", "dawn": "rose-pine-dawn",
}
SIBLINGS = (("catppuccin", "catppuccin-latte"), ("tokyo-night", "tokyo-night-day"),
            ("gruvbox", "gruvbox-light"), ("one-dark", "one-light"),
            ("solarized", "solarized-light"), ("kanagawa", "kanagawa-lotus"),
            ("rose-pine", "rose-pine-dawn"))


@lru_cache(maxsize=512)
def nearest(rgb, colors=256):
    candidates = range(16, 256) if colors >= 256 else range(max(1, colors))
    return min(candidates, key=lambda i: sum((a - b) ** 2 for a, b in zip(rgb, RGB[i])))


def parse_color(value):
    if not isinstance(value, str):
        return 6
    value = value.strip().lower()
    if value in NAMED:
        return NAMED[value]
    if re.fullmatch(r"#[0-9a-f]{3}", value):
        value = "#" + "".join(char * 2 for char in value[1:])
    if re.fullmatch(r"#[0-9a-f]{6}", value):
        return nearest(tuple(int(value[i:i + 2], 16) for i in (1, 3, 5)))
    match = re.fullmatch(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", value)
    if match and all(int(v) <= 255 for v in match.groups()):
        return nearest(tuple(map(int, match.groups())))
    return 6  # Herdr's fallback for an unrecognized color.


def canonical(name):
    name = str(name).lower().replace(" ", "-").replace("_", "-")
    return ALIASES.get(name, name)


@dataclass(frozen=True)
class Palette:
    name: str
    colors: dict[str, int]

    def __getitem__(self, name):
        return self.colors[name]

    def rich(self, name):
        color = self[name]
        return "default" if color < 0 else f"color({color})"


def resolve(config=None, appearance="dark"):
    config = config if isinstance(config, dict) else {}
    theme = config.get("theme", {})
    theme = theme if isinstance(theme, dict) else {}
    name = canonical(theme.get("name", "catppuccin"))
    fallback = "catppuccin"
    custom = theme.get("custom", {})
    custom = custom if isinstance(custom, dict) else {}
    mode = {}
    if theme.get("auto_switch") is True:
        dark, light = next((pair for pair in SIBLINGS if name in pair), (name, name))
        fallback = "catppuccin-latte" if appearance == "light" else "catppuccin"
        name = canonical(theme.get(f"{appearance}_name", light if appearance == "light" else dark))
        mode = custom.get(appearance, {})
        mode = mode if isinstance(mode, dict) else {}
    name = name if name in BUILTINS else fallback
    values = dict(BUILTINS[name])
    values.update({key: value for key, value in custom.items() if key in values})
    ui = config.get("ui", {})
    accent = ui.get("accent", "cyan") if isinstance(ui, dict) else "cyan"
    if accent != "cyan" and "accent" not in custom:
        values["accent"] = accent
    values.update({key: value for key, value in mode.items() if key in values})
    return Palette(name, {key: parse_color(value) for key, value in values.items()})


def terminal_color(index, count, default_supported=True, background=False):
    if index < 0:
        return -1 if default_supported else 0 if background else min(7, count - 1)
    return index if index < count else nearest(RGB[index], count)
