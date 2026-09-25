"""Read-only commit and file history for the navigator."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import re
import subprocess


PAGE_SIZE = 100
MAX_PATCH_BYTES = 512 * 1024


@dataclass(frozen=True)
class Commit:
    oid: str
    date: str
    author: str
    subject: str
    body: str
    path: str = ""


@dataclass(frozen=True)
class ChangedFile:
    status: str
    path: str
    previous: str = ""


def run(repository: Path, *args: str, input: bytes | None = None) -> bytes:
    result = subprocess.run(
        ["git", "--literal-pathspecs", "-C", str(repository), *args],
        input=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode(errors="replace").strip() or "Git history unavailable")
    return result.stdout


def branch(repository: Path) -> str:
    return run(repository, "branch", "--show-current").decode(errors="replace").strip() or "detached HEAD"


def commits(repository: Path, offset: int = 0, path: str = "") -> tuple[list[Commit], bool]:
    # --skip can jump over a rename before --follow has learned the old path.
    # For file history, walk from HEAD and slice after rename tracking.
    count = offset + PAGE_SIZE + 1 if path else PAGE_SIZE + 1
    args = ["log", "--date=short", f"--max-count={count}",
            "--format=COMMIT%x00%H%x00%ad%x00%an%x00%s%x00%b%x00", "-z"]
    if not path:
        args.append(f"--skip={offset}")
    if path:
        args.extend(["--follow", "--name-only", "--", path])
    data = run(repository, *args)
    result = []
    # A filename can itself be COMMIT, so accept a delimiter only when followed
    # by a complete object ID. NUL is forbidden in Git paths.
    parts = re.split(rb"COMMIT\0(?=[0-9a-f]{40}(?:\0|[0-9a-f]{24}\0))", data)
    for part in parts[1:]:
        fields = part.split(b"\0", 5)
        if len(fields) < 6:
            continue
        oid, date, author, subject, body = (field.decode("utf-8", "replace") for field in fields[:5])
        names = [name for name in fields[5].split(b"\0") if name]
        # Git puts one separator newline before the first name in -z log output.
        first = names[0].removeprefix(b"\n") if names else b""
        historic_path = os.fsdecode(first) if path and first else path
        result.append(Commit(oid, date, author, subject, body.strip(), historic_path))
    start = offset if path else 0
    return result[start:start + PAGE_SIZE], len(result) > start + PAGE_SIZE


def parents(repository: Path, oid: str) -> list[str]:
    fields = run(repository, "rev-list", "--parents", "-n", "1", oid).decode("ascii").split()
    return fields[1:]


def empty_tree(repository: Path) -> str:
    return run(repository, "hash-object", "-t", "tree", "--stdin", input=b"").decode("ascii").strip()


def changed_files(repository: Path, oid: str) -> list[ChangedFile]:
    parent = (parents(repository, oid) or [empty_tree(repository)])[0]
    data = run(repository, "diff", "--name-status", "-z", "--find-renames", parent, oid)
    fields = iter(data.split(b"\0"))
    result = []
    for raw in fields:
        if not raw:
            continue
        status = raw.decode("ascii", "replace")
        first = next(fields, b"")
        if status.startswith(("R", "C")):
            destination = next(fields, b"")
            result.append(ChangedFile(status, os.fsdecode(destination), os.fsdecode(first)))
        else:
            result.append(ChangedFile(status, os.fsdecode(first)))
    return result


def patch(repository: Path, oid: str, file: ChangedFile) -> str:
    parent = (parents(repository, oid) or [empty_tree(repository)])[0]
    paths = [file.previous, file.path] if file.previous else [file.path]
    data = run(repository, "diff", "--no-ext-diff", "--no-textconv", "--find-renames",
               "--binary", parent, oid, "--", *paths)
    if len(data) > MAX_PATCH_BYTES:
        data = data[:MAX_PATCH_BYTES] + b"\n[Diff truncated at 512 KiB]"
    return data.decode("utf-8", "replace") or "(No text diff for this file)"
