---
name: audit-turn-clarity
# Extremely short — see `audit-turn-claims` for why. guard's router names this skill and the
# caller invokes it by name, so the description never has to attract anything.
description: Invoked by guard only.
argument-hint: '<turn id>'
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). One `clarity-auditor` judges on both
# paths; what differs is where its inputs come from, and that is what this file carries.
context: fork
agent: guard:clarity-auditor
# `true`, the default, stated. Both routers now dispatch their audits in one message and neither
# caller applies a finding until the last report is in, so there is no order for a blocking
# invocation to hold — `false` would only serialise what the template asks to overlap. It was
# tried while the turn path was serial and is recorded in `dev/design.md`. The cost of `true` is
# the narrower background tool set, which does not bite: `clarity-auditor` carries
# `Read, Grep, Glob, Bash, SendMessage` and the filter keeps all five.
background: true
---

# Gather the inputs for a turn, then audit it

Your subject is one finished assistant turn. This file tells you where its parts are; what
makes an explanation followable is in your own definition, and it governs.

You have no conversation history — you were forked clean. Everything below is how you get
what you need.

## 1. Resolve the paths

The turn id is `$ARGUMENTS`. Run `guard-inputs $ARGUMENTS`; it is on your `PATH` and prints
one `key: value` per line. You want:

- **`answer file`** — the answer this turn is giving, written during the turn by the session
  that gave it. **This is what you audit.**
- **`transcript`** and **`turn`** — present when the session recorded a transcript. Step 3.

Read the paths as printed. If the command fails or prints no answer file, say so in one line
and stop — a path you rebuild by guessing at guard's layout points at an empty turn, and an
empty turn reads as a clean one.

If you were given no turn id at all, say that and stop.

## 2. Triage before you gather anything else

Read the answer file. If nothing in it could make a reader stuck — an acknowledgement, a bare
list of paths, a question back to the user, a command to run, a one-line report of an action
— report `verdict: pass` and stop **here**. Do not open the transcript and do not open the
repository. An answer only has clarity findings if it was trying to make someone understand
something.

## 3. The session's history, only for terms you are actually weighing

This is how you answer "was this already explained?", and it is the one thing this path has
that the document path does not. Extract narrowly:

```
<guard_hook.py> transcript find  --transcript <path> --pattern <regex> --until <turn id> --last 25
<guard_hook.py> transcript turn  --transcript <path> --turn <turn id>
<guard_hook.py> transcript index --transcript <path> --last 25
```

Each writes a file and prints its path plus a one-line summary; Read the file. Search for the
**term itself**, windowed with `--until <turn id>` so you only count explanations that came
*before* this answer — an explanation later in the session cannot have helped a reader reading
this turn.

**If extraction fails** — no transcript path was printed, the file is missing, the range was
compacted away — you cannot tell an unexplained term from one explained three turns ago. Do
not guess in either direction. `SendMessage` the main session and ask whether the term was
introduced earlier and where; that answer is testimony from the author, so say in your report
that the finding rests on it. If it cannot answer either, report the term as **unverifiable**
rather than as a finding.

## 4. The repository

The working directory you were launched in. It settles one question and only one: whether a
name in the answer is a real identifier the reader can go open, or a term the answer coined
and owes an explanation for.

## Then audit

Against your reader profile, by the criteria in your definition. Report in the block your
definition specifies, and change nothing but your own memory.
