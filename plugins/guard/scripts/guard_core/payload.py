"""The hook payload on stdin, and the session id inside it."""

from __future__ import annotations

import json
import re
import sys



# --------------------------------------------------------------------------- #
# payload / config / state
# --------------------------------------------------------------------------- #
def _read_payload() -> dict | None:
    try:
        raw = sys.stdin.read()
    except OSError:
        return None
    if not raw.strip():
        return None
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return None
    return payload if isinstance(payload, dict) else None


_SESSION_ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")


def _session_id(payload: dict) -> str | None:
    sid = payload.get("session_id")
    if not isinstance(sid, str) or not sid:
        return None
    # Defensive: session_id is interpolated into state/log filenames. Reject any
    # value that could escape the state directory (path separators, `..`). Note
    # the charclass alone still admits "..", so exclude that explicitly.
    if ".." in sid or not _SESSION_ID_RE.match(sid):
        return None
    return sid
