---
name: audit-turn
# The autocomplete label, read by a person about to type it. It is not in any session's
# standing context — see `disable-model-invocation` below — so unlike the `audit-turn-*`
# descriptions it has nothing to deter and can simply say what the command does.
description: Audit the assistant turn that just finished — triage it and run the audits that have material in it. Takes a turn id; with none, audits the turn guard recorded last.
argument-hint: '[turn id]'
# A NAMED argument, not `$ARGUMENTS`: an omitted named argument expands to the empty string
# while an omitted `$0` stays in the body as literal text, and omitting it is the normal case
# here (`wiki/ref/claude-code-skill-arguments.md`).
arguments: turn
# The user's, and only the user's, and this is the switch the whole redesign turns on. The turn
# audit was dispatched from the Stop hook on every turn that had an answer file, and the common
# result was a router reporting that there was nothing in the turn. Moving the trigger to the
# user is only half of that fix: left model-invocable, this description would sit in every
# session's context inviting the model to audit turns on its own initiative, which is the same
# unasked audit arriving by a different door. Disabled, it also keeps its own description out of
# that context, so the entry point costs nothing on a turn nobody audits.
#
# The three `audit-turn-*` skills stay model-invocable, and must: the router names them for the
# CALLER to invoke, so blocking that would break the only path that dispatches them. What keeps
# THEM from being chosen unasked is their own descriptions, which say nothing about what they
# audit.
disable-model-invocation: true
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). One `router` triages on both paths; `router.md`
# holds how to judge materiality, which is the same either way, and this file holds what is in
# front of it here — where the turn's parts are, what the turn path changes about each cue, and
# the templates, which differ by path because what the caller does with the answer differs.
context: fork
agent: guard:router
# `false`, against the default, and this is the one entry point where that matters: the report
# IS the next instruction, so the caller has to have it in the turn it asked for the audit in. A
# backgrounded router would hand the user's request back to them and deliver the routing later
# as a notification. It also keeps the full tool set, which a backgrounded fork does not get.
background: false
---

# Triage the turn that just finished

Your subject is one finished assistant turn. This file tells you where its parts are, what
this path changes about each candidate, and what to print; how to judge materiality is in your
own definition, and it governs.

## 1. Resolve the turn

The turn id is `$turn`, and it is normally empty — the user asks about the turn they just read
rather than naming one. Run `guard-inputs $turn`.

With an id it resolves that turn. With nothing it resolves **the last turn guard recorded**,
which is the one the user means. What it prints:

- **turn** — the id of the turn you are triaging. It is the id your answer carries and the id
  every audit you name is invoked with, so take it from here rather than from the argument you
  were handed — an audit invoked with an empty id resolves a turn of its own.
- **answer file** — the response this turn gave, cut from the transcript by guard and not
  written by the session that gave it. This is your evidence, and the only thing that can put
  a candidate on the list: one is worth running because of something the *assistant* wrote,
  never because of what a command printed and never on the strength of the request alone. What
  you name goes to the transcript itself for what the turn ran and what earlier turns
  established, so do not ask for that, do not wait for it, and do not treat its absence as a
  reason to pick or skip anything.
- **request file** — the user's words for this turn, verbatim, saved by guard. It may not be
  there; when it is not, judge from the answer alone. It is not part of the answer, nothing
  audits it and nothing corrects it, and it has exactly one use: the materiality call in § 2.

If the answer file is missing or empty, say so in one line and pick nothing. Do not go looking
for the turn elsewhere.

## 2. Materiality is relative to the request, which is why you are given it

A paragraph explaining how something works is the answer's substance when the user asked how
it works. The same paragraph hung off "turn setting X on" is padding: that turn is a state
change and its confirmation, and the explanation is there because the answer had a file to
fill, not because anyone asked. Read the request first, then ask what in the answer the user
actually came for — and weigh the rest of it lightly.

Two limits, and they are what keep this from undoing the rule in § 1. The request can only
ever make you name **fewer** audits than the answer alone would — it is never itself the
reason to name one. And "the user did not ask for this" discounts a passage as padding; it
never excuses skipping an audit whose material is there anyway, because an unsupported claim
is unsupported whatever prompted it. If you cannot tell whether a passage was asked for, treat
it as asked for.

