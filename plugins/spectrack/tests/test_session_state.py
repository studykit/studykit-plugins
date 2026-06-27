"""Tests for workflow hook session state storage."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import session_state  # noqa: E402
from session_state import read_session_issues  # noqa: E402


def test_issue_records_survive_concurrent_parent_state_updates(
    tmp_path: Path,
) -> None:
    if session_state.fcntl is None:
        pytest.skip("session state locking requires fcntl on this platform")

    start_file = tmp_path / "start"
    recorder = tmp_path / "record_session_issues.py"
    recorder.write_text(
        "\n".join(
            [
                "import sys",
                "import time",
                "from pathlib import Path",
                f"sys.path.insert(0, {str(_SCRIPTS_DIR)!r})",
                "from session_state import record_session_issues",
                "project = Path(sys.argv[1])",
                "start_file = Path(sys.argv[2])",
                "issue = sys.argv[3]",
                "deadline = time.time() + 5",
                "while not start_file.exists():",
                "    if time.time() > deadline:",
                "        raise SystemExit('timed out waiting for start signal')",
                "    time.sleep(0.01)",
                "record_session_issues(",
                "    project,",
                "    'parent-session',",
                "    [issue],",
                "    'announced',",
                "    runtime='codex',",
                ")",
                "raise SystemExit(0)",
                "",
            ]
        ),
        encoding="utf-8",
    )

    expected_issues = {str(100 + index) for index in range(16)}
    processes = [
        subprocess.Popen(
            [sys.executable, str(recorder), str(tmp_path), str(start_file), issue],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for issue in sorted(expected_issues)
    ]
    start_file.write_text("go\n", encoding="utf-8")

    for process in processes:
        stdout, stderr = process.communicate(timeout=10)
        assert process.returncode == 0, stdout + stderr

    # Every concurrent append must survive: the exclusive file lock in
    # _mutate_session_state serializes the read-modify-write so no recorder
    # clobbers another's entry.
    recorded = read_session_issues(tmp_path, "parent-session", "announced", runtime="codex")

    assert recorded == expected_issues
