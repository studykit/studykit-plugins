# Claude Code — the main conversation's auto memory, and whether a subagent sees it

Source: https://code.claude.com/docs/en/memory.md (section "Auto memory")
Source: https://code.claude.com/docs/en/sub-agents.md (sections "What loads at startup",
"Enable persistent memory", "Fork the current conversation")
Retrieved: 2026-09-03 via the `.md` endpoints (`curl`, not a summarizing fetch)
Probed: `claude` 2.1.258

This file records two different things and keeps them apart on purpose: what the pages say,
and what a probe of the shipped binary did. They disagree on one point.

## The two memories are different directories

Auto memory belongs to the **conversation**; subagent memory belongs to the **agent
definition**. Nothing connects them.

> Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`. The
> `<project>` path is derived from the git repository, so all worktrees and subdirectories
> within the same repo share one auto memory directory. Outside a git repo, the project root
> is used instead.

> The directory contains a `MEMORY.md` index and one topic file per memory

> To store auto memory in a different location, set `autoMemoryDirectory` in your
> `settings.json`. It is read from any [settings scope](/docs/en/settings#settings-precedence):
> user, project, local, policy, or `--settings`.
>
> The value must be an absolute path or start with `~/`.

Subagent memory is the `memory:` frontmatter field and its own tree — see
`claude-code-subagent-memory.md` for the scopes and directories.

> A subagent's own auto memory, enabled with the subagent `memory` field, is a separate
> directory.

## What is loaded, and when

> The first 200 lines of `MEMORY.md`, or the first 25KB, whichever comes first, are loaded at
> the start of every conversation. Content beyond that threshold is not loaded at session
> start.

> Claude Code doesn't load topic files such as `user_role.md` or `feedback_testing.md` at
> startup. Claude reads them on demand using its standard file tools when it needs the
> information.

So the index is context; the topic files are files. Anything that must reach a reader
automatically has to be on a `MEMORY.md` line, not in a topic file.

## The documented claim about subagents

`memory.md`, under "How it works":

> The main conversation's auto memory isn't loaded into
> [subagents](/docs/en/sub-agents#what-loads-at-startup); the exception is a
> [fork](/docs/en/sub-agents#fork-the-current-conversation), which inherits the parent
> conversation and system prompt. A subagent's own auto memory, enabled with the subagent
> `memory` field, is a separate directory.

`sub-agents.md`, under "What loads at startup" → "Some main-conversation state never reaches
a non-fork subagent":

> * **Auto memory**: the main conversation's [auto memory](/docs/en/memory#auto-memory) isn't
>   loaded. To give a subagent persistent memory of its own, use the
>   [`memory` field](#enable-persistent-memory).

Note which "fork" the exception names. It links to `#fork-the-current-conversation`, which is
the conversation fork — `/subtask`, or the Agent tool's `fork` subagent type:

> A fork is a subagent that inherits the entire conversation so far instead of starting fresh.
> This drops the input isolation that subagents otherwise provide: a fork sees the same system
> prompt, tools, model, and message history as the main session

That is **not** a skill's `context: fork`, which runs an ordinary agent type and, per
`skills.md`, "won't have access to your conversation history"
(`claude-code-skill-fork-context.md`). By the documented rule, then, a `context: fork` skill's
agent should be in the "isn't loaded" case.

## Probe: it is loaded anyway

Measured 2026-09-03, `claude` 2.1.258, in a throwaway git project at
`/private/tmp/memauto-probe`, headless (`claude -p ... --permission-mode bypassPermissions`).

Setup. The project's auto memory directory
(`~/.claude/projects/-private-tmp-memauto-probe/memory/`) was seeded with a `MEMORY.md` whose
only content was an index line carrying a nonce, `QUOKKA-5104`, and one topic file carrying a
different nonce that the index never quotes. The nonce appears **nowhere** in the project, in
any skill body, or in any prompt sent — that is what makes the result evidence rather than an
echo.

The probe agent was defined with `tools: WebSearch` and **no** `memory:` field, so it has no
filesystem tool at all and no memory grant. It was asked to print any marker code already
visible in its context, or `NONE`, and to say what carried it.

| Run | Entry point | Marker reported | Source the agent named |
| --- | --- | --- | --- |
| 1 | main session, no subagent (control) | `QUOKKA-5104` | a `system-reminder` naming the `MEMORY.md` path |
| 2 | `Agent` tool, `subagent_type: noreadagent` | `QUOKKA-5104` | a `system-reminder`, quoting the `MEMORY.md` index line |
| 3 | skill with `context: fork` + `agent: noreadagent`, `background: false` | `QUOKKA-5104` | a `system-reminder`, naming the `MEMORY.md` path |

Run 2's confounds were closed rather than assumed:

- **Relay from the parent.** The delegation could have carried the nonce. The recorded
  `tool_use` input in the session transcript was read back: `prompt` is the probe text
  verbatim and contains no marker (`'QUOKKA' in input: False`).
- **The agent reading the file itself.** Its whole tool list is `WebSearch`; an earlier
  iteration of the probe used a `Read`-capable agent and the result is discarded here for
  that reason. The run reported zero tool calls.

An earlier iteration also put the nonce *in the question* ("does `WALRUS-8812` appear…") and
its answer is worthless; it is recorded only so the number is not mistaken for a second
confirmation.

**So on 2.1.258 the main conversation's `MEMORY.md` index does reach a non-fork subagent, and
reaches a `context: fork` skill's agent, as a `system-reminder` — contrary to both pages.**

What the probe does **not** establish:

- Whether the mechanism is the same "Recalled memories" injection the user sees in the UI, or
  a separate per-agent reminder. The agents describe a `system-reminder`; nothing exposes
  which code path built it.
- Whether **topic files** reach a subagent. They are not loaded at session start for the main
  conversation either, and nothing suggests an agent gets more; the probe did not test the
  topic-file nonce separately.
- Behaviour with auto memory disabled (`autoMemoryEnabled: false` /
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY`), or under a non-default `autoMemoryDirectory`.
- Whether this is intended. It may be a documentation lag or a regression; either way it is
  the kind of fact that can change without notice, which is the argument against building on
  it.

## What to build on

Two consequences for anything shipped from this repository.

**Do not design a plugin around a subagent inheriting the session's auto memory.** The
documented contract says it does not, and the observed behaviour is the undocumented side.
A plugin that needs a fact to reach an agent must put it there itself: in the agent's own
`memory:` directory, in the dispatch prompt, or in the skill body that becomes the fork's
task.

**Do not assume it is absent either, when the concern is confinement.** An agent dispatched
in a session whose auto memory holds notes about the user receives that index today. An agent
definition that must not see such material cannot rely on the documented isolation to keep it
out.
