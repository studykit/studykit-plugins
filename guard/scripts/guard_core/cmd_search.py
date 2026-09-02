"""``pre-search`` (PreToolUse on the search tools).

Refuses a filesystem-wide search: `find /`, `grep -r /`, `rg /`, and the same thing spelled
as a Glob or Grep tool call with `/` as its path. A search rooted at the filesystem root
walks every mounted volume — other checkouts, caches, home-directory dotfiles, network
mounts — so it is slow enough to blow the tool timeout, and what it returns is mostly other
people's files. The user's global instructions in this repository state the rule outright
("Never run `find`, `grep`, `rg`, or similar search tools with `/` as the search target");
this makes it a refusal rather than a request.

Independent of the agent switches, and of the session mute. The switches govern whether
guard *says* something unasked at the end of a turn; this is a prohibition on a tool call,
and a prohibition that a mute could lift would not be one. It is the same reasoning that
keeps the refs-index check in ``cmd_edit`` outside the switches.

Scope, stated as a boundary rather than a limitation: this denies the ROOT of a search, not
searches it dislikes. `/etc`, `/usr`, and every other absolute path are allowed — they are
bounded, and deciding which bounded directories a project may read is not guard's business.
What is denied is the unbounded case, plus the spellings that reach it without naming it: a
bare `/`, and any glob whose first path segment carries a wildcard (`/*`, `/**/*.py`).

Why a deny and not an ask: the reason string reaches the model verbatim as the tool's error
result (measured — ``wiki/ref/claude-code-pretooluse-deny-reason-visibility.md``), so a
refusal that names the narrower search is acted on in the same turn. An `ask` would put a
permission dialog in front of a call that is nearly always a slip, and the cost of the slip
falls on the user's session either way.
"""

from __future__ import annotations

import re
import shlex

from pathlib import Path
from typing import Any

from .emit import _emit_pre_tool_deny
from .paths import _project_dir, _trace
from .payload import _read_payload, _session_id


# Commands whose non-flag arguments name directories to walk. Matched on the basename of
# argv[0], so `/usr/bin/find` and a `\find` that bypasses an alias both count. `fd`/`fdfind`
# and `ag` are here because they are the same tool wearing a different name — a rule that
# only knew the three names in the user's sentence would be trivially stepped around, and
# not deliberately: whoever types `fd` types it because it is what they use.
_SEARCH_COMMANDS = {"find", "grep", "egrep", "fgrep", "rgrep", "rg", "ripgrep",
                    "ag", "ack", "fd", "fdfind", "locate", "glocate", "mlocate"}


# Option-taking flags whose VALUE is a path or a pattern, and must therefore not be read as
# a search root. Without this, `grep -f / pattern` and `find . -newer /` would be misread.
# Only the value-taking spellings matter; a boolean flag's next word is a real argument.
_VALUE_FLAGS = {
    # grep family
    "-e", "--regexp", "-f", "--file", "--include", "--exclude", "--exclude-dir",
    "-m", "--max-count", "-A", "--after-context", "-B", "--before-context",
    "-C", "--context", "-d", "--directories", "-D", "--devices", "--binary-files",
    "--color", "--colour", "--label",
    # rg / ag / ack
    "-g", "--glob", "--iglob", "-t", "--type", "-T", "--type-not", "--type-add",
    "--ignore-file", "--path-separator", "--pre", "--sort", "--sortr", "-M",
    "--max-columns", "--max-filesize", "--max-depth", "--maxdepth", "-j", "--threads",
    "--context-separator", "--field-match-separator", "--hostname-bin",
    # find
    "-name", "-iname", "-path", "-ipath", "-regex", "-iregex", "-newer", "-anewer",
    "-cnewer", "-type", "-size", "-perm", "-user", "-group", "-mtime", "-atime",
    "-ctime", "-mmin", "-amin", "-cmin", "-exec", "-execdir", "-ok", "-okdir",
    "-mindepth", "-printf", "-fprintf", "-links", "-inum",
    # NOT here: `-prune` and `-print0`, which take no value ("This primary always
    # evaluates to true" — find(1)). Listing them cost the rule two real denials, because
    # a match here skips the NEXT token too: `find -print0 /` and `find . -prune / -name y`
    # both walked the root unrefused. A boolean primary in this set is not a redundant
    # entry, it is a hole in the prohibition.
    # fd
    "-E", "--exclude", "-X", "--exec-batch", "-x", "--exec", "--search-path",
}


