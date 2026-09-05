---
name: audit-plan-clarity
# Extremely short — see `audit-turn-claims` for why. The `audit-plan` skill names this one in
# its stage 2 table and invokes it by name; nobody chooses it from a description, and the line
# is loaded into every session's context whether or not a plan is ever audited.
description: Invoked by guard only.
argument-hint: '<path to the plan file>'
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). One `clarity-auditor` judges on all three
# paths; what differs is who the reader is, and on this path that is the sharpest it gets —
# the reader is deciding whether to approve what they are reading.
#
# An entry rather than a plan critic of its own, for the reason every shared audit splits
# here: a memory directory is named after the agent, and this agent's holds the READER
# PROFILE. A second definition would be a second profile, and neither would be the reader's.
context: fork
agent: guard:clarity-auditor
# `true`, the default, stated — see `audit-turn-clarity`. Stage 2 dispatches every critic in one
# message and applies nothing until they have all reported, so blocking would buy no ordering.
background: true
---

# Gather the inputs for a plan, then audit whether its reader can follow it

Your subject is one **implementation plan the user has already approved**, held before it is
built. This file tells you where it is and who is reading it; what makes an explanation
followable is in your own definition, and it governs.

You have no conversation history — you were forked clean. Everything below is how you get what
you need.

## 1. Resolve the path

The plan is at `$ARGUMENTS`. Run `guard-inputs --file $ARGUMENTS`; it is on your `PATH`. It
prints the resolved path, and use that rather than the one you were handed.

If it says there is no file at that path, say so in one line and stop. Do not go looking for the
plan elsewhere, and do not audit the path itself as though it were the text.

It may also print a `knowledge dir` line. **That is not your input** — skip it.

If you were given no path at all, say that and stop.

## 2. Who the reader is, which is what this path settles

**The reader is the person deciding whether to approve this plan** — the user of the session
that dispatched you, which is exactly the person your reader profile describes. Use it as
written; this is the one path where the profile's reader and the text's reader are certainly
the same person.

That fixes the bar. It is not "would a stranger follow this" and not "is this well written".
It is: **can they tell what they are agreeing to?** A plan is approved once and then executed;
a passage the approver cannot picture is a passage they are waving through, and what gets
built is whatever the implementer read into it.

There is a second reader — whoever implements it — and they are covered by the same finding
from the other side. Where the approver cannot tell what a step means, the implementer will
decide it alone.

## 3. There is no history, and that is the shape rather than a gap

`guard-inputs --file` prints no transcript and no turn id. So the question this audit asks on
the turn path — "was this term already explained earlier in the conversation?" — has no
conversation to ask it of, and it should not be asked here anyway.

**A plan is approved as a document.** The user reads it and answers it; nothing they were told
three turns ago travels with it into the work. A term explained nowhere in the plan is
unexplained, and there is no credit for context that was in the conversation.

**Do not go looking for a transcript**, and do not treat its absence as an extraction failure.
The session that dispatched you wrote this plan, so `SendMessage` it for one thing only —
*where to look* when a reference in the plan is ambiguous. Then look yourself. Never ask it
what a passage means: an author explaining their own plan is the plan the reader did not get.

## 4. What is yours here, and what belongs to the critics beside you

Six others read this plan in the same message, and two of them sit close to you:

- **The deferrals audit** holds a decision the plan did **not make**. Yours is a decision it
  **did** make and the reader cannot tell what it was. "Handle errors appropriately" is
  theirs; a step that names a real mechanism in terms the reader has never met is yours.
- **`plan-coherence`** holds whether the steps connect — a step whose input nothing produces.
  Yours is whether the reader can follow the step at all.

Do not report a finding because it is also true; report it because it is yours.

## 5. The repository

The working directory you were launched in. It settles one question and only one: whether a
name in the plan is a real identifier the reader can go open, or a term the plan coined and
owes an explanation for.

## Then audit

Against your reader profile, by the criteria in your definition. If you have no profile, say so
and run the degraded audit your definition describes — do not invent a reader.

Report in the block it specifies, and change nothing but your own memory.
