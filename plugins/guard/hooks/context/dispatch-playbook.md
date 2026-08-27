# guard turn closeout

What to do with what guard's agents report, and how the turn is closed out afterwards. **How
to dispatch them is not here** — it comes with the dispatch itself: the router's report says
it for the agents it picked, and guard's Stop hook says it for the ones it names directly.
Nothing sends you here to find out how to call something.

So there is a section only where the caller has a judgment to make that no report can carry
for it. The routed audits have none — you apply what they report to the answer file, and the
router's report says so — which is why they have no section here. `ext-docs-fetcher` has none
for the same reason on the other path: nothing dispatches it on guard's behalf, and what to
do with what it reports is in its report.

**Read only the sections you were named, plus `Presenting the result`, which closes every
routed turn.** Everything specific to this turn — the answer file, the source files, the
transcript pointer — comes with the dispatch that sent you here, never from this file.

You never gather the session's history — the agents that need it read the transcript for
themselves. See "The answer file, and the session's history".

**English until the audits are done; the user's language last.** The answer file is written
in **English**, and so is everything around it — what you write in a dispatch, what the
agents report back, what you say to an agent, what one agent says to another. The audits run
against that English file.

**You do not write the user's language yourself.** Every word of Korean the user reads comes
from `korean-translator` and is then checked by `korean-corrector`. Neither has a switch, so
the user cannot turn them off — but that is not the same as running on every turn. Whether
this turn has substance being delivered to a reader is the router's call, and when it names
neither of them there is no translation at all: you do not write one in their place. The one
exception is the short line you type in the terminal beside the path — a pointer, not the
deliverable — and it stays short for that reason.

Only after the audits have run and their findings are applied is the version the user reads
produced, in their language, as a **separate file**: the answer file's path with `.md`
replaced by `.<lang>.md` (`.ko.md` for Korean). That translation is the last step of the
turn, and `Presenting the result` says how. Your reply to the user is in their language too.

Why this order rather than the obvious one: the auditors are measurably weaker on non-English
prose. The same answer, translated, drew findings that its original passed clean — twice, from
two different agents. Auditing the English and translating after is how the user's language
stops costing them the audit. The translation is then written by `korean-translator` and
checked in its own right by `korean-corrector`, which is why those two run after the others
rather than beside them: neither has an input until the English is corrected.

Never relay an agent's English report to the user untranslated. What changed goes in the
answer file, which is translated; the line you type beside the path says it in one sentence.

This file exists so that text is stored once and read only when a turn actually gets
routed. Guard's hook output is paid for in your context on every turn, so it carries as
little as it can: on a routed turn, the turn id alone. The paths that go with it — this
file, the answer file, the transcript — come from `guard-inputs <turn id>`, run by whoever
opens them rather than relayed through you. The router's report names them for you.

## The answer file, and the session's history

The **answer file** is where this turn's substance lives. You wrote it during the turn; the
reply you gave the user was short and named this path. It is not a copy of something already
delivered — it is the deliverable, which is why the agents can still fix it.

Two rules. Do not paste its contents into a reply: printing the text is what this shape
exists to avoid, and printing it twice (before and after correction) is the waste that
motivated the whole arrangement. **Summarising it is the same failure in a shorter form** —
a bulleted digest of the file, or a preview of how it opens, puts the unaudited answer in
front of the user just as effectively as quoting it, and it passes for brevity while doing
so. And if you find the file empty or missing, guard filled it in from the response after
the fact and said so in a comment at the top; treat it as the answer anyway, and write it
properly next time.

The **session's history** — what the user asked, what this turn ran, what an earlier turn
established — is in the transcript, and an agent that needs it extracts what it needs
itself. Pass the turn id straight through to any agent whose section says it may need
history, and let it run `guard-inputs <turn id>` for the transcript path the same way you
would. **Do not run the extraction yourself and do not summarize the session for the
agent.** Gathering it here would put the largest cost of an audit in the context the user is
talking to, before anything is known to need it.

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

## Common to every dispatch

Whoever sent you named what each agent gets. Pass **only that**, unchanged. An audit learns
what to look for from being that audit, not from a scope argument, so do not add instructions
of your own about what to look for, and do not tell it what you think of the turn. It forms
its own view; an argument from the turn's author is the one thing that can bias all of them at
once.

Type no `/guard:*` slash command to do any of this. Those are the user's own entry point —
`/guard:settings`, `/guard:reader-profile` — and they are a different surface from the
`guard:audit-*` skills, which you invoke as skills and the user never types.

