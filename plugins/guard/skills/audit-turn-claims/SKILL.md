---
name: audit-turn-claims
# Extremely short, and deliberately. This line is loaded into every session's context whether
# or not guard runs, so its cost is paid on every turn — while its only job is to keep the
# model from choosing this skill for itself. It never has to attract an invocation: guard's
# router names this skill by name and the caller invokes it from the router's report, so a
# description that described the audit would buy nothing and would get it run over turns
# nobody routed. `disable-model-invocation: true` is not the answer — it would shut guard out
# too, and guard is the only thing that should be invoking this.
description: Invoked by guard only.
argument-hint: '<turn id>'
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). One `claims-auditor` judges on both paths;
# what differs is where its evidence comes from, and that is what this file carries.
context: fork
agent: guard:claims-auditor
# The default, stated — see `audit-turn-clarity` for why it is not `false`.
background: true
---

# Gather the evidence behind a turn, then audit it

Your subject is one finished assistant turn. This file tells you where its parts are and what
counts as evidence on this path; what makes a claim supported is in your own definition, and
it governs.

You have no conversation history — you were forked clean. Everything below is how you get what
you need.

## 1. Resolve the paths

The turn id is `$ARGUMENTS`. Run `guard-inputs $ARGUMENTS`; it is on your `PATH` and prints one
`key: value` per line. You want:

- **`answer file`** — the answer this turn is giving, written by guard from the response itself
  and verbatim. **This is what you audit.** Nobody appends to it, so it will not tell you what
  the turn ran or what an earlier turn established; that is what the transcript is for.
- **`transcript`** and **`turn`** — present when the session recorded a transcript. Step 3.

Read the paths as printed. If the command fails or prints no answer file, say so in one line
and stop — a path you rebuild by guessing at guard's layout points at an empty turn, and an
empty turn reads as a clean one.

If you were given no turn id at all, say that and stop.

## 2. Triage, and on this path it can end the audit

Read the answer file and scan it for a load-bearing claim. If it has none — it only asks the
user a question, or reports an action it just took — the turn passes: **do not read the
repository and do not extract anything**, and report `verdict: pass`. Do not open the repo for
a turn that asserts nothing verifiable.

This early exit is specific to the turn path. A turn is an answer to somebody and is often just
an acknowledgement; that shape does not occur in the document path's material.

Remember what triage does **not** excuse — a proposal is not "nothing verifiable". Your
definition says why.

## 3. The session's history, and it is evidence

This is what this path has that the document path does not. Two things live in the transcript
and both bear on whether a claim is backed:

- **the tool activity** — the commands the turn ran and what they printed. Treat that output as
  **first-class evidence**: a claim that restates or directly follows from a command's output is
  SUPPORTED even if the answer does not re-cite it.
- **the user's request** — context. It may contain facts the user already confirmed; treat those
  as given, not as claims to re-verify.

Take what you need; nothing lands in your context that you did not ask for:

```
<guard_hook.py> transcript index --transcript <path> --last 12
<guard_hook.py> transcript turn  --transcript <path> --turn <turn id>
<guard_hook.py> transcript find  --transcript <path> --pattern <regex> --until <turn id> --last 12
```

Each writes a file and prints its path plus a one-line summary; Read the file. Start narrow —
`find` for the phrase or number you are checking, windowed with `--until <turn id>` so you are
looking at what came *before* the answer — and widen only if that turns up nothing. `index`
first when you do not yet know which turn to ask for.

**If extraction fails** — no transcript path was printed, the file is missing, the turn id is
not in it, the range was compacted away — `SendMessage` the main session and ask it for the
specific text you need. That answer is testimony, not evidence: it comes from the author of the
text you are auditing, so use it, and say in your report that the finding rests on what the
main session told you rather than on the transcript. If it cannot supply it either, report on
what you could check and name what you could not.

**Anything else you find you need, ask the main session for it** — a file it referred to
obliquely, which of two candidate paths it meant, what a term in the answer refers to. One
question is cheaper than a wrong verdict. What you must NOT do is treat an answer as evidence:
the main session is the author, so its account of what a command showed is a claim, not proof.
Ask it *where to look*, then look yourself.

## 4. The repository

The working directory you were launched in. Read it directly, and expect to: where the activity
cannot settle a claim, the repository as it stands now is what does.

## 5. Documentation citations: a local copy is required here

This is the ruling your definition defers to the skill. On this path the answer must point to a
local saved copy under the refs directory (`refs_dir`); confirm the file exists and supports the
claim. **A docs claim with no existing local copy, or with a path that resolves to nothing, is
unsupported.** The session that wrote this turn is told to save one, so its absence is a defect
rather than a limitation.

## Then audit

By the criteria in your definition. Report in the block it specifies, and change nothing but
your own memory.
