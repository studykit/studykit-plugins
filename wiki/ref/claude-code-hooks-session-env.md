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

## SessionStart matcher / `source` values

Retrieved 2026-08-22 from the same page (https://code.claude.com/docs/en/hooks.md).
From the matcher-patterns table:

| Event | What the matcher filters | Example matcher values |
|-------|--------------------------|------------------------|
| `SessionStart` | how the session started | `startup`, `resume`, `clear`, `compact`, `fork` |

A `SessionStart` entry with **no** `matcher` therefore fires on every one of these,
`compact` included — so a hook that prints standing context at session start restates
it after a context compaction drops it.

## Plain stdout as model-visible context

Retrieved 2026-08-22, same page:

> For most events, stdout is written to the debug log but not shown in the transcript.
> The exceptions are `UserPromptSubmit`, `UserPromptExpansion`, and `SessionStart`,
> where Claude Code adds plain-text stdout as context that Claude can see and act on.
