"""Filesystem and Git operations independent of the terminal host."""
from __future__ import annotations

import os
from pathlib import Path
import shlex
import shutil
import stat
import subprocess
import sys
from collections import deque
from dataclasses import dataclass, field

PREVIEW_BYTES = 256 * 1024
MAX_FILES = 50000
SKIP_DIRS = {".git", ".hg", ".svn", "node_modules", ".venv", "venv", "__pycache__"}
VCS_DIRS = {".git", ".hg", ".svn"}


def breadth_first_walk(root, onerror):
    # Large ignored caches must not consume the budget before sibling source
    # folders are even visited. Never follow directory symlinks.
    pending = deque([os.fspath(root)])
    while pending:
        directory = pending.popleft()
        dirs, names = [], []
        try:
            with os.scandir(directory) as entries:
                for entry in entries:
                    if entry.name in VCS_DIRS:
                        continue
                    if entry.is_dir():
                        if not entry.is_symlink():
                            dirs.append(entry.name)
                    else:
                        names.append(entry.name)
        except OSError as error:
            onerror(error)
            continue
        dirs.sort()
        names.sort()
        yield directory, dirs, names
        pending.extend(os.path.join(directory, name) for name in dirs)


def git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "--literal-pathspecs", "-C", str(root), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15,
    )


def parse_status(data: bytes) -> dict[str, str]:
    result = {}
    records = iter(data.split(b"\0"))
    for record in records:
        if len(record) < 4:
            continue
        status = record[:2].decode("ascii", "replace")
        result[os.fsdecode(record[3:])] = status
        if "R" in status or "C" in status:
            next(records, None)  # -z reports destination before the original path.
    return result


@dataclass
class Index:
    root: Path
    files: list[str]
    status: dict[str, str]
    repository: Path | None
    note: str = ""
    directories: list[str] = field(default_factory=list)
    status_pending: bool = False
    status_error: str = ""


def read_status(root: Path, repository: Path) -> dict[str, str]:
    changes = git(repository, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--", str(root))
    if changes.returncode:
        raise RuntimeError(changes.stderr.decode(errors="replace"))
    status = {}
    for name, code in parse_status(changes.stdout).items():
        try:
            relative = (repository / name).relative_to(root).as_posix()
        except ValueError:
            continue
        status[relative] = code
    return status


def apply_status(index: Index, status: dict[str, str]):
    # Staged deletions are absent from ls-files but still belong in the tree.
    files = (set(index.files) | status.keys()) - set(index.directories)
    limit = max(0, MAX_FILES - len(index.directories))
    index.files = sorted(files, key=lambda name: (name.casefold(), name))[:limit]
    if len(files) > limit and "Listing limited" not in index.note:
        index.note = (index.note + "; " if index.note else "") + f"Listing limited to {MAX_FILES:,} entries; change root to a subfolder to see more"
    index.status = status
    index.status_pending = False
    index.status_error = ""


def scan(root: Path, include_ignored: bool = False, *, include_status: bool = True) -> Index:
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError(f"Not a directory: {root}")
    repository = None
    status = {}
    notes = []
    directories = set()
    files = set()
    try:
        probe = git(root, "rev-parse", "--show-toplevel")
        if probe.returncode == 0:
            repository = Path(os.fsdecode(probe.stdout).rstrip("\n"))
    except FileNotFoundError:
        notes.append("Git unavailable; using filesystem listing")
    if repository:
        listing = git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", ".")
        if listing.returncode:
            raise RuntimeError(listing.stderr.decode(errors="replace"))
        files = {os.fsdecode(name) for name in listing.stdout.split(b"\0") if name}
        if include_status:
            status = read_status(root, repository)
            files.update(status)
    if not repository or include_ignored:
        def walk_error(error):
            notes.append(str(error))
        excluded = VCS_DIRS if include_ignored else SKIP_DIRS
        walk = breadth_first_walk(root, walk_error) if include_ignored else os.walk(root, followlinks=False, onerror=walk_error)
        for directory, dirs, names in walk:
            if not include_ignored:
                dirs[:] = sorted(d for d in dirs if d not in excluded and not os.path.islink(os.path.join(directory, d)))
            # Walkers already constrain entries to this root. Compute the prefix
            # once per directory, not a pathlib ancestry search for every entry.
            relative_dir = os.path.relpath(directory, root)
            prefix = "" if relative_dir == "." else relative_dir + "/"
            if include_ignored:
                for name in dirs:
                    if len(files) + len(directories) >= MAX_FILES:
                        break
                    relative = prefix + name
                    directories.add(relative)
                    # Git may list nested repositories as directory entries.
                    files.discard(relative)
                    files.discard(relative + "/")
            for name in names:
                if name in VCS_DIRS:
                    continue  # Worktrees can have a .git file instead of a directory.
                if len(files) + len(directories) >= MAX_FILES:
                    break
                files.add(prefix + name)
            if len(files) + len(directories) >= MAX_FILES:
                break
    names = sorted(files, key=lambda name: (name.casefold(), name))
    if len(names) + len(directories) >= MAX_FILES:
        notes.append(f"Listing limited to {MAX_FILES:,} entries; change root to a subfolder to see more")
    return Index(root, names[:MAX_FILES], status, repository, "; ".join(notes), sorted(directories),
                 status_pending=bool(repository and not include_status))


def search(files: list[str], query: str) -> list[str]:
    """Rank filename matches ahead of path matches; allow subsequence searches."""
    needle = query.casefold().strip()
    if not needle:
        return files
    ranked = []
    for name in files:
        path = name.casefold()
        base = path.rsplit("/", 1)[-1]
        if needle == base:
            score = 0
        elif base.startswith(needle):
            score = 1
        elif needle in base:
            score = 2
        elif needle in path:
            score = 3
        else:
            letters = iter(path if "/" in needle else base)
            if not all(char in letters for char in needle):
                continue
            score = 4
        ranked.append((score, len(name), path, name))
    return [row[-1] for row in sorted(ranked)]


def highlights(name: str, query: str) -> set[int]:
    """Indexes of the characters in name that the search matched, the way search() matched them."""
    needle = query.casefold().strip()
    path = name.casefold()
    start = path.rfind("/") + 1
    if not needle:
        return set()
    found = path.find(needle, start)
    if found < 0:
        found = path.find(needle)
    if found >= 0:
        return set(range(found, found + len(needle)))
    marks, position = set(), 0 if "/" in needle else start
    for char in needle:
        position = path.find(char, position)
        if position < 0:
            return set()
        marks.add(position)
        position += 1
    return marks


@dataclass(frozen=True)
class Row:
    path: str
    directory: bool = False
    depth: int = 0


def rows(files: list[str], expanded: set[str], query: str = "", directories=()) -> list[Row]:
    if query:
        return [Row(name) for name in search(files, query)]
    children: dict[str, dict[str, bool]] = {"": {}}
    for name, is_directory in [(name, False) for name in files] + [(name, True) for name in directories]:
        parts = name.split("/")
        for i in range(len(parts)):
            parent = "/".join(parts[:i])
            path = "/".join(parts[:i + 1])
            siblings = children.setdefault(parent, {})
            siblings[path] = siblings.get(path, False) or is_directory or i < len(parts) - 1
    result = []
    def visit(parent: str, depth: int):
        for name, directory in sorted(children.get(parent, {}).items(), key=lambda item: (not item[1], item[0].casefold())):
            result.append(Row(name, directory, depth))
            if directory and name in expanded:
                visit(name, depth + 1)
    visit("", 0)
    return result


def checked_path(root: Path, name: str) -> Path:
    path = root / name
    if Path(name).is_absolute() or ".." in Path(name).parts:
        raise ValueError("File must be inside the project directory")
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("Symlink points outside the project directory")
    return path


def read_text(root: Path, name: str) -> tuple[str, bool]:
    path = checked_path(root, name)
    # O_NONBLOCK prevents a replaced file/FIFO from hanging the UI.
    fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK)
    with os.fdopen(fd, "rb") as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise ValueError("Only regular files can be previewed")
        data = stream.read(PREVIEW_BYTES + 1)
    if b"\0" in data:
        raise ValueError("Binary file; use an external application to open it")
    return data[:PREVIEW_BYTES].decode("utf-8", "replace"), len(data) > PREVIEW_BYTES


