"""Command table and completion for the `:` / Alt+X command line."""

from dataclasses import dataclass
import curses
import os
import sys
from pathlib import Path


@dataclass(frozen=True)
class Command:
    name: str
    aliases: tuple[str, ...]
    usage: str
    help: str
    choices: tuple[str, ...] = ()  # Fixed argument values offered by Tab.
    argument: str = ""  # "file" or "directory" for path completion.


COMMANDS = (
    Command("open", ("e", "find-file"), "open FILE", "Preview a file", argument="file"),
    Command("goto", ("goto-line",), "goto LINE", "Jump to a preview line (or type the number alone)"),
    Command("find", ("search",), "find TEXT", "Find text in the preview"),
    Command("cd", ("root",), "cd DIR", "Change the navigation root", argument="directory"),
    Command("top", (), "top", "Jump to the start of the preview"),
    Command("bottom", ("end",), "bottom", "Jump to the end of the preview"),
    Command("zoom", (), "zoom in|out|fit|PERCENT", "Zoom the current diagram",
            ("in", "out", "fit", "25", "50", "75", "100", "125", "150", "200", "300", "400")),
    Command("align", (), "align left|center|right", "Align diagrams", ("left", "center", "right")),
    Command("source", (), "source", "Show diagram source"),
    Command("diagram", ("image",), "diagram", "Show diagram images"),
    Command("changes", (), "changes", "List changed files only"),
    Command("project", ("all",), "project", "List every project file"),
    Command("ignored", (), "ignored [on|off]", "Show or hide Git-ignored files", ("on", "off")),
    Command("refresh", ("reload",), "refresh", "Reload the file list and preview"),
    Command("editor", ("vim", "emacs"), "editor", "Open the current file in an editor"),
    Command("launch", ("xdg-open", "start"), "launch [FILE]",
            "Open the selected file or folder in the application the OS assigns", argument="file"),
    Command("with", ("app",), "with [APP]",
            "Open the selected file or folder with an application; alone, list them", argument="application"),
    Command("diff", ("vimdiff",), "diff", "Compare the current file with HEAD"),
    Command("icons", (), "icons nerd|plain", "Use Nerd Font icons or plain text in the tree",
            ("nerd", "plain")),
    Command("layout", (), "layout popup|overlay|left|right", "Switch display mode",
            ("popup", "overlay", "left", "right")),
    Command("config", ("settings",), "config", "Edit Lens settings (config.toml) and reload them"),
    Command("help", ("?",), "help [COMMAND]", "List commands or describe one"),
    Command("quit", ("q", "exit", "kill-emacs"), "quit", "Close Lens"),
)


def lookup(word):
    """The command a word names: an exact name or alias, else a unique name prefix."""
    for command in COMMANDS:
        if word == command.name or word in command.aliases:
            return command
    found = [command for command in COMMANDS if command.name.startswith(word)]
    return found[0] if word and len(found) == 1 else None


def common(words):
    if not words:
        return ""
    return os.path.commonprefix(words)


def directories(root, partial):
    """Directory names under root that complete partial, with a trailing slash."""
    head, _, tail = partial.rpartition("/")
    base = Path(head or ("/" if partial.startswith("/") else ".")).expanduser()
    if not base.is_absolute():
        base = root / base
    try:
        names = sorted(entry.name for entry in os.scandir(base)
                       if entry.is_dir() and entry.name.startswith(tail)
                       and (tail.startswith(".") or not entry.name.startswith(".")))
    except OSError:
        return []
    prefix = partial[:len(partial) - len(tail)]
    return [prefix + name + "/" for name in names]


def applications(platform=sys.platform):
    """Application names for :with completion: .app bundles on macOS, else commands on PATH."""
    names = set()
    if platform == "darwin":
        for base in ("/Applications", "/Applications/Utilities", "/System/Applications",
                     "/System/Applications/Utilities", str(Path.home() / "Applications")):
            try:
                names.update(entry.name[:-4] for entry in os.scandir(base) if entry.name.endswith(".app"))
            except OSError:
                pass
    else:
        for base in os.environ.get("PATH", "").split(os.pathsep):
            try:
                names.update(entry.name for entry in os.scandir(base)
                             if entry.is_file() and os.access(entry.path, os.X_OK))
            except OSError:
                pass
    return sorted(names)


