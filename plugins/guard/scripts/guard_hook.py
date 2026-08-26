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
- pre-search     PreToolUse on the search tools — ``guard_core.cmd_search``
- stop           Stop — ``guard_core.cmd_stop``
- session-start  SessionStart — ``guard_core.cmd_session``
- toggle         UserPromptExpansion for ``/guard:toggle`` — ``guard_core.cmd_status``
- toggle-cli     CLI (argv), the same mute from a shell — ``guard_core.cmd_status``
- status         CLI (stdin JSON), the status-line segment — ``guard_core.cmd_status``
- settings       CLI (argv), run by the ``guard:settings`` skill — ``guard_core.cmd_settings``
- refs-dir       CLI, prints the resolved refs directory — ``guard_core.cmd_settings``
- candidates     CLI (argv), run by the router — ``guard_core.cmd_candidates``
- inputs         CLI (argv), run by a dispatched agent — ``guard_core.cmd_inputs``
- knowledge-dirs CLI, prints the configured knowledge dirs — ``guard_core.cmd_plan``
- exit-plan      PreToolUse/ExitPlanMode, gates an unaudited plan — ``guard_core.cmd_plan_gate``
- plan-audited   CLI (argv), records the audited plan — ``guard_core.cmd_plan_gate``
- plan-toggle-cli CLI (argv), the plan-audit session switch — ``guard_core.cmd_plan_gate``
- transcript     CLI (argv), run by an audit agent — ``guard_core.transcript``

Requires Python 3.11+ (``enum.StrEnum``).
"""

from __future__ import annotations

import sys

from guard_core.paths import _project_dir, _trace
from guard_core.transcript import cmd_transcript
from guard_core.cmd_turn import cmd_user_prompt
from guard_core.cmd_edit import cmd_post_edit
from guard_core.cmd_search import cmd_pre_search
from guard_core.cmd_stop import cmd_stop
from guard_core.cmd_session import cmd_session_start
from guard_core.cmd_candidates import cmd_candidates
from guard_core.cmd_inputs import cmd_inputs
from guard_core.cmd_plan import cmd_knowledge_dirs
from guard_core.cmd_plan_gate import cmd_exit_plan, cmd_plan_audited, cmd_plan_toggle_cli
from guard_core.cmd_settings import cmd_refs_dir, cmd_settings
from guard_core.cmd_status import cmd_status, cmd_toggle, cmd_toggle_cli


SUBCOMMANDS = {
    "user-prompt": cmd_user_prompt,
    "post-edit": cmd_post_edit,
    "pre-search": cmd_pre_search,
    "settings": cmd_settings,
    "stop": cmd_stop,
    "session-start": cmd_session_start,
    "refs-dir": cmd_refs_dir,
    "candidates": cmd_candidates,
    "inputs": cmd_inputs,
    "knowledge-dirs": cmd_knowledge_dirs,
    "exit-plan": cmd_exit_plan,
    "plan-audited": cmd_plan_audited,
    "plan-toggle-cli": cmd_plan_toggle_cli,
    "transcript": cmd_transcript,
    "toggle": cmd_toggle,
    "toggle-cli": cmd_toggle_cli,
    "status": cmd_status,
}


# The one subcommand that must NOT fail open. Everything else here runs as a hook, where
# swallowing guard's own crash is the whole policy: a broken plugin must not block someone's
# session. `toggle-cli` has no session to protect — a person is standing at a prompt reading
# the output — and silence there is indistinguishable from success. That is not theoretical:
# a missing argument in this verb's own call raised TypeError, was swallowed here, and
# printed nothing while exiting 0, which is exactly what the user would have read as "guard
# is off now".
_MUST_REPORT = {"toggle-cli"}


def main() -> int:
    if len(sys.argv) < 2:
        return 0
    verb = sys.argv[1]
    handler = SUBCOMMANDS.get(verb)
    if handler is None:
        return 0
    try:
        return handler()
    except Exception as e:  # never let guard's own failure surface as a hook error
        _trace(_project_dir(), None, verb, "exception", error=repr(e))
        if verb in _MUST_REPORT:
            print(f"guard: {verb} failed — {e!r}. Nothing changed.", file=sys.stderr)
            return 1
        return 0


if __name__ == "__main__":
    sys.exit(main())
