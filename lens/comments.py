"""Line-range comments collected in the preview and sent to an agent pane.

Each target agent pane has its own buffer, keyed by pane and terminal identity so a
reused pane ID never inherits another agent's comments. Paths are stored absolute;
the reference text is made relative to the target's working directory only when the
message is composed, because the target decides what "relative" means.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import os
from pathlib import Path
import tempfile
import time


VERSION = 1
MAX_COMMENTS = 500
MAX_NOTE = 1000
MAX_DRAFT = 64 * 1024
MAX_READ = 4 * 1024 * 1024
STALE_DAYS = 30


@dataclass(frozen=True)
class Target:
    pane_id: str
    terminal_id: str

    def key(self) -> str:
        return hashlib.sha256(json.dumps([self.pane_id, self.terminal_id]).encode()).hexdigest()


@dataclass(frozen=True)
class Comment:
    id: int
    path: str  # Absolute.
    start: int  # 1-based, inclusive; 0 and 0 for a whole file or folder.
    end: int
    note: str
    digest: str  # Of the lines when added, to notice later edits.


@dataclass
class Buffer:
    comments: list[Comment] = field(default_factory=list)
    draft: str | None = None
    drafted: set[int] = field(default_factory=set)  # Comment IDs already written into the draft.

    def add(self, path: str, start: int, end: int, note: str, digest: str) -> Comment:
        number = max((comment.id for comment in self.comments), default=0) + 1
        comment = Comment(number, path, start, end, note[:MAX_NOTE], digest)
        self.comments = [*self.comments, comment][-MAX_COMMENTS:]
        return comment

    def clear(self):
        self.comments, self.draft, self.drafted = [], None, set()


def lines_digest(lines: list[str]) -> str:
    return hashlib.sha256("\n".join(lines).encode("utf-8", "surrogatepass")).hexdigest()[:16]


def read_lines(path: Path) -> list[str] | None:
    try:
        with path.open("rb") as stream:
            raw = stream.read(MAX_READ + 1)
    except OSError:
        return None
    if len(raw) > MAX_READ:
        return None
    return raw.decode("utf-8", "replace").splitlines()


def changed(comment: Comment) -> bool:
    """Whether the commented lines differ from when they were added, or are gone."""
    if comment.start == 0:
        return not Path(comment.path).exists()  # A whole file or folder changes too freely to track.
    lines = read_lines(Path(comment.path))
    if lines is None or comment.end > len(lines):
        return True
    return lines_digest(lines[comment.start - 1:comment.end]) != comment.digest


def reference(comment: Comment, cwd: Path | None) -> str:
    path = Path(comment.path)
    shown = str(path)
    if cwd is not None:
        try:
            shown = path.relative_to(cwd).as_posix()
        except ValueError:
            pass  # Outside the target's directory: the absolute path is the only honest one.
    if comment.start == 0:
        # A folder ends in a slash so the agent can tell it from a file; the target's own folder is "./".
        return ("./" if shown == "." else shown + "/") if path.is_dir() else shown
    lines = f"{comment.start}" if comment.start == comment.end else f"{comment.start}-{comment.end}"
    return f"{shown}:{lines}"


def line(comment: Comment, cwd: Path | None) -> str:
    text = reference(comment, cwd)
    return f"{text} — {comment.note}" if comment.note else text


def compose(buffer: Buffer, cwd: Path | None) -> str:
    """The message to edit: the saved draft, then comments added after it was saved."""
    fresh = [line(comment, cwd) for comment in buffer.comments if comment.id not in buffer.drafted]
    if buffer.draft is None:
        return "\n".join(fresh)
    if not fresh:
        return buffer.draft
    return buffer.draft.rstrip("\n") + "\n" + "\n".join(fresh)


def valid_text(value, limit: int) -> bool:
    return isinstance(value, str) and len(value) <= limit and "\0" not in value


def decode_buffer(payload) -> Buffer:
    buffer = Buffer()
    if not isinstance(payload, dict) or payload.get("version") != VERSION:
        return buffer
    for item in payload.get("comments", [])[:MAX_COMMENTS] if isinstance(payload.get("comments"), list) else []:
        if not isinstance(item, dict):
            continue
        number, path, start, end = item.get("id"), item.get("path"), item.get("start"), item.get("end")
        note, digest = item.get("note", ""), item.get("digest", "")
        if (type(number) is int and valid_text(path, 4096) and Path(path).is_absolute()
                and type(start) is int and type(end) is int and (1 <= start <= end or start == end == 0)
                and valid_text(note, MAX_NOTE) and valid_text(digest, 64)):
            buffer.comments.append(Comment(number, path, start, end, note, digest))
    draft = payload.get("draft")
    if valid_text(draft, MAX_DRAFT):
        buffer.draft = draft
        drafted = payload.get("drafted", [])
        if isinstance(drafted, list):
            buffer.drafted = {number for number in drafted if type(number) is int}
    return buffer


def encode_buffer(target: Target, buffer: Buffer) -> dict:
    return {"version": VERSION, "target": {"pane_id": target.pane_id, "terminal_id": target.terminal_id},
            "comments": [{"id": c.id, "path": c.path, "start": c.start, "end": c.end,
                          "note": c.note, "digest": c.digest} for c in buffer.comments],
            "draft": buffer.draft, "drafted": sorted(buffer.drafted)}


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".comments-", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump(value, stream)
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def read_json(path: Path):
    try:
        with path.open("rb") as stream:
            raw = stream.read(MAX_READ + 1)
        return json.loads(raw) if len(raw) <= MAX_READ else None
    except (OSError, ValueError, RecursionError):
        return None


class Store:
    """Buffers and each source pane's last chosen target, under the plugin state directory."""

    def __init__(self, directory: Path):
        self.directory = directory / "comments"

    def load(self, target: Target) -> Buffer:
        return decode_buffer(read_json(self.directory / f"{target.key()}.json"))

    def save(self, target: Target, buffer: Buffer):
        path = self.directory / f"{target.key()}.json"
        if not buffer.comments and buffer.draft is None:
            path.unlink(missing_ok=True)
            return
        write_json(path, encode_buffer(target, buffer))
        self.prune()

    def load_target(self, source: Target) -> Target | None:
        value = read_json(self.directory / "targets" / f"{source.key()}.json")
        if (isinstance(value, dict) and valid_text(value.get("pane_id"), 256)
                and valid_text(value.get("terminal_id"), 256)):
            return Target(value["pane_id"], value["terminal_id"])
        return None

    def save_target(self, source: Target, target: Target):
        path = self.directory / "targets" / f"{source.key()}.json"
        if target == source:
            path.unlink(missing_ok=True)
        else:
            write_json(path, {"pane_id": target.pane_id, "terminal_id": target.terminal_id})

    def prune(self):
        # Closed panes leave their buffers behind; drop the ones untouched for a month.
        cutoff = time.time() - STALE_DAYS * 86400
        for folder in (self.directory, self.directory / "targets"):
            try:
                entries = list(os.scandir(folder))
            except OSError:
                continue
            for entry in entries:
                try:
                    if entry.name.endswith(".json") and entry.stat().st_mtime < cutoff:
                        os.unlink(entry.path)
                except OSError:
                    pass
