# guard dispatch playbook

How to run each of guard's agents and what to do with what it reports. You are sent here by
section name — guard's router names the sections for the agents it picked, and guard's Stop
hook names `ext-docs-auditor` directly when the turn wrote a saved reference. There is no
section for the router itself: routing is its own job, described in its definition, and its
report tells you what to do next. `ext-docs-fetcher` has no section either, for the opposite
reason — nothing dispatches it on guard's behalf, so there is no caller to instruct: the main
session picks it from its description like any other agent, and what to do with what it
reports is in its report.

**Read only the sections you were named, and do exactly what they say.** Everything each
agent needs that is specific to this turn — the answer file, the source files, the
transcript pointer — comes with the dispatch that sent you here, never from this file.

You never gather the session's history — the agents that need it read the transcript for
themselves. See "The answer file, and the session's history".

**English until the audits are done; the user's language last.** The answer file is written
in **English**, and so is everything around it — what you write in a dispatch, what the
agents report back, what you say to an agent. The audits run against that English file.

Only after they have run and their findings are applied do you produce the version the user
reads, in their language, as a **separate file**: the answer file's path with `.md` replaced
by `.<lang>.md` (`.ko.md` for Korean). That translation is the last step of the turn, and
`Presenting the result` says how. Your reply to the user is in their language too.

Why this order rather than the obvious one: the auditors are measurably weaker on non-English
prose. The same answer, translated, drew findings that its original passed clean — twice, from
two different agents. Auditing the English and translating after is how the user's language
stops costing them the audit. The translation is then checked in its own right by
`korean-corrector`, which is why that agent alone runs after the others rather than beside
them.

Never relay an agent's English report to the user untranslated: say in the user's language
what changed.

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

**`korean-corrector` is the one exception and must not go in that message.** Its input does
not exist yet — it audits the translation, and the translation is made after the other agents
have reported and their findings are applied. Dispatch it on its own, at the step
`Presenting the result` names. Sending it with the others points it at an English file, which
it correctly declines to audit, and the turn ships an unchecked translation.

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

## `claims-auditor`

Audits the turn for claims asserted without adequate evidence.

Inputs: the answer file, plus the transcript path, this turn's id and the extraction
command — it may need history, since a claim is often grounded by a command run several
turns ago and an auditor that cannot reach it reports a backed claim as unbacked.

It changes nothing you need to review — it writes nothing at all. If it reports
violations, address them; otherwise continue.

## `deferrals-auditor`

Audits the turn for work punted as TBD / 확인 필요 that the repository could have answered.

Inputs: the answer file, plus the transcript path, this turn's id and the extraction
command — it may need history, since the user's request is what separates a deferral the
assistant owed from a decision it correctly handed back.

It changes nothing you need to review — it writes nothing at all. If it reports
violations, address them; otherwise continue.

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

Audits Korean prose that reads as translated English rather than written. On this turn that
prose is the **translation**, not the answer file — the answer file is English and this agent
would rightly report nothing about it.

So this section runs **out of order**, after the other agents have reported, after you have
applied their findings, and after you have written the translation. `Presenting the result`
is where it belongs in the sequence; the router names it here only to tell you it is switched
on and in which mode.

