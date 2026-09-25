"""Resolve Obsidian embeds (`![[...]]`) to notes and images inside one vault.

Only files inside the vault are read; nothing is fetched or executed.
"""
from __future__ import annotations

import os
from pathlib import Path
import re


# The image formats Obsidian embeds; other files keep their placeholder.
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg", ".avif"}
NOTE_SUFFIXES = {".md", ".markdown"}
MAX_NOTE_BYTES = 1024 * 1024
MAX_DEPTH = 4  # Notes embedding notes; a cycle stops earlier.
MAX_FILES = 50_000  # Filename lookups stop scanning a huge folder here.
HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$")
BLOCK_ID = re.compile(r"(?:^|[ \t])\^([A-Za-z0-9-]+)[ \t]*$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
LIST_ITEM = re.compile(r"^[ \t]*(?:[-*+]|\d+[.)])[ \t]")
SIZE = re.compile(r"(\d+)(?:x(\d+))?")


def vault_root(file: Path, fallback: Path) -> Path:
    """The folder holding `.obsidian`, as Obsidian opens it, else the browsed root."""
    for folder in file.resolve().parents:
        if (folder / ".obsidian").is_dir():
            return folder
    return fallback.resolve()


def split_target(target: str) -> tuple[str, str]:
    """`Note#Heading` or `Note#^block` as (file, subpath)."""
    name, _, subpath = target.partition("#")
    return name.strip(), subpath.strip()


def image_size(alias: str) -> tuple[int, int] | None:
    """Obsidian's `|100` or `|100x145` image size, in pixels."""
    match = SIZE.fullmatch(alias.strip())
    return (int(match[1]), int(match[2] or 0)) if match else None


class Vault:
    def __init__(self, root: Path, current: Path, index=None):
        self.root = root.resolve()
        self.current = current
        self._index = index if index is not None else {}

    def at(self, current: Path) -> Vault:
        """The same vault, resolving relative targets from another note."""
        return Vault(self.root, current, self._index)

    def inside(self, path: Path) -> Path | None:
        try:
            resolved = path.resolve()
        except OSError:
            return None
        return resolved if resolved.is_relative_to(self.root) and resolved.is_file() else None

    def index(self) -> dict[str, list[str]]:
        # Shared by every Vault from one preview; filled on the first filename lookup.
        if not self._index:
            count = 0
            for folder, folders, files in os.walk(self.root):
                folders[:] = [name for name in folders if not name.startswith(".") and name != "node_modules"]
                relative = Path(folder).relative_to(self.root)
                for name in files:
                    self._index.setdefault(name.lower(), []).append((relative / name).as_posix())
                    count += 1
                if count >= MAX_FILES:
                    break
            self._index.setdefault("", [])  # Marks the scan done, even for an empty vault.
        return self._index

    def find(self, name: str) -> Path | None:
        """A link target as Obsidian resolves it: a path from this note or the vault root,
        else the file of that name anywhere in the vault, nearest the root first."""
        name = name.strip().lstrip("/")
        if not name:
            return None
        suffix = Path(name).suffix.lower()
        candidates = [name] if suffix in IMAGE_SUFFIXES | NOTE_SUFFIXES else [name + ".md", name]
        for candidate in candidates:
            for base in (self.current.parent, self.root):
                if found := self.inside(base / candidate):
                    return found
        for candidate in candidates:
            wanted = candidate.lower()
            matches = [path for path in self.index().get(Path(candidate).name.lower(), [])
                       if path.lower() == wanted or path.lower().endswith("/" + wanted)]
            for path in sorted(matches, key=lambda path: (path.count("/"), path)):
                if found := self.inside(self.root / path):
                    return found
        return None

    def note(self, path: Path, subpath: str) -> str | None:
        """The embedded part of a note: all of it, one heading's section, or one block."""
        try:
            if path.stat().st_size > MAX_NOTE_BYTES:
                return None
            text = path.read_text(errors="replace")
        except OSError:
            return None
        return section(text, subpath)


def body_lines(text: str) -> list[str]:
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for number, line in enumerate(lines[1:], 1):
            if line.rstrip() in ("---", "..."):
                return lines[number + 1:]  # An embed shows no Properties panel.
    return lines


def outside_fences(lines: list[str]) -> list[bool]:
    result, fence = [], None
    for line in lines:
        match = FENCE.match(line)
        if fence is None and match:
            fence = match[1][0]
            result.append(False)
        elif fence is not None:
            if match and match[1][0] == fence:
                fence = None
            result.append(False)
        else:
            result.append(True)
    return result


def section(text: str, subpath: str) -> str | None:
    lines = body_lines(text)
    if not subpath:
        return "\n".join(lines)
    prose = outside_fences(lines)
    if subpath.startswith("^"):
        return block(lines, prose, subpath[1:])
    # Obsidian writes nested headings as `Note#Parent#Child`; the last one is the target.
    wanted = " ".join(subpath.split("#")[-1].split()).lower()
    for start, line in enumerate(lines):
        match = HEADING.match(line) if prose[start] else None
        if match and " ".join(match[2].split()).lower() == wanted:
            level, end = len(match[1]), start + 1
            while end < len(lines):
                following = HEADING.match(lines[end]) if prose[end] else None
                if following and len(following[1]) <= level:
                    break
                end += 1
            return "\n".join(lines[start:end])
    return None


def block(lines: list[str], prose: list[bool], block_id: str) -> str | None:
    for number, line in enumerate(lines):
        match = BLOCK_ID.search(line) if prose[number] else None
        if not match or match[1] != block_id:
            continue
        marked = line[:match.start()].rstrip()
        if not marked.strip():
            # An ID on a line of its own names the list, table or quote above it,
            # which Obsidian separates from the ID with a blank line.
            end = number
            while end > 0 and not lines[end - 1].strip():
                end -= 1
            start = end
            while start > 0 and lines[start - 1].strip():
                start -= 1
            return "\n".join(lines[start:end]) or None
        if LIST_ITEM.match(line):
            return marked
        start = number
        while start > 0 and lines[start - 1].strip() and not HEADING.match(lines[start - 1]):
            start -= 1
        return "\n".join([*lines[start:number], marked])
    return None
