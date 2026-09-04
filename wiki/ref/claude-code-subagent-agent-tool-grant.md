# Granting a subagent the ability to dispatch subagents

Source: <https://code.claude.com/docs/en/sub-agents>

Retrieved: 2026-09-03 (fetched as `https://code.claude.com/docs/en/sub-agents.md`, the raw
markdown endpoint — a summarizing `WebFetch` of this page is not evidence of absence)

Local path: `wiki/ref/claude-code-subagent-agent-tool-grant.md`

## The tool is named `Agent`, and a bare `Agent` is the grant

> To allow spawning any subagent without restrictions, use `Agent` without parentheses:
>
> ```yaml
> tools: Agent, Read, Bash
> ```
>
> If you omit `Agent` from the `tools` list entirely, the agent can't spawn any subagents with
> the Agent tool.

So the `tools:` entry is the whole of the grant — there is no companion field, no permission
mode and no setting that also has to be turned on.

## `Agent(type, …)` is NOT the syntax for a subagent definition

> When an agent runs as the main thread with `claude --agent`, it can spawn subagents using the
> Agent tool. To restrict which subagent types it can spawn, use `Agent(agent_type)` syntax in
> the `tools` field.

> The `Agent(agent_type)` allowlist syntax applies only to an agent running as the main thread
> with `claude --agent`. In a subagent definition, listing `Agent` in `tools` lets that subagent
> spawn subagents of its own while the [depth limit] allows it, but any type list inside the
> parentheses is ignored.

This is the trap: writing `tools: Agent(docs-finder), Read` in an `agents/*.md` file that is
dispatched as a subagent does **not** restrict it to `docs-finder`. The parentheses are ignored
and the agent can spawn anything. Restricting a *subagent's* choice of subagent is not
expressible in `tools`; the documented lever is `permissions.deny` with `Agent(<name>)` rules,
which is session-wide rather than per-agent.

## The two filters, and why `background: true` does not withhold `Agent`

> Subagents inherit the built-in tools and MCP tools available in the main conversation, narrowed
> by two filters: the first removes a short list of tools from every subagent, and the second
> reduces the built-in tool set for subagents that run in the background, which is the default.
> Forks skip both filters and receive the main conversation's exact tool pool. The first filter
> removes these tools, even when listed in the `tools` field:
>
> * `Agent`, when the subagent is at the depth limit; in a fork the tool stays listed but returns
>   an error instead of spawning
> * `AskUserQuestion`
> * `EndConversation` […]
> * `EnterPlanMode`
> * `ExitPlanMode`, unless the subagent's `permissionMode` is `plan`
> * `ScheduleWakeup`
> * `TaskOutput`
> * `WaitForMcpServers`
> * `Workflow`

> The second filter applies to subagents running in the background. **Apart from `Agent` and
> `ExitPlanMode`, which follow the first filter's conditions wherever the subagent runs**, a
> background subagent keeps every MCP tool but only these built-in tools: `Read`, `Grep`, `Glob`,
> `Bash`, `PowerShell`, `Edit`, `Write`, `NotebookEdit`, `WebFetch`, `WebSearch`, `TodoWrite`,
> `Skill`, `ToolSearch`, `EnterWorktree`, `ExitWorktree`, `Monitor`, `TaskStop`, `SendMessage`,
> and `Artifact`. Claude Code removes every other built-in tool from a background subagent,
> whether inherited or listed in the `tools` field […]

`Agent` is absent from that background allowlist but is carved out by name in the sentence
introducing it, so a `background: true` subagent keeps `Agent` as long as the depth limit allows
it. Emphasis added.

Note the same list: **`AskUserQuestion` is removed from every subagent, first filter, even when
listed in `tools`.** A subagent a subagent dispatches therefore has no way to put a question to
the user.

## The depth limit is the one thing that can withhold it silently

> By default, a subagent can spawn subagents of its own, up to three layers below the main
> conversation. At the depth limit, Claude Code withholds the `Agent` tool from every subagent
> except a fork, so a subagent at the limit does its delegated work itself and returns one
> summary. […]
>
> To change the limit, set `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` to the number of subagent
> layers you want below your main conversation. […] Set `1` to turn nesting off.

> Only the top-level subagent's summary returns to you.

Version history the page records for that default:

> * **v2.1.172 through v2.1.216**: subagents could nest by default, up to five layers deep, and
>   the limit couldn't be changed.
> * **v2.1.217 through v2.1.218**: the limit defaulted to one, so a subagent couldn't spawn its
>   own unless you raised it; v2.1.219 raised the default to three.

So an agent dispatched from the main conversation sits at layer 1 and can spawn at layer 2 under
the default. A project that sets the variable to `1` disarms the grant with no error — the tool
is simply not in the list.

## Concurrency, separately

> By default, when 20 subagents are running in a session, spawning another with the Agent tool
> fails with `Concurrent subagent limit reached`, and the error tells Claude not to retry.
> […] To change the limit, set `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` to any positive whole
> number.

## Turning it off for one agent

> To keep one subagent from spawning while nesting is on, such as a reviewer that should stay
> read-only, omit `Agent` from its `tools` list or add it to `disallowedTools`.
