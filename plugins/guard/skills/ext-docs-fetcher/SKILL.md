---
name: ext-docs-fetcher
description: "Get the documentation a question rests on: what this project has already saved, or the primary source fetched and saved if it has not. guard dispatches the ext-docs-fetcher subagent, which searches, quotes, writes the reference file and indexes it, and reports the local path saying which it did. Claude Code only."
argument-hint: '<question>'
disable-model-invocation: true
allowed-tools: Agent, Bash, Read
---

# Fetch documentation

The work goes to the `guard:ext-docs-fetcher` subagent. It is the only agent with network access,
and the reason it exists is that a page pulled into this session is paid for on every turn
after, while a page read in passing is a page nobody saves.

## What to dispatch it with

**The user's question, verbatim.** Their wording, not your restatement and not keywords you
distilled from it — a question already condensed into search terms has lost exactly the
context that separates a reference from a lookalike.

With **no argument**, the question is whatever the user was just asking about. Say what you
understood the subject to be before dispatching, in one line, so a wrong reading is caught
before a fetch is spent on it.

Dispatch it **alone and in the foreground**: you need the result now, and there is nothing
else in flight to batch it with. Add nothing of your own — not what you expect the answer to
be, not which page you think it is on. It resolves the refs directory itself.

## Relay the result

Its report gives one line per file, each saying **already saved** or **fetched and saved**, or
`none`. Relay which it was; that distinction is the answer, not a detail.

- **Already saved** — read the file and tell the user it was already here, with the path.
  Nothing changed on disk.
- **Fetched and saved** — read it, and say plainly that the repository changed: a new file
  under the refs directory and a row in that directory's index. Name the file. Then
  **dispatch `guard:ext-docs-auditor` on exactly those paths**, unchanged. The agent that wrote a
  reference is the one party that must not grade it, and on this path no turn-end audit has
  run. Relay what it finds.
- **`none`** — say that nothing saved covers the question and no primary source was findable.
  Do not fill the gap from memory; that is the whole failure this arrangement prevents.

When you go on to answer from one of these files, cite **both** the source URL recorded inside
it and its local path, per the refs rule guard states at session start.

If the report has a line marked as **for your caller, not the file**, that is a project-specific
conclusion the fetcher was forbidden from writing into the reference. Surface it and say where
it should live — a design note, an `AGENTS.md`, a comment next to the code. Putting it back
into the reference is the one thing you must not do with it.
