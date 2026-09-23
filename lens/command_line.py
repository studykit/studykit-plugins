"""Command table and completion for the `:` / Alt+X command line."""

from dataclasses import dataclass
import os
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
    Command("diff", ("vimdiff",), "diff", "Compare the current file with HEAD"),
    Command("icons", (), "icons nerd|plain", "Use Nerd Font icons or plain text in the tree",
            ("nerd", "plain")),
    Command("layout", (), "layout popup|overlay", "Switch display mode", ("popup", "overlay")),
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


def complete(text, root, files):
    """Complete the command line. Returns (new text, candidates shown when ambiguous)."""
    word, space, rest = text.lstrip().partition(" ")
    if not space:
        names = sorted({name for command in COMMANDS for name in (command.name, *command.aliases)
                        if name.startswith(word)})
        if len(names) == 1:
            return names[0] + " ", names
        return (common(names) or word), names
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
    else:
        options = [choice for choice in command.choices if choice.startswith(rest)]
    if not options:
        return text, []
    completed = options[0] if len(options) == 1 else common(options) or rest
    return f"{word} {completed}", options


def describe(word=""):
    if word:
        command = lookup(word)
        if command is None:
            return f"Unknown command: {word}"
        aliases = f" (also {', '.join(command.aliases)})" if command.aliases else ""
        return f":{command.usage} — {command.help}{aliases}"
    return "Commands: " + "  ".join(command.name for command in COMMANDS) + "  ·  :help NAME for details"
