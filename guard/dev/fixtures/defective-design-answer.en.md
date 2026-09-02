# Dropping `disable-model-invocation` as the premise — recalculated

## Conclusion

Granted that premise, it holds up. One of the objections I raised last turn is overturned;
one of them survives as the condition that decides the design. And the part I left as an
inference last turn, I actually measured — the result narrows the implementation to one shape.

The biggest gain is not the context saving. It is that **the model's transcription step
disappears from the path**. Today the hook prints six lines of paths and the model copies
them into an Agent prompt. I retyped those six lines by hand again this turn. On the skill
path those values go from the script straight into the fork, never through the model.

---

## Measured: the two invocation paths behave differently

Confirmed against `claude` 2.1.240 with a throwaway plugin attached via `--plugin-dir`. Same
skill, same matcher, two runs differing only in the prompt.

| Invocation path | `UserPromptExpansion` | Body `` !`command` `` injection |
| --- | --- | --- |
| User types `/tp:probeskill` | fires (697-byte payload) | runs |
| Model calls the `Skill` tool | **does not fire** (log 0 bytes) | **runs** |

Also, putting a **plugin-scoped name** (`tp:probeagent`) in the `agent:` of `context: fork`
worked. The docs only go as far as custom subagents under `.claude/agents/`, which is why I
had left this unverified. In fact the fork ran under that agent's system prompt, and the
injected marker arrived with it.

The procedure, the source quotes and the basis for the verdict are saved in
`wiki/ref/claude-code-skill-invocation-paths.md` (sources
https://code.claude.com/docs/en/skills.md, https://code.claude.com/docs/en/hooks.md).

One design constraint falls out of this. A skill the model can also invoke cannot receive its
data from `UserPromptExpansion`. Half the invocations arrive with no data. So dynamic
injection has to go through **body injection alone**, and that diverges structurally from the
matcher approach the existing `/guard:claims-auditor` family uses. Wire up both and a
user-typed invocation gets the hook stdout and the body injection twice over.

## The gain, recalculated

Last turn's "roughly break-even" left out the model's transcription cost. Counting again
against the block lengths actually printed in this conversation:

| | Today | Skill path |
| --- | --- | --- |
| Hook output | about 650 chars | about 90 chars (one line) |
| The model's router dispatch | about 600 chars (field transcription) | about 30 chars (Skill call) |
| Router report | about 400 chars | about 500 chars (answer file path included) |
| Total | **about 1,650 chars** | **about 620 chars** |

This is a character count, not a token measurement. The saving (around 250 tokens per routed
turn) is a side benefit. The main point is the transcription going away. When one path never
passes through the model's hands, no typo or omission can arise on that path.

## Design

### `plugins/guard/skills/routing/SKILL.md`

```yaml
---
name: routing
description: >
  Route the finished turn to guard's audit agents. guard's Stop hook asks for this at the
  end of an audited turn; invoke it then, and not otherwise. Claude Code only.
argument-hint: ''
context: fork
agent: guard:turn-router
background: false
allowed-tools: Bash(uv run --script ${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py route*)
---

!`uv run --script "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" route --session ${CLAUDE_SESSION_ID}`
```

An almost empty body is correct here. Under `context: fork`, **the agent definition is the
system prompt and the skill body is the task**. The method of judgment is already in
`agents/turn-router.md`. The body only has to carry this turn's inputs.

Using the same `${CLAUDE_PLUGIN_ROOT}` string in `allowed-tools` is mandatory. Injected
commands never prompt for permission, and anything other than an allow verdict **aborts the
whole invocation**.

### `cmd_route()` — `scripts/guard_core/cmd_turn.py`

Same skeleton as `cmd_verify()`, calling `_router_context` instead of `_dispatch_context`.
Every value it needs is already in session state: `pending_verify_prompt_id`,
`transcript_path`, and the edited-file buckets `_eligible_agents` uses. The session id comes
from `--session`, falling back to `CLAUDE_CODE_SESSION_ID` — the way `cmd_settings` already
does it.

It must never exit non-zero. Per the docs, when an injected command fails it is not just that
placeholder that comes up empty: the whole skill invocation is cancelled and the model never
sees the body at all. Routing disappears silently. When there is no turn to audit, or the turn
was already routed, it has to print that in one line and exit 0.

`cmd_route` ignores the switches for the same reason `cmd_verify` does.

### `_ROUTE_LEAD` — `scripts/guard_core/dispatch.py`

```
guard: audit the turn you just finished — invoke the `guard:routing` skill.
```

The field block moves into `cmd_route`'s stdout. The block for the file-reading agents
(`comment-corrector` and friends) never goes through the router, so it stays where it is.

### `agents/turn-router.md` — add the answer file path to the output

This is the easy-to-miss mandatory change. Today the main agent gets the answer file path from
the hook block. On the skill path that block goes only into the fork. If the router does not
carry that path back in its report, the main agent cannot dispatch the audit agents. One line
added to each of the two templates in the `Output` section does it.

## What has to be changed alongside, if the premise is granted

- **The invariant in `AGENTS.md`.** The sentence today is "It names **agents**, never guard's
  own skills." That sentence itself has to be rewritten. That is different from leaving the
  rule broken. For example: the hook names agents, with one exception — `routing`, the
  router's entry point and the only `/guard:*` file without `disable-model-invocation`.
- **The `Dispatching` section of `dispatch-playbook.md`.** State the same exception against
  "Never invoke a `/guard:*` skill to do it".
- **The `router_model` setting dies.** Today the hook prints
  `- dispatch guard:turn-router with model: …` and that reflects the value in `guard.local.json`.
  A skill's `model:` is frontmatter, so it is static. Either fold the setting away and hardcode
  `opus` in the frontmatter, or keep the Agent dispatch path alive for this one item — I would
  take the former.

## Remaining risks

- **It may not be invoked when it should be.** The model already has to dispatch the router
  today, so the failure grade is the same. What is new is the silent failure above: injection
  fails and the invocation vanishes whole. `cmd_route` has to leave a trace on every call for
  that to be distinguishable after the fact.
- **It may be invoked when it should not be.** Dropping `disable-model-invocation` puts the
  description in the main context permanently (the docs say so), and the model can call it at
  any point. The way to stop that is in the script, not in prose. Make `cmd_route` idempotent
  per turn (a marker like `routed_prompt_id`). The second call ends with a one-line "already
  routed". Then a stray invocation is harmless and costs almost nothing.
- **Getting the fork's report in the same turn requires `background: false`.** On the default
  (`true`) the result arrives on the next turn.
- **Codex is unaffected.** Codex's stop path does not route at all; it recommends the whole
  eligible set. The file has to live under `skills/` to be registered by the Codex manifest,
  but the skill itself is Claude-only.

## Proposal

The two unverified items are settled by measurement (whether `UserPromptExpansion` fires, and
the plugin-scoped `agent:`), so what is left is taste rather than design. Shall I build it?
