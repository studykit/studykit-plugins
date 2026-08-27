"""``handover-written`` — record the handover file this session just wrote.

Run from the ``handover`` skill, through the ``guard-handover`` wrapper on ``PATH``, as its
last step. It writes one path into ``state/<sid>.json``; everything that happens afterwards is
``cmd_session``'s — ``SessionEnd`` on ``/clear`` copies the path into the handoff record, and
the ``SessionStart`` that replaces the session tells the model to offer it.

**Why the skill records it rather than the next session looking for it.** The alternative was
scanning ``.handover/`` at session start for the newest untracked file, which needs no
cooperation from the skill and answers a different question: it finds a handover, not *this
session's* handover. A file left by a session two days ago, or by a colleague, or by the same
session three clears ago, all look identical to that scan, and each one offered is a session
told to resume work that is already done. The path recorded here is known to belong to the
session the ``/clear`` is replacing, which is the only case the offer is right for.

The cost is that a skill step can be skipped: a session that crashes between writing the file
and running this leaves nothing to carry. That is the correct direction to fail — nothing is
offered, and the user still has the file.
"""

from __future__ import annotations

import os
import sys

from pathlib import Path

from .config import CLEAR_INHERIT_MAX_AGE_SECONDS, _load_config
from .paths import _cli_project_dir, _trace
from .state import _read_state, _write_state


def cmd_handover_written() -> int:
    """Record ``<path>`` as this session's handover.

        handover-written <handover-file-path>

    The path is resolved to an absolute one before it is stored: it is read back in a
    different process, in a different session, whose cwd is nobody's to predict.

    The file must exist. This is not validation for its own sake — it is what makes the check
    happen while someone can still act on it. The alternative is a record that names a path
    the next session cannot open, discovered at the one moment the session has no way to ask
    what went wrong.

    Fail-open and quiet, like ``plan-audited``: a missing session id or an unwritable state
    directory prints to stderr and exits 0. The cost is one un-offered handover, and the file
    itself — the thing worth having — is already on disk.
    """
    session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    project_dir = _cli_project_dir()
    if not session_id:
        print("guard-handover: no CLAUDE_CODE_SESSION_ID in this environment — nothing "
              "recorded. The handover file itself is unaffected.", file=sys.stderr)
        return 0
    if len(sys.argv) < 3 or not sys.argv[2].strip():
        print("guard-handover: needs the handover file path.", file=sys.stderr)
        return 0

    try:
        path = Path(sys.argv[2].strip()).expanduser().resolve()
    except (OSError, RuntimeError) as exc:
        print(f"guard-handover: cannot resolve that path ({exc}).", file=sys.stderr)
        return 0
    if not path.is_file():
        print(f"guard-handover: {path} does not exist — write the handover first, then "
              "record it.", file=sys.stderr)
        _trace(project_dir, session_id, "handover-written", "missing_file")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    state["handover_file"] = str(path)
    _write_state(project_dir, session_id, state)
    # The window is read from the constant rather than written out: it is the handoff
    # record's expiry, and a sentence naming a number would go stale the moment it moved.
    minutes = max(1, CLEAR_INHERIT_MAX_AGE_SECONDS // 60)
    print(f"guard: handover recorded — {path}. Clear this session within {minutes} minutes "
          "and the session replacing it is offered this file.")
    _trace(project_dir, session_id, "handover-written", "recorded")
    return 0