def _is_root_target(token: str) -> bool:
    """True when this argument roots a search at the filesystem root.

    Three spellings, all of which walk everything:

    - ``/`` itself, and the equivalent runs of slashes (``//``, ``///``).
    - ``/*`` and friends — a root-anchored glob. The shell expands it to every top-level
      entry before the command ever sees it, so the walk is the same one; it just arrives
      as a list. (An unexpanded ``/*`` reaching the tool verbatim is denied for the same
      reason.)
    - ``/.`` and ``/..`` — the root reached by a path that does not end in a slash.

    Not denied: any other absolute path. ``/etc`` is bounded and is not this rule's business.
    """
    t = token.strip()
    if not t:
        return False
    # A wildcard in the FIRST path segment makes the whole walk root-anchored, whatever
    # follows it: `/**/*.py` and `/*.py` descend from `/` exactly as `/*` does. Testing
    # the first segment rather than stripping a trailing one is the difference between
    # covering those and covering only the bare forms — `/**/*.py` is the ordinary way to
    # write a root-anchored glob, and it was the shape that got through.
    if t.startswith("/"):
        first = t[1:].split("/", 1)[0]
        if "*" in first or "?" in first or first.startswith("["):
            return True
    # Strip a trailing glob segment: `/*`, `/**`, `/*/`. What remains is the root it is
    # anchored to, which is what the walk actually covers.
    t = re.sub(r"/\*+/?$", "/", t)
    if set(t) == {"/"}:
        return True
    # `/.` and `/..` both resolve to the root without a trailing slash.
    return t.rstrip("/") in {"", "/.", "/.."} and t.startswith("/")


def _root_search_in_command(command: str) -> str | None:
    """The offending command word when `command` roots a search at `/`, else None.

    Splits the shell string, walks each pipeline/list segment separately (`cmd A && cmd B`,
    `a | b`, `a; b`) so a root search anywhere in a compound command is caught rather than
    only a leading one, and reads the non-flag arguments of any segment whose command word
    is a search tool.

    Fails OPEN on anything it cannot parse — an unbalanced quote, a construct `shlex` will
    not take. guard never blocks because its own parsing broke, and a command this function
    cannot read is one it also cannot make a claim about.
    """
    try:
        tokens = shlex.split(command, comments=True)
    except ValueError:
        return None
    if not tokens:
        return None

    separators = {"|", "||", "&&", ";", "&", "|&"}
    segment: list[str] = []
    segments: list[list[str]] = []
    for tok in tokens:
        if tok in separators:
            if segment:
                segments.append(segment)
            segment = []
        else:
            segment.append(tok)
    if segment:
        segments.append(segment)

    for seg in segments:
        # Skip a leading env assignment or `sudo`/`xargs`-style wrapper so the real command
        # word is the one that gets classified.
        i = 0
        while i < len(seg) and ("=" in seg[i] and not seg[i].startswith("-")):
            i += 1
        while i < len(seg) and Path(seg[i]).name in {"sudo", "command", "nice", "nohup",
                                                     "time", "env", "xargs"}:
            i += 1
        if i >= len(seg):
            continue
        name = Path(seg[i].lstrip("\\")).name
        if name not in _SEARCH_COMMANDS:
            continue
        args = seg[i + 1:]
        j = 0
        while j < len(args):
            arg = args[j]
            if arg == "--":
                j += 1
                continue
            if arg in _VALUE_FLAGS:
                # Skip the flag AND its value: the value is a pattern or a path filter,
                # never the search root.
                j += 2
                continue
            if arg.startswith("-") and arg != "-":
                # `--include=*.py` carries its value inline; a bundled short flag
                # (`-rn`) takes none. Either way the next word is still an argument.
                j += 1
                continue
            if _is_root_target(arg):
                return name
            j += 1
    return None


