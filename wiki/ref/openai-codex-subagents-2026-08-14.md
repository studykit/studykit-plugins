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
