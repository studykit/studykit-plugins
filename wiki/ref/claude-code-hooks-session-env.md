# Claude Code hooks — SessionStart env persistence & output fields

Source: https://code.claude.com/docs/en/hooks.md (fetched 2026-07-09)

## CLAUDE_ENV_FILE (SessionStart)

> SessionStart hooks have access to the `CLAUDE_ENV_FILE` environment variable,
> which provides a file path where you can persist environment variables for
> subsequent Bash commands.

Usage (from the docs example):

```bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=production' >> "$CLAUDE_ENV_FILE"
  echo 'export DEBUG_LOG=true' >> "$CLAUDE_ENV_FILE"
fi
```

Persistence scope:

> Any variables written to this file will be available in all subsequent Bash
> commands that Claude Code executes.

Notes: `CLAUDE_ENV_FILE` is an environment variable provided *to* the
SessionStart hook process (a path to write `export` lines to), not a JSON
output field. Variables reach the Bash tool environment; they are not
substituted inside other tools (e.g. Write/Edit file paths).

## SessionStart hookSpecificOutput fields

| Field | Description |
|-------|-------------|
| `additionalContext` | String added to Claude's context at session start |
| `initialUserMessage` | First user message for non-interactive mode |
| `sessionTitle` | Sets the session title |
| `watchPaths` | Array of paths to watch for FileChanged events |
| `reloadSkills` | Boolean to reload skills after hook completes |
