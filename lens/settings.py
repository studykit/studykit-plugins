"""User settings from ~/.config/lens/config.toml."""
from __future__ import annotations

import curses
from dataclasses import dataclass, field
from pathlib import Path
import tomllib

# Actions a [keys] binding may name, with the built-in key each one stands for.
ACTIONS = {
    "focus": "\t", "back": "\x1b", "quit": "\x03",
    "search": "/", "command": ":", "next-match": "n", "prev-match": "N",
    "preview": " ", "edit": "\x05", "diff": "\x04", "changes": "c", "ignored": "\x08",
    "refresh": "\x12", "root": "\x0f", "git-root": "t", "parent": curses.KEY_BACKSPACE,
    "layout": "\x17", "popup-size": "\x19", "top": "g", "bottom": "G",
    "zoom-in": "+", "zoom-out": "-", "zoom-fit": "0", "align": "a",
    "prev-diagram": "[", "next-diagram": "]", "source": "v", "launch": "o", "launch-with": "O",
}

NAMED = {
    "space": " ", "tab": "\t", "enter": "\n", "escape": "\x1b", "esc": "\x1b",
    "backspace": curses.KEY_BACKSPACE, "delete": curses.KEY_DC,
    "up": curses.KEY_UP, "down": curses.KEY_DOWN, "left": curses.KEY_LEFT, "right": curses.KEY_RIGHT,
    "home": curses.KEY_HOME, "end": curses.KEY_END,
    "pageup": curses.KEY_PPAGE, "pagedown": curses.KEY_NPAGE,
    "plus": "+", "minus": "-",
}

TEMPLATE = """\
# Lens settings. Changes apply the next time Lens opens (or after :config).

[editor]
# Command used by Ctrl+E and :editor. {file} and {line} are replaced; without
# {file}, the path is appended. Unset: $VISUAL, $EDITOR, then nvim/vim/vi.
# command = "nvim +{line} {file}"
# command = "code --wait --goto {file}:{line}"

[diff]
# Command used by Ctrl+D and :diff, instead of the built-in vimdiff. {before} is
# the HEAD copy, {after} the working copy, {name} the path; both copies are
# temporary files. Without {before}/{after}, the two paths are appended.
# Emacs ediff in the terminal; quitting ediff (q) also closes its frame:
# command = '''emacsclient -nw -a '' --eval '(ediff-files "{before}" "{after}" (list (lambda () (let ((frame (selected-frame))) (add-hook (quote ediff-quit-hook) (lambda () (run-at-time 0 nil (function delete-frame) frame)) t t)))))' '''
# command = "difft {before} {after}"
# pause = true        # Wait for Enter afterwards, for tools that print and exit

[open]
# Optional. Unset, "o" and :launch use the application the OS assigns to each
# file or folder (open on macOS, xdg-open on Linux, start on Windows). Set a
# command only to override that; {file} is replaced, else the path is appended.
# command = "xdg-open {file}"

[ui]
# icons = "nerd"      # Nerd Font icons in the file tree, or "plain"
# align = "center"    # Diagram alignment: left, center, right
# tree_padding = 1    # Blank columns on each side of the file tree's rows (0 - 8)

[keys]
# Extra bindings: a key, then a Lens action or a ":" command line.
# "ctrl+f" = "search"
# "alt+z" = ":zoom fit"
# "ctrl+l" = ":icons nerd"
"""


@dataclass
class Settings:
    editor: str = ""
    diff: str = ""
    diff_pause: bool = False
    opener: str = ""
    icons: str | None = None
    align: str | None = None
    tree_padding: int | None = None
    keys: dict = field(default_factory=dict)  # curses key -> action name or ":command"
    errors: list[str] = field(default_factory=list)


