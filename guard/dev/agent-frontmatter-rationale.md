# Why each agent's frontmatter is the way it is

Contributor notes for the people editing `guard/agents/*.md`. Not runtime context —
the agents never read this file.

This used to live as YAML comments inside each agent's frontmatter. It was moved here because
the same eight sentences were repeated across eight files, and because frontmatter is the
wrong place for an argument: a reader editing `tools:` sees the list, not the reasoning, and a
comment above a key drifts from the key below it without anything failing.

The underlying measurements are in `dev/design.md`. This file records the per-agent *choice*
and points there for the *mechanism*; where the two disagree, design.md is the one with the
run behind it.

## What is true of every agent here

**`memory:` silently grants Write and Edit, and the host does not scope that grant.** This is
measured, not inferred from the field's documented purpose: an agent declaring `tools: ["Read"]`
with a `memory:` scope reported Write and Edit present and wrote successfully to an absolute
path outside both the project and its own memory directory. The symmetric run without the field
had `Read` alone and no Write tool to call. See design.md § "A stored verdict is invisible when
it is wrong" for the run, the dates, and the CLI version.

Three consequences that bear on every edit to these files:

- **Omitting `memory:` is how "reports; edits nothing" becomes a fact about the tool list**
  rather than a promise in prose. For every agent below that has no `memory:` line, that is
  part of why — it is not only about what would be stored.
- **For the agents that do carry `memory:`, the boundary rests entirely on the agent's body.**
  Nothing refuses such a write. Prose telling an agent to stay inside its memory directory was
  tried and broken. A subagent's own `hooks:` frontmatter cannot carry the boundary either —
  the host ignores that field for plugin subagents, as it does `permissionMode` and
  `mcpServers`. A `pre-write` hook enforcing it was built and then removed at the maintainer's
  direction; design.md keeps the facts so nobody rebuilds it by accident.
- **A stored VERDICT is the specific hazard, and it is self-concealing.** `deferrals-auditor`
  once wrote into memory that deferrals needing a live runtime are legitimate, then cited that
  entry back as its reason for passing exactly the deferral it exists to catch. Deleting the
  entry did not hold; the next run wrote a fresh one. With a store available, matching a stored
  pattern is always cheaper than re-deriving the judgement, and a wrong stored verdict cannot
  be found by looking — it suppresses the finding that would have exposed it. This is why most
  of the auditing agents have no store at all.

