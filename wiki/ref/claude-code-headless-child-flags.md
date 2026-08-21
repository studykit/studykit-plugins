# Launching a lightweight `claude -p` child (CLI flags)

Source: `claude --help` on Claude Code 2.1.238 (local binary; the flags below are quoted
from its own output)
Retrieved: 2026-08-21

Why this is saved: guard's Stop hook spawns one `claude -p` child as its router. Which
flags make that child cheap — and which one would break it — is the basis of
`_router_argv`, and "does `--safe-mode` disable hooks" decides whether the child can
recurse into guard itself.

## `--safe-mode` — what guard relies on

> `--safe-mode`  Start with all customizations (CLAUDE.md, skills, plugins, hooks, MCP
> servers, custom commands and agents, output styles, workflows, custom themes,
> keybindings, and more) disabled — useful for troubleshooting a broken configuration.
> Admin-managed (policy) settings still apply. Auth, model selection, built-in tools, and
> permissions work normally. Sets `CLAUDE_CODE_SAFE_MODE=1`.

Two clauses carry the design:

- **"hooks … disabled"** — the child does not run the project's hooks, so guard's own
  Stop hook cannot fire inside it. Without this the router would trip the hook that
  spawned it.
- **"Auth … work normally"** — the child authenticates the same way the parent does, so
  the router works for an OAuth user with no API key in the environment.

It also drops MCP servers, plugins, CLAUDE.md, and skills, which is most of the startup
cost a child would otherwise pay for context it cannot use.

## `--bare` — lighter, and rejected

> `--bare`  Minimal mode: skip hooks, LSP, plugin sync, attribution, auto-memory,
> background prefetches, keychain reads, and CLAUDE.md auto-discovery. Sets
> `CLAUDE_CODE_SIMPLE=1`. **Anthropic auth is strictly `ANTHROPIC_API_KEY` or
> `apiKeyHelper` via `--settings` (OAuth and keychain are never read).** 3P providers
> (Bedrock/Vertex/Foundry) use their own credentials. Skills still resolve via
> `/skill-name`. Explicitly provide context via: `--system-prompt[-file]`,
> `--append-system-prompt[-file]`, `--add-dir` (CLAUDE.md dirs), `--mcp-config`,
> `--settings`, `--agents`, `--plugin-dir`.

`--bare` skips strictly more than `--safe-mode` (LSP, plugin sync, keychain reads,
background prefetches). guard does not use it because of the emphasized clause: an OAuth
user with no `ANTHROPIC_API_KEY` gets a child that cannot authenticate, and guard fails
open silently — so the router would simply never run, with nothing to see. A flag that
works for some users and quietly does nothing for others is worse than a slower one that
works for all.

## The other flags in `_router_argv`

> `--no-session-persistence`  Disable session persistence - sessions will not be saved to
> disk and cannot be resumed (only works with `--print`)

> `--output-format <format>`  Output format (only works with `--print`): "text"
> (default), "json" (single result), or "stream-json" (realtime streaming)

> `--json-schema <schema>`  JSON Schema for structured output validation.

> `--allowedTools, --allowed-tools <tools...>`  Comma or space-separated list of tool
> names to allow (e.g. "Bash(git *) Edit")

> `--disallowedTools, --disallowed-tools <tools...>`  Comma or space-separated list of
> tool names to deny (e.g. "Bash(git *) Edit")

> `--max-turns <turns>`  Limit the number of agentic turns in non-interactive mode

## Withholding tools from the child — measured, because the docs do not say

The help text does not state what happens when `--allowedTools` is omitted. It was
probed directly on 2.1.238: a working directory holding `probe.txt` containing
`SECRET_MARKER_9f3a`, and the prompt "Read the file probe.txt in the current directory
and print its exact contents. If you cannot use any tool, say NO_TOOLS." Every run added
`--safe-mode --model haiku --effort low --output-format json --no-session-persistence`.

| Flags added | Marker returned? | Notes |
| --- | --- | --- |
| (none) | **yes** | `permission_denials: []`. A child with no tool flags is fully tooled. |
| `--allowedTools ""` | **yes** | The empty value changes nothing. |
| `--disallowedTools Read` | **yes** | Denying one tool just routes it through another (Bash/Glob). |
| `--disallowedTools Read Bash Grep Glob` | no | Answered `NO_TOOLS` — and volunteered that `Agent` was still available. |
| `--disallowedTools` + the full list guard uses | no | Blocked. Residual tools are non-filesystem ones (ToolSearch, Workflow, Skill, Cron*). |
| `--max-turns 1` | no | But `rc=1`, `is_error: true`, `subtype: error_max_turns`, `result: null` — it fails the run rather than answering without tools. |

What this means for guard:

- **Omitting `--allowedTools` does NOT produce a tool-less child.** Any comment or design
  note claiming otherwise is wrong; guard carried exactly that mistake from its earlier
  in-hook judges until this was probed.
- The tools have to be **named** in `--disallowedTools`, and the list has to cover every
  route to the filesystem, not just `Read`. `Agent` belongs in it too: a router able to
  spawn subagents would dispatch the agents it was only asked to nominate.
- `--max-turns 1` is not usable as a tool guard. It turns "the model reached for a tool"
  into an error indistinguishable from a real failure, and guard fails open on failures —
  so the router would silently stop running whenever the model happened to probe.

## Not verified here

Whether `--strict-mcp-config` / `--mcp-config` would add anything on top of
`--safe-mode`'s MCP disabling was not tested — `--safe-mode` already covers it per its
own text, so guard passes neither. The residual non-filesystem tools left after the
denylist (ToolSearch, Workflow, Skill, Cron*) were observed in the child's own listing
but not probed for whether they can be invoked.
