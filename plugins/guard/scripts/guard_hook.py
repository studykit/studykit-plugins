#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""guard hook dispatcher.

Dependency-free, and run through `uv run --script` — both the hook commands in
`hooks/hooks.json` (as `guide/adapter-guide.md` requires) and this file's own shebang, for
the agents and commands that invoke it over Bash by path. The `requires-python` above is the
reason: a bare `#!/usr/bin/env python3` takes whatever interpreter happens to be first on
the PATH of whatever process launched the hook, and on macOS that is /usr/bin/python3 (3.9),
where `enum.StrEnum` does not exist. Every hook then died with an ImportError traceback in
the user's session — the loudest possible failure, once per hook per turn — and, having
produced no output, left the model free to report success it had not achieved. uv picks an
interpreter that satisfies the constraint instead.

Every subcommand exits 0; blocking is expressed through decision payloads on stdout, never
through a non-zero exit. Internal failures are silent and fail-open (guard never blocks
because its own machinery broke).

This file stays at ``scripts/guard_hook.py`` because that path is a published interface:
``hooks/hooks.json``, the command and agent definitions that shell out to the CLI, the
dispatch playbook, and the Codex adapter all name it. The implementation is in
``guard_core``, one module per layer, and each subcommand's own docstring is in the module
that implements it — see ``guard_core/__init__.py`` for the layering.

Subcommands
-----------
- user-prompt    UserPromptSubmit  — ``guard_core.cmd_turn``
- post-edit      PostToolUse on the write tools — ``guard_core.cmd_edit``
- pre-write      PreToolUse on the write tools — ``guard_core.cmd_write_guard``
- stop           Stop — ``guard_core.cmd_stop``
- session-start  SessionStart — ``guard_core.cmd_session``
- toggle         UserPromptExpansion for ``/guard:toggle`` — ``guard_core.cmd_status``
- status         CLI (stdin JSON), the status-line segment — ``guard_core.cmd_status``
- settings       CLI (argv), run by the ``guard:settings`` skill — ``guard_core.cmd_settings``
- refs-dir       CLI, prints the resolved refs directory — ``guard_core.cmd_settings``
- transcript     CLI (argv), run by an audit agent — ``guard_core.transcript``

Requires Python 3.11+ (``enum.StrEnum``).
"""

from __future__ import annotations

import sys

from guard_core.paths import _project_dir, _trace
from guard_core.transcript import cmd_transcript
from guard_core.cmd_turn import cmd_user_prompt
from guard_core.cmd_edit import cmd_post_edit
from guard_core.cmd_stop import cmd_stop
from guard_core.cmd_session import cmd_session_start
from guard_core.cmd_settings import cmd_refs_dir, cmd_settings
from guard_core.cmd_status import cmd_status, cmd_toggle
from guard_core.cmd_write_guard import cmd_pre_write


SUBCOMMANDS = {
    "user-prompt": cmd_user_prompt,
    "post-edit": cmd_post_edit,
    "pre-write": cmd_pre_write,
    "settings": cmd_settings,
    "stop": cmd_stop,
    "session-start": cmd_session_start,
    "refs-dir": cmd_refs_dir,
    "transcript": cmd_transcript,
    "toggle": cmd_toggle,
    "status": cmd_status,
}


def main() -> int:
    if len(sys.argv) < 2:
        return 0
    handler = SUBCOMMANDS.get(sys.argv[1])
    if handler is None:
        return 0
    try:
        return handler()
    except Exception as e:  # never let guard's own failure surface as a hook error
        _trace(_project_dir(), None, sys.argv[1] if len(sys.argv) > 1 else "?", "exception", error=repr(e))
        return 0


if __name__ == "__main__":
    sys.exit(main())
