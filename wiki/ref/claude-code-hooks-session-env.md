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

The documented JSON example for this event:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "The user is working on a React migration project. ..."
  }
}
```

## `systemMessage` — the one field the USER sees

Retrieved 2026-09-07 from the same page. From the JSON-output table:

> `systemMessage` | Plain-text message to add to the transcript as a system note, visible to
> Claude. Not all events keep it; see each event's section. If multiple hooks return
> `systemMessage` for the same event, Claude Code concatenates them with newlines. A
> `systemMessage` longer than 4,000 characters is truncated. On `UserPromptSubmit`,
> `SessionStart`, and `PostModelSwitch`, the message is prepended to the assistant's next
> response as a system note. On `PostToolUse` and `PostToolUseFailure`, it's shown in the
> transcript after the tool result. On all other events that support it, it's appended to the
> transcript as a standalone system note and Claude sees it on the next model call.

And from the `SessionStart` event section's decision control:

> `SystemMessage` is kept in the context where Claude can see it.

Elsewhere on the page, on choosing between the two:

> To surface a message to the user on any platform, return `systemMessage` in JSON output.
> Some events discard it or deliver it elsewhere, and each event's section says so. To trigger
> a desktop notification, set a window title, or ring the bell, return `terminalSequence`
> instead.

Two consequences worth stating, neither of them documented as such. The message arrives **with
the assistant's next response**, not at the moment the session opens — there is no pre-prompt
display channel on this event. And because stdout is parsed as JSON *or* as plain text and
never as both, one `systemMessage` moves every plain-text context line into
`additionalContext`; the two cannot be mixed on one hook.

`terminalSequence` is the only other user-facing field here (supported on `UserPromptSubmit`,
`SessionStart`, `PostModelSwitch` and `Stop`, silently ignored elsewhere) and it carries an
ANSI escape — a bell, a window title, a desktop notification — not text for the transcript.

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