def preview(index: Index, name: str) -> str:
    text, truncated = read_text(index.root, name)
    return text + ("\n[Preview truncated at 256 KiB]" if truncated else "")


def editor_command(configured: str, path: Path, line: int = 1) -> list[str]:
    if configured:
        command = shlex.split(configured)
        if not command or not shutil.which(command[0]):
            raise ValueError("Configured editor was not found on PATH")
    else:
        command = next(([name] for name in ("nvim", "vim", "vi") if shutil.which(name)), [])
        if not command:
            raise ValueError("Set VISUAL or EDITOR to an installed editor")
    # Placeholders are substituted per argument, after splitting, so a path
    # with spaces or shell characters stays one literal argument.
    target = str(path.absolute())
    if any("{file}" in part for part in command):
        return [part.replace("{file}", target).replace("{line}", str(line)) for part in command]
    return [*(part.replace("{line}", str(line)) for part in command), target]


def opener_command(configured: str, path: Path, platform: str = sys.platform) -> list[str]:
    """The command that hands a file or folder to the application the OS associates with it."""
    if configured:
        command = shlex.split(configured)
    elif platform == "darwin":
        command = ["open"]
    elif platform.startswith("win"):
        command = ["cmd", "/c", "start", ""]
    else:
        command = ["xdg-open"]
    if not command or not shutil.which(command[0]):
        raise ValueError(f"{command[0] if command else 'Open command'} was not found on PATH")
    target = str(path.absolute())
    if any("{file}" in part for part in command):
        return [part.replace("{file}", target) for part in command]
    return [*command, target]


def application_command(app: str, path: Path, platform: str = sys.platform) -> list[str]:
    """The command that opens a file or folder with a chosen application."""
    target = str(path.absolute())
    if platform == "darwin":
        return ["open", "-a", app, target]  # open reports an unknown application itself.
    if platform.startswith("win"):
        return ["cmd", "/c", "start", "", app, target]
    command = shlex.split(app)
    if not command or not shutil.which(command[0]):
        raise ValueError(f"{app} was not found on PATH")
    return [*command, target]
