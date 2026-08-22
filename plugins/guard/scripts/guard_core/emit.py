"""The two shapes guard writes to stdout.

Both are ``additionalContext`` rather than a decision, and every subcommand exits 0
regardless: blocking is expressed through a decision payload, never through an exit code.
"""

from __future__ import annotations

import json
import sys



def _emit_expansion(msg: str) -> None:
    output = {"hookSpecificOutput": {"hookEventName": "UserPromptExpansion", "additionalContext": msg}}
    json.dump(output, sys.stdout)


def _emit_stop_context(msg: str) -> None:
    """Emit a Stop hook's ``additionalContext``.

    Not ``decision: "block"``. Per the official hooks docs
    (https://code.claude.com/docs/en/hooks, "Stop decision control"; excerpt at
    ``wiki/ref/claude-code-stop-hook-decision-control.md``) both keep the conversation
    going so Claude can act on the text, and both run under the same loop protections
    (``stop_hook_active`` and the 8-consecutive-continuation cap). The difference is how
    it reads: block surfaces as a hook error, while this is labelled ``Stop hook
    feedback``. guard's recommendation is guard working, not guard failing.
    """
    output = {"hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": msg}}
    json.dump(output, sys.stdout)
