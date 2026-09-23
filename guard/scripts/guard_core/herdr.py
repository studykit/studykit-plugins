"""Best-effort presentation of Guard's pending queue inside Herdr."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any


_BUCKETS = ("edited_files", "edited_agent_docs", "edited_docs")
_SOURCE = "plugin:studykit.guard"


def report_pending(state: dict[str, Any]) -> None:
    """Refresh the current pane's display token when Guard runs inside Herdr.

    The report is deliberately optional. Herdr rejects plugin-owned metadata when the
    companion plugin is not linked or is disabled; that is the clean opt-out path and Guard
    remains fully functional without Herdr.
    """
    if os.environ.get("HERDR_ENV") != "1":
        return
    pane_id = os.environ.get("HERDR_PANE_ID")
    if not pane_id:
        return
    paths = {
        raw
        for bucket in _BUCKETS
        for raw in state.get(bucket, [])
        if isinstance(raw, str) and raw and Path(raw).is_file()
    }
    binary = os.environ.get("HERDR_BIN_PATH") or "herdr"
    command = [binary, "pane", "report-metadata", pane_id, "--source", _SOURCE]
    if paths:
        command.extend(["--token", f"guard_pending=Guard · {len(paths)} pending"])
    else:
        command.extend(["--clear-token", "guard_pending"])
    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       timeout=2, check=False)
    except (OSError, subprocess.SubprocessError):
        pass