**`memory: project` is chosen for reviewability, not for sharing.** It puts the store in
`.claude/agent-memory/<agent>/`, which is tracked, so a wrong entry arrives in a pull request
and is read by someone. Review was always the check on content — no scope prevents a bad entry,
one scope just makes it visible. (The host's recommended default is also `project`.)

**Naming a tool's purpose is not narrowing it.** Several agents below say what `Bash` is *for*.
That is orientation, not a boundary, and the comments were deliberately not written as
restrictions: the host injects a standing instruction to route work through `Bash` wherever it
can do the job, so a rule here confining `Bash` to a purpose list would be contradicted on
every turn. Use it for anything else it does well.

**`model: opus` is argued from the failure mode, except twice.** Only `docs-finder` (under its
former name `ext-docs-fetcher`) and `ext-docs-auditor` were run head-to-head on `sonnet` and `opus` before the field was set;
design.md § "Picking a model for an agent" records what those runs showed and what to re-run
before changing either field. Every other `opus` in this directory is a claim about the job,
not a measurement — and so is the `sonnet` on the Korean pair, which was set by decision rather
than by a run.

**`color` warns about the user's own files; it is not an identity.** Red for report-only,
yellow where the agent can write. See design.md.

## Turn-auditing agents

### `agents-md-auditor`

`tools: Read, Grep, Glob, Bash`

`Read` for the files under audit and for whatever they point at — a pointer is only good if the
thing on the other end exists and answers the question. `Grep`/`Glob` settle the axis that
separates this agent from a style checker: whether a sentence in the file is something the code
already shows, which can only be answered by going and looking at the code. `git log` /
`git ls-files` are worth reaching for — how big the project is and how recently a named path
moved is what tells a map that has drifted from one that was never right.

No `SendMessage`: the whole input is on disk, so there is nothing to ask the author that reading
the repository would not answer better.

`memory: project` for the reviewability. `model: opus`.

Note: this file's `description` value starts with a backtick, which strict YAML rejects as the
start of a plain scalar. The host parses it; a strict parser will not. Left as-is deliberately —
changing it is a change to the shipped value.

### `claims-auditor`

One agent for both dispatch paths, entered through the `audit-turn-claims` and
`audit-report-claims` skills. Hand-written — nothing about it is generated.

`tools: Read, Grep, Glob, Bash, SendMessage`

`SendMessage` is how "ask the main session where to look" actually happens. It is **not** a way
to obtain evidence: an answer from the turn's author is a claim, so use it to be pointed at a
file, then read the file yourself.

The skill narrows it further on the document path, and says so there: the agent may ask which
of two candidate paths a reference means, but must not ask what the document says or how it
came to say it. The main session did not write the document and did not watch it being written,
so its account there is not even the author's testimony.

`memory: project` for the reviewability — and it is what settles the one-agent question, since
the directory is named after the agent and two definitions would learn this repository twice.
`model: opus`.

### `clarity-auditor`

`tools: Read, Grep, Glob, Bash, SendMessage`

guard's `transcript` extractor is the reason `Bash` is present: whether a term was already
explained is a question about earlier turns, and the extractor is the only route to them. The
repository settles whether a name the answer used is a real identifier the reader can go look at
or a term the answer invented. `SendMessage` asks the main session what a passage was meant to
convey — never whether it was clear, which is the question being audited.

`memory: user`, **not `project` like guard's other agents — the only one, deliberately.** What
this agent needs to remember is a *person*: their field, how long they have worked in it, what
vocabulary they own. None of that changes when they switch repositories, and an agent that
relearned it per checkout would start every new project uncalibrated, which is the one state in
which its findings are worse than silence. Project-specific jargon is the exception that stays
out of memory: a term defined in the repository is settled by reading the repository. The
profile is only ever written from what the user said — never inferred from the repository, since
the code someone works in is not evidence of their vocabulary, and a guess written to memory
becomes a calibration fact for months. See design.md on the reader profile and `profile: MISSING`.

`model: opus`.

### `deferrals-auditor`

One agent for all three dispatch paths, entered through the `audit-turn-deferrals`,
`audit-report-deferrals` and `audit-plan-deferrals` skills. Hand-written — nothing about it is
generated.

`tools: Read, Grep, Glob, Bash, SendMessage`

`Bash` carries three things worth naming: guard's `transcript` extractor, checking whether a
named command exists on this machine (asked the way this platform asks it), and reproducing a
deferred behaviour inside a throwaway directory of your own.

**The reproduction allowance replaced a flat ban.** Instances given the ban crossed it anyway —
independently, at more than one model — because a deferral of the form "this needed a live
runtime" is settled far more cheaply by spending a minute proving the component runs headless
than by arguing from the code. They also bounded themselves sensibly while doing it, and said so.
A rule that is reliably broken for good reasons is better replaced than restated, so the line
moved to where the risk actually is.

What stays forbidden is about EFFECT, not about which tool produced it, and none of it is needed
to settle a deferral: writing anywhere but your own temporary directory (never the repository,
never the project's real state), touching the user's account or machine configuration, reaching
the network, and launching interactive sessions of the very agent you are running inside.

Everything that is not command-shaped is still established by READING — an MCP server, a
subagent, a test runner, a staging endpoint are found in the project's config, its docs, and the
turn's own tool activity. And a verdict never requires a reproduction: the code answering the
deferral, or the repository documenting how to exercise it, is enough. The execution is a
shortcut to certainty, not the standard of proof.

`SendMessage` is the fallback when an extract cannot be had, and the way to ask where to look —
never for the finding itself.

`memory: project` for the reviewability. This is the agent whose stored verdict caused the
failure recorded in the shared section above; it additionally carries the asymmetric rule in
prose — never store a remembered `legitimate` — because that specific direction is the one that
reproduces itself.

That store is what the plan path took on when `design-deferrals` was retired into
`audit-plan-deferrals` (v0.123.0), and it is the one thing the swap made worse rather than
better: the retired agent had no store and so could not remember a ruling, while this one can
and is held back only by prose. It was accepted because the prose is the mitigation that was
already carrying the other two paths, and because two definitions of one audit is the failure
this repository has measured — a memory directory is named after the AGENT, so the retired
critic could never learn what this one already knows about the repository it audits. If the
stored-`legitimate` failure ever reappears on the plan path, the fix is the same rule, not a
second agent.

`model: opus`, and here the reason is specific. This agent's whole job is noticing that a
sentence claiming impossibility is actually a sentence about effort, which means holding the
deferral, the code, and the project's testing surface in view at once and disbelieving a
plausible excuse. Weaker models pass the excuse through: they reduce the question to "is the
answer stored in this project?", answer no, and stop. The cost is real — a deferrals audit is now
an opus call — and a project that would rather trade the catch rate for it changes one word in
the file.

### `router`

`tools: Read, Bash`

`Read` for the files it is pointed at. `Bash` for exactly two of guard's own commands:
`guard-inputs`, which turns the turn id or path it is given into those files, and
`guard-candidates`, which tells it which audits it may name. Both are fetched by the router
rather than passed in, so each stays with its only reader.

`Bash` is otherwise not for this agent's use. It routes from what it is given, so it needs no
search and no web access: whatever needs the repository is the job of the audit it names, which
has it. And no `Agent`: a router that could dispatch would be running the very audits it was
asked to merely nominate.

**No `memory:`, deliberately.** Memory would inject this project's accumulated triage habits into
every routing decision, and the one thing routing must not do is decide from a pattern instead of
from this turn — a remembered "this project rarely writes Korean" is exactly how a Korean turn
goes unrouted, silently, at the step nothing else checks. That is also why nothing here is held
open across turns — see design.md on the removal of `reuse`.

`model: opus`, not the cheapest model that fits the method. Every other agent here is paid for by
a decision this one makes, so a router that misreads a subject does not save anything: it either
omits the audit that would have caught the defect, or spends a full subagent for each audit it
named on material that was not there. The second failure is the one that compounds — it is what
teaches the user to wave the recommendation through unread, and then the omissions stop being
caught either. The triage itself is short, so the model is the cheap part of it.

**The mute is honored by `guard-candidates`, not by this agent.** There is no hook in front of
either path to check it — the user asks for the audit — so the switch check lives in the command
the router already runs. Since v0.118.0 that is true of the turn path as well: a turn audit is
invoked rather than recommended, so this command is the only thing standing between `guard off`
and an audit that runs anyway.

#### It was two agents until v0.128.0, and the argument for splitting it was recorded here

`turn-router` and `report-router` were separate definitions, and this file argued for that: the
two share the mechanism and disagree on three judgments, each of which would have to become a
conditional inside a body that was already the longest in this plugin. Three reasons were given.
Two survived and one had gone stale, and the difference is what decided it.

- **No request file.** `turn-router`'s materiality call leans on what the user asked for. A
  document had no user in front of it, so that whole section is inapplicable rather than merely
  empty. **Still true**, and it now lives in `skills/audit-turn/SKILL.md` § 2 — where it is not a
  conditional at all, because the document path's task file simply does not contain it.
- **A declared-open section has to be read as a claim, not as a clearance.** A document that
  carries `Open` or `Could not determine` headings — the interview brief this path was built for
  did — got skipped by the first draft of that router, as the document doing its job. That was
  backwards: the heading asserts that somebody decided to leave these open, and an author is
  perfectly capable of parking a question it never asked under it. **Still true**, and it lives
  in `skills/audit-report/SKILL.md` § 2.
- **`korean-corrector` can never be named on the document path**, because on the turn path the
  caller writes a translation *after* routing. **This had been false since v0.121.0**, when the
  turn path stopped producing a translation at all. By the time the merge was considered, neither
  path could name the corrector, and the retired `turn-router.md` said so outright ("no section
  for the translation"). It had sat here for four minor versions describing an asymmetry that no
  longer existed.

So the premise the split rested on was that the alternative meant conditionals in one body. It
did not: the alternative is the entry split every shared audit here already uses — the agent is
the system prompt and a skill per path is the task, so a judgment that belongs to one path is
absent from the other rather than switched off in it. What the two definitions were actually
carrying was one triage method written twice; `report-router.md` opened by calling itself "the
same triage step as guard's turn router" and then restated it, and the two copies had already
drifted (the materiality paragraph, the empty-answer paragraph and the reason-quality rule were
each worded differently for no reason anyone recorded).

Note which argument is doing the work, because it is not the usual one. The rule in `AGENTS.md`
justifies the entry split by **memory** — one agent, one memory directory. The router has no
memory and must not get one, per the paragraph above, so nothing was consolidated by merging it.
The duplication was enough on its own.

**What this costs.** The two paths' report templates are now in the skills rather than in the
agent, so a change to what the caller does with a routing answer is a change to a task file and
not to the router. That is the right home — what the caller does differs by path — but it means
the router can no longer be read end to end to learn what it emits. Anyone tracing a bad dispatch
instruction starts at `skills/audit-turn/SKILL.md` § 5 or `skills/audit-report/SKILL.md` § 4.

## Correctors

### `comment-corrector`

`tools: Read, Grep, Glob, Bash, Edit, Write, SendMessage`

`Edit` to fix comments in place. `Write` **only** to emit a long report as a file — it can create
files, which `Edit` cannot — never to rewrite a file it was asked to audit.

**No `memory:`.** A corrector with a store starts trusting its own paraphrase of a project's
comment policy instead of re-reading where that policy is written, and a rule it inferred wrongly
then costs a diff on every later turn. What a run learns goes in the report, and the user decides
whether it is worth writing down.

`model: opus`. `color: yellow` — this one edits the user's files.

### The Korean pair — moved out of this plugin

`korean-translator` and `korean-corrector` are no longer guard's definitions. Since v0.125.0
they are user-level agents, shipped from this repository's `global/agents/` and dispatched by
the bare name; `../dev/design.md` § "The Korean pair leaves the plugin" has why, and the
frontmatter reasoning moved with them to `../../global/dev/agent-frontmatter-rationale.md`.

## External-documentation agents

### `ext-docs-auditor`

`tools: Read, Grep, Glob, Bash`

`Read`/`Grep`/`Glob` for the refs directory and for the repository it searches to tell an external
fact from a local one. `Bash` for `refs-dir` and for `git log` on a file whose history says when a
passage arrived.

No `WebFetch`/`WebSearch`: what is auditable is the file's internal honesty, all of which is on
disk, and a page that reads differently today says nothing about whether the excerpt was honest
when taken.

**No `memory:`.** It would store VERDICTS, and matching a stored one is cheaper than re-reading
the file — a wrong stored verdict then suppresses the finding that would expose it.

`model: opus` — one of the two fields set by measurement; see design.md.

### `docs-finder`

`tools: WebSearch, WebFetch, Read, Write, Edit, Grep, Glob, Bash`

`WebSearch` finds the primary source, `WebFetch` reads it, `Bash` covers the five commands the
body names (`refs-dir`, `knowledge-dirs`, `date +%F`, `curl`, the MarkItDown one-liner),
`Write`/`Edit` save the file and its index row, and `Read`/`Grep`/`Glob` do the local search that
comes first.

The read tools now reach the repository as well as the refs directory, and the write tools
still do not: the body carries "write nothing outside the refs directory", which is a promise
rather than a grant the host scopes — the same arrangement as every "reports; edits nothing"
agent here.

No `Agent` and no `SendMessage`: it cannot delegate the reading, and it cannot ask the caller to
narrow a vague question — hence the instruction in the body to report what it took the question to
mean.

`memory: project`, and **this is the exception to the no-stores rule**: nothing here is a VERDICT.
What accumulates is operational — which vendors serve raw markdown, which pages `WebFetch`
summarizes, this project's naming conventions — so a stale entry costs a visible wasted fetch
rather than a suppressed finding.

`model: sonnet`, `effort: medium`. The head-to-head in design.md § "Picking a model for an agent"
argued for `opus`, but on a run that predates the `curl` step now in the body — **re-run it before
treating either tier as settled.** `color: yellow` — this one writes files.

## Plan critics

These are dispatched against a plan the user has approved rather than against a finished turn.
All of them report and none of them writes, which the tool lists make a fact: no `Edit`, no
`Write`, and no `memory:` (which would grant both).

**They were named `design-*` until v0.123.0.** The prefix was read as *visual* design — a
reviewer opening `agents/` could not tell whether `design-fit` judged a layout or an
implementation plan — and every one of them takes a plan file as its subject. `plan-` is also
what the rest of the path is already called: `audit-plan`, `guard-plan`, the plan gate,
`plan_audited_hash`. Renaming an agent is silent at runtime, so the whole set moved at once and
`skills/audit-plan/SKILL.md` moved with it; nothing derives these names from anything else.

The shared reason none of them has a store: what a design critic would remember is a **verdict**
about a design, and the next proposal will resemble the one that was cleared. Matching the stored
verdict is cheaper than working the problem again, and the stored one is what suppresses the
finding. Each entry below adds the agent-specific form of that.

### `plan-adversary`

`tools: Read, Grep, Glob, Bash`. A failure mode is only real if the code admits it: the proposal
says what it intends, the repository says what it will actually do when the input is empty, the
call is concurrent, or the dependency is down.

No `memory:` — it would store verdicts about designs, and a design cleared once is exactly what a
later proposal will resemble.

`model: opus`.

### `plan-alternatives`

`tools: Read, Grep, Glob, Bash`. The strongest alternative is usually already in the repository —
a mechanism that solves the same problem, which the proposal either did not find or did not say
why it passed over. Finding it is a search task.

No `memory:` — a store here would accumulate "this project prefers X", and the whole value of this
agent is asking whether X was actually weighed THIS time.

`model: opus`.

### `plan-coherence`

`tools: Read, Grep, Glob, Bash`. `Read` for the plan, which is most of the work — this agent's
findings come from holding the whole plan in view at once, not from searching. `Grep`/`Glob`/`Bash`
for the times a step's output has to be checked against what the next step consumes, which is a
question about the code.

No `memory:` — coherence is a property of THIS plan; there is nothing about a previous one worth
carrying, and what would carry is a habit of expecting the shape the last plan had.

`model: opus`.

### the deferrals critic, which is no longer an agent

There is no `plan-deferrals`. The sixth seat in stage 2 is the `audit-plan-deferrals` skill, a
`context: fork` entry onto `deferrals-auditor` — the same agent that reads a finished turn and a
standalone document.

What it replaced was `design-deferrals`, and the two asked the same question in almost the same
words: not "does the plan defer something", which is visible in the plan, but "does it defer
something the REPOSITORY already answers". The shared agent asks it better — it carries the
second half the retired one never had, that an answer obtainable by RUNNING the thing was also
within reach — and asks it out of a store of what it has already learned about this repository.
The plan-specific part is small enough to be a skill: what a plan may legitimately leave open,
and the rule that a decision genuinely the user's has to be put to them AT approval rather than
carried past it.

Its `tools:` and `model:` are `deferrals-auditor`'s, not this seat's, which is the cost of the
share and is recorded there along with what the store brings with it.

### `plan-env-prober`

`tools: Bash, Read, Grep, Glob`

**`Bash` is the point of this agent and also its whole risk: it is the only agent guard ships that
runs commands against infrastructure rather than against the repository.** The boundary is
READ-ONLY, it is stated in the body rather than in the tool list, and it cannot be enforced by the
tool list — `Bash` is `Bash`. What keeps it honest is that this agent is small, does one thing, and
is dispatched only by `plan-environment`; a boundary in a general-purpose agent's prose would be
one paragraph among many.

No `Agent`: a prober that could dispatch could route around its own boundary. No
`AskUserQuestion`: it reports what it observed. Interpreting a gap and deciding whether to trouble
the user is the caller's job, and a prober that asks would be asking about a design it was
deliberately not shown.

No `memory:` — it would store observations of a live system, which is the class of fact with the
shortest useful life. A remembered address or replica count read back next week is worse than no
answer, because it looks like an answer. Omitting the field also leaves Write and Edit off, which
matters more here than anywhere: this agent has shell access to infrastructure and nothing it does
should produce a file.

`model: sonnet`, `effort: medium`. `color: yellow` — it acts on things outside the repository.

### `plan-environment`

`tools: Read, Grep, Glob, Bash, Agent, AskUserQuestion`

**`Agent` is the one thing that separates this agent's tool list from the other design critics, and
it is deliberate:** the environment is the one input that is NOT in the repository, so when the
knowledge directories are silent this agent has to send someone to look. It dispatches
`guard:plan-env-prober` and nothing else — see the body's "When the files do not answer".

`AskUserQuestion` is the last resort, and it is a real one: an environment fact that exists only in
the user's head is still the fact the design will be judged by in production, and reporting
`UNKNOWN` where a question would have settled it is how this agent produces a clean report about a
design that cannot be deployed.

No `memory:` — tempting here and wrong: the deployed environment is the input most likely to have
changed since it was written down, and a remembered topology is indistinguishable from a current
one at the moment it is read. Every run re-reads.

`model: opus`.

### `plan-feasibility`

`tools: Read, Grep, Glob, Bash`. These are the whole job: this agent's verdict is a claim about
THIS codebase, so every finding has to come from having gone and looked. `Bash` also runs the
project's own checks where they are cheap and already documented — whether a dependency is actually
present beats reasoning about whether it might be.

No `memory:` — what it would store is this project's shape, which is exactly the thing that changes
between the turn that stored it and the turn that reads it. A remembered "there is no async here"
is how a proposal gets failed for a constraint that was lifted last month. Read the repository
every time.

`model: opus`.

### `plan-fit`

`tools: Read, Grep, Glob, Bash, SendMessage`

`Read` for the plan file and the request. `Grep`/`Glob`/`Bash` because "does this solve the user's
problem" often turns on what the problem actually is — which the repository and the session's
history answer better than the proposal's own framing of it. `Bash` also reaches guard's transcript
extractor, which is how the original ask is recovered when the proposal has drifted several turns
away from it.

No `memory:` — what the user wants is per-request, and a store here would carry one turn's reading
of their intent into the next one, which is the exact error this agent detects.

`model: opus`.

### `plan-premises-lister`

`tools: Read, Grep, Glob, Bash`

`Read` for the plan. `Grep`/`Glob`/`Bash` are for **telling premises apart, never for checking
them**: whether "the loader validates types" is one claim or three depends on what the code
actually looks like, and a lister that cannot look splits and merges premises by guesswork.
Checking is a different agent's job, run three times over.

No `memory:` — a store would carry "this project always X" into the enumeration, and that is
precisely how a premise stops being listed. The ones that go unlisted are never checked by anyone.

`model: opus`.

### `plan-premises-checker`

`tools: Read, Grep, Glob, Bash` **and nothing else**, because a verdict here is worth exactly the
evidence behind it: every CONFIRMED and every FALSE has to come from having opened the file or run
the command.

Three instances of this agent check the same premises independently, which only works if each one
actually looks. **Hence no `SendMessage`:** an instance that could ask another is one that can
inherit a verdict instead of reaching it, and three agents agreeing because they talked is worth
less than one agent that read the code.

No `memory:` — it would store verdicts, and matching a stored verdict is cheaper than checking
again, which is the failure this agent exists to prevent, made permanent.

`model: opus`.

### `plan-premises-recheck`

`tools: Read, Grep, Glob, Bash` for the one thing this agent does: go to the evidence the three
checkers cited and see which of them actually read it right.

**No `SendMessage`, and this is the load-bearing omission.** This agent settles a disagreement
between three checkers WITHOUT talking to any of them: asking would make it a moderator of
opinions, and it is a re-reader of files. The three reports are already in its dispatch; what is
not in the dispatch is the file, and that is the only thing that decides.

No `memory:` — same reason as the checkers, and stronger here: a stored ruling on a contested
premise is the one most likely to be wrong.

`model: opus`.
