# Claude Code — persistent memory for subagents

Source: https://code.claude.com/docs/en/sub-agents (section "Persistent Memory for
Subagents"), fetched 2026-08-22 via the `.md` endpoint.
Related: https://code.claude.com/docs/en/memory#auto-memory

Verbatim excerpts.

## The field

```yaml
---
name: code-reviewer
description: Reviews code for quality and best practices
memory: user
---
```

## Accepted values

| Scope | Location | Use when |
| :--- | :--- | :--- |
| `user` | `~/.claude/agent-memory/<name-of-agent>/` | the subagent should remember learnings across all projects |
| `project` | `.claude/agent-memory/<name-of-agent>/` | the subagent's knowledge is project-specific and shareable via version control |
| `local` | `.claude/agent-memory-local/<name-of-agent>/` | the subagent's knowledge is project-specific but shouldn't be checked into version control |

## How memory works

> When memory is enabled, the subagent automatically receives:
>
> 1. **System prompt enhancement**: Instructions for reading and writing to the memory
>    directory are included in the subagent's system prompt.
>
> 2. **Memory file content**: The first 200 lines or 25KB of `MEMORY.md` in the memory
>    directory (whichever comes first) is automatically included in the subagent's system
>    prompt, with instructions to curate `MEMORY.md` if it exceeds that limit.
>
> 3. **Tool access**: Read, Write, and Edit tools are automatically enabled so the
>    subagent can manage its memory files.

## Auto memory dependency

> Subagent memory is part of auto memory: if you disable auto memory with the
> `autoMemoryEnabled` setting or the `CLAUDE_CODE_DISABLE_AUTO_MEMORY` environment
> variable, the `memory` field has no effect. The subagent will launch without memory
> instructions or memory tool access.

## Best practices

> - **`project` is recommended** as the default scope, making subagent knowledge shareable
>   via version control with your team
> - **Ask the subagent to consult memory first**: "Review this PR, and check your memory
>   for patterns you've seen before."
> - **Ask the subagent to update memory after tasks**: "Now that you're done, save what
>   you learned to your memory." This builds institutional knowledge across conversations
> - **Include memory instructions in the prompt**: Have the subagent proactively maintain
>   its knowledge base by discovering and documenting codepaths, patterns, library
>   locations, and architectural decisions

## Bearing on guard

Three consequences, in decreasing order of how easy they are to get wrong.

**Item 3 overrides the `tools:` allowlist.** `memory` silently enables Write and Edit.
guard's two auditors are declared read-only ("never writes anything"), so enabling memory
on them widens what they can do, and the boundary has to be stated in prose instead: they
may write inside their own memory directory and nowhere else.

**Neither scope is gitignored for free.** `project` writes `.claude/agent-memory/<agent>/`
and `local` writes `.claude/agent-memory-local/<agent>/`; the "shouldn't be checked into
version control" in the table is the scope's *intent*, not something the runtime enforces.
Checked in this repository: both paths are `WOULD BE COMMITTED` under its current
`.gitignore` (`**/*.local.*` does not match `agent-memory-local`). guard therefore ships
`local` — it runs in repositories it does not own, and `project` would put agent-written
files in other people's commits — while leaving the ignore decision to each project.

**Memory is not the same thing as guard's `reuse` mode, and neither replaces the other.**
Memory is cross-session, curated, and small — the conventions of this project. `reuse` is
within-session and uncurated — the full history of what this instance has already read and
judged, including the turn it saw ten minutes ago. An agent can sensibly have both.

**Memory depends on auto memory being on.** A user who has set `autoMemoryEnabled: false`
or `CLAUDE_CODE_DISABLE_AUTO_MEMORY` gets no memory and no warning, so nothing in guard
may treat a memory file as guaranteed to exist.

Not verified: what `<name-of-agent>` resolves to for a *plugin* subagent — the bare name
(`korean-corrector`) or the namespaced one (`guard:korean-corrector`). The docs say only
"name-of-agent". guard does not depend on the answer: it never reads or writes these
directories itself, and each agent is told to use whatever directory it was given.
