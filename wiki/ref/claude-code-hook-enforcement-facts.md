# Claude Code Hooks — Enforcement & Decision Control Facts

**Source:** https://code.claude.com/docs/en/hooks.md (official reference)  
**Verified:** 2026-08-21

This document captures authoritative facts about hook output schemas, decision fields, and blocking behavior—focused on enforcement use cases (blocking actions, preventing stops, injecting context).

---

## 1. PostToolUse Hook: Output Fields & Blocking Capability

### Input Payload
```json
{
  "session_id": "abc123",
  "transcript_path": "...",
  "cwd": "...",
  "permission_mode": "default",
  "hook_event_name": "PostToolUse",
  "tool_name": "Bash",     // or Edit, Write, Read, etc.
  "tool_input": {
    "command": "npm test"   // tool-specific arguments
  },
  "tool_response": {        // The tool's actual return value
    "stdout": "...",
    "stderr": "",
    "interrupted": false,
    "isImage": false
  },
  "tool_use_id": "toolu_...",
  "duration_ms": 12
}
```

**For `Read` tool:** `PostToolUse` **does fire** for the Read tool (fires for all tools except `EndConversation`). The `tool_response` contains the file contents and metadata.

### Output Fields & Capability

PostToolUse output shape (both forms shown):

**Form 1: Modern — hookSpecificOutput only**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "string (10k char limit)",
    "updatedToolOutput": { /* replaces tool result */ },
    "classifierContext": "string (for auto mode classifier)"
  },
  "systemMessage": "string (10k char limit)"
}
```

**Form 2: With feedback decision (top-level)**
```json
{
  "decision": "block",
  "reason": "string",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "string"
  }
}
```

### Key Facts

1. **Can inject `additionalContext`?** ✅ **Yes.** 
   - Field location: either top-level OR nested in `hookSpecificOutput.additionalContext`
   - Added to Claude's context alongside the tool result
   - Maximum 10k characters

2. **Can emit blocking/feedback decision?** ⚠️ **Partial.** 
   - `decision: "block"` with `reason` → feeds `reason` to Claude as a warning line **next to the tool result**
   - Tool has **already executed** — you cannot prevent the action, only provide feedback
   - Exit code 2 shows stderr to Claude; structured JSON is preferred
   - `updatedToolOutput` can replace the tool's result **before Claude sees it** (but the side effect already happened)

3. **Model reacts to the decision?** ✅ **Yes.** When you return `decision: "block"` + `reason`, Claude sees it and can adjust. Default exit code 0 with no JSON = no feedback.

4. **Fires for Read?** ✅ **Yes.** PostToolUse fires for Read and includes the file contents in `tool_response`.

### Quote from Reference
> PostToolUse hooks fire after a tool has already executed successfully. The input includes both `tool_input`, the arguments sent to the tool, and `tool_response`, the result it returned. … Your hook script can return these event-specific fields: `decision` ("block"), `reason` (explanation shown to Claude when `decision` is "block"), `additionalContext` (String added to Claude's context alongside the tool result).

---

## 2. Stop Hook: Exact JSON Shape & `stop_hook_active` Semantics

### Input Payload
```json
{
  "session_id": "abc123",
  "prompt_id": "uuid",
  "transcript_path": "...",
  "cwd": "...",
  "permission_mode": "default",
  "hook_event_name": "Stop",
  "last_assistant_message": "The final response text from Claude...",
  "stop_hook_active": true,   // See semantics below
  "effort": { "level": "medium" }
}
```

### Output JSON Shape

**Recommended form:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "decision": "allow" | "block",
    "reason": "string (required when decision is 'block')"
  },
  "systemMessage": "string",
  "additionalContext": "string"
}
```

**Alternative (top-level) form:**
```json
{
  "decision": "block",
  "reason": "string"
}
```

### Decision Values & Behavior

| Decision | Effect |
|----------|--------|
| `"allow"` (or no decision) | Claude stops normally. Next turn begins. |
| `"block"` | Prevents Claude from stopping. Conversation continues. The `reason` is fed to Claude. |

### `stop_hook_active` Field Semantics

