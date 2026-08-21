# guard dispatch playbook

How to run each of guard's audit agents and what to do with what it reports. You are sent
here by section name: guard's Stop hook names the router's section, the router names the
sections for the agents it picked, and a `/guard:*` command names one section directly.

**Read only the sections you were named, and do exactly what they say.** Everything each
agent needs that is specific to this turn — the turn record, the files, the rewrite path —
comes with the dispatch that sent you here, never from this file.

You never gather anything: the record is guard's, and the session's history is the
transcript, which the agents that need it read for themselves. See "The turn record, and
the session's history".

This file exists so that text is stored once and read only when a turn actually gets
routed. Guard's hook output is paid for in your context on every turn, so it carries only
what changes per turn: the paths, which agents are switched on, and what mode each is in.

## The turn record, and the session's history

Two different things, and you produce neither.

The **turn record** is written by guard and holds one thing: the response being audited,
verbatim. Do not edit it, do not append to it, and do not write a replacement — it is the
text under audit, and a copy that passed through the author of that text is worth nothing
to an auditor.

The **session's history** — what the user asked, what this turn ran, what an earlier turn
established — is in the transcript, and an agent that needs it extracts what it needs
itself. When the dispatch that sent you here included a transcript path, a turn id and an
extraction command, pass all three straight through to any agent whose section says it may
need history. **Do not run the extraction yourself and do not summarize the session for the
agent.** Gathering it here would put the largest cost of an audit in the context the user is
talking to, before anything is known to need it.

**Fallback.** An agent can fail to get an extract — no transcript path was passed, the file
is gone, the turn id is not in it, a compaction dropped the range. It is then allowed to
`SendMessage` you and ask, and answering is the right thing to do. Two limits on your
answer, and they are the reason this is a fallback rather than the normal path:

- Give it the **raw text** — the command and its output as they were, the request as it was
  worded. Not your account of what happened, and not your reasoning about why the response
  was right.
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
found. A pick that plainly misread the turn is worth saying so about rather than working
around.

## `claims-auditor`

Audits the turn for claims asserted without adequate evidence.

Inputs: the turn record, plus the transcript path, this turn's id and the extraction
command — it may need history, since a claim is often grounded by a command run several
turns ago and an auditor that cannot reach it reports a backed claim as unbacked.

It changes nothing you need to review — it may update its own project memory, and
nothing else. If it reports violations, address them; otherwise continue.

## `deferrals-auditor`

Audits the turn for work punted as TBD / 확인 필요 that the repository could have answered.

Inputs: the turn record, plus the transcript path, this turn's id and the extraction
command — it may need history, since the user's request is what separates a deferral the
assistant owed from a decision it correctly handed back.

It changes nothing you need to review — it may update its own project memory, and
nothing else. If it reports violations, address them; otherwise continue.

## `korean-corrector`

Audits the turn for Korean prose that reads as translated English rather than written.

Inputs: the turn record and the rewrite path, the latter passed as
`rewrite path (write the corrected text here): <path>`. No history: Korean prose is judged
as prose, so do not pass it the transcript.

On violations it writes the corrected response to that path and names it in its report:
read the file and use its text as the corrected wording, keeping any phrase it listed as
unfixed for yourself to resolve. On a pass it writes nothing and there is nothing to do.

## `comment-corrector`

Audits the source files it is given for comments that are false, that only restate the
code, or that are missing where the intent is not obvious.

Inputs: the absolute file paths you were given, and only those — pass them through
unchanged. Adding a file means editing something this turn never touched. It reads neither
the turn record nor the transcript.

It **edits the comments in place**, so its changes are already in the files when it
reports. Relay what it changed AND what it left unfixed — an unfixed finding needs the
user — and do not re-edit its work.

## `router`

Triages the finished turn and names which of the switched-on agents are worth running.

Inputs: the turn record, the candidate agents with their modes, the files this turn wrote
(when `comment-corrector` is a candidate), and the rewrite path (when `korean-corrector`
is). No transcript: it triages from the response, which is the whole of the record. Always a
**fresh** instance, whatever the agents are set to.

It answers with one line per pick — the agent's key and why — or `none`.

- **`none`, or nothing named** — a normal and frequent result: the turn had nothing for
  any of them. Say nothing about auditing and continue.
- **one or more keys** — read those sections above and dispatch exactly those agents, in
  the order it listed them, passing each the inputs its section names. A key that was not
  in the candidates you gave it is not dispatchable: the user
  has that agent switched off, so ignore it and say so in one line.
