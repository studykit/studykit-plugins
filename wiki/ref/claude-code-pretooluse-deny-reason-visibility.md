# How a PreToolUse `deny` reason reaches the model

Source: probe of `claude` 2.1.240 (Claude Code), headless `claude -p`

Retrieved: 2026-08-23

The hooks reference documents the `permissionDecision` values and says `"deny"` "Blocks the
tool call", and it documents `permissionDecisionReason` as accompanying the decision — but it
states only that the reason is shown to the **user** in the permission dialog for `"ask"`. It
does not say what happens to the reason on `"deny"`, and the prompt-hooks page records the same
gap in the other direction: it does not specify "how a block/deny is surfaced to the model."
(Both excerpts: `claude-code-pretooluse-permission-decision.md`,
`claude-code-prompt-hooks.md`.) So this was measured.

## What was run

A project-local `.claude/settings.json` registered a `PreToolUse` hook on the matcher
`WebFetch|WebSearch` whose command emitted:

```json
{"hookSpecificOutput": {"hookEventName": "PreToolUse",
                        "permissionDecision": "deny",
                        "permissionDecisionReason": "<a sentence naming a replacement agent>"}}
```

Then, from that project:

```
claude -p "Use the WebFetch tool on https://example.com right now. Then tell me exactly
what happened: quote verbatim any message you got back from the tool or from a hook."
--allowedTools WebFetch
```

## Result

**The reason reaches the model verbatim, as the tool's error result.** The child reported that
its `WebFetch` call returned "not the page content but an `<error>`", and quoted the reason
string back word for word. It never received the page.

Two further observations from the same run:

**The tool call is attempted, then blocked.** The model selected and invoked `WebFetch`
normally — `PreToolUse` is what stops it — so a deny costs one tool round-trip, not zero. It
is not equivalent to withholding the tool from the model's list.

**A reason that names a replacement is not self-executing.** The child read the instruction to
dispatch a named subagent and declined to follow it, giving two grounds: its own session
instructions told it not to use the Agent tool unless the user asked, and the named agent was
not in its available agent list. The second is an artifact of the probe setup (no plugin
installed there), but the first is not: a deny reason is read as tool output, not as a user
instruction, and it is weighed against whatever else the session has been told. So a deny
reliably enforces a *prohibition* and only suggests a *redirect* — anything relying on the
redirect actually happening needs to state it somewhere the session treats as instruction.