Nothing escapes those two limits: there is no candidate on this path that the answer file
cannot evidence.

## 3. The shapes that come up empty here

An empty answer is normal and frequent on this path. Some shapes that produce one — the list
is examples, not the set, so a turn that resembles none of them can still be empty: an
acknowledgement, a relay, a question back to the user, a turn whose whole content is output
you can see was quoted from the tool activity, a check that something works whose finding is
that it does.

**The user addressing an agent directly is one of these, and it is the one worth naming.**
When the request begins by naming an agent — `@some-agent`, `@plugin:some-agent` — the answer
you are reading is not that agent's. The session dispatched it and reported that it is
running; the agent is talking to the user somewhere you cannot see. So the answer file holds a
relay, and picking anything means auditing a sentence whose whole content is "it is running".

What that agent eventually says is auditable, but not by you and not on this turn. It reaches
guard as a **file** — the agent writes one and reports its path, and the user audits that path
on the document path when they want it audited. A turn spent dispatching one is empty; return
`none`.

## 4. The candidates on this path

Run `guard-candidates` — bare, with no argument; that is the form that answers for the turn
path. The keys it prints are the ones below, and the key is what you print and what your
caller invokes.

| Key | Your definition's section | What this path adds |
| --- | --- | --- |
| `audit-turn-claims` | Claims | the exclusion below |
| `audit-turn-deferrals` | Deferrals | nothing |
| `audit-turn-clarity` | Clarity | nothing |

**`audit-turn-claims`, and it is the one cue this path changes.** No, also, when the response
only **reports what just happened in this session** — which hooks fired, what a command
printed, what the assistant was instructed to do, what state the session is in. A reader
cannot check these against anything outside the turn, because the evidence and the assertion
arrived together; there is no repository, no file and no transcript that could disagree.
Paraphrasing rather than quoting does not change that: the same sentence in the assistant's
own words is still a report of what the session just observed, and it is the paraphrase that
most often smuggles this past the rule.

The distinction is whether the claim has somewhere to be wrong. "The `Stop` hook fired and
asked for an audit" is this turn narrating itself. "The `Stop` hook fires on every turn" is a
claim about how the tool behaves — checkable, and therefore material.

**There is deliberately no translation candidate here.** `guard-candidates` does not offer one
on this path and you may not name one: an ordinary turn produces no document, so there is
nothing here to translate. If a candidate line ever names a translator, treat it as the roster
being wrong and say so rather than picking it.

## 5. What to print

**When you pick nothing**, say exactly this:

```
none — nothing in this turn for any candidate. Tell the user in one line, and do nothing else.
```

No path goes in that answer, and that is the difference from the template below. The user read
this turn before asking about it, so a clean result is one sentence — not a summary of what was
checked, and not a re-delivery of the turn.

**When you pick one or more**, use this, with one numbered line per pick in the order
`guard-candidates` printed them in:

```
Dispatch these CONCURRENTLY, all in one message, and wait until every one of them has reported. Every name is a SKILL: invoke `guard:<name>` with the turn id <turn id> and nothing else — not with the Agent tool, and with no instructions of your own about what to look for. Then REPORT what they found to the user, in the user's language, taking them in the order below: a line or two per finding, with the reason for the pick alongside what that pick found. A clean result is one line. Correct NOTHING: the turn these audits judge was printed to the user before they asked for this, so there is no document to fix and the answer file is guard's own copy — editing it changes nothing the user will ever read. Do not re-run an audit, do not open a file for this, and do not write the report anywhere: it is a reply, not a deliverable.
Answer file: <answer file path>
1. `audit-turn-claims` — asserts "Redis가 Postgres보다 항상 빠릅니다" as settled fact
2. `audit-turn-deferrals` — leaves "정확한 수치는 확인 필요" for a number the repo records
3. `audit-turn-clarity` — the whole explanation is new to this reader
```

**There is no second round on this path.** The audits report and the user is told; nothing is
corrected, so there is no corrected prose for a further round to read. Do not invite one.

**Nothing about a translation is yours to instruct.** There is no block to add here and no
translator to name.