def chord(spec):
    """One key chord such as "ctrl+s", "alt+x", "shift+a", "f", or "pagedown" as curses input."""
    if spec in ("+", "-"):
        return spec
    *mods, name = spec.lower().split("+") if len(spec) > 1 else [spec]
    if not set(mods) <= {"ctrl", "alt", "shift"}:
        return None
    if len(spec) == 1:
        return spec  # Keep the case of a bare key: "N" differs from "n".
    if name in NAMED:
        key = NAMED[name]
        return key if not mods else None
    if len(name) != 1:
        return None
    if "shift" in mods:
        name = name.upper()
    if "ctrl" in mods:
        if not "a" <= name.lower() <= "z":
            return None
        name = chr(ord(name.lower()) - 96)
    return "\x1b" + name if "alt" in mods else name


def known(word):
    import command_line
    return word.isdigit() or command_line.lookup(word) is not None


def location(env) -> Path:
    """LENS_CONFIG, else config.toml under $XDG_CONFIG_HOME/lens (~/.config/lens)."""
    if env.get("LENS_CONFIG"):
        return Path(env["LENS_CONFIG"]).expanduser()
    base = Path(env["XDG_CONFIG_HOME"]) if env.get("XDG_CONFIG_HOME") else Path.home() / ".config"
    return base / "lens" / "config.toml"


def load(file: Path | None) -> Settings:
    settings = Settings()
    if file is None:
        return settings
    try:
        with file.open("rb") as stream:
            data = tomllib.load(stream)
    except FileNotFoundError:
        return settings
    except (OSError, ValueError) as error:
        settings.errors.append(f"config.toml: {error}")
        return settings

    def section(name):
        value = data.get(name, {})
        if isinstance(value, dict):
            return value
        settings.errors.append(f"config.toml: [{name}] must be a table")
        return {}

    command = section("editor").get("command", "")
    if isinstance(command, str):
        settings.editor = command.strip()
    else:
        settings.errors.append("config.toml: editor.command must be a string")
    diff = section("diff")
    if isinstance(diff.get("command", ""), str):
        settings.diff = diff.get("command", "").strip()
    else:
        settings.errors.append("config.toml: diff.command must be a string")
    if isinstance(diff.get("pause", False), bool):
        settings.diff_pause = diff.get("pause", False)
    else:
        settings.errors.append("config.toml: diff.pause must be true or false")
    opener = section("open").get("command", "")
    if isinstance(opener, str):
        settings.opener = opener.strip()
    else:
        settings.errors.append("config.toml: open.command must be a string")
    ui = section("ui")
    if ui.get("icons") is not None:
        if ui["icons"] in ("nerd", "plain"):
            settings.icons = ui["icons"]
        else:
            settings.errors.append("config.toml: ui.icons must be \"nerd\" or \"plain\"")
    if ui.get("align") is not None:
        if ui["align"] in ("left", "center", "right"):
            settings.align = ui["align"]
        else:
            settings.errors.append("config.toml: ui.align must be left, center, or right")
    if ui.get("tree_padding") is not None:
        padding = ui["tree_padding"]
        if isinstance(padding, int) and not isinstance(padding, bool) and 0 <= padding <= 8:
            settings.tree_padding = padding
        else:
            settings.errors.append("config.toml: ui.tree_padding must be a whole number from 0 to 8")
    for spec, target in section("keys").items():
        key = chord(spec)
        if key is None:
            settings.errors.append(f"config.toml: unknown key {spec!r}")
        elif not isinstance(target, str) or not (target in ACTIONS or target.startswith(":")):
            settings.errors.append(f"config.toml: {spec!r} needs an action or a \":\" command")
        elif target.startswith(":") and not known(target[1:].split(" ")[0]):
            settings.errors.append(f"config.toml: unknown command in {spec!r}")
        else:
            settings.keys[key] = target
    return settings


def ensure(file: Path) -> Path:
    """The config file, created from the commented template when missing."""
    file.parent.mkdir(parents=True, exist_ok=True)
    if not file.exists():
        file.write_text(TEMPLATE)
    return file
