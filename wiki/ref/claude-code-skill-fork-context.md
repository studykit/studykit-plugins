# Claude Code — running a skill in a forked subagent (`context: fork`)

Source: https://code.claude.com/docs/en/skills.md
Retrieved: 2026-08-22

The frontmatter that moves a skill's whole body out of the main session. Note this is a
**skill** field; subagent frontmatter has no `context` field (that table is
`name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`,
`skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation`, `color`,
`initialPrompt` — see `claude-code-subagent-frontmatter.md`).

## The fields

| Field | Documented behavior |
| --- | --- |
| `context` | "Set to `fork` to run in a forked subagent context." |
| `agent` | "Which subagent type to use when `context: fork` is set." Built-ins are `Explore`, `Plan`, `general-purpose`, plus any custom subagent in `.claude/agents/`; **"If omitted, uses `general-purpose`."** So spelling `agent: general-purpose` out states the default rather than changing anything. |
| `background` | "Only applies with `context: fork`. Set to `false` to wait for the forked subagent's result in the turn that invoked the skill, instead of running it in the background. Default: `true`. Requires Claude Code v2.1.218 or later." |
| `model` | "With `context: fork`, the value sets the forked subagent's model instead." |
| `effort` | "Effort level when this skill is active. Overrides the session effort level. Default: inherits from session. Options: `low`, `medium`, `high`, `xhigh`, `max`; available levels depend on the model." Note what is *not* said: `model` carries an explicit "with `context: fork`, the value sets the forked subagent's model instead" and `effort` has no counterpart sentence, so whether it reaches the fork or only the invoking turn is undocumented. Set it if you want it, but do not depend on it. |

## What it does

> Add `context: fork` to your frontmatter when you want a skill to run in isolation. The
> skill content becomes the prompt that drives the subagent. **It won't have access to your
> conversation history.**

That last sentence is the one that matters for cost. Despite the name, `context: fork` is
**not** `/subtask` — `/subtask` inherits the whole conversation ("Forks get everything the
main session has"), while a `context: fork` skill starts clean. So it is the cheap option,
not the expensive one: the skill body and everything the run produces stay out of the main
session's context.

What the two directions load:

> | Approach | System prompt | Task | Also loads |
> | --- | --- | --- | --- |
> | Skill with `context: fork` | From agent type | SKILL.md content | CLAUDE.md, except when the agent is Explore or Plan |
> | Subagent with `skills` field | Subagent's markdown body | Claude's delegation message | Preloaded skills + CLAUDE.md |

> With `context: fork`, you write the task in your skill and pick an agent type to execute
> it.

So the split is fixed by the runtime: **the agent definition is the system prompt, the skill
body is the task.** Durable knowledge and tool limits belong in the agent; what to do this
run belongs in the skill.

## Background by default

> The forked subagent runs in the background: you keep working while it runs, and its result
> arrives in your conversation when it completes. Set `background: false` in the frontmatter
> to instead wait for the result in the turn that invoked the skill. Before v2.1.218, forked
> skills always blocked the turn until they finished.

Claude Code waits for the result anyway in these cases:

> * In non-interactive mode, with the `-p` flag or the Agent SDK
> * When you set `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` to `1`, which also turns off all
>   other background task features
> * When you invoke a forked skill while an earlier invocation of the same skill is still
>   running
> * When a scheduled task fires with the skill as its prompt

## Two limits to design around

> A backgrounded fork also runs with the narrower tool set that applies to background
> subagents: the skill's subagent is a regular agent type, so the exemption for subagents
> that fork the conversation doesn't cover it. If your skill's steps depend on a tool
> outside that set, set `background: false` to keep the full tool set.

Two filters, from https://code.claude.com/docs/en/sub-agents.md (retrieved 2026-08-22).
The first drops `Agent`, `AskUserQuestion`, `EndConversation`, `EnterPlanMode`,
`ExitPlanMode`, `ScheduleWakeup`, `TaskOutput`, `WaitForMcpServers` and `Workflow` from
**every** subagent, foreground or background. The second leaves a background subagent with
`Read`, `Grep`, `Glob`, `Bash`, `PowerShell`, `Edit`, `Write`, `NotebookEdit`, `WebFetch`,
`WebSearch`, `TodoWrite`, `Skill`, `ToolSearch`, `EnterWorktree`, `ExitWorktree`, `Monitor`,
`TaskStop`, `SendMessage` and `Artifact`. Forks of the conversation skip both filters — but
that is the `/subtask` kind of fork, not a `context: fork` skill, as the quote above says.

Two consequences for a `context: fork` skill that changes files:

- **It can still edit.** `Edit`, `Write` and `Bash` survive the background filter, so a
  skill whose job is to write a file works backgrounded.
- **It cannot ask a bounded question.** `AskUserQuestion` is gone from the first filter, so
  a skill that needs the user's agreement before writing has to get it in prose, in its own
  transcript — which the user reaches through the panel `background: true` puts it in
  (`claude-code-subagent-resume.md`). A skill that must ask in the main conversation needs
  to stay unforked.

> A forked skill that runs in the background applies its edits outside your session's
> checkpoints, so `/rewind` doesn't undo them; use git to revert them.

And a warning on when the whole shape is wrong:

> `context: fork` only makes sense for skills with explicit instructions. If your skill
> contains guidelines like "use these API conventions" without a task, the subagent receives
> the guidelines but no actionable prompt, and returns without meaningful output.

## Commands are skills

> **Custom commands have been merged into skills.** A file at `.claude/commands/deploy.md`
> and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same
> way. Your existing `.claude/commands/` files keep working.

So a file under `commands/` takes this frontmatter too.

## Placeholder substitution carries into the fork

Not stated as such on either page, but settled by putting the two together, so record it
here rather than re-asking.

`claude-code-skill-substitutions.md` says substitution happens in **"the skill's markdown
content"** (and in `allowed-tools` Bash rules) — it is a property of building the content,
with no fork-mode carve-out. This page says **"the skill content becomes the prompt that
drives the subagent."** The thing handed to the fork is therefore the already-substituted
content; there is no second, unsubstituted copy for it to receive.

So `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_SESSION_ID}` and `$ARGUMENTS` in a `context: fork`
skill reach the subagent as resolved values. `${CLAUDE_PLUGIN_ROOT}` additionally requires
the file to be a **plugin** skill ("Substituted only in plugin skills"), which is the only
condition worth checking.

## Bearing on guard

`/guard:settings` used to run in the main session. That put a ~1,200-word body plus the
whole exchange into the context the user is talking to, and a session late in its life
re-pays for all of it on every turn the exchange takes. `context: fork` moves both out for
one frontmatter line, and the background default is what puts the agent in the interactive
panel so the user can keep adjusting settings by talking to it
(`claude-code-subagent-resume.md`).

A custom `agent:` would be the way to make the tool restriction enforced rather than
merely stated: guard's settings file may only be written through its CLI, and an agent whose
`tools` is `Bash` alone cannot open the file at all. guard does not do this — it runs on the
default `general-purpose` and leans on `disallowed-tools` plus a prohibition in the body,
because that field's reach into a fork is undocumented. Worth revisiting if the prose ever
fails to hold.

`/guard:statusline` is forked for the same cost reason, and pays a price `/guard:settings`
does not: it asks the user before writing their settings file, `AskUserQuestion` is stripped
from every subagent, so that exchange moved into the background transcript.