# Tools whose input is a shell command line. `Bash` is Claude Code's, verified against real
# payloads. The rest are candidate spellings for Codex's shell tool, which is NOT confirmed:
# `wiki/ref/openai-codex-pretooluse-payload.md` documents `tool_name` as a "Canonical hook
# tool name" without ever naming that tool, and no saved reference names it either. Guessing
# wide is the safe direction here — an extra name that no host sends costs nothing, while a
# missing one silently drops the shell branch and the rule stops applying to Codex commands.
# Confirm the real spelling next time the Codex docs are consulted and prune this.
_SHELL_TOOLS = {"Bash", "shell", "Shell", "local_shell"}


# Tool inputs that name a search root directly, by tool name.
_PATH_KEYS = {"Grep": "path", "Glob": "path"}


def _root_search_in_tool_input(tool_name: str, tool_input: Any) -> str | None:
    """The offending tool when a Grep/Glob call is rooted at `/`, else None.

    The dedicated tools reach the same filesystem walk without going through a shell, so a
    rule that only read Bash commands would leave the easier route open.
    """
    if not isinstance(tool_input, dict):
        return None
    key = _PATH_KEYS.get(tool_name)
    if key is None:
        return None
    raw = tool_input.get(key)
    if isinstance(raw, str) and _is_root_target(raw):
        return tool_name
    # A Glob whose PATTERN is absolute from the root walks the root even with no `path`.
    pattern = tool_input.get("pattern")
    if tool_name == "Glob" and isinstance(pattern, str) and _is_root_target(pattern):
        return tool_name
    return None


def _deny_reason(offender: str) -> str:
    """The sentence the model receives as the tool's error result.

    It has to do two things, because a deny reason is read as tool output and not as an
    instruction (measured — ``wiki/ref/claude-code-pretooluse-deny-reason-visibility.md``):
    say plainly that the call was refused, and name the narrower search precisely enough
    that retrying correctly needs no further guessing. A reason that only forbade would be
    followed by the same call against `/System`, `/Users`, and so on, one directory per turn.
    """
    return (
        f"guard refused this `{offender}`: it is rooted at `/`, so it walks every mounted "
        "volume — other checkouts, caches, network mounts — and returns mostly files that "
        "have nothing to do with this project. Re-run it against the directory the answer "
        "is actually in: the project root, or a named subdirectory of it. If you need a "
        "path outside the project, name that directory explicitly (`/etc`, "
        "`~/some/dir`) — any bounded path is allowed; only `/` itself is refused."
    )


def cmd_pre_search_payload(payload: dict, project_dir: Path | None,
                           session_id: str | None) -> None:
    """The rule itself, over an already-parsed payload. Shared by both hosts.

    Split out from ``cmd_pre_search`` so the Codex adapter — which reads stdin once, for its
    own dispatch — can apply the same rule without a second read. Both hosts document
    ``tool_name`` and ``tool_input`` on this event, which is the whole of what this needs.
    """
    tool_name = payload.get("tool_name")
    tool_input = payload.get("tool_input")
    if not isinstance(tool_name, str):
        return

    offender: str | None = None
    if tool_name in _SHELL_TOOLS:
        command = tool_input.get("command") if isinstance(tool_input, dict) else None
        if isinstance(command, str) and command.strip():
            offender = _root_search_in_command(command)
    else:
        offender = _root_search_in_tool_input(tool_name, tool_input)

    if offender is None:
        return

    _trace(project_dir, session_id, "pre-search", "root_search_denied",
           tool=tool_name, offender=offender)
    _emit_pre_tool_deny(_deny_reason(offender))


def cmd_pre_search() -> int:
    """PreToolUse on Bash/Grep/Glob: deny a search rooted at the filesystem root.

    Silent (no output, normal permission flow) for every call that is not one. Fails open
    on a malformed payload and on any internal error, like every other guard hook: a search
    that guard could not parse runs under the host's ordinary rules.
    """
    payload = _read_payload()
    if payload is None:
        return 0
    cmd_pre_search_payload(payload, _project_dir(), _session_id(payload))
    return 0
