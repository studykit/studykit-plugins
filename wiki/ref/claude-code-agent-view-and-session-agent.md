# Claude Code — `claude agents` (Agent View), `--agent` session-wide flag, and automatic vs explicit subagent invocation

Source: https://code.claude.com/docs/en/agent-view.md, https://code.claude.com/docs/en/sub-agents.md,
and https://code.claude.com/docs/en/cli-reference.md
Retrieved: 2026-08-27

## What `claude agents` is

From `agent-view.md`:

> Agent view, opened with `claude agents`, is one screen for all your background sessions:
> what's running, what needs your input, and what's done. Dispatch new sessions, watch their
> state at a glance instead of scrolling through transcripts, and step in only when one needs
> you. Each background session is a full Claude Code conversation that keeps running without a
> terminal attached, so you can open it, reply, and leave whenever you want.

> Agent view is in research preview. The interface and keyboard shortcuts may change as the
> feature evolves.

Derived from the quote above: `claude agents` is a TUI that lists and dispatches **background
sessions** ("a full Claude Code conversation that keeps running without a terminal attached"),
not a way to pre-select which agent definition drives the *current* conversation's main loop.
That selection is the separate `--agent` flag (below).

> By default the list shows every background session you've started, across all your projects.
> ... Interactive sessions you have open in other terminals don't appear until you background
> them. **Subagents and teammates a session spawns aren't listed as separate rows.**

## `claude agents` CLI options (from `cli-reference.md`)

> `claude agents` — Open agent view to monitor and dispatch parallel background sessions. Use
> `--cwd <path>` to show only sessions started under that directory, or `--json` to print
> active sessions as a JSON array for scripting (`--json --all` also includes completed
> background sessions). Pass `--permission-mode`, `--model`, `--effort`, or `--agent` to set
> defaults for dispatched sessions. Accepts `--settings`, `--add-dir`, `--plugin-dir`, and
> `--mcp-config` like the top-level `claude` command. Opening agent view requires an
> interactive terminal.

From `agent-view.md`, on the `--agent` default for dispatched rows:

> `--agent` sets the subagent used when a dispatch prompt doesn't name one, either with `@name`
> or as the first word. It defaults to the `agent` setting if one is set, otherwise the
> built-in catch-all `claude` agent. Naming a subagent in the dispatch input overrides both.

## "FleetView"

Neither `agent-view.md` nor `cli-reference.md` nor `sub-agents.md` (as fetched 2026-08-27)
contains the string "FleetView". The documented name for the surface is **agent view**. This is
a recorded absence in the pages fetched, not a claim about where the term does come from.

## `--agent` (session-wide, from your shell) — replaces the main thread

From `sub-agents.md`, "Invoke subagents explicitly":

> Three patterns escalate from a one-off suggestion to a session-wide default:
> * **Natural language**: name the subagent in your prompt; Claude decides whether to delegate
> * **@-mention**: guarantees the subagent runs for one task
> * **Session-wide**: the whole session uses that subagent's system prompt, tool restrictions,
>   and model via the `--agent` flag or the `agent` setting

> **Run the whole session as a subagent.** Pass `--agent <name>` to start a session where the
> main thread itself takes on that subagent's system prompt, tool restrictions, and model:
>
> ```bash
> claude --agent code-reviewer
> ```
>
> The subagent's system prompt replaces the default Claude Code system prompt entirely, the
> same way `--system-prompt` does. `CLAUDE.md` files and project memory still load through the
> normal message flow. The agent name appears as `@<name>` in the startup header so you can
> confirm it's active.
>
> This works with built-in and custom subagents, and the choice persists when you resume the
> session: Claude Code restores the agent's system prompt, tool restrictions, and model along
> with the conversation. If the agent no longer exists when you resume, the session continues
> with the default tools and system prompt and shows a warning naming the agent.

Plugin-provided agent, disambiguation, and project default:

> For a plugin-provided subagent, you can pass only the agent name and Claude Code finds it:
> `claude --agent security-reviewer`. If multiple plugins provide agents with the same name,
> pass the scoped name to disambiguate: `claude --agent my-plugin:security-reviewer`. If the
> plugin places the agent in a subfolder of its `agents/` directory, include the subfolder in
> the scoped name, for example `claude --agent my-plugin:review:security`.
>
> To make it the default for every session in a project, set `agent` in `.claude/settings.json`:
> ```json
> { "agent": "code-reviewer" }
> ```
> The CLI flag overrides the setting if both are present.

