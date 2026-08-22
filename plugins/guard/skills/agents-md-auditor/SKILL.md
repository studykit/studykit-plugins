---
name: agents-md-auditor
description: "Audit AGENTS.md / CLAUDE.md files as agent instruction files: whether CLAUDE.md is a thin @AGENTS.md import, whether the content is a map pointing at deeper docs or a payload that grows with the project, whether it holds implementation detail, spec-class material, or things any model already knows, whether its pointers still resolve, and what hazard the repository has that it never mentions. guard dispatches the agents-md-auditor subagent, which judges the files in a fresh context and reports. It edits nothing. Claude Code only."
argument-hint: '[file | directory] …'
disable-model-invocation: true
allowed-tools: Agent, Bash, Glob, Read
---

# AGENTS.md audit

The work goes to the `guard:agents-md-auditor` subagent in a **fresh context**, and that
separation is the point. An instruction file's author cannot judge what it costs: they know
which parts they skip, so the file reads as short to them and as a wall to the session that
loads all of it. If you wrote or edited any of these files earlier in the session, you are
the least reliable judge of them.

The auditor asks one question per axis and answers it against the repository: is `CLAUDE.md`
a thin import, is the content a map or a payload, is anything here implementation detail /
spec material / general knowledge, do the pointers resolve, and what hazard is missing.

## Which files

With **no argument**, audit the instruction files at the repository root — `AGENTS.md` and
`CLAUDE.md` if they exist. Say which you found before dispatching. If neither exists, say
so and stop; there is nothing to audit and creating one is not this skill's job.

With a **directory argument**, take the `AGENTS.md` / `CLAUDE.md` directly in it — not the
whole tree beneath it. A monorepo has one per package and they are separate audits with
separate verdicts; sweeping them all into one dispatch produces a report nobody can act on.
If the user asked for a subtree, dispatch **one auditor per directory**, in parallel, in one
message, each given only that directory's files.

With **file arguments**, pass exactly those.

Skip vendored and generated trees (`node_modules`, `vendor`, build output). If the
expansion covers more than roughly 10 directories, say how many you found and ask whether
to narrow before dispatching.

## Dispatch the auditor

Dispatch `guard:agents-md-auditor` with the Agent tool. Give it:

- the explicit list of files to audit;
- any instruction the user attached to the invocation ("only the pointer check", "ignore
  the length findings"), passed through verbatim;
- nothing else. Do not summarize the files, pre-judge any section, or tell the auditor what
  you expect it to find — that is the bias the fresh context exists to avoid. It reads the
  repository itself and forms its own view.

## Relay the result

The auditor changes nothing, so everything it reports is still yours to decide about.

Report what it found, grouped as it grouped them, quoting each passage verbatim in its
original language. Then separate the findings into two lists, because they are not the same
kind of work:

- **What you can fix now** — a dead pointer with an obvious current path, a paragraph the
  code already states, a line of generic advice, content sitting in `CLAUDE.md` that belongs
  in `AGENTS.md`. Deletions and moves within files that already exist. Make these, and say
  what you changed.
- **What needs a decision** — every finding whose fix is "this belongs in its own document":
  a spec buried in the instruction file, a long section that should become a deeper doc and
  a pointer. Creating those documents is a change the user has not asked for. Name the
  finding, name where the auditor said the content should live, and leave it.

If the auditor reports that what remains does not justify loading the file in every session,
say that plainly rather than folding it into the list. It is a judgment about the file as a
whole and the user should hear it as one.

If the auditor reports a finding as **unverified**, relay it as unverified and say what it
could not check. Do not go and check it yourself to promote it — you would be the author
verifying the audit of your own file.

A clean audit is one line. That is the expected outcome for a file that is already a map,
not a sign the audit failed.
