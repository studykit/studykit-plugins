Source: https://learn.chatgpt.com/docs/agent-configuration/subagents
Retrieved: 2026-08-14

> To define your own custom agents, add standalone TOML files under
> `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped
> agents. Each file defines one custom agent.

> Every standalone custom agent file must define: `name`, `description`,
> `developer_instructions`.

> Codex identifies the custom agent by its `name` field. Matching the filename
> to the agent name is the simplest convention, but the `name` field is the
> source of truth.

## No memory field — re-checked 2026-09-03

Re-fetched https://learn.chatgpt.com/docs/agent-configuration/subagents.md as raw markdown
(`curl`, 22,084 bytes, not a summarizing fetch) on 2026-09-03. The required-field table is
still exactly the three above:

> | `name`                   | string |   Yes    | Agent name Codex uses when spawning or referring to this agent. |
> | `description`            | string |   Yes    | Human-facing guidance for when Codex should use this agent.     |
> | `developer_instructions` | string |   Yes    | Core instructions that define the agent's behavior.             |

and the extension clause names the optional keys:

> You can also include other supported `config.toml` keys in a custom agent file, such as
> `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, and `skills.config`.

A case-insensitive grep for `memory` over that page returns **zero** matches, as it does over
https://learn.chatgpt.com/docs/build-skills.md (10,925 bytes). The documentation index at
https://learn.chatgpt.com/llms.txt lists no memory page; the nearest concept is
`agent-configuration/agents-md` — static instruction files, not an agent-written store.

**So Codex has no counterpart to Claude Code's subagent `memory:` field**
(`claude-code-subagent-memory.md`) and no per-project auto memory
(`claude-code-auto-memory-in-subagents.md`). A cross-runtime plugin that wants an agent to
carry knowledge between runs has to own the store itself — a path under the project that the
agent is told about in its instructions — because the host will not provide one on the Codex
side. This is an absence established by grepping the raw pages, not by a summary; it can be
falsified by a page that is not in `llms.txt`.
