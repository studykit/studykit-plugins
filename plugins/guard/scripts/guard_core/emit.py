"""The three shapes guard writes to stdout.

Every subcommand exits 0 regardless: blocking is expressed through a decision payload,
never through an exit code.
"""

from __future__ import annotations

import json
import sys



def _emit_expansion(msg: str) -> None:
    """Emit ``/guard:toggle``'s result and END the turn, without invoking a model.

    ``decision: "block"`` rather than ``additionalContext``, which is the opposite of the
    Stop choice below and for a reason that does not carry over: on Stop the two are
    presentation, both continuing the turn, while here they are the whole cost. The
    expansion path sends ``additionalContext`` *to the model* — the docs list this event
    among the three where "Claude Code adds plain-text stdout as context that Claude can
    see and act on" — so relaying a sentence the hook has already finished costs a model
    call. ``reason`` is instead "Shown to the user", and blocking means "the turn ends
    ... regardless of ``continue``". Source: official hooks docs
    (https://code.claude.com/docs/en/hooks.md, "UserPromptExpansion decision control");
    excerpt at ``wiki/ref/claude-code-userpromptexpansion-hook.md``, fetched 2026-08-25.

    So ``msg`` is read by a person, not by an agent: it must be a finished sentence and
    must not carry instructions for a model that will never see it.

    What the docs do NOT say is that inference is skipped — "the turn ends" is the
    strongest wording on the page, and the model-call lifecycle is never described. The
    turn ending is documented; zero inference is an inference.

    The command file behind the matcher still has to exist. The host resolves ``/name``
    against the command/skill files BEFORE any hook runs, so deleting it disarms this
    silently (``wiki/ref/claude-code-userpromptexpansion-needs-a-command-file.md``).
    """
    json.dump({"decision": "block", "reason": msg}, sys.stdout)


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
