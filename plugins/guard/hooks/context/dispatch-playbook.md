# guard dispatch playbook

How to run each of guard's agents and what to do with what it reports. You are sent here by
section name — guard's router names the sections for the agents it picked, a `/guard:*`
command names one section directly, and guard's session-opening context names
`refs-finder`, which runs before an answer exists and so is never routed. There is no
section for the router itself: routing is its own job, described in its definition, and its
report tells you what to do next.

**Read only the sections you were named, and do exactly what they say.** Everything each
agent needs that is specific to this turn — the answer file, the source files, the
transcript pointer — comes with the dispatch that sent you here, never from this file.

You never gather the session's history — the agents that need it read the transcript for
themselves. See "The answer file, and the session's history".

**Two audiences, two languages.** The answer file and your reply to the user are in the
user's language, because a person reads them. Everything in between — what you write in a
dispatch, what the agents report back, what you say to an agent — is English, because only
agents read it. So a Korean answer is audited by agents reporting in English, and the
corrections still land in the file as Korean. Do not translate the answer file, and do not
relay an agent's English report to the user untranslated: say in the user's language what
changed.

This file exists so that text is stored once and read only when a turn actually gets
routed. Guard's hook output is paid for in your context on every turn, so it carries only
what changes per turn: the paths, which agents are switched on, and what mode each is in.

## The answer file, and the session's history

The **answer file** is where this turn's substance lives. You wrote it during the turn; the
reply you gave the user was short and named this path. It is not a copy of something already
delivered — it is the deliverable, which is why the agents can still fix it.

Two rules. Do not paste its contents into a reply: printing the text is what this shape
exists to avoid, and printing it twice (before and after correction) is the waste that
motivated the whole arrangement. And if you find the file empty or missing, guard filled it
in from the response after the fact and said so in a comment at the top; treat it as the
answer anyway, and write it properly next time.

The **session's history** — what the user asked, what this turn ran, what an earlier turn
established — is in the transcript, and an agent that needs it extracts what it needs
itself. When the dispatch that sent you here included a transcript path and a turn id, pass
both straight through to any agent whose section says it may need history, along with the
extractor: `scripts/guard_hook.py` in the plugin directory holding this playbook — this file
is `hooks/context/dispatch-playbook.md`, so it is `../../scripts/guard_hook.py` from here,
and you know this file's absolute path because you were given it. **Do not run the extraction
yourself and do not summarize the session for the agent.** Gathering it here would put the
largest cost of an audit in the context the user is talking to, before anything is known to
need it.

**Fallback.** An agent can fail to get an extract — no transcript path was passed, the file
is gone, the turn id is not in it, a compaction dropped the range. It is then allowed to
`SendMessage` you and ask, and answering is the right thing to do. Two limits on your
answer, and they are the reason this is a fallback rather than the normal path:

- Give it the **raw text** — the command and its output as they were, the request as it was
  worded. Not your account of what happened, and not your reasoning about why the answer was
  right.
- Say plainly that it came from you rather than from the transcript. You wrote the text
  being audited, so anything you supply is testimony, not evidence, and the agent is
  required to mark a finding that rests on it.

If you cannot supply it either, say so and let the agent report on what it has. An audit
that names what it could not check is useful; one that treats unverifiable as verified is
not.

## Dispatching

Common to every agent section below.

Dispatch with the **Agent** tool and `subagent_type: "guard:<key>"` — `guard:claims-auditor`
for the `claims-auditor` section, and so on. Never invoke a `/guard:*` skill to do it;
those are the user's own entry point.

Send every agent you were named in **ONE message** so they run concurrently. Keep the
order the sections were given in: the read-only auditors report before a corrector edits
anything, so a corrector never rewrites a sentence an auditor was about to flag.

Each dispatch carries **only its own inputs** — the ones handed to you with the section
name. An agent learns what to audit from being that agent, not from a scope argument, so
do not add instructions of your own about what to look for, and do not tell it what you
think of the turn. It forms its own view; an argument from the turn's author is the one
thing that can bias all of them at once.

Two modes, given per agent as `= fresh` or `= reuse`:

- **`fresh`** — dispatch a new instance. Nothing else to do.
- **`reuse`** — one instance serves the whole session, named `guard-<key>`
  (`guard-korean-corrector` for `korean-corrector`). **Look for it first:** if it already
  exists in this session, `SendMessage` it (`to: "guard-<key>"`) and it resumes with
  everything it has already read and judged. Only if it does not exist, dispatch it with
  the Agent tool and `name: "guard-<key>"` so later turns can find it. Resume first,
  dispatch second — the other order spawns a second instance under a name that is already
  taken, and then two of them exist with divergent histories and no way to tell which one
  answered.

When you report back, relay the router's reason for each pick alongside what that agent
found. **A clean result is one line** — every agent passing is the common case, and a
paragraph celebrating it trains the user to skip the report that matters. A pick that
plainly misread the turn is worth saying so about rather than working around.

## `refs-finder`

Names the reference documents already saved in this project that bear on the user's
question, so you read the saved copy instead of answering from memory or fetching the page
again.

This one is not part of the turn-end fan-out and three of the rules above do not reach it.
It runs **before you answer**, so dispatch it **alone and in the foreground** — you need
its result this turn, and there is nothing else in flight to batch it with. The
auditors-before-correctors ordering is about the answer file, which does not exist yet. And
you are sent here by guard's session-opening context rather than by the router, once, for
whichever questions call for it — not by a per-turn instruction, so deciding that a
question could rest on saved documentation is yours.

