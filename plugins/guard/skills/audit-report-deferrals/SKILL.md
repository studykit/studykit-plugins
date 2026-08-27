---
name: audit-report-deferrals
# Extremely short — see `audit-turn-claims` for why. guard's router names this skill and the
# caller invokes it by name, so the description never has to attract anything.
description: Invoked by guard only.
argument-hint: '<path to the document>'
context: fork
agent: guard:deferrals-auditor
# `true`, the default, stated — see `audit-turn-clarity`: the audits are dispatched together and
# nothing is applied until they have all reported, so blocking would buy no ordering.
background: true
---

# Gather the context around a document, then audit its deferrals

Your subject is one standalone document — a brief, a research write-up, a design note. This
file tells you where it is and what you have to test a deferral against; what makes a deferral
resolvable is in your own definition, and it governs.

You have no conversation history — you were forked clean. Everything below is how you get what
you need.

## 1. Resolve the path

The document is at `$ARGUMENTS`. Run `guard-inputs --file $ARGUMENTS`; it is on your `PATH`. It
prints the resolved path, and use that rather than the one you were handed.

If it says there is no file at that path, say so in one line and stop. Do not go looking for the
document elsewhere, and do not audit the path itself as though it were the text.

It may also print a `knowledge dir` line. **That is not your input** — skip it.

If you were given no path at all, say that and stop.

## 2. There is no history, and that is the shape rather than a gap

`guard-inputs --file` prints no transcript and no turn id, deliberately: the document was not
written in a turn of the session that dispatched you. So there is no request fixing what was in
scope, and no record of what its author already tried.

**Do not go looking for a transcript, and do not treat its absence as an extraction failure.**
Do not ask the main session why something was deferred: it did not write this document and was
not present when it was written, so its account is not the author's testimony but a third party
recalling something it never saw. `SendMessage` it for one thing only — *where to look* when a
reference in the document is ambiguous. Then look yourself.

**The repository as it stands now is therefore what settles every deferral.** Open it.

## 3. Triage, and the heading that looks like an answer

Scan the document for a deferral — a place it postpones or declares uncertainty about a matter
of fact. If there is none, it passes: **do not read the repository**, and report
`verdict: pass`. An "Open questions" heading with nothing factual under it is not a deferral;
an empty section is not a finding.

**A heading that declares the section open is a claim, not a licence.** Written work collects
its unresolved items under "Open questions", "TBD", "남은 것" — and the heading asserts that
somebody decided to leave them open. That assertion can be false. An item nobody ever put to a
person, or one the repository would have answered if anyone had looked, sits in that section
looking exactly like a real one, and the heading is what makes it look accounted for. Audit
every item under such a heading on its merits. The heading is the reason to look harder, never
the reason to skip.

## 4. Deferrals handed to a person: the document has to carry the evidence

This is the ruling your definition defers to the skill, and it is the reverse of the turn
path's. On a turn, an assistant handing a decision back to the user is plainly legitimate —
the user was there. **Here nobody was**, so "the user decided to leave this open" is legitimate
only when the document records the question actually being put to them: the question asked, and
the person declining to settle it or choosing to settle it later.

A bare "this is up to the user" with no sign the user ever saw it is the author deferring on
their own behalf and calling it someone else's call. Say so.

## 5. The repository

The working directory you were launched in. It is your only source, so expect to open it —
whether it could have answered a deferral is what you are judging.

## Then audit

By the criteria in your definition. Report in the block it specifies, and change nothing but
your own memory.
