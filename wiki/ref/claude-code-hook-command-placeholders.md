# Hook command path placeholders, and the common hook input fields

Source: https://code.claude.com/docs/en/hooks
Retrieved: 2026-08-23

Saved for the project-local hooks in `.claude/settings.json`, which reach their script
through `${CLAUDE_PROJECT_DIR}` and read `prompt_id` / `session_id` off the payload.

## `${CLAUDE_PROJECT_DIR}` in a hook `command`

Under **Reference scripts by path**:

> Use these placeholders to reference hook scripts relative to the project or plugin root,
> regardless of the working directory when the hook runs:
>
> * `${CLAUDE_PROJECT_DIR}`: the project root where the session started. Claude Code also
>   sets this variable in the environment of stdio MCP servers and plugin LSP servers.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/check-style.sh",
            "args": []
          }
        ]
      }
    ]
  }
}
```

> Prefer exec form for any hook that references a path placeholder. In shell form, wrap each
> placeholder in double quotes.

## Common input fields

> **Common input fields** Hook events receive these fields as JSON, in addition to
> event-specific fields documented in each hook event section.

| Field | Description |
| --- | --- |
| `session_id` | Current session identifier |
| `prompt_id` | UUID identifying the user prompt currently being processed. Matches the `prompt.id` attribute on OpenTelemetry events, so you can correlate hook output with telemetry for a single prompt. Absent until the first user input. Requires Claude Code v2.1.196 or later |
| `transcript_path` | Path to conversation JSON. The transcript file is written asynchronously and may lag the in-memory conversation, so it may not yet include the current turn's most recent messages when a hook fires. Hooks that need the final assistant text of the current turn should use `last_assistant_message` on Stop and SubagentStop instead of reading the transcript |
| `cwd` | Current working directory when the hook is invoked |
| `permission_mode` | Current permission mode: `"default"`, `"plan"`, `"acceptEdits"`, `"auto"`, `"dontAsk"`, or `"bypassPermissions"` |
| `effort` | Object with a `level` field holding the active effort level for the turn. Present for events that fire within a tool-use context, such as `PreToolUse`, `PostToolUse`, `Stop`, and `SubagentStop` |
| `hook_event_name` | Name of the event that fired |

The page documents no `PostToolUse`-specific input table beyond these common fields plus the
event-specific tool fields (`tool_name`, `tool_input`, `tool_response`).

## Related

- `claude-code-stop-hook-decision-control.md` — the Stop hook's `additionalContext` output.
- `claude-code-hooks-in-subagents.md` — that `PostToolUse` fires for a subagent's writes too.
- `claude-code-skill-substitutions.md` — the same placeholder as seen from a skill.
