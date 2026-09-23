"""Disposable HEAD/working-tree snapshots, independent of Herdr and agent hosts."""

from contextlib import contextmanager
import os
from pathlib import Path
import shutil
import stat
import subprocess
import tempfile


MAX_DIFF_BYTES = 8 * 1024 * 1024


def _git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "--literal-pathspecs", "-C", str(root), *args],
        capture_output=True, timeout=15,
    )


def _output(root: Path, *args: str) -> bytes:
    result = _git(root, *args)
    if result.returncode:
        raise ValueError(result.stderr.decode(errors="replace").strip() or "Git diff failed")
    return result.stdout


def snapshots(project: Path, path: Path) -> tuple[str, bytes, bytes]:
    project = project.resolve()
    path = project / path
    path = path.parent.resolve() / path.name
    if not path.is_relative_to(project) or not path.resolve().is_relative_to(project):
        raise ValueError("File must be inside the project directory")
    repository = _git(project, "rev-parse", "--show-toplevel")
    if repository.returncode:
        raise ValueError("Git diff is unavailable outside a Git repository")
    root = Path(os.fsdecode(repository.stdout).rstrip("\n")).resolve()
    name = path.relative_to(root).as_posix()
    original = name
    before = after = b""
    head = _git(root, "rev-parse", "--verify", "HEAD")
    if head.returncode == 0:
        revision = head.stdout.decode("ascii").strip()
        # Staged renames need the original HEAD path, as in Lens.
        records = iter(_output(root, "diff", "--name-status", "-z", "--find-renames",
                               revision, "--").split(b"\0"))
        for status in records:
            if not status:
                continue
            source = os.fsdecode(next(records, b""))
            if status.startswith((b"R", b"C")):
                destination = os.fsdecode(next(records, b""))
                if destination == name:
                    original = source
                    break
        entry = _output(root, "ls-tree", "-z", revision, "--", original)
        if entry:
            metadata = entry.split(b"\t", 1)[0].split()
            if metadata[1] != b"blob" or metadata[0] == b"120000":
                raise ValueError("Only regular files can be compared")
            blob = metadata[2].decode("ascii")
            if int(_output(root, "cat-file", "-s", blob)) > MAX_DIFF_BYTES:
                raise ValueError("Diff is limited to files up to 8 MiB per side")
            before = _output(root, "cat-file", "blob", blob)
    if path.is_symlink():
        raise ValueError("Only regular files can be compared")
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK)
    except FileNotFoundError:
        pass
    else:
        with os.fdopen(fd, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise ValueError("Only regular files can be compared")
            after = stream.read(MAX_DIFF_BYTES + 1)
        if len(after) > MAX_DIFF_BYTES:
            raise ValueError("Diff is limited to files up to 8 MiB per side")
    if b"\0" in before or b"\0" in after:
        raise ValueError("Binary files cannot be compared in the text diff viewer")
    return name, before, after


@contextmanager
def comparison(project: Path, path: Path):
    binary = shutil.which("vimdiff") or shutil.which("vim")
    if not binary:
        raise ValueError("Install Vim with diff support (vimdiff or vim) to compare files")
    name, before, after = snapshots(project, path)
    with tempfile.TemporaryDirectory(prefix="guard-diff-") as directory:
        root = Path(directory)
        left, right = Path("HEAD") / name, Path("WORKTREE") / name
        for relative, content in ((left, before), (right, after)):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        # Even a forced save targets a disposable snapshot, not the project file.
        command = [binary, "-N", "-u", "NONE", "-U", "NONE", "-i", "NONE", "-n", "-R",
                   "--noplugin", "--cmd", "set nomodeline", "-d", "-O",
                   "-S", str(Path(__file__).with_name("vimdiff.vim")),
                   "--", str(left), str(right)]
        yield command, root
