# Stop hook decision control (Claude Code)

Source: https://code.claude.com/docs/en/hooks (raw markdown: `https://code.claude.com/docs/en/hooks.md`), section "Stop decision control"
Retrieved: 2026-08-21

Why this is saved: guard's Stop hook chooses between `decision: "block"` and
`hookSpecificOutput.additionalContext` for delivering its audit recommendation. The
difference in continuation behavior and in how the transcript labels the output is the
whole basis of that choice.

## Excerpt — "Stop decision control"

> `Stop` and `SubagentStop` hooks can control whether Claude continues. In addition to
> the JSON output fields available to all hooks, your hook script can return these
> event-specific fields:
>
> | Field | Description |
> | --- | --- |
> | `decision` | `"block"` prevents Claude from stopping. Omit to allow Claude to stop |
> | `reason` | Required when `decision` is `"block"`. Tells Claude why it should continue |
> | `hookSpecificOutput.additionalContext` | Non-error feedback for Claude. The conversation continues so Claude can act on it, but unlike `decision: "block"` it is shown in the transcript as hook feedback rather than a hook error |
>
> A hook that blocks by exiting 2 routes the same way as `reason`: Claude receives the
> stderr message as the explanation for why it should continue.
>
> Use `additionalContext` when the hook is working as designed and giving Claude
> guidance, such as "run the test suite before finishing". It keeps the conversation
> going through the same loop protections as `decision: "block"`, namely the
> `stop_hook_active` input and the 8-consecutive-continuation cap, but the transcript
> labels it `Stop hook feedback` and no hook error notification is shown:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "additionalContext": "Please run the test suite before finishing"
  }
}
```

## Excerpt — the decision-control summary table

> | UserPromptSubmit, UserPromptExpansion, PostToolUse, PostToolUseFailure, PostToolBatch, Stop, SubagentStop, ConfigChange, PreCompact | Top-level `decision` | `decision: "block"`, `reason`. Stop and SubagentStop also accept `hookSpecificOutput.additionalContext` for non-error feedback that continues the conversation |

## Excerpt — how `additionalContext` reaches the model

> The `additionalContext` field passes a string from your hook into Claude's context
> window. Claude Code wraps the string in a system reminder and inserts it into the
> conversation at the point where the hook fired. Claude reads the reminder on the next
> model request, but it doesn't appear as a chat message in the interface.

> Hook output strings, including `additionalContext`, `systemMessage`, and plain stdout,
> are capped at 10,000 characters. Output that exceeds this limit is saved to a file and
> replaced with a preview and file path […]

## What guard takes from this

- `additionalContext` on Stop is **not** a passive note for the next turn: the
  conversation continues and Claude acts on it in the same turn, exactly as with
  `decision: "block"`.
- The loop protections are identical (`stop_hook_active`, 8-consecutive-continuation
  cap), so guard's once-per-turn guard is unaffected by the choice.
- The only differences are cosmetic and they favor `additionalContext`: the transcript
  labels it `Stop hook feedback` rather than raising a hook error. A recommendation is
  guidance working as designed, not an error, so guard uses `additionalContext`.
- The 10,000-character cap bounds the recommendation text; guard passes file paths
  rather than turn content, so it stays far below it.
