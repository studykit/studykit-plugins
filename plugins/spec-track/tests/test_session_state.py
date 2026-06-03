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
from session_state import (  # noqa: E402
    read_authoring_resolution,
    read_subagent_starts,
    record_authoring_resolution,
)


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


def test_record_and_read_authoring_resolution_round_trip(tmp_path: Path) -> None:
    key = {"type": "task", "role": "issue", "provider": "github", "scope": "content"}

    assert record_authoring_resolution(
        tmp_path,
        "claude",
        "sess-1",
        tag="reading",
        anchor="task-issue",
        key=key,
        emitted_at="2026-05-21T00:00:00+00:00",
    )

    entry = read_authoring_resolution(
        tmp_path, "claude", "sess-1", tag="reading", anchor="task-issue"
    )

    assert entry is not None
    assert entry["key"] == key
    assert entry["emitted_at"] == "2026-05-21T00:00:00+00:00"


def test_record_authoring_resolution_separates_tags(tmp_path: Path) -> None:
    key = {"type": "task", "role": "issue", "provider": "github", "scope": "content"}

    assert record_authoring_resolution(
        tmp_path,
        "claude",
        "sess-1",
        tag="reading",
        anchor="task-issue",
        key=key,
        emitted_at="2026-05-21T00:00:00+00:00",
    )
    assert record_authoring_resolution(
        tmp_path,
        "claude",
        "sess-1",
        tag="notes",
        anchor="task-issue",
        key=key,
        emitted_at="2026-05-21T00:00:01+00:00",
    )

    reading_entry = read_authoring_resolution(
        tmp_path, "claude", "sess-1", tag="reading", anchor="task-issue"
    )
    notes_entry = read_authoring_resolution(
        tmp_path, "claude", "sess-1", tag="notes", anchor="task-issue"
    )

    assert reading_entry is not None
    assert notes_entry is not None
    assert reading_entry["emitted_at"] == "2026-05-21T00:00:00+00:00"
    assert notes_entry["emitted_at"] == "2026-05-21T00:00:01+00:00"


def test_record_authoring_resolution_overwrites_existing_entry(tmp_path: Path) -> None:
    record_authoring_resolution(
        tmp_path,
        "claude",
        "sess-1",
        tag="reading",
        anchor="task-issue",
        key={"type": "task", "role": "issue", "provider": "github", "scope": "content"},
        emitted_at="2026-05-21T00:00:00+00:00",
    )
    record_authoring_resolution(
        tmp_path,
        "claude",
        "sess-1",
        tag="reading",
        anchor="task-issue",
        key={"type": "task", "role": "issue", "provider": "jira", "scope": "content"},
        emitted_at="2026-05-21T00:01:00+00:00",
    )

    entry = read_authoring_resolution(
        tmp_path, "claude", "sess-1", tag="reading", anchor="task-issue"
    )

    assert entry is not None
    assert entry["key"]["provider"] == "jira"
    assert entry["emitted_at"] == "2026-05-21T00:01:00+00:00"


def test_record_authoring_resolution_handles_null_provider(tmp_path: Path) -> None:
    record_authoring_resolution(
        tmp_path,
        "claude",
        "sess-1",
        tag="reading",
        anchor="spike-issue",
        key={"type": "spike", "role": "issue", "provider": None, "scope": "content"},
        emitted_at="2026-05-21T00:00:00+00:00",
    )

    entry = read_authoring_resolution(
        tmp_path, "claude", "sess-1", tag="reading", anchor="spike-issue"
    )

    assert entry is not None
    assert entry["key"]["provider"] is None


def test_read_authoring_resolution_returns_none_when_absent(tmp_path: Path) -> None:
    assert (
        read_authoring_resolution(
            tmp_path, "claude", "sess-1", tag="reading", anchor="task-issue"
        )
        is None
    )


def test_authoring_resolutions_survive_concurrent_recorders(tmp_path: Path) -> None:
    if session_state.fcntl is None:
        pytest.skip("session state locking requires fcntl on this platform")

    start_file = tmp_path / "start"
    recorder = tmp_path / "record_authoring_resolution.py"
    recorder.write_text(
        "\n".join(
            [
                "import sys",
                "import time",
                "from pathlib import Path",
                f"sys.path.insert(0, {str(_SCRIPTS_DIR)!r})",
                "from session_state import record_authoring_resolution",
                "project = Path(sys.argv[1])",
                "start_file = Path(sys.argv[2])",
                "anchor = sys.argv[3]",
                "deadline = time.time() + 5",
                "while not start_file.exists():",
                "    if time.time() > deadline:",
                "        raise SystemExit('timed out waiting for start signal')",
                "    time.sleep(0.01)",
                "ok = record_authoring_resolution(",
                "    project,",
                "    'codex',",
                "    'parent-session',",
                "    tag='reading',",
                "    anchor=anchor,",
                "    key={",
                "        'type': anchor.split('-')[0],",
                "        'role': 'issue',",
                "        'provider': 'github',",
                "        'scope': 'content',",
                "    },",
                "    emitted_at='2026-05-21T00:00:00+00:00',",
                ")",
                "raise SystemExit(0 if ok else 1)",
                "",
            ]
        ),
        encoding="utf-8",
    )

    expected_anchors = {f"a{index:02d}-issue" for index in range(8)}
    processes = [
        subprocess.Popen(
            [sys.executable, str(recorder), str(tmp_path), str(start_file), anchor],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for anchor in sorted(expected_anchors)
    ]
    start_file.write_text("go\n", encoding="utf-8")

    for process in processes:
        stdout, stderr = process.communicate(timeout=10)
        assert process.returncode == 0, stdout + stderr

    for anchor in expected_anchors:
        entry = read_authoring_resolution(
            tmp_path, "codex", "parent-session", tag="reading", anchor=anchor
        )
        assert entry is not None, anchor
        assert entry["key"]["type"] == anchor.split("-")[0]