def candidates(text, root, files):
    """The fixed part of the command line and the candidates for the word after it."""
    word, space, rest = text.lstrip().partition(" ")
    if not space:
        return "", sorted({name for command in COMMANDS for name in (command.name, *command.aliases)
                           if name.startswith(word)})
    command = lookup(word)
    if command is None:
        return text, []
    rest = rest.lstrip()
    if command.argument == "file":
        options = [name for name in files if name.startswith(rest)]
        # Complete one path component at a time, like a shell.
        options = sorted({name[:name.find("/", len(rest)) + 1] if "/" in name[len(rest):] else name
                          for name in options})
    elif command.argument == "directory":
        options = directories(root, rest)
    elif command.argument == "application":
        # Application names often contain spaces; match case-insensitively.
        options = [name for name in applications() if name.lower().startswith(rest.lower())]
    else:
        options = [choice for choice in command.choices if choice.startswith(rest)]
    return f"{word} ", options


def accept(head, option):
    """The command line with option chosen; a command name is followed by its argument's space."""
    return head + option + ("" if head else " ")


def complete(text, root, files):
    """Complete the command line. Returns (new text, candidates shown when ambiguous)."""
    head, options = candidates(text, root, files)
    if not options:
        return text, []
    if len(options) == 1:
        return accept(head, options[0]), options
    return head + (common(options) or text[len(head):].lstrip()), options


def describe(word=""):
    if word:
        command = lookup(word)
        if command is None:
            return f"Unknown command: {word}"
        aliases = f" (also {', '.join(command.aliases)})" if command.aliases else ""
        return f":{command.usage} — {command.help}{aliases}"
    return "Commands: " + "  ".join(command.name for command in COMMANDS) + "  ·  :help NAME for details"


def word_start(text, cursor):
    """Where the word before cursor begins, skipping the gap in front of it, as Emacs M-b does."""
    while cursor and not text[cursor - 1].isalnum():
        cursor -= 1
    while cursor and text[cursor - 1].isalnum():
        cursor -= 1
    return cursor


def word_end(text, cursor):
    """Where the word after cursor ends, as Emacs M-f does."""
    while cursor < len(text) and not text[cursor].isalnum():
        cursor += 1
    while cursor < len(text) and text[cursor].isalnum():
        cursor += 1
    return cursor


def field_start(text, cursor):
    """Where the space-separated field before cursor begins: C-w kills a whole path at once."""
    while cursor and text[cursor - 1] == " ":
        cursor -= 1
    while cursor and text[cursor - 1] != " ":
        cursor -= 1
    return cursor


def edit(text, cursor, key, killed):
    """Apply one Emacs-style editing key to the line. Returns (text, cursor, killed), or None if the key
    is not an editing key. killed holds the last killed text, for C-y."""
    moves = {"\x01": 0, curses.KEY_HOME: 0, "\x05": len(text), curses.KEY_END: len(text),
             "\x02": max(0, cursor - 1), curses.KEY_LEFT: max(0, cursor - 1),
             "\x06": min(len(text), cursor + 1), curses.KEY_RIGHT: min(len(text), cursor + 1),
             "\x1bb": word_start(text, cursor), "\x1bf": word_end(text, cursor)}
    if key in moves:
        return text, moves[key], killed
    # Kills: the span removed, which C-y can put back.
    spans = {"\x0b": (cursor, len(text)), "\x15": (0, cursor),
             "\x1bd": (cursor, word_end(text, cursor)),
             "\x1b\x7f": (word_start(text, cursor), cursor), "\x1b\x08": (word_start(text, cursor), cursor),
             "\x17": (field_start(text, cursor), cursor)}
    if key in spans:
        start, end = spans[key]
        if start == end:
            return text, cursor, killed
        return text[:start] + text[end:], start, text[start:end]
    if key in ("\x04", curses.KEY_DC):
        return text[:cursor] + text[cursor + 1:], cursor, killed
    if key in ("\b", "\x7f", curses.KEY_BACKSPACE):
        return text[:max(0, cursor - 1)] + text[cursor:], max(0, cursor - 1), killed
    if key == "\x19":
        return text[:cursor] + killed + text[cursor:], cursor + len(killed), killed
    if isinstance(key, str) and key.isprintable():
        return text[:cursor] + key + text[cursor:], cursor + len(key), killed
    return None