- **`stop_hook_active: true`** → this Stop hook has already blocked and Claude is
  continuing because of it. The hook must exit early (allow) so it does not loop.
- **`stop_hook_active: false`** → normal first-pass state; the hook may block.
- Claude Code also overrides a Stop hook after it blocks eight times in a row
  without progress.

NOTE (corrected 2026-08-21): an earlier revision of this file stated the inverse
(that `false` meant "already blocked 8+ times"). That contradicted the doc quote
below, which says to exit early when the field is `true`. The quote governs.
A direct re-fetch of https://code.claude.com/docs/en/hooks.md did not surface the
`stop_hook_active` prose at all, so the field's exact semantics are NOT confirmed
verbatim from the reference page — verify before relying on it.

Per the docs:
> Claude Code overrides a Stop hook after it blocks eight times in a row without progress. Your hook script needs to check whether it already triggered a continuation. Parse the `stop_hook_active` field from the JSON input and exit early if it's `true`

**Correct pattern:**
```bash
#!/bin/bash
INPUT=$(cat)
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0  # Allow Claude to stop on 8+ consecutive blocks
fi
# ... rest of validation logic
```

---

## 3. PreToolUse Hook: Permission Decision Values

### Output JSON Shape

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow" | "deny" | "ask" | "escalate",
    "permissionDecisionReason": "string"
  }
}
```

### Valid `permissionDecision` Values

| Value | Effect |
|-------|--------|
| `"allow"` | Skip the interactive permission prompt. Built-in deny rules still apply. |
| `"deny"` | Cancel the tool call and send the reason to Claude. |
| `"ask"` | Show the permission prompt to the user (interactive). |
| `"escalate"` | Same as `"ask"` — escalate to user for approval. |
| `"defer"` | (Non-interactive mode only with `-p` flag) Exit gracefully so tool can be resumed later. |

### Deprecated Format (PreToolUse only)

PreToolUse previously used top-level `decision` and `reason` fields:
```json
{
  "decision": "approve" | "block",   // DEPRECATED
  "reason": "string"
}
```

Maps to:
- `"approve"` → `permissionDecision: "allow"`
- `"block"` → `permissionDecision: "deny"`

**Current code must use `hookSpecificOutput.permissionDecision`** (new format).

### `permissionDecisionReason` Field

- Shown to the user when decision is `"allow"` or `"ask"` (hidden from Claude)
- Shown to **Claude** when decision is `"deny"` (so it can adjust)
- Ignored when decision is `"defer"`

### Quote from Reference
> PreToolUse previously used top-level `decision` and `reason` fields, but these are deprecated for this event. Use `hookSpecificOutput.permissionDecision` and `hookSpecificOutput.permissionDecisionReason` instead. The deprecated values `"approve"` and `"block"` map to `"allow"` and `"deny"` respectively. Other events like PostToolUse and Stop continue to use top-level `decision` and `reason` as their current format.

---

## 4. Prompt-Based Hooks: Event Support & Output Format

### Which Events Support `type: "prompt"`?

Per the docs, prompt-based hooks (type: "prompt") are available on events that require judgment rather than deterministic rules. The guide states they can be used on:

- `Stop` and `SubagentStop` — evaluate if turn is complete
- `PreToolUse` — evaluate if tool call should be allowed
- `PostToolUse` — evaluate if result is acceptable
- `PostToolBatch` — evaluate if batch processing should end
- `UserPromptSubmit` — evaluate if prompt should proceed
- `UserPromptExpansion` — evaluate if command expansion should proceed

### Prompt Hook Output Format

A prompt hook must return JSON with these fields:

```json
{
  "ok": true | false,
  "reason": "string (required when ok is false)",
  "impossible": true  // (Stop/SubagentStop only) marks condition as un-satisfiable
}
```

**Behavior:**
- `ok: true` → action proceeds
- `ok: false` → depends on event:
  - `Stop`/`SubagentStop`: Continue (unless `impossible: true` then stop anyway); `reason` is fed to Claude as next instruction
  - `PreToolUse`: Deny the tool call; `reason` shown to Claude (unless `continueOnBlock: true` then `reason` becomes tool error)
  - `PostToolUse`: Turn ends; `reason` shown as warning (unless `continueOnBlock: true` then `reason` fed back to Claude)
  - Other events: Turn ends; `reason` shown as warning in chat

### Example: Stop Hook with Prompt Evaluation

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Check if all tasks in this response are complete. If not, respond with {\"ok\": false, \"reason\": \"what remains to be done\"}.",
            "model": "claude-haiku-4-5-20241022"
          }
        ]
      }
    ]
  }
}
```

