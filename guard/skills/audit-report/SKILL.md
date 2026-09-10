---
name: audit-report
# The user's entry to the document path, and the counterpart of `audit-turn`. Both are
# `disable-model-invocation: true`, so this line is NOT in any session's standing context: it
# is the autocomplete label, read by a person who is about to type it, and nothing here has to
# deter a model that cannot reach it.
description: Audit a document — triage the file and run the audits that have material in it. Takes the file's path, and the language its reader reads when that is not English.
argument-hint: '<file path> [reader language]'
# Named arguments: the path is required and the language is optional, and an omitted named
# argument expands to the empty string rather than staying in the body as literal text
# (`wiki/ref/claude-code-skill-arguments.md`).
arguments: file language
# The user's, and only the user's. A document audit costs one router plus a fork per pick, and
# there is no event behind it — nothing produces a document for this path, so the only way it
# can be wanted is that somebody wants it. Left model-invocable, this description would sit in
# every session's context inviting the model to audit any file it happened to write, which is
# the same unasked-audit failure the turn path was rebuilt to remove.
#
# The three `audit-report-*` skills stay model-invocable, and must: the router names them for
# the CALLER to invoke, so blocking that would break the only path that dispatches them.
disable-model-invocation: true
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). One `router` triages on both paths; `router.md`
# holds how to judge materiality, which is the same either way, and this file holds what is in
# front of it here — what it is pointed at, the three judgments this path makes differently,
# and the templates, which differ by path because what the caller does with the answer differs.
context: fork
agent: guard:router
# `false`, against the default: the report IS the next instruction, so the caller has to have
# it in the turn it asked for the audit in, and it keeps the full tool set.
background: false
---

# Triage a document

Your subject is one standalone document — a brief, a research write-up, a design note. This
file tells you what you are pointed at, what this path changes about each candidate, and what
to print; how to judge materiality is in your own definition, and it governs.

## 1. Resolve the file

Your invocation supplies two lines:

- file: `$file`
- language: `$language`

If no file was named, say that in one line and stop. Otherwise run `guard-inputs --file $file`
— the second form of the same verb, and the one that answers for a path rather than a turn id.
It prints `file` (the same path, resolved) and any `knowledge dir` the project has configured.
**Use the resolved path in your answer, not the one you were handed.**

If it says there is no file at that path, say so in one line and pick nothing — do not go
looking for the document elsewhere, and do not audit the path you were given as though it were
the text.

**`language` is the only thing you cannot work out for yourself, which is why it is handed to
you.** The document is written in English by design, so reading it tells you nothing about who
reads it, and unlike the turn path you get no request file — nobody typed a prompt that
produced this document. When the line is empty, the document is not being delivered to a
reader in another language and there is nothing to translate.

## 2. What makes this different from a turn

Three things, and each one changes a judgment you would otherwise make the same way.

**There is no request file, and there was no user in front of this text.** A turn is an answer
to somebody; a document is written to be read later by someone who was not there. So you
cannot discount a passage as "not what the user asked for", and you should not try: weigh the
document on what it asserts and explains, not on what prompted it.

**You are the only path that weighs a translation at all.** Here nobody is answering anyone:
the file already exists, in English by design, and whether it is delivered to a reader in
another language is a fact only your caller holds, which is why it hands you `- language:` and
why the translation is a pick you can make. `korean-corrector` is still not yours — the
translator's own report reaches it — and `guard-candidates --doc` offers you exactly what you
may name.

**A section that declares itself open is the strongest reason to name
`audit-report-deferrals`, not a reason to skip it.** Written work often collects its
unresolved questions under a heading that says so, and the heading is a claim: that these are
questions somebody decided to leave open. The claim can be false. An item nobody ever put to
the user, or one the repository could have answered if anyone had looked, sits in that section
indistinguishable from a real one — and the heading is what makes it look accounted for.
Whether each item is a genuine open question is the auditor's call, and it needs to be given
the chance to make it.

## 3. The candidates on this path

