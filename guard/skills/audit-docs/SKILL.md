---
name: audit-docs
# Extremely short — see `audit-turn-claims` for why. guard's Stop hook names this skill and the
# caller invokes it by name, so the description never has to attract anything.
description: Invoked by guard only.
argument-hint: '<paths to the documents>'
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). What the agent's definition holds is what
# makes a passage redundant; what this file holds is which files, and what a document edited in
# a turn brings with it that a document handed over cold does not.
context: fork
agent: guard:doc-auditor
# `true`, the default, stated: this runs alongside whatever else the turn's edits named, and
# nothing is applied until they have all reported.
background: true
---

# Audit the documents a turn just changed

Your subject is one or more of this repository's documents. This file tells you where they are
and what this path gives you; what makes a passage redundant is in your own definition, and it
governs.

You have no conversation history — you were forked clean.

## 1. The files

`$ARGUMENTS` lists them, absolute. Audit those and no others. If it is empty, say so in one line
and stop; do not go looking for documents to audit.

If one of them is an `AGENTS.md` or a `CLAUDE.md`, drop it and say you did — your definition
says why.

## 2. What the turn changed, and why you still read the whole file

Something in this turn wrote these files, which is why you were dispatched. `git diff HEAD --
<path>` shows what changed and is worth reading **first**: new prose is where a fresh
restatement or a fresh paragraph of dead history most often lands.

But **the diff is not your subject** — the file is. A duplicate introduced three turns ago is
still a duplicate, and a document that only gained a heading this turn can still be carrying
the same passage in two places. Read each file in full and report what is in it now.

The one thing the diff settles that the file cannot: whether a passage is new. Say so when it
is. A finding on a line the turn just wrote is one the author can still act on cheaply, and
that is worth a caller knowing.

## 3. There is no turn text and no answer file

Nothing was extracted from the transcript for you and nothing should be. The document is the
whole of what you audit, and the repository is what you check it against.

`SendMessage` the main session for one thing only — *where to look*, when a pointer in the
document is ambiguous and you cannot resolve it from the tree. Not for what a passage means,
and not for whether the author intended it: the author's account of why a paragraph is there
is not evidence that a reader needs it.

## 4. The project's own machinery

Before reporting a finding on axis 5, check whether the project already automates it. A
repository with a linter for link shape, frontmatter or citation format has that tool as the
authority for those rules, and a finding restating what it would print is noise the caller has
to sort through.

Nothing here runs that tool. Whether it runs, and in what order relative to an edit, is the
project's business and its caller's — you report, and the caller applies.

## Then audit

By the criteria in your definition. Report in the block it specifies, and change nothing.
