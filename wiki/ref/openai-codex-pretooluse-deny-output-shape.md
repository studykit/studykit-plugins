# Codex — `PreToolUse` deny/block output shape

Source: https://learn.chatgpt.com/docs/hooks.md
Retrieved: 2026-08-26

Fetched to settle: what exact JSON on stdout a Codex `PreToolUse` hook must return to
block/deny a tool call before it runs, what carries the reason, where the reason surfaces,
and whether exit codes matter.

## The block/deny shapes

> Plain text on `stdout` is ignored.
>
> JSON on `stdout` can use `systemMessage`. To deny a supported tool call, return
> this hook-specific shape:
>
> ```json
> {
>   "hookSpecificOutput": {
>     "hookEventName": "PreToolUse",
>     "permissionDecision": "deny",
>     "permissionDecisionReason": "Destructive command blocked by hook."
>   }
> }
> ```
>
> Codex also accepts this older block shape:
>
> ```json
> {
>   "decision": "block",
>   "reason": "Destructive command blocked by hook."
> }
> ```
>
> You can also use exit code `2` and write the blocking reason to `stderr`.

So Codex supports two accepted shapes for the same effect — the current one nested under
`hookSpecificOutput` (`permissionDecision: "deny"` + `permissionDecisionReason`), and an
older flat one (`decision: "block"` + `reason`) kept for compatibility. Exit code `2` with the
reason on stderr is a third, non-JSON path to the same block outcome.

## Non-blocking companions, for contrast

> To add model-visible context without blocking, return
> `hookSpecificOutput.additionalContext`:
>
> ```json
> {
>   "hookSpecificOutput": {
>     "hookEventName": "PreToolUse",
>     "additionalContext": "The pending command touches generated files."
>   }
> }
> ```
>
> To rewrite a supported tool call without blocking, return
> `permissionDecision: "allow"` with `updatedInput`:
>
> ```json
> {
>   "hookSpecificOutput": {
>     "hookEventName": "PreToolUse",
>     "permissionDecision": "allow",
>     "updatedInput": {
>       "command": "echo rewritten"
>     }
>   }
> }
> ```
>
> For Bash commands and `apply_patch`, `updatedInput` must include a string
> `command` field. For MCP and other local function tools, `updatedInput` is the
> replacement arguments object. Return `updatedInput` only with
> `permissionDecision: "allow"`; other `updatedInput` shapes are reported as
> errors.
>
> `permissionDecision: "ask"`, legacy `decision: "approve"`, `continue: false`,
> `stopReason`, and `suppressOutput` are parsed but not supported yet. Codex marks
> the hook run as failed, reports the error, and continues the tool call.

So `permissionDecision: "ask"` is recognized syntax but not a supported outcome today — using
it fails the hook run (logged as an error) and the tool call proceeds, i.e. it does not block.

## Where the block decision actually stops the call

> - A hook can block an operation when the tool returns a blocking decision.
>   Errors, missing servers, and unavailable tools don't block the operation.

> | `PreToolUse` blocks | The tool promise rejects before the tool runs. |

(from the "code mode" nested-call table, describing the same `PreToolUse` blocking outcome
when a tool is invoked via JS code mode rather than directly)

> Background hooks can't block, approve, rewrite, or otherwise control the
> operation that triggered them. Use synchronous hooks for tool policies,
> permission decisions, prompt rejection, or turn continuation.

Derived, from these two passages together: a blocking `permissionDecision`/`decision` value is
only effective on a **synchronous** `PreToolUse` hook — a background hook's output cannot stop
the call at all, regardless of what JSON it returns.

## Common output fields do NOT apply to PreToolUse the same way

> `PreToolUse` and `PermissionRequest` support `systemMessage`, but `continue`,
> `stopReason`, and `suppressOutput` aren't currently supported for those events.
> If a `PreToolUse` hook returns one of those unsupported fields, Codex marks
> that hook run as failed, reports the error, and continues the tool call.

So the generic `continue: false` block pattern used by other events (`Stop`, `UserPromptSubmit`,
etc.) does **not** block a `PreToolUse` call; only `permissionDecision: "deny"` /
`decision: "block"` / exit code `2` do.

## What the page does not say

- No stated precedence rule for what happens if a `PreToolUse` hook returns both the new
  `hookSpecificOutput.permissionDecision: "deny"` shape and the old `decision: "block"` shape
  in the same JSON object.
- No stated behavior for what happens if multiple matching `PreToolUse` hooks disagree (one
  denies, another allows) — this is documented for `PermissionRequest` (`any deny wins`), but
  not stated for `PreToolUse` on this page.
- No explicit statement of where `permissionDecisionReason` / `reason` is displayed (UI,
  transcript, or fed back to the model as tool error output) — the page only says the call is
  denied, not how the denial reason is surfaced downstream.