Run `guard-candidates --doc`. **The `--doc` is what makes it answer for this path**; without
it you get the turn path's roster, which names entries that would arrive at your document
expecting a transcript. Every name it prints is an audit that exists for documents — nothing
you would have to refuse is offered.

| Key | Your definition's section | What this path adds |
| --- | --- | --- |
| `audit-report-claims` | Claims | the strongest case, below |
| `audit-report-deferrals` | Deferrals | the declared-open rule in § 2 |
| `audit-report-clarity` | Clarity | nothing |
| `korean-translator` | — | judged from `language`, not from the text |

**`audit-report-claims`.** A document that reports research is the strongest case there is:
findings carried forward into someone else's work, where a claim nobody checked becomes a
decision nobody questions.

**`korean-translator`. Do not judge this one from the document**, which is English by design
and tells you nothing about who will read it. The question is whether `language` was supplied.
If it was, this document is being delivered to a reader in that language and the translation
is how they get it. If it was not, do not name this agent. Materiality still applies, the same
as everywhere: a document with nothing in it worth delivering — a stub, a file that records
that there was nothing to record — has nothing to translate either. Do **not** judge any of
the prose, and do not judge how it would translate: word choice and phrasing are this agent's
whole job, and the text it would be judged on does not exist yet.

**A name beginning `audit-` is a SKILL your caller invokes**; anything else is an AGENT it
dispatches with the Agent tool. You invoke nothing yourself, but your output has to say which
it is, because nothing else on this path says it for you.

## 4. What to print

**When you pick nothing**, which is a normal result, say exactly this, with the path filled
in:

```
none — nothing in this file for any candidate. Nothing to dispatch and nothing to change: tell the user in one line that the audit found no material here.
File: <resolved path>
```

**When you pick one or more**, say this, with one line per pick in the order
`guard-candidates --doc` printed them in:

```
Dispatch these CONCURRENTLY, all in one message, handing each one this file and nothing else, and change nothing until every one of them has reported. Every name below is a SKILL, not a subagent: invoke `guard:<name>` with the file path as its argument, and do not dispatch it with the Agent tool. Once they have all reported, apply their findings to the file in one pass, taking them in the order below. Then run ONE more round over the corrected file: dispatch again, concurrently and in one message, exactly those audits whose findings you actually applied — an audit you changed nothing for is finished and does not run again — and apply that round's findings the same way. Stop there; there is no third round. Then say in one line what changed.
File: <resolved path>
- `audit-report-claims` — states "the API rate-limits at 100 rps" with no source
```

**If `korean-translator` is among your picks**, add this after the last one. It is an AGENT,
not a skill, and it runs last — its source is the file after the final round's findings are in
it. Its name takes no `guard:` prefix: it is a user-level agent rather than one of guard's,
which is why the line below spells the name out the way it does. Copy it exactly:

```
Last, once the final round's findings are in the file, dispatch `korean-translator` (subagent_type: "korean-translator") on its own, with two inputs and nothing else: the file above as its source, and <translation path> as the file it writes. Give it no history and no repository paths, and write no draft of your own for it to fix. Then do what its report tells you. If no agent of that name is available, say so in one line and leave the file in English rather than translating it yourself.
```

`<translation path>` is the file's path with `.md` replaced by `.<lang>.md` — `.ko.md` for
Korean. Write it out in full; your caller does no string surgery on a path.

Each pick is given that path and nothing else — the audits resolve what else they need
themselves, and there is no turn id and no transcript to pass, because the document was not
written in a turn.

Keep the order you were given. It is no longer the order anything runs in — they all go out at
once — but it is the order their findings go into the file, in both rounds, and
`korean-translator` is after all of them because its source is the corrected file.

The second round is in the template because the corrections are prose no audit has read, and
it is limited to the audits that actually produced a correction: one that had nothing to fix
has already passed this file, and the edits it did not ask for are not its subject. Which
audits the re-round contains is therefore your caller's to determine, not yours — you cannot
know from here what it ended up changing, so name nobody for it.
