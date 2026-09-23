"""Resolve ordinary directory colors from explicit ls environment settings."""
from __future__ import annotations

import re

from markdown_preview import Style, sgr


def directory_style(env, platform):
    """Return safe styling only; never emit environment-provided escape sequences."""
    gnu = env.get("LS_COLORS", "")
    directory = None
    for entry in gnu.split(":"):
        key, separator, value = entry.partition("=")
        if separator and key == "di":
            directory = value
    if directory is not None:
        if len(directory) <= 256 and re.fullmatch(r"[0-9;]*", directory):
            return sgr(Style(), directory)
        return None

    bsd = env.get("LSCOLORS", "")
    if bsd:
        pair = bsd[:2]
        if len(pair) != 2 or any(char.lower() not in "abcdefghx" for char in pair):
            return None
        foreground, background = pair
        return Style(
            foreground=-1 if foreground.lower() == "x" else ord(foreground.lower()) - ord("a"),
            background=-1 if background.lower() == "x" else ord(background.lower()) - ord("a"),
            bold=foreground.isupper(), underline=background.isupper(),
        )

    # BSD ls defaults to blue; GNU ls defaults to bold blue for directories.
    return Style(foreground=4, bold=not (platform == "darwin" or "bsd" in platform))
