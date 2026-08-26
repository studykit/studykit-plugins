"""The three shapes guard writes to stdout.

Every subcommand exits 0 regardless: blocking is expressed through a decision payload,
never through an exit code.
"""

from __future__ import annotations

import json
import sys


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


def _emit_pre_tool_deny(reason: str) -> None:
    """Emit a PreToolUse denial, blocking the tool call before it runs.

    `permissionDecision: "deny"` rather than `"ask"`: the refused calls are unbounded
    filesystem walks, and a permission dialog in front of one only moves the decision to a
    user who did not write the command. Values and shape: official hooks docs
    (https://code.claude.com/docs/en/hooks.md); excerpt at
    ``wiki/ref/claude-code-pretooluse-permission-decision.md``.

    `reason` reaches the MODEL, verbatim, as the tool's `<error>` result — measured, not
    assumed (``wiki/ref/claude-code-pretooluse-deny-reason-visibility.md``). The docs only
    promise the reason is shown to the user on `"ask"`. So this string is written for the
    model that must now do something else, and the same measurement is why it states a
    prohibition and not a redirect to some other agent: a deny reason is weighed as tool
    output, so a redirect in one is a suggestion the session may decline.
    """
    output = {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                     "permissionDecision": "deny",
                                     "permissionDecisionReason": reason}}
    json.dump(output, sys.stdout)


def _emit_post_tool_block(reason: str) -> None:
    """Emit a PostToolUse block, sending ``reason`` to the model after the tool ran.

    The tool has already executed — blocking here does not undo it, it tells the model to do
    something before going on. That is exactly the shape the plan gate needs on
    ``ExitPlanMode``: the plan is approved and plan mode is over, and what must not happen
    next is the plan being built unaudited.

    ``decision: "block"`` with ``reason`` rather than ``additionalContext``: the reason is
    documented as the "explanation shown to Claude when decision is block", and a plain
    context string is advisory where this must redirect the turn. Fields and semantics:
    official hooks docs (https://code.claude.com/docs/en/hooks.md); excerpt at
    ``wiki/ref/claude-code-hook-enforcement-facts.md``.
    """
    json.dump({"decision": "block", "reason": reason}, sys.stdout)
