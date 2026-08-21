# Claude Code subagent frontmatter

Source: <https://code.claude.com/docs/en/sub-agents>

Fetched: 2026-08-21

Local path: `wiki/ref/claude-code-subagent-frontmatter.md`

## Required fields

| Field | Meaning |
|---|---|
| `name` | Unique identifier, lowercase letters and hyphens. Cannot contain `:` (reserved for plugin-scoped identifiers). Delivered to hooks as `agent_type`. |
| `description` | When Claude should delegate to this subagent. |

## Optional fields

| Field | Meaning |
|---|---|
| `tools` | Tools the subagent can use. **Inherits every tool available to subagents if omitted.** |
| `disallowedTools` | Tools to deny. Applied first; `tools` then resolves against the remaining pool. |
| `model` | `sonnet`, `opus`, `haiku`, `fable`, a full model ID, or `inherit`. Defaults to `inherit`. |
| `permissionMode` | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`, or `manual` (alias for `default`). |
| `maxTurns` | Maximum agentic turns before the subagent stops. |
| `skills` | Skills preloaded into the subagent's context at startup; full skill content is injected. |
| `mcpServers` | MCP servers available to this subagent. **Ignored for plugin subagents.** |
| `hooks` | Lifecycle hooks scoped to this subagent. **Ignored for plugin subagents.** |
| `memory` | Persistent memory scope: `user`, `project`, `local`. |
| `background` | `true` keeps the subagent in the background when Claude asks to run it in foreground. |
| `effort` | `low`, `medium`, `high`, `xhigh`, `max`. Overrides session effort. |
| `isolation` | `worktree` runs the subagent in a temporary git worktree. |
| `color` | `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`. |
| `initialPrompt` | Auto-submitted as the first user turn when the agent runs as main session agent. |

## The `tools` field

Format: comma-separated list of tool names or patterns.

Valid tool names include `Read`, `Grep`, `Glob`, `Bash`, `PowerShell`, `Edit`, `Write`,
`NotebookEdit`, `WebFetch`, `WebSearch`, `TodoWrite`, `Skill`, `ToolSearch`,
`EnterWorktree`, `ExitWorktree`, `Monitor`, `TaskStop`, `SendMessage`, `Artifact`, and
MCP tools.

MCP patterns: `mcp__<server>` / `mcp__<server>__*` grants every tool from that server;
`mcp__*` removes every MCP tool (in `disallowedTools` only).

Agent spawning is restricted with `Agent(agent_type)` syntax, e.g.
`tools: Agent(worker, researcher), Read, Bash`.

## Notes for guard

Omitting `tools` **inherits every tool**, so a read-only auditor must list its tools
explicitly. There is no way to express "no tools": if no entry resolves to a tool,
"Claude Code usually refuses to launch the subagent and the Agent tool returns an error
naming the unresolved entries", with the message `Agent would be spawned with zero
tools`. That is why `korean-corrector` is declared `tools: Read` (plus `Write` for its
rewrite file) rather than an empty list.