Every one is a **new instance**. The mode you are given is always `= fresh`; there is no other
value, and no instance from an earlier turn to look for or resume. Each judges this turn on its
own, which is the shape every definition here is written for.

When you report back, relay the router's reason for each pick alongside what it
found. **A clean result is one line** — every agent passing is the common case, and a
paragraph celebrating it trains the user to skip the report that matters. A pick that
plainly misread the turn is worth saying so about rather than working around.

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
   reply. `audit-turn-clarity`'s findings are the one kind that ask you to **add** rather than
   correct — a definition, an example, a paragraph cut — and they go in the same way. If its
   report says the reader profile is MISSING, relay that in one line: the user establishes one
   with `/guard:reader-profile`, and until they do, the axis its own report names as skipped
   stays skipped. Say it once; repeating it every turn is how a useful notice becomes noise.
2. **Have it translated. You do not write the translation.** The corrected text goes to a
   **new file**: the answer file's path with `.md` replaced by `.<lang>.md` (`.ko.md` for
   Korean). **Dispatch `korean-translator` now** — alone, and with exactly two inputs: the
   answer file, which is its source, and that translation path, which is where it writes. No
   history and no repository paths; it translates prose and checks nothing the answer asserts.
   Hand it the two paths and let it write the file — a draft of your own in front of it anchors
   it to the wording it was brought in to avoid, which is what produces 직역. It reports when the
   file exists; relay any sentence it listed as translated-but-unsure, and answer it if it
   `SendMessage`s you mid-run, because that is a question about what the English meant.

   The English file stays as it is: it is what a later audit of this turn reads, and
   overwriting it would leave that path with the weaker version.

   **Skip this step entirely when the router did not name `korean-translator`** — including
   every turn you are answering in English, where it never appears. That is the router saying
   this turn has nothing worth translating, and the answer to it is no translation, not a
   translation you write instead.
3. **Check the translation.** Only when step 2 made one. Dispatch `korean-corrector` now —
   alone, and on the **translation file** only: no history, since Korean prose is judged as
   prose, and not the answer file, which is the English original and not what the user reads.
   It edits in place, so its corrections are already applied when it reports; relay any phrase
   it listed as unfixed. The translator's own report ends by telling you to dispatch it, and
   that instruction stands whether or not the router named the agent: the two are one step, so
   a translation that exists is always checked. With no translation there is nothing for it to
   read.
4. **Reply short.** What changed and why, in a line or two per finding, then the path. A
   clean audit is one line. Do not restate the answer and do not paste the file. This reply
   reports on the answer; it never stands in for it. The user reads the document — so a
   reply that would let them skip opening it has replaced the thing it was reporting on,
   and has done it with text no agent audited.
5. **Open the file, but only if an agent has read it** (see below):
   `open <path>` on macOS, `xdg-open <path>` on Linux, `start <path>` on Windows. Once, at
   the end, after every correction has landed — opening it mid-audit shows the user text
   that is still being fixed.

The path in step 4 is the one the **user** reads: the translation when you made one, the
answer file when you did not. Name it in the reply either way.

**Open only a file that was actually audited.** Opening is not "here is where it is" — the
user has the path from your reply. It is you putting a document in front of them, and doing
that with text nothing checked presents an unchecked draft as a finished one. So:

- A translation exists and `korean-corrector` ran on it → open the translation. This is the
  normal case on a turn that got one: step 3 always follows step 2.
- A translation exists and `korean-corrector` did **not** run → open nothing, and name the
  path. `korean-translator` having written it does not substitute: it is the author of that
  file, and nothing has read it. Say the translation is unchecked, and say why the corrector
  did not run — with no switch to be off, the only reasons left are ones the user should hear. Say the translation is unchecked only when the reader would otherwise assume it was:
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

**When the router picked nothing**, steps 1 through 3 and step 5 do not apply either. `none`
means no agent had material here — the Korean pair included, since the router judges them on
the same materiality bar as everything else. So there are no findings to apply, no translation
to make, and nothing audited to open: reply per step 4, in the user's language, naming the
answer file. Say nothing about auditing; a turn that drew no agent is not news.

**When the dispatch named no answer file**, steps 1 through 3 and step 5 do not apply — there
is nothing to correct, nothing to translate and nothing to open. That is the file-reading agents dispatched on their own:
`comment-corrector`, `agents-md-auditor` and `ext-docs-auditor` work on the files the turn wrote,
and a turn with no turn-reading agent eligible never wrote an answer file in the first place.
Reply per step 4, naming the files that changed and the findings you did not apply; the user
reads those in the diff, not in an opened document.
