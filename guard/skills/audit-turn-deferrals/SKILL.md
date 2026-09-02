---
name: audit-turn-deferrals
# Extremely short — see `audit-turn-claims` for why. guard's router names this skill and the
# caller invokes it by name, so the description never has to attract anything.
description: Invoked by guard only.
argument-hint: '<turn id>'
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). One `deferrals-auditor` judges on both paths;
# what differs is the record of what the author already did, and that is what this file carries.
context: fork
agent: guard:deferrals-auditor
# `true`, the default, stated — see `audit-turn-clarity`: the audits are dispatched together and
# nothing is applied until they have all reported, so blocking would buy no ordering.
background: true
---

# Gather the context around a turn, then audit its deferrals

Your subject is one finished assistant turn. This file tells you where its parts are and what
you have to test a deferral against; what makes a deferral resolvable is in your own
definition, and it governs.

You have no conversation history — you were forked clean. Everything below is how you get what
you need.

## 1. Resolve the paths

The turn id is `$ARGUMENTS`. Run `guard-inputs $ARGUMENTS`; it is on your `PATH` and prints one
`key: value` per line. You want:

- **`answer file`** — the answer this turn is giving, written by guard from the response itself
  and verbatim. **The deferrals you audit are in it.** It does not carry the user's request,
  which matters here as much as the response — that comes from the transcript.
- **`transcript`** and **`turn`** — present when the session recorded a transcript. Step 3.

Read the paths as printed. If the command fails or prints no answer file, say so in one line
and stop — a path you rebuild by guessing at guard's layout points at an empty turn, and an
empty turn reads as a clean one.

If you were given no turn id at all, say that and stop.

## 2. Triage

Read the answer file and scan it for a deferral. If there is none, the turn passes: **do not
read the repository**, and report `verdict: pass`.

## 3. The session's history

Two things live in the transcript and both bear on this audit:

- **the user's request** — what was in scope. This is what separates a deferral the assistant
  owed the user from a decision it correctly handed back to them, so extract it whenever that
  distinction is what you are deciding.
- **the turn's tool activity** — what the assistant already looked at. A question deferred
  *after* running the command that answers it is a clearer violation, and this is the strongest
  evidence there is for "was a means of exercising it available": a session that already used a
  capability plainly had it.

Take what you need:

```
<guard_hook.py> transcript index --transcript <path> --last 12
<guard_hook.py> transcript turn  --transcript <path> --turn <turn id>
<guard_hook.py> transcript find  --transcript <path> --pattern <regex> --until <turn id> --last 12
```

Each writes a file and prints its path plus a one-line summary; Read the file. Start narrow —
`find` for the phrase you are checking, windowed with `--until <turn id>` — and widen only if
that turns up nothing. `index` first when you do not yet know which turn to ask for.

**If extraction fails** — no transcript path was printed, the file is missing, the turn id is
not in it, the range was compacted away — `SendMessage` the main session and ask it for the
specific text you need. That answer is testimony, not evidence: it comes from the author of the
text you are auditing, so use it, and say in your report that the finding rests on what the main
session told you rather than on the transcript. If it cannot supply it either, report on what
you could check and name what you could not.

**Anything else you need, ask the main session for it** — which file it meant, where a component
lives. But never take its answer as the finding itself: it authored the text you are auditing,
so ask it *where to look*, then look yourself.

## 4. Deferrals handed to the user: legitimate here

This is the ruling your definition defers to the skill. A question the assistant explicitly
hands to the user as their decision — "your call", "email vs log — up to you" — **is
legitimate on this path, and needs no further evidence.** The user was there and being asked is
the point.

The one thing that overrides it: a question the repository already fixes the answer to. Handing
a settled matter back is still a punt.

## 5. The repository

The working directory you were launched in. Read it directly — whether it could have answered a
deferral is what you are judging.

## Then audit

By the criteria in your definition. Report in the block it specifies, and change nothing but
your own memory.