Inputs: **the user's question, verbatim** — their wording, not your restatement of it and
not keywords you distilled from it. guard keeps no copy of the prompt, so you are the only
source it has, and a question you have already condensed into search terms has had exactly
the context stripped out that tells a reference apart from a lookalike. Nothing else: it
resolves the refs directory itself.

What it returns is a list of paths with one line each, or `none`. Then:

- **On a result** — read the files it named, yourself. It deliberately quotes nothing, so
  its report is a set of pointers and not evidence. When your answer rests on one, cite
  both the source URL recorded inside the reference and its local path, per the refs rule
  guard states at session start.
- **On `none`** — proceed and say nothing about it. This is the common case, and a line
  reporting that a lookup found nothing is noise in an answer the user asked for something
  else in.

Either way, do not paste its report into your reply and do not tell the user a lookup
happened. It changes nothing on disk.

## `claims-auditor`

Audits the turn for claims asserted without adequate evidence.

Inputs: the answer file, plus the transcript path, this turn's id and the extraction
command — it may need history, since a claim is often grounded by a command run several
turns ago and an auditor that cannot reach it reports a backed claim as unbacked.

It changes nothing you need to review — it may update its own project memory, and
nothing else. If it reports violations, address them; otherwise continue.

## `deferrals-auditor`

Audits the turn for work punted as TBD / 확인 필요 that the repository could have answered.

Inputs: the answer file, plus the transcript path, this turn's id and the extraction
command — it may need history, since the user's request is what separates a deferral the
assistant owed from a decision it correctly handed back.

It changes nothing you need to review — it may update its own project memory, and
nothing else. If it reports violations, address them; otherwise continue.

## `clarity-auditor`

Audits the turn for whether its reader can follow it: terms used but never explained,
mechanisms given with no concrete example, and explanation pitched wrong for what this
reader already knows.

Inputs: the answer file, plus the transcript path, this turn's id and the extraction
command — it needs history, because a term explained two turns ago does not need explaining
again and it has no other way to know.

It changes nothing you need to review — it may update its own memory, and nothing else. Its
findings are the one kind that ask you to **add** to the answer rather than correct it: a
definition, an example, a paragraph cut. Apply them in the answer file like any other
finding.

If its report says the reader profile is MISSING, relay that in one line — the user
establishes one with `/guard:reader-profile`, and until they do, axis 3 is not being checked.
Say it once; repeating it every turn is how a useful notice becomes noise.

## `korean-corrector`

Audits the turn for Korean prose that reads as translated English rather than written.

Inputs: the answer file. No history — Korean prose is judged as prose, so do not pass it
the transcript.

It **edits the answer file in place**, so its corrections are already applied when it
reports. Relay any phrase it listed as unfixed; that one is yours to resolve. On a pass it
changes nothing.

## `comment-corrector`

Audits the source files it is given for comments that are false, that only restate the
code, or that are missing where the intent is not obvious.

Inputs: the absolute file paths you were given, and only those — pass them through
unchanged. Adding a file means editing something this turn never touched. It reads neither
the turn record nor the transcript.

It **edits the comments in place**, so its changes are already in the files when it
reports. Relay what it changed AND what it left unfixed — an unfixed finding needs the
user — and do not re-edit its work.

## `agents-md-auditor`

Audits the `AGENTS.md` / `CLAUDE.md` files it is given as agent instruction files: whether
`CLAUDE.md` is a thin `@AGENTS.md` import, whether the content is a map pointing at deeper
docs or a payload that grows with the project, whether it carries implementation detail,
spec-class material, or things any model already knows, whether its pointers still resolve,
and what hazard the repository has that it never mentions.

Inputs: the absolute file paths you were given, and only those — pass them through
unchanged. Adding a file means auditing something this turn never touched. It reads neither
the turn record nor the transcript; it reads the repository itself, which is where its
evidence comes from.

It **changes nothing** — it may update its own project memory, and nothing else. Its
findings are the kind you must not apply on autopilot: deleting a section usually means
moving its content into a deeper doc that does not exist yet, and creating that document is
a change the user has not asked for. So relay what it found and what it proposes, and make
the deletions and pointer fixes you can make without inventing a new document. Where a
finding needs a file created, say so and leave it to the user.

## Presenting the result

The correctors have already edited what they were given. What is left is yours:

1. **Apply the auditors' findings to the file.** An unsupported claim, a deferral the repo
   could have answered — fix it where it is written, in the file, with `Edit`. A finding you
   are leaving unfixed stays unfixed on purpose and is named in your reply.
2. **Reply short.** What changed and why, in a line or two per finding, then the path. A
   clean audit is one line. Do not restate the answer and do not paste the file.
3. **Open the file** so the user reads the corrected version without hunting for it:
   `open <path>` on macOS, `xdg-open <path>` on Linux, `start <path>` on Windows. Once, at
   the end, after every correction has landed — opening it mid-audit shows the user text
   that is still being fixed.

The path in steps 2 and 3 is the **answer file the dispatch named**. It is the one holding
the answer to the user's question, corrections and all. Do not open a file you wrote during
the audit, and do not start a new one for this report: an audit summary is worth a line in
the reply, not a document, and opening it hands the user a memo about the answer instead of
the answer.

**When the dispatch named no answer file**, steps 1 and 3 do not apply — there is nothing to
correct and nothing to open. That is the file-reading agents dispatched on their own:
`comment-corrector` and `agents-md-auditor` work on the files the turn wrote, and a turn
with no turn-reading agent eligible never wrote an answer file in the first place. Reply
per step 2, naming the files that changed and the findings you did not apply; the user
reads those in the diff, not in an opened document.
