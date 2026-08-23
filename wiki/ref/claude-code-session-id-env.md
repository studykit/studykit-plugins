# `CLAUDE_CODE_SESSION_ID` — the session id in Bash and hook subprocesses

Source: https://code.claude.com/docs/en/env-vars (raw markdown:
`https://code.claude.com/docs/en/env-vars.md`), environment-variable table
Retrieved: 2026-08-23

Why this is saved: guard is considering moving its turn-end dispatch out of the Stop hook's
`additionalContext` and into a model-invoked skill. A skill has no hook payload, so how a
script it runs learns the session id decides whether the design can find the turn at all.
This row is the documented contract; the alternatives (`${CLAUDE_SESSION_ID}` skill
substitution, exporting a variable through `CLAUDE_ENV_FILE`) are no longer needed for that.

Retrieval note: the page is ~464 KB, and a `WebFetch` of it answered "SESSION_ID does not
appear" — twice. The variable is there. Grep the raw `.md` yourself for a
presence/absence question on a page this size; a summarizing fetch is not evidence of
absence.

## Excerpt

> | `CLAUDE_CODE_SESSION_ID` | Set automatically to the current session ID in Bash and
> PowerShell tool subprocesses, [hook command](/docs/en/hooks) subprocesses, and stdio
> [MCP server](/docs/en/mcp) subprocesses. For Bash, PowerShell, and hooks this matches the
> `session_id` field in the hook JSON input and is updated on `/clear`. An MCP server
> subprocess retains the ID it was spawned with. On `--resume <session-id>` it receives the
> resumed ID, matching hooks and Bash. On `--continue` or `--resume` without an explicit ID
> it may receive the initial startup ID instead. Use to correlate scripts and external tools
> with the Claude Code session that launched them |

Two neighbours, for contrast — neither is the general-purpose session id:

> | `CLAUDE_CODE_BRIDGE_SESSION_ID` | Set automatically in Bash tool and hook command
> subprocesses while the session has an active Remote Control connection, and removed when
> the connection ends. The value is the session's ID in `session_` form […] |

> | `CLAUDE_CODE_REMOTE_SESSION_ID` | Set automatically in cloud sessions to the current
> session's ID […] |

## What guard takes from this

- A script run from a skill's body can resolve the session itself. No argument to pass, no
  `${CLAUDE_SESSION_ID}` substitution, no `CLAUDE_ENV_FILE` export.
- "matches the `session_id` field in the hook JSON input" is the load-bearing sentence: it
  is the same key guard's state and turn directories are named by.
- "updated on `/clear`" means the session boundary does not drift from the hook's view.
- The `--continue` / bare `--resume` carveout is the one failure mode: the variable may
  carry the startup id while the hooks carry the resumed one. A lookup that finds no pending
  turn under that id must say so and stop, never fall back to some other turn — auditing the
  wrong turn is worse than auditing none.