Inputs: the **translation file** (the answer file's path with `.md` replaced by `.ko.md`), and
nothing else. No history — Korean prose is judged as prose, so do not pass it the transcript.
Do not pass it the answer file; that is the English original and not what the user reads.

It **edits the translation in place**, so its corrections are already applied when it reports.
Relay any phrase it listed as unfixed; that one is yours to resolve. On a pass it changes
nothing.

## `comment-corrector`

Audits the source files it is given for comments that are false, that only restate the
code, or that are missing where the intent is not obvious.

Inputs: the absolute file paths you were given, and only those — pass them through
unchanged. Adding a file means editing something this turn never touched. It reads neither
the turn record nor the transcript.

It **edits the comments in place**, so its changes are already in the files when it
reports. Relay what it changed AND what it left unfixed — an unfixed finding needs the
user — and do not re-edit its work.

## `ext-docs-auditor`

Audits the saved reference files it is given against what a reference may contain: a
trustworthy source named, the content attributed to it rather than recalled, and — the rule
this exists for — nothing in them about this repository.

Inputs: the absolute file paths you were given, and only those — pass them through
unchanged. It reads neither the turn record nor the transcript, and it has no network by
design; its evidence is the files and the repository around them.

You are sent here whenever the turn wrote a file under the refs directory, whoever wrote it —
this agent has no switch, because the party most likely to break the rule it enforces is the
party that just saved the file, and that party must not be the one deciding whether it gets
checked.

It **changes nothing**, and carries no tool that could. Its findings split cleanly and you
should treat the halves differently:

- **A heading, a source line, an index row** — fix it. Renaming a section that labels
  general observations as this project's notes, adding a missing `Retrieved:` date, adding
  the index row: these move nothing and lose nothing.
- **A passage that is project content** — do not delete it. The fix is to move it where it
  belongs, and the auditor names where; if that document does not exist yet, creating it is
  a change the user has not asked for. Name the finding, name the destination, and leave it.
- **An unattributed assertion** — do not repair it from memory, which is the failure being
  reported. Either quote what the source actually says, which means fetching it, or mark it
  as the derivation it is. Both are decisions, not fixes; say so.

A clean audit is one line.

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

It **changes nothing** — it writes nothing at all. Its findings are the kind you must not
apply on autopilot: deleting a section usually means
moving its content into a deeper doc that does not exist yet, and creating that document is
a change the user has not asked for. So relay what it found and what it proposes, and make
the deletions and pointer fixes you can make without inventing a new document. Where a
finding needs a file created, say so and leave it to the user.

## Presenting the result

The file-reading correctors have already edited what they were given. What is left is yours,
in this order:

1. **Apply the auditors' findings to the answer file.** An unsupported claim, a deferral the
   repo could have answered — fix it where it is written, in the English answer file, with
   `Edit`. A finding you are leaving unfixed stays unfixed on purpose and is named in your
   reply.
2. **Translate.** If you are answering the user in a language other than English, write the
   translation to a **new file**: the answer file's path with `.md` replaced by `.<lang>.md`
   (`.ko.md` for Korean). Translate the corrected text — everything, at full length, not a
   summary. The English file stays as it is; it is what a later audit of this turn reads,
   and overwriting it would leave that path with the weaker version. Skip this step entirely
   when you are answering in English; there is nothing to translate and no second file.
3. **Check the translation.** If `korean-corrector` was among the agents you were named,
   dispatch it now — alone, on the translation file, per its section. It edits in place.
   Relay what it left unfixed.
4. **Reply short.** What changed and why, in a line or two per finding, then the path. A
   clean audit is one line. Do not restate the answer and do not paste the file.
5. **Open the file, but only if an agent has read it** (see below):
   `open <path>` on macOS, `xdg-open <path>` on Linux, `start <path>` on Windows. Once, at
   the end, after every correction has landed — opening it mid-audit shows the user text
   that is still being fixed.

The path in step 4 is the one the **user** reads: the translation when you made one, the
answer file when you did not. Name it in the reply either way.

**Open only a file that was actually audited.** Opening is not "here is where it is" — the
user has the path from your reply. It is you putting a document in front of them, and doing
that with text nothing checked presents an unchecked draft as a finished one. So:

- You wrote a translation and `korean-corrector` ran on it → open the translation.
- You wrote a translation and `korean-corrector` did **not** run → open nothing, and name the
  path. Say the translation is unchecked only when the reader would otherwise assume it was:
  after an audit that did run and that you are reporting. On a turn where the router cleared
  everything you are already saying nothing about auditing — do not start now.
- You are answering in English, so there is no translation, and at least one agent audited the
  answer file → open the answer file. Here it is both the audited document and the one the
  user reads, so nothing is being substituted.
- No agent read anything this turn → open nothing.

The one substitution to avoid: when the user reads another language and the translation went
unchecked, do not open the English file in its place. It was checked, but it is not what this
user reads, so handing it over answers a different question than they asked. That is about
standing in for a translation — it says nothing against opening the answer file for a reader
whose language it already is.

And do not open a file you wrote during the audit, or start a new one for this report: an
audit summary is worth a line in the reply, not a document, and opening it hands the user a
memo about the answer instead of the answer.

**When the dispatch named no answer file**, steps 1 through 3 and step 5 do not apply — there
is nothing to correct, nothing to translate and nothing to open. That is the file-reading agents dispatched on their own:
`comment-corrector`, `agents-md-auditor` and `ext-docs-auditor` work on the files the turn wrote,
and a turn with no turn-reading agent eligible never wrote an answer file in the first place.
Reply per step 4, naming the files that changed and the findings you did not apply; the user
reads those in the diff, not in an opened document.
