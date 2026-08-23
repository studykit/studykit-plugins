---
name: audit
description: 'guard''s turn-end audit. Invoked only when guard''s Stop hook asks for it, with the finished turn''s id as the argument — never on your own initiative. Claude Code only.'
user-invocable: false
context: fork
background: false
arguments: [turn]
allowed-tools: Bash(uv run --script ${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py *)
---

# guard: audit this turn

## The dispatch

!`uv run --script ${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py dispatch --turn $turn`

The block above names guard's playbook and the sections to read, one per agent it picked,
along with this turn's own inputs. It has already run: take it as given, and do not re-run it
to confirm or go looking around the plugin for anything else.

Two cases that are not a dispatch, and they are not the same:

- **It says there is nothing to audit** — no record for this turn, no eligible agent, no
  usable turn id. That is the answer, not a failure: audit nothing, report that line, stop.
  Do not go looking for the turn yourself.
- **It is empty, or reads `[shell command execution disabled by policy]`.** Then the command
  did not run. Run the one on the line above yourself with `Bash` and use its output. If that
  fails too, audit nothing and say so.

## What you do

Everything the playbook's `Dispatching` section says, and nothing past it:

1. Dispatch the agents you were named — the router first when the block names it, then the
   agents its report names, following each one's section.
2. **Skip `korean-corrector` even when it is named.** Its input is the translated answer,
   which does not exist yet. Name it as pending in your report instead.
3. Collect what every agent reported.

## What you return

One report to the session that invoked you. It is acting on this alone, so it carries:

- **Per agent**: why it was picked, and what it found. A clean agent is one line.
- **Per finding**: where it is in the answer file, what is wrong, and the evidence the agent
  gave for it — enough to fix it without re-reading the report you are summarizing.
- **What already changed**: the files any corrector edited in place.
- **What is pending**: whether `korean-corrector` was named.

## What you do not do

You do not edit the answer file, you do not translate it, and you do not reply to the user.
Those belong to the session that invoked you: it wrote the answer, it has the conversation
the answer was written for, and it knows which language the user reads. Steps 1 through 5 of
the playbook's `Presenting the result` are its work — your findings are what make its first
step possible.

You also add nothing of your own to a dispatch. Each agent learns what to audit from being
that agent; an opinion from you about the turn is the one thing that can bias all of them at
once.
