# Claude Code — subagent naming, resumption, and transcript persistence

Source: https://code.claude.com/docs/en/sub-agents
Retrieved: 2026-08-22

Excerpt of the parts that bear on reusing a subagent across dispatches rather than
spawning a fresh instance each time.

## Naming a subagent at dispatch

> Claude can give a subagent a name by passing a `name` parameter on the Agent tool
> call, and may do so on its own, without asking you first. The name makes the subagent
> addressable: Claude can message or resume it by name after it finishes.

## Resume subagents

> Each subagent invocation creates a new instance rather than continuing an earlier one.
> To continue an existing subagent's work instead of starting over, ask Claude to resume
> it.
>
> Resumed subagents retain their full conversation history, including all previous tool
> calls, results, and reasoning. The subagent picks up exactly where it stopped rather
> than starting fresh.
>
> When a subagent completes, Claude receives its agent ID. The built-in Explore and Plan
> agents are one-shot and return no agent ID, so they can't be resumed; use
> `general-purpose` or a custom subagent when you need to continue the work.
>
> Claude uses the `SendMessage` tool with the agent's ID or name as the `to` field to
> resume it. `SendMessage` doesn't require agent teams to be enabled; only structured
> team-protocol messages such as `shutdown_request` and `plan_approval_response` do.

> A completed subagent that receives a `SendMessage` auto-resumes in the background
> without a new `Agent` invocation.

Documented example of the interaction shape:

> ```
> Use the code-reviewer subagent to review the authentication module
> [Agent completes]
>
> Continue that code review and now analyze the authorization logic
> [Claude resumes the subagent with full context from previous conversation]
> ```

## Transcript persistence

> Subagent transcripts persist independently of the main conversation:
>
> * **Main conversation compaction**: when the main conversation compacts, subagent
>   transcript are unaffected. They're stored in separate files.
> * **Session persistence**: subagent transcripts persist within their session. You can
>   resume a subagent after restarting Claude Code by resuming the same session.

Stored at `~/.claude/projects/{project}/{sessionId}/subagents/`, named
`agent-{agentId}.jsonl`.

## Bearing on guard

Reuse is per-session, not per-project: the transcript lives under the session id, so a
new session starts every agent fresh whatever the setting says. Custom subagents (which
all of guard's are) return an agent ID and are resumable; the one-shot built-ins are not.

## The user talking to a running subagent (interactive UI)

Retrieved 2026-08-22 from the same page. This is the capability that makes a forked,
user-addressable agent viable where an in-session skill used to be the only sensible shape.

> ## Monitoring Running Subagents (Interactive UI)
>
> When subagents run in background, they appear in a panel below the prompt:
>
> | Key | Action |
> |-----|--------|
> | `↑` / `↓` | Move between subagent rows |
> | `Enter` | Open transcript, send follow-up messages |
> | `x` | Stop running subagent or dismiss completed one |
> | `Esc` | Return to prompt |
>
> Running subagents also appear in `/tasks` command.

So the reach is **not** Claude-only: `SendMessage` is how *Claude* resumes an agent, and
this panel is how the *user* does it. The user can open a background agent's transcript and
send it follow-up messages directly, without going through the main session.

## Invoking one by `@`-mention (the user's own entry point)

Retrieved 2026-08-26 from the same page. This is what makes a user-addressable agent need no
slash command of its own.

The page contrasts three ways to request a specific subagent:

> * **Natural language**: name the subagent in your prompt; Claude decides whether to delegate
> * **@-mention**: guarantees the subagent runs for one task
> * **Session-wide**: the whole session uses that subagent's system prompt, tool restrictions, and model via the `--agent` flag or the `agent` setting

Syntax, including the plugin-scoped form:

> **@-mention the subagent.** Type `@` and pick the subagent from the typeahead, the same way
> you @-mention files. This ensures that specific subagent runs rather than leaving the choice
> to Claude

> You can also type the mention manually without using the picker: `@agent-<name>` for local
> subagents, or `@agent-` followed by the scoped name for plugin subagents, for example
> `@agent-my-plugin:code-reviewer`. While you type this form the typeahead shows file matches
> rather than agents. The agent mention still resolves when you submit.

> Subagents provided by an enabled plugin appear in the typeahead under their scoped name, such
> as `my-plugin:code-reviewer` [...]. Named background subagents currently running in the
> session also appear in the typeahead, showing their status next to the name.

What it does and does not control:

> Your full message still goes to Claude, which writes the subagent's task prompt based on what
> you asked. The @-mention controls which subagent Claude invokes, not what prompt it receives.

And how an @-mentioned agent behaves:

> An @-mentioned subagent runs according to the normal foreground/background rules. Where fork
> mode is on (the default in interactive sessions), the subagent runs in the background.

> @-mentioned subagents appear in the subagent panel below the prompt input, following the same
> display rules as other subagents.

Bearing: a plugin agent meant for the user to converse with needs no command to launch it.
`@agent-<plugin>:<name>` guarantees it runs, lands it in the background panel, and — because a
running named agent stays in the typeahead — is also how the user gets back to the one already
going. What the mention does NOT fix is the opening prompt, which the main agent still writes;
that has to be handled by the agent's own body.

## Foreground vs background, and what decides it

> **Foreground:** Blocks main conversation, permission prompts go directly to you
>
> **Background** (default in interactive sessions):
> - Runs concurrently while you work
> - Permission prompts surface in main session
> - Smaller built-in tool set available
> - Results arrive as completion notification

> Claude Code picks based on:
> 1. If in-process agent team teammate spawned it → foreground
> 2. If `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` → foreground
> 3. If fork mode on → background
> 4. If fork mode off → background by default (Claude asks for foreground if needed)

> **Set `background: true` in frontmatter** to keep subagent in background even when Claude
> wants foreground result.

Bearing: the panel only lists **background** agents, so an agent meant to be conversed with
must not be dispatched foreground. `background: true` in its frontmatter is what pins that
rather than leaving it to the caller.

## Fork vs a plain subagent

> ### Fork the conversation
> Start a fork with `/subtask` (v2.1.212+):
> ```
> /subtask draft unit tests for the parser changes so far
> ```
> A fork inherits your entire conversation instead of starting fresh—useful when a side
> task needs significant context. Results come back clean to main conversation.

> **Forks** get everything the main session has.

And what a non-fork subagent starts with:

> Each non-fork subagent starts fresh with:
> - ✓ System prompt from definition
> - ✓ Task delegation message
> - ✓ CLAUDE.md files (except Explore/Plan)
> - ✓ Git status snapshot (except Explore/Plan)
> - ✓ Preloaded skills (from `skills` field)
> - ✗ Conversation history
> - ✗ Main conversation's output style
> - ✗ Main conversation's auto memory

Bearing: "addressable by the user" and "inherits the conversation" are separate axes. A
plain background subagent is addressable without inheriting anything, which is what a task
that needs no conversation history wants.