---

## Summary Table: Hook Decision Schemas

| Event | Output Field | Valid Values | Blocking? | Model Feedback? |
|-------|--------------|--------------|-----------|-----------------|
| **PreToolUse** | `hookSpecificOutput.permissionDecision` | allow, deny, ask, escalate, defer | ✅ Yes | ✅ Yes (via reason) |
| **PostToolUse** | `hookSpecificOutput.additionalContext` | (string) | ❌ No (tool ran) | ✅ Yes (context) |
| **PostToolUse** | `decision` (top-level or nested) | "block" | ⚠️ Feedback only | ✅ Yes (reason) |
| **Stop** | `decision` (top-level or in hookSpecificOutput) | allow, block | ✅ Yes | ✅ Yes (via reason) |
| **Stop** | `stop_hook_active` (input) | true, false | N/A (check, don't set) | N/A |

---

## Key Distinction: Output Field Nesting

The docs show that **decision field nesting varies by event:**

- **PreToolUse**: `decision` is **always** in `hookSpecificOutput.permissionDecision` (new format)
- **PostToolUse**: `decision` can be **top-level** (`"decision": "block"`) or in `hookSpecificOutput` (both supported)
- **Stop**: `decision` can be **top-level** or in `hookSpecificOutput.decision` (both supported)

When in doubt, nest inside `hookSpecificOutput` with the `hookEventName` field—this is the modern, explicit form that works across all events.

---

## Cites & URLs

All facts verified against:
- https://code.claude.com/docs/en/hooks.md — Complete hooks reference with all event schemas, decision control, exit code behavior
- https://code.claude.com/docs/en/hooks-guide.md — Guide with examples and common patterns


---

## 5. Subagents and hooks (retrieved 2026-08-21)

Source: https://code.claude.com/docs/en/hooks.md

> Hooks from settings files, managed policy settings, and plugins also run
> inside subagents. When a subagent calls a tool, tool events such as
> `PreToolUse` and `PostToolUse` fire the same configured hooks as in the main
> conversation, and the input carries the `agent_id` and `agent_type` common
> input fields that identify the subagent.

- `agent_id` — "Unique identifier for the subagent. Present only when the hook
  fires inside a subagent call. Use this to distinguish subagent hook calls from
  main-thread calls."
- `agent_type` — "Agent name (for example, `"Explore"` or
  `"security-reviewer"`). Present when the session uses `--agent` or the hook
  fires inside a subagent."
- `session_id` is a common input field for all hooks including subagent ones;
  the page does NOT state that a subagent gets its own session id. Treat
  "subagents share the parent session_id" as inferred, not quoted.

### SubagentStop

- Fires "When a subagent finishes"; the main-session `Stop` does not fire for
  subagent completion.
- Can block: exit-code table lists `SubagentStop` → "Prevents the subagent from
  stopping".
- IMPORTANT shape difference from what this file records for `Stop` above:

> For `Stop` and `SubagentStop`: exit 0 with valid JSON containing
> `permissionDecision: "block"` prevents the event from completing. A
> `permissionDecision` of `"allow"` or absence of the field lets it proceed
> normally.

This conflicts with the top-level `decision: "block"` + `reason` shape recorded
in section 2 for `Stop`. Both forms appear in the docs; the top-level `decision`
form is what section 2's quote gives for `Stop`, and PreToolUse's own section
says "Other events like PostToolUse and Stop continue to use top-level
`decision` and `reason` as their current format". VERIFY against the live
runtime before relying on either for `SubagentStop`.

### SessionStart source values

> `SessionStart` | how the session started | `startup`, `resume`, `clear`,
> `compact`, `fork`

`PreCompact` ("Before context compaction") and `PostCompact` ("After context
compaction completes") also exist; `PostCompact` cannot block.