Spawning further subagents from a `--agent` main thread:

> When an agent runs as the main thread with `claude --agent`, it can spawn subagents using the
> Agent tool. To restrict which subagent types it can spawn, use `Agent(agent_type)` syntax in
> the `tools` field.

> The `Agent(agent_type)` allowlist syntax applies only to an agent running as the main thread
> with `claude --agent`. In a subagent definition, listing `Agent` in `tools` lets that subagent
> spawn subagents of its own while the depth limit allows it, but any type list inside the
> parentheses is ignored.

`initialPrompt` frontmatter field, relevant only in this mode:

> `initialPrompt` — Auto-submitted as the first user turn when this agent runs as the main
> session agent (via `--agent` or the `agent` setting). Commands and skills are processed.
> Prepended to any user-provided prompt.

Hooks defined in the agent's own frontmatter also apply in this mode:

> Frontmatter hooks fire when the agent is spawned as a subagent through the Agent tool or an
> @-mention, and when the agent runs as the main session via `--agent` or the `agent` setting.
> In the main-session case they run alongside any hooks defined in `settings.json`.

Also usable to dispatch a *background* session running as a given agent (a third surface,
distinct from both "current interactive session" and "agent-view row default"):

> To run a specific subagent you have defined, such as a `code-reviewer`, as the session's main
> agent, combine `--bg` with `--agent`:
> ```bash
> claude --agent code-reviewer --bg "address review comments on PR 1234"
> ```
> If the name doesn't match any of your subagents, the launch fails: Claude Code prints a
> `no agent named` warning and still reports the session as backgrounded, but the session exits
> immediately with an `--agent '<name>' not found` error.

## `@agent-name` mention syntax (interactive prompt, mid-conversation)

From `sub-agents.md`, "Invoke subagents explicitly":

> **@-mention the subagent.** Type `@` and pick the subagent from the typeahead, the same way
> you @-mention files. This ensures that specific subagent runs rather than leaving the choice
> to Claude:
> ```text
> @"code-reviewer (agent)" look at the auth changes
> ```
> Your full message still goes to Claude, which writes the subagent's task prompt based on what
> you asked. The @-mention controls which subagent Claude invokes, not what prompt it receives.
>
> Subagents provided by an enabled plugin appear in the typeahead under their scoped name, such
> as `my-plugin:code-reviewer` or `my-plugin:review:security` ... Named background subagents
> currently running in the session also appear in the typeahead, showing their status next to
> the name.
>
> You can also type the mention manually without using the picker: `@agent-<name>` for local
> subagents, or `@agent-` followed by the scoped name for plugin subagents, for example
> `@agent-my-plugin:code-reviewer`. While you type this form the typeahead shows file matches
> rather than agents. The agent mention still resolves when you submit.

This dispatches a genuine subagent (fresh context unless the agent is `fork`), not a change to
the main thread — contrast with `--agent`, above, which replaces the main thread itself. See
also `claude-code-subagent-resume.md` in this directory for foreground/background rules that
apply to an @-mentioned subagent, and the interactive panel used to converse with a running one.

## Automatic ("proactive") invocation

From `sub-agents.md`, "Understand automatic delegation":

> Claude automatically delegates tasks based on the task description in your request, the
> `description` field in subagent configurations, and current context. To encourage proactive
> delegation, include phrases like "use proactively" in your subagent's description field.

Built-in subagents:

> Claude Code includes built-in subagents that Claude automatically uses when appropriate. Each
> inherits the parent conversation's permissions; most run with a restricted tool set.

> Claude Code includes additional helper agents for specific tasks. These are typically invoked
> automatically, so you don't need to use them directly.

Example `description` phrasing shown in the docs for encouraging automatic delegation:
`"Expert code reviewer. Use proactively after code changes."` and `"Proactively reviews code
for quality, security, and maintainability. Use immediately after writing or modifying code."`

## What the pages do not say

For the @-mention case the weighting *is* documented, and the excerpts above carry it: the
mention "ensures that specific subagent runs rather than leaving the choice to Claude" and
"guarantees the subagent runs for one task" — so an explicit mention overrides automatic
delegation, which decides the same thing.

What no page states is how automatic delegation interacts with a `--agent` main thread. Derived
(not quoted): `--agent` selects the thread while delegation happens within its turns, so the two
sit at different levels — but neither page says so.

Neither page uses the term "FleetView"; see the note above. Neither page states a JSON schema
for `claude agents --json` output beyond "prints active sessions as a JSON array for
scripting."
