"""``stop`` (Stop) — recover writes from interrupted shell calls, silently.

A turn == the transcript ``prompt_id``, and this hook now uses it only to find an interrupted
shell call's pre-use snapshot. It records nothing about the turn, names no answer file, and
reads none of the response.

Everything it used to do about the turn's TEXT is gone as of v0.122.0. The answer file moved
to ``/guard:answer``, which writes its own; the turn audit resolves its target by walking the
transcript when the user asks for one (``transcript._last_auditable_prompt_id``), so there is
no marker to keep and no copy to make. The three skips that protected that marker — non-human
origin, guard's own control commands, a user ``!`` command — moved with it.

Edited files now accumulate across turns and are audited only through the explicit
``audit-files`` checkpoint. Stop remains registered because a cancelled Bash call has no
post-tool event; consuming its pre-call snapshot here is the last chance to retain writes that
completed before the interruption. It emits no context and never launches an audit.
"""

from __future__ import annotations

from .config import _load_config
from .paths import _project_dir, _trace
from .payload import _read_payload, _session_id
from .cmd_edit import recover_shell_writes


def cmd_stop() -> int:
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0

    # The prompt id selects interrupted shell snapshots belonging to this turn.
    prompt_id = payload.get("prompt_id")
    if not (isinstance(prompt_id, str) and prompt_id):
        _trace(project_dir, session_id, "stop", "skip_no_prompt_id")
        return 0

    recovered = recover_shell_writes(project_dir, payload, _load_config(project_dir))
    _trace(project_dir, session_id, "stop", "shell_recovery_only",
           prompt_id=prompt_id, recovered=len(recovered))
    return 0
