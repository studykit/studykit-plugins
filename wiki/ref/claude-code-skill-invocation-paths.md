# A skill's two invocation paths: what fires on each

Source: probe of `claude` 2.1.240 (the docs state neither result; see "What the docs do and
do not say" below for the sentences this probe was run against)
Retrieved: 2026-08-23

A skill without `disable-model-invocation: true` can be started two ways — the user types
`/name`, or the model calls the `Skill` tool. The two are not equivalent, and the difference
decides where a skill may get its per-invocation data from.

## Result

| Invocation path | `UserPromptExpansion` hook | `` !`command` `` injection in the body |
| --- | --- | --- |
| User types `/tp:probeskill` | **fires** (697-byte JSON payload delivered) | runs |
| Model calls the `Skill` tool | **does not fire** (hook log empty) | runs |

## The probe

A throwaway plugin `tp` under `--plugin-dir`, with one skill and one hook.

`skills/probeskill/SKILL.md` — no `disable-model-invocation`, so both paths are open:

```markdown
---
name: probeskill
description: Probe skill. Use this whenever the user says the word probeskill.
allowed-tools: Bash(echo *)
---

# Probe

Injected marker: !`echo INJECTION_RAN_$$`

Reply with exactly the injected marker line above, nothing else.
```

`hooks/hooks.json` — the hook appends its stdin payload to a file named by `$PROBE_LOG`:

```json
{"hooks": {"UserPromptExpansion": [{"matcher": "^(tp:)?probeskill$",
  "hooks": [{"type": "command",
             "command": "sh -c 'cat >> \"$PROBE_LOG\"; echo >> \"$PROBE_LOG\"'",
             "timeout": 5}]}]}}
```

Two runs, same plugin, log truncated before each:

```bash
# model-invoked
claude -p --plugin-dir "$PLUG" --permission-mode bypassPermissions \
  "Invoke the probeskill skill now using the Skill tool, then do what it says." < /dev/null
# -> stdout: INJECTION_RAN_42556        (injection ran)
# -> $PROBE_LOG: 0 bytes                 (expansion hook did not fire)

# user-typed
claude -p --plugin-dir "$PLUG" --permission-mode bypassPermissions "/tp:probeskill" < /dev/null
# -> stdout: INJECTION_RAN_42685        (injection ran)
# -> $PROBE_LOG: 697 bytes              (expansion hook fired, full payload)
```

The matcher, the plugin, and the skill file are identical across both runs; only the prompt
differs. So the empty log on the first run is the event not firing, not a matcher miss.

## What the docs do and do not say

The hook lifecycle table (https://code.claude.com/docs/en/hooks.md, retrieved 2026-08-23)
describes the event as:

> When a **user-typed** command expands into a prompt, before it reaches Claude. Can block
> the expansion

(emphasis added; "user-typed" is the page's word). That is consistent with the probe but
stops short of saying what happens on a `Skill` tool call, which is why the probe was run.

For injection, https://code.claude.com/docs/en/skills.md (retrieved 2026-08-23) says:

> The `` !`<command>` `` syntax runs shell commands **before the skill content is sent to
> Claude**.

No carve-out for either path is stated, and the probe finds none.

## The consequence for a skill that needs per-invocation data

A skill open to both paths cannot get its per-invocation data from a
`UserPromptExpansion` hook: half its invocations would arrive with nothing. Body injection is
the only mechanism that covers both, and three documented properties of it are load-bearing
for anything built that way (all from the skills page, retrieved 2026-08-23):

> A failed command aborts the entire skill invocation, not just its own placeholder. Claude
> never sees the skill content for that invocation.

> Injected commands never prompt for permission. When a command's permission check returns
> anything other than allow, Claude Code aborts the invocation. This includes a rule that
> would normally ask you.

> When Claude re-invokes a skill whose rendered content is identical to the copy already in
> context, Claude Code adds a short note that the skill is already loaded rather than a
> second copy of the content. When the rendered content differs, because the arguments
> changed or a dynamic context command produced new output, Claude Code appends the full
> content again.

So: a non-zero exit silently deletes the whole invocation, the command must be pre-approved
via `allowed-tools` (the same `${…}` variable in both places is the documented way), and a
body whose injected output changes on every invocation is re-appended in full every time rather
than deduplicated.

## Companion probe: `agent:` accepts a plugin-scoped subagent

Same 2.1.240 session, same throwaway plugin. The docs say only "Which subagent type to use
when `context: fork` is set", and https://code.claude.com/docs/en/skills.md names built-ins
plus "any custom subagent in `.claude/agents/`" — leaving open whether a **plugin's** agent,
which is addressed as `<plugin>:<name>`, is a legal value.

`agents/probeagent.md` (system prompt: "your entire reply must be the single line
IAM_PROBEAGENT followed by the marker you were given") plus:

```markdown
---
name: forkprobe
description: Fork probe. Use when the user says forkprobe.
context: fork
agent: tp:probeagent
background: false
allowed-tools: Bash(echo *)
---

Marker: !`echo FORK_MARKER_OK`

Report who you are and the marker.
```

Model-invoked, the skill returned `IAM_PROBEAGENT FORK_MARKER_OK`.

Both halves matter. `IAM_PROBEAGENT` can only come from the agent's own system prompt, so the
plugin-scoped `agent:` value resolved rather than silently falling back to
`general-purpose`; and `FORK_MARKER_OK` shows the body injection ran and reached the fork as
substituted text, on the model-invoked path.

## What `disable-model-invocation` costs in context

From the same skills page (retrieved 2026-08-23), the table under "Control who invokes a
skill":

> | Frontmatter                      | You can invoke | Claude can invoke | When loaded into context                                     |
> | (default)                        | Yes            | Yes               | Description always in context, full skill loads when invoked |
> | `disable-model-invocation: true` | Yes            | No                | Description not in context, full skill loads when you invoke |
> | `user-invocable: false`          | No             | Yes               | Description always in context, full skill loads when invoked |

And the note under it:

> In a regular session, skill descriptions are loaded into context so Claude knows what's
> available, but full skill content only loads when invoked.

So dropping `disable-model-invocation` from a skill is not only a permission change: it moves
that skill's `description` into the session's standing context, where it is paid for on every
turn and is the only thing steering when the model decides to invoke.
