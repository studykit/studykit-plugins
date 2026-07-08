# PreToolUse `permissionDecision` values

Source: https://code.claude.com/docs/en/hooks.md (Hooks reference, retrieved 2026-07-09)

A `PreToolUse` hook returns a decision via
`hookSpecificOutput.permissionDecision`. Allowed values:

| Value     | Behavior                                                    |
|-----------|-------------------------------------------------------------|
| `"allow"` | Permits the tool call to proceed                            |
| `"deny"`  | Blocks the tool call                                        |
| `"ask"`   | Escalates to the user with a permission prompt              |
| `"defer"` | Defers to the normal permission flow                        |

`permissionDecisionReason` accompanies the decision. With `"ask"`, the reason is
shown to the user in the permission dialog, explaining why the hook is requesting
approval before the tool executes.

Example payload:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "ask",
    "permissionDecisionReason": "..."
  }
}
```
