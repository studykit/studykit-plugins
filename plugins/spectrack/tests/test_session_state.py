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
from session_state import read_subagent_starts  # noqa: E402


def test_subagent_start_records_survive_concurrent_parent_state_updates(
    tmp_path: Path,
) -> None:
    if session_state.fcntl is None:
        pytest.skip("session state locking requires fcntl on this platform")

    start_file = tmp_path / "start"
    recorder = tmp_path / "record_subagent_start.py"
    recorder.write_text(
        "\n".join(
            [
                "import sys",
                "import time",
                "from pathlib import Path",
                f"sys.path.insert(0, {str(_SCRIPTS_DIR)!r})",
                "from session_state import record_subagent_start",
                "project = Path(sys.argv[1])",
                "start_file = Path(sys.argv[2])",
                "agent_id = sys.argv[3]",
                "deadline = time.time() + 5",
                "while not start_file.exists():",
                "    if time.time() > deadline:",
                "        raise SystemExit('timed out waiting for start signal')",
                "    time.sleep(0.01)",
                "ok = record_subagent_start(",
                "    project,",
                "    'codex',",
                "    'parent-session',",
                "    agent_id=agent_id,",
                "    agent_type='worker',",
                ")",
                "raise SystemExit(0 if ok else 1)",
                "",
            ]
        ),
        encoding="utf-8",
    )

    expected_agent_ids = {f"agent-{index:02d}" for index in range(16)}
    processes = [
        subprocess.Popen(
            [sys.executable, str(recorder), str(tmp_path), str(start_file), agent_id],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for agent_id in sorted(expected_agent_ids)
    ]
    start_file.write_text("go\n", encoding="utf-8")

    for process in processes:
        stdout, stderr = process.communicate(timeout=10)
        assert process.returncode == 0, stdout + stderr

    starts = read_subagent_starts(tmp_path, "codex", "parent-session")

    assert {item["agent_id"] for item in starts} == expected_agent_ids
    assert {item["agent_type"] for item in starts} == {"worker"}
