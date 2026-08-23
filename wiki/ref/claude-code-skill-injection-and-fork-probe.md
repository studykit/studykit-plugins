# What a model-invoked skill gets: arguments inside `!` injection, and a fork's tools

Source: probe of `claude` 2.1.241 (both results are undocumented; see "Why this was probed")
Retrieved: 2026-08-23

Two questions the docs leave open, both load-bearing for any design that moves per-turn data
out of a hook's visible output and into a model-invoked skill:

1. Is an argument placeholder substituted **before** an injected `` !`command` `` runs, or
   does the command receive it literally?
2. Does a `context: fork` skill keep the `Agent` tool, so it can dispatch subagents of its
   own?

## Results

| Question | Answer |
| --- | --- |
| `$turn` (named), `$ARGUMENTS`, `${CLAUDE_SESSION_ID}` inside an injected command | **all substituted before the command runs** — the script received real values in `argv` |
| Injected command as a visible tool call | **no** `tool_use` event of its own; the output arrives inline in the skill content |
| `user-invocable: false` + `Skill` tool call | works — the model invokes it normally |
| `context: fork` + `background: false`, invoked from the main conversation | **keeps `Agent`**; dispatched an `Explore` subagent successfully |
| A forked skill dispatching a **plugin-scoped** agent (`tp2:mini`) | **works** — returned the agent's token |
| What the main agent receives from the fork | only the fork's final message, as the Skill tool's result |
| Whether the fork's own tool calls surface upward | they appear as events in the parent's `stream-json` (`Agent`, `Bash`), even though their content is not in the main agent's context |

## The probe

Throwaway plugin `tp` under `--plugin-dir`, two skills, each with a script that logs its own
`argv` to a file — so the evidence is on disk rather than reported by a model.

`skills/probe/SKILL.md` (question 1):

```markdown
---
name: probe
description: Probe skill. Invoke this with the Skill tool whenever the user says the word probeskill.
user-invocable: false
arguments: [turn]
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/log.sh *)
---

PROSE_TURN=[$turn]
PROSE_ARGUMENTS=[$ARGUMENTS]
PROSE_SESSION=[${CLAUDE_SESSION_ID}]

INJECTED: !`${CLAUDE_SKILL_DIR}/log.sh turn=$turn args=$ARGUMENTS session=${CLAUDE_SESSION_ID}`
```

`log.sh` appends `ARGC=%s ARGV=[%s]` for `"$#"` / `"$*"`. Run:

```bash
claude -p --plugin-dir "$SP/tp" --permission-mode bypassPermissions \
  --output-format stream-json --verbose \
  "probeskill: invoke the probe skill with the Skill tool, passing exactly TURNXYZ789 as its argument."
```

Log:

```
ARGC=3 ARGV=[turn=TURNXYZ789 args=TURNXYZ789 session=01d019d6-ab69-44f2-9090-30e80c89b915]
```

An unsubstituted `$turn` would have reached the Bash tool's shell and expanded to the empty
string, so `ARGC=3` with three real values is the substitution happening first. The stream
carried one `tool_use` — `Skill` — and no `Bash`, with the script's stdout inlined in the
skill content the model received.

A third skill in a second plugin (`tp2`) checks that the fork can reach a **plugin** agent
rather than only a built-in one — the case guard actually needs, since every agent it
dispatches is plugin-scoped. A `context: fork` skill instructed to dispatch
`subagent_type: "tp2:mini"` logged `PLUGIN_AGENT=ok REPLY=MINI_OK`.

`skills/forkprobe/SKILL.md` (question 2) adds `context: fork` and `background: false`, and
instructs the fork to check for `Agent`, dispatch one `Explore` subagent, and append its
finding to a log with `echo`. Log:

```
FORK_INJECTION_RAN ARGV=[fork turn=TURNABC111 session=383319d7-0d64-405c-8df7-20ceccf7574f]
AGENT_TOOL=yes DISPATCH=ok REPLY=PONG
```

The parent stream shows `Skill` → `Agent`(`subagent_type: Explore`) → `Bash` → then the
Skill tool's result: `Skill "tp:forkprobe" completed (forked execution).\n\nResult:\nAGENT_TOOL=yes DISPATCH=ok REPLY=PONG`.

## Why this was probed

- On substitution order the docs say only that substitution happens in "the skill's markdown
  content" and that injected **output** is not re-scanned for further placeholders
  (https://code.claude.com/docs/en/skills.md). Neither sentence settles which pass runs first.
- On the fork's tools, https://code.claude.com/docs/en/sub-agents.md withholds `Agent` "when
  the subagent is at the depth limit" and lists a narrower built-in set for **background**
  subagents that does not include `Agent`. A foreground fork one layer down is outside both
  conditions, but the page does not say so directly.

## Consequences for a design like guard's

- Pass the turn id as an argument and use it inside the injection directly
  (`… dispatch --turn $turn`). No cross-check sentence, no state lookup.
- `background: false` is mandatory, not stylistic: a backgrounded fork loses `Agent` and could
  not dispatch the audit agents at all.
- Context and display are different wins. The main agent's context gets only the fork's final
  message — that part is settled. The terminal may still render the fork's tool calls, since
  they reach the parent as events, so "nothing on screen" is not what this buys.
