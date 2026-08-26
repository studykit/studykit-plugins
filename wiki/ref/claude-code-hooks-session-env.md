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
SessionStart hook process (a path to write shell lines to), not a JSON
output field. Variables reach the Bash tool environment; they are not
substituted inside other tools (e.g. Write/Edit file paths).

## Observed: the file is sourced, so it carries more than `export`

Measured 2026-08-26 in a live session, because the docs describe the file only in terms
of environment variables and every example writes `export` lines — which reads as a
constraint on what the file may contain. It is not one.

The path is `~/.claude/session-env/<session-id>/sessionstart-hook-<n>.sh`, and it is
**sourced** before Bash tool commands rather than scanned for assignments. So it accepts
any shell code, not only assignments — both of these were verified in a live session:

```
export GUARD_PROJECT_DIR=/…/proj
export PATH=/…/plugins/guard/shell/bin:$PATH   ← `command -v guard` then resolves
guard() { … }                                  ← also survives; `type guard` sees it
```

What this buys: a plugin can ship a shell command with nothing for the user to install
and nothing left behind when the session ends, since no startup file is touched.

**Prefer a `PATH` entry over a function.** A function exists only in the shell that
sourced it, so a subprocess one level down (`sh -c 'guard status'`, a Makefile recipe, a
script the agent writes) will not find it. An executable on `PATH` is inherited like any
other command. Measured both ways: the nested `sh -c` case fails with a function and
works with an executable.

Two cautions. The `.sh` name and the sourcing behavior are observed, not documented, so
keep the underlying script reachable by path and treat the convenience as a convenience.
And the sourcing shell is the Bash tool's, not the user's login shell — write POSIX `sh`,
not zsh- or bash-specific syntax.

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
