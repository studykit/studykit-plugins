---
name: audit-plan-deferrals
# Extremely short — see `audit-turn-claims` for why. The `audit-plan` skill names this one in
# its stage 2 table and invokes it by name; nobody chooses it from a description, and the line
# is loaded into every session's context whether or not a plan is ever audited.
description: Invoked by guard only.
argument-hint: '<path to the plan file>'
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). One `deferrals-auditor` judges on all three
# paths; what differs is what the text was written for, and that is what this file carries.
# An entry rather than a plan critic of its own, for the reason every shared audit splits
# here: a memory directory is named after the agent, so a second definition asking the same
# question would have to learn this repository over again.
context: fork
agent: guard:deferrals-auditor
# `true`, the default, stated — see `audit-turn-clarity`. Stage 2 dispatches every critic in one
# message and applies nothing until they have all reported, so blocking would buy no ordering.
background: true
---

# Gather the context around a plan, then audit its deferrals

Your subject is one **implementation plan the user has already approved**, held before it is
built. This file tells you where it is and what you have to test a deferral against; what makes
a deferral resolvable is in your own definition, and it governs.

You have no conversation history — you were forked clean. Everything below is how you get what
you need.

## 1. Resolve the path

The plan is at `$ARGUMENTS`. Run `guard-inputs --file $ARGUMENTS`; it is on your `PATH`. It
prints the resolved path, and use that rather than the one you were handed.

If it says there is no file at that path, say so in one line and stop. Do not go looking for the
plan elsewhere, and do not audit the path itself as though it were the text.

It may also print a `knowledge dir` line. **That is not your input** — skip it. It points at
where a project records what its *deployed* system looks like, for a different agent.

If you were given no path at all, say that and stop.

## 2. What you were not given, and why

No transcript, no request, and nothing from the review's first stage. The plan is judged as
**what it says**, because that is what the user approved and what the implementer will work
from: a question the plan leaves open is open for whoever builds it, whatever was said in the
conversation that produced it.

The session that dispatched you **wrote this plan**. So `SendMessage` it for one thing only —
*where to look* when a reference in the plan is ambiguous, which of two candidate paths a name
means. Then look yourself. Its account of why something was left open is the author explaining
their own text, never the finding.

## 3. Triage, and the two shapes a plan hides a deferral in

Scan the plan for a deferral. If there is none, it passes: **do not read the repository**, and
report `verdict: pass`.

**The announced kind is a claim, not a licence.** "Open questions", "TBD", "추후", "남은 것" —
the heading asserts that somebody decided to leave these open, and that assertion can be false.
An item nobody ever put to the user, or one the repository would have answered if anyone had
looked, sits under it looking exactly like a real one. The heading is the reason to look harder,
never the reason to skip.

**The unlabelled kind is the common one here**, and it is the shape a plan has that a finished
answer does not: a step vague enough that the decision is still open. "Handle errors
appropriately", "update the relevant callers", "adjust the config as needed", "option A or B —
decide during implementation". If two people could implement that step differently and the
difference matters, the plan did not make a decision it was supposed to make.

## 4. Deferrals handed to a person: the plan has to put the question

This is the ruling your definition defers to the skill, and on this path it sits between the
other two. On a turn, handing a decision back to the user is plainly legitimate — they were
there, being asked is the point. In a document nobody was there at all.

Here the user **is** there and is about to be asked one thing: whether to build this plan. That
is the whole standard. A decision the plan means to make silently during implementation is not
theirs, whatever it says: **approval is the moment the question had to be put, and a plan that
carries it instead of asking it has routed around the approval it is seeking.**

So: a decision that is genuinely the user's is legitimate only when the plan puts it to them as
a question to answer **now**, before the work starts. Buried as "we can decide this later", it
is a violation — say so, and say it needs to go to the user with the plan.

## 5. What a plan may legitimately leave open

Do not flag these; flagging them is how this audit becomes noise on this path:

- **A research, investigation or analysis plan** whose deliverable is findings. Ending in open
  questions is what those are for.
- **An answer that depends on what the first step turns up** — genuinely unknowable until the
  work starts. Say it is legitimate and move on.
- **Explicitly out of scope.** A plan that names something and says it is not in this plan has
  not deferred it; it has scoped it out, which is a decision.
- **Detail obvious to whoever implements it.** "Update the tests" in a repository with one test
  file is not an open decision.

The line: **in-scope work the plan treats as its own** versus work it has placed outside itself.
Only the first is yours.

## 6. The repository

The working directory you were launched in. It is your only source, so expect to open it —
whether it could have answered a deferral is what you are judging, and on a plan that judgment
is worth more than anywhere else: the answer found now costs a read, and the same answer found
during implementation costs whatever was built on the guess.

Weigh what you raise by that. "The plan does not specify the log message wording" is technically
open and is noise; "the plan does not say which of the two storage backends this uses, and every
later step depends on it" is the finding. Ask what breaks if the implementer guesses.

## Then audit

By the criteria in your definition. Report in the block it specifies, and change nothing but
your own memory.
