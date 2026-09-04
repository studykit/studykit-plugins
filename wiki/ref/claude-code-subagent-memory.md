# Claude Code — persistent memory for subagents

Source: https://code.claude.com/docs/en/sub-agents (section "Persistent Memory for
Subagents"), fetched 2026-08-22 via the `.md` endpoint. Section re-read verbatim
2026-09-03 (now titled "Enable persistent memory"): the field, the three scopes, their
directories, the auto-memory dependency and the three "when memory is enabled" bullets are
unchanged in substance.
Related: https://code.claude.com/docs/en/memory#auto-memory, and
`claude-code-auto-memory-in-subagents.md` for the *session's* auto memory, which is a
different directory and a different question.

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
Declaring memory on an agent declared read-only widens what it can actually do, and the
boundary can only be stated in prose — the runtime does not scope the write.

Measured 2026-08-23, claude 2.1.239. An ad-hoc agent declared `tools: ["Read"]` with
`memory: local` reported Write and Edit present in its tool set, and a single Write call
to an absolute path **outside the project and outside its memory directory** returned
`File created successfully at: ...`; the file existed afterwards with the written content.
So the docs' "so the subagent can manage its memory files" states the *purpose* of the
grant, not a restriction on it. Anything that must not be writable has to be kept out of
reach some other way — which is why guard's reporting agents carry no `memory:` at all.

**`local` vs `project` is location and version-control intent, nothing more.** Re-checked
against the live page 2026-08-23: the only stated difference is the directory and whether the
knowledge is "shareable via version control" (`project`) or "shouldn't be checked into
version control" (`local`). Neither scope changes what the memory tools may touch, and
neither is a permission boundary. The page's wording for the three "when memory is enabled"
bullets was rephrased since the 2026-08-22 fetch above (numbered list → bullets); the
substance is unchanged.

**The docs recommend the pattern that failed here.** Under tips: "Include memory
instructions directly in the subagent's markdown file so it proactively maintains its own
knowledge base." That is precisely what guard's auditors had, and it is what produced a
stored verdict the agent then cited back instead of re-deriving it. The advice is sound for
an agent accumulating codebase knowledge; it is wrong for one whose output is a verdict,
because a stored verdict suppresses the finding that would reveal it as wrong. guard follows
the tip for neither, having removed `memory:` from its reporting agents.

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

## `<name-of-agent>` for a plugin subagent — measured

The docs say only "name-of-agent" and never say what that is for a plugin-scoped agent.
Measured 2026-09-03, `claude` 2.1.258: it is the **namespaced identifier with the colon
replaced by a hyphen**.

A throwaway plugin `memprobe-plugin` shipping `agents/plugmem.md` with `memory: local`, loaded
with `--plugin-dir` and dispatched through a `context: fork` skill, reported its memory
directory as `<project>/.claude/agent-memory-local/memprobe-plugin-plugmem/`, and the file it
wrote landed there. This repository's own tree agrees on both halves of the rule: the
plugin agent `guard:clarity-auditor` (`memory: user`) has
`~/.claude/agent-memory/guard-clarity-auditor/`, while the project-level agent
`plugin-agent-doc-auditor` (no plugin scope) has
`.claude/agent-memory/plugin-agent-doc-auditor/`.

The consequence worth stating: **renaming a plugin moves every one of its agents' memory
directories**, and nothing migrates the old contents.

## The `memory` grant reaches a `context: fork` skill's agent — measured

The pages describe `memory:` on the agent and say nothing about how it interacts with a skill
that runs that agent via `context: fork`. Measured 2026-09-03, `claude` 2.1.258, with a
throwaway agent carrying `tools: Read, Grep, Glob, Bash` and `memory: local`, invoked by a
`context: fork` skill naming it in `agent:` with `background: false`:

- the fork's system prompt **did** carry the memory instructions and named the memory
  directory absolutely;
- it **did** carry the seeded `MEMORY.md` content — a nonce in the index came back verbatim
  with no tool call;
- it did **not** carry the topic file's content, matching the documented "first 200 lines or
  25KB of `MEMORY.md`" and nothing else;
- the reported tool list included `Write` and `Edit`, neither declared — the silent grant
  above, confirmed on this path too.

This is what the skills page's own loading table predicts ("System prompt: from agent type"),
but it is inference from two pages until measured, so it is measured here. The pattern it
licenses is the one guard uses: durable knowledge lives in the agent's memory, the forked
skill body carries only this run's task.

Separate and not to be confused with the above: the *session's* auto memory also reaches
these agents on 2.1.258 even though both pages say it does not — see
`claude-code-auto-memory-in-subagents.md`.
