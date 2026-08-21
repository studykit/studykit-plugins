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
