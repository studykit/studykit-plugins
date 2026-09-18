"""Prepare a read-only HEAD/working-tree comparison for Vim."""
from contextlib import contextmanager
import os
from pathlib import Path
import shutil
import stat
import tempfile

from core import Index, checked_path, git

MAX_DIFF_BYTES = 8 * 1024 * 1024


def snapshots(index: Index, name: str) -> tuple[bytes, bytes]:
    if not index.repository:
        raise ValueError("Git diff is unavailable outside a Git repository")
    path = checked_path(index.root, name)
    relative = path.relative_to(index.repository).as_posix()
    before = after = b""
    head = git(index.repository, "rev-parse", "--verify", "HEAD")
    if head.returncode == 0:
        revision = head.stdout.decode("ascii").strip()
        # Find the original name of a staged rename before looking up its blob.
        changes = git(index.repository, "diff", "--name-status", "-z", "--find-renames",
                      revision, "--")
        if changes.returncode:
            raise RuntimeError(changes.stderr.decode(errors="replace"))
        records = iter(changes.stdout.split(b"\0"))
        for status in records:
            if not status:
                continue
            source = os.fsdecode(next(records, b""))
            if status.startswith((b"R", b"C")):
                destination = os.fsdecode(next(records, b""))
                if destination == relative:
                    relative = source
                    break
        entry = git(index.repository, "ls-tree", "-z", revision, "--", relative)
        if entry.returncode:
            raise RuntimeError(entry.stderr.decode(errors="replace"))
        if entry.stdout:
            metadata = entry.stdout.split(b"\t", 1)[0].split()
            if metadata[1] != b"blob":
                raise ValueError("Directory and submodule diffs are not supported")
            blob = metadata[2].decode("ascii")
            size = git(index.repository, "cat-file", "-s", blob)
            if size.returncode:
                raise RuntimeError(size.stderr.decode(errors="replace"))
            if int(size.stdout) > MAX_DIFF_BYTES:
                raise ValueError("Diff is limited to files up to 8 MiB per side")
            content = git(index.repository, "cat-file", "blob", blob)
            if content.returncode:
                raise RuntimeError(content.stderr.decode(errors="replace"))
            before = content.stdout
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK)
    except FileNotFoundError:
        pass  # Deletions compare the HEAD blob to an empty buffer.
    else:
        with os.fdopen(fd, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise ValueError("Only regular files can be compared")
            after = stream.read(MAX_DIFF_BYTES + 1)
        if len(after) > MAX_DIFF_BYTES:
            raise ValueError("Diff is limited to files up to 8 MiB per side")
    if b"\0" in before or b"\0" in after:
        raise ValueError("Binary files cannot be compared in the text diff viewer")
    return before, after


@contextmanager
def comparison(index: Index, name: str):
    binary = shutil.which("vimdiff") or shutil.which("vim")
    if not binary:
        raise ValueError("Install Vim with diff support (vimdiff or vim) to compare files")
    before, after = snapshots(index, name)
    with tempfile.TemporaryDirectory(prefix="file-nav-diff-") as directory:
        root = Path(directory)
        left, right = Path("HEAD") / name, Path("WORKTREE") / name
        for relative, content in ((left, before), (right, after)):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        # Both buffers are disposable snapshots, so even :w! cannot edit the project.
        command = [binary, "-N", "-u", "NONE", "-U", "NONE", "-i", "NONE", "-n", "-R",
                   "--noplugin", "--cmd", "set nomodeline", "-d", "-O",
                   "-S", str(Path(__file__).with_name("vimdiff.vim")),
                   "--", str(left), str(right)]
        yield command, root
