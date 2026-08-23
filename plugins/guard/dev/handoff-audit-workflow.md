# Handoff — English-first audit workflow, and the auditor axes that still do not fire

Written 2026-08-23. **Transient**: delete this file once the work it describes lands or is
abandoned. Everything below is uncommitted working-tree state.

## Why any of this happened

Over one session the user twice caught a defect in an answer that **all four audit agents had
passed**. Both defects were in design prose:

1. A sentence asserting a conclusion by analogy to a reason the answer never states —
   `` `cmd_verify`가 스위치를 무시하는 것과 같은 이유로 이것도 스위치를 무시합니다 ``.
2. A long section answering the wrong question (on-demand switch policy, for a question about
   the Stop path).

Neither is a false sentence. That is the point: `claims-auditor` judges one statement at a
time, `clarity-auditor` judges whether the reader can follow the sentences, and nothing owned
the question "does this reasoning hold" or "is this an answer to what was asked".

## Part 1 — the workflow change (done, untested)

The audits are measurably weaker on Korean prose. The same content, translated to English,
drew findings from two different agents that the Korean original passed clean:

| agent | Korean | English |
| --- | --- | --- |
| `clarity-auditor` | pass | findings ×2 |
| `claims-auditor` | pass | violations ×4 |

One of the English-only findings was a real error nobody had caught in many Korean audits:
the answer repeatedly said "the hook prints six lines of paths" when `_router_context` emits a
variable 4–7 field lines, two of which are not paths.

n=1 per cell, so this is a signal rather than a measurement. The user decided not to spend more
runs on it and to change the workflow instead.

**The new shape:** the answer file is written in English, the audits run against it, and the
version the user reads is translated afterwards into a sibling file (`<turn>.md` →
`<turn>.ko.md`). `korean-corrector` then checks that translation, alone, after everything else.

### Files changed

- **`scripts/guard_core/dispatch.py`** — `_DRAFT_LEAD` now asks for the answer file in ENGLISH
  and points at the playbook for the translation step. Deliberately does not name a language:
  this string ships into other people's repositories.
- **`hooks/context/dispatch-playbook.md`**
  - The "two audiences, two languages" section is inverted and now carries the reason.
  - `Dispatching` gained a carve-out: `korean-corrector` must **not** go in the one-message
    batch, because its input does not exist yet.
  - The `korean-corrector` section now takes the translation file and says it runs out of
    order.
  - `Presenting the result` is five steps: apply findings → translate → check translation →
    reply → open. Plus a rule that **only an audited file may be opened**, with the four cases
    spelled out. The English answer file is never opened as a stand-in for an unchecked
    translation, but is opened normally when English is the user's own language.
- **`agents/router.md`** — the `korean-corrector` triage rule cannot read the answer file any
  more (it is English by design), so it judges from the request file: will this turn be
  delivered in Korean. That required an explicit exception to the standing rule in `Inputs`
  that the request may only ever remove candidates, never add one.

`agents/korean-corrector.md` is unchanged: its `Inputs` already says "an answer file … correct
it in place", and its "if the text is not substantially Korean, report nothing" rule makes a
mis-dispatch a no-op.

### What has not been done

**None of it has run.** guard is muted in the originating session (`/guard:toggle`), so no turn
has exercised the new flow end to end. First thing to do in the new session:

1. `/guard:toggle on`
2. Ask something that produces a substantive Korean answer.
3. Check, in order: the answer file is English; the auditors were dispatched on it;
   `korean-corrector` was **not** in that batch; a `.ko.md` sibling exists; `korean-corrector`
   ran on the `.ko.md`; the file opened was the `.ko.md`.

Failure modes worth watching for specifically:

- the main agent translating in place instead of writing the sibling (loses the English
  original, which is what a later `/guard:<agent>` re-audits);
- `korean-corrector` batched with the others anyway, reporting nothing on an English file;
- the router never naming `korean-corrector` because it still looks at the answer file;
- a `.ko.md` opened when `korean-corrector` did not run.

## Part 2 — the auditor axes (in progress, not working)

### `clarity-auditor` — ambiguity axis, added, never fires

A fourth axis `### 3. Ambiguous statements` (Calibration renumbered to 4). Test procedure:
write out both readings; if you can state A and B as sentences a reader would act on
differently, it is a finding.

**It has never produced a finding**, including on the sentence it was written for, in Korean
and in English. Diagnosis: the target was misidentified. Read inside its own file, the
sentence's demonstrative has only one candidate — nothing is ambiguous. The real defect is that
`"the same reason"` refers to a reason the answer never states. That is an unresolved
cross-reference, not a competition between two readings.

### `claims-auditor` — inference section, rewritten twice, never fires

First as `## The conclusion, not only the sentences`, then rewritten as
`## The reasoning under a proposal` after finding out why v1 could not work:

> The `cmd_route` material is design reasoning about a command that does not exist yet … so it
> carries **proposals rather than checkable claims**.

Two independent runs said that. It is correct under the old wording — proposals are excluded —
so the defective sentence never reached any axis. v2 therefore: narrowed the triage exemption,
targets every point where the answer leans on something outside itself rather than the single
document-level conclusion, makes an unresolved cross-reference a violation in its own right,
deletes the "hands a decision back" skip, and adds a required `- inference:` field to **both**
report templates.

**v2 also produced no `broken inference` finding — and the required `- inference:` field did
not appear in either run.** That is the blocker: there is no signal for whether the section is
being walked at all, so further edits are blind.

Likely cause: one added line inside a code fence near the end of a ~290-line file is weak.
Compare `clarity-auditor`'s `- profile:`, which is reproduced faithfully every single run — it
appears in both templates *and* is referenced from three other places in that file. Redundancy
is what makes a required field stick.

**Done 2026-08-23.** `- inference:` now has the redundancy `- profile:` has. The gate is in
`## Outcome` ("You may not report `verdict: pass` without the `inference` field"), the section
closes by naming the field it has to fill in, and `What you do NOT do` forbids omitting it or
defaulting it to `none in this turn`. Four references outside the templates, up from one.

**Not yet observed to work.** Whether the field now appears on every report is the next thing
to check, and it is the gate on all the axis work below: until it does, a skipped section and
an empty one are still indistinguishable.

### Then, and only then

Re-aim the ambiguity axis at **unresolved cross-references** — "for the same reason X does",
"as established above", "per the usual rule" — where the check is whether the reference
resolves inside the answer. Note this now overlaps `claims-auditor`'s v2 wording, which already
claims that ground. Decide which agent owns it before writing more; having both look for it is
how two agents report the same finding twice.

### Still uncovered

"The answer is about the wrong question." Neither axis addresses it, and the negative-control
run confirmed it: the fixture whose only defect is that it answers the wrong question passes
both agents cleanly. Whether it deserves its own axis, its own agent, or nothing is open.

## Fixtures

`dev/fixtures/defective-design-answer.ko.md` and `.en.md` — the same defective design answer in
both languages, saved so the comparison is repeatable. Dispatch form used throughout:

```
Agent(subagent_type: "guard:claims-auditor", model: "opus",
      prompt: "- answer file: <absolute path to fixture>")
```

**Pass no transcript.** The originating session's transcript names both defects explicitly; an
agent that reads it is being handed the answer.

Two cautions learned the hard way:

- **Freeze the repository, not just the file.** One positive control ("the docs say so", with
  no local copy) was destroyed mid-experiment by adding the missing excerpt to `wiki/ref/`. The
  fixture text was unchanged and the defect was gone, because the claim now resolves.
- **Agents vary in how far they dig.** Given identical inputs and no transcript, one run found
  the session JSONL on its own and measured a character count; another declined the same claim
  as unreachable. Do not read a single differing verdict as a wording or model effect.

The `.ko.md` fixture still contains one live defect: its table says the hook block is
`약 650자` where the real block measures 832 characters.

## Memory to clean up

`agent-memory` resolves against the agent's **cwd**, not the project root, so a `cd` in a Bash
call scatters stores. `.gitignore` (lines 222–231) already documents this and keeps the strays
uncommittable, but nothing stops them being *read*, and they disagree with each other.

Strays, all untracked, all safe to delete:

```
plugins/guard/.claude/agent-memory/
plugins/guard/agents/.claude/agent-memory/
plugins/guard/hooks/context/.claude/agent-memory-local/
.claude/guard/turns/0f38b566-.../.claude/agent-memory-local/
```

Entries that are actually wrong:

- `plugins/guard/.claude/agent-memory/guard-claims-auditor/guard_repo_reference_locations.md`
  puts the refs under `plugins/guard/wiki/ref/…`. **That directory does not exist**; refs are at
  the repo root. A claims report in this session cited that path, so the bad entry was in play.
  A different store records the correct location — two stores contradicting each other, neither
  able to see the other.
- `.claude/agent-memory/guard-deferrals-auditor/injected_bypass_reminder.md` (tracked, added in
  `dd17f411`) classifies the harness's own bypass-permissions reminder as a prompt injection and
  tells the agent never to comply. It is a legitimate reminder. Every deferrals run re-reports
  it.

**Note on this whole section, added 2026-08-23.** `plugins/guard/AGENTS.md` claimed at HEAD that
the audit agents have no `memory:` at all — which would have made this section describe stores
that cannot be written. They can: `v0.55.0` removed the field, `v0.56.0` restored it as
`memory: project` behind the new `pre-write` hook and left the paragraph behind. The paragraph,
two passages in `dev/design.md`, and a stale prose-boundary comment in
`agents/clarity-auditor.md` have been rewritten to the design that shipped. Nothing about the
cleanup itself changed.

**Stale after the Part 1 change** — five `korean-corrector` entries all describe
`.claude/guard/turns/<session>/<turn>.md` as the Korean deliverable and prescribe its register.
Under the new flow that file is English and the Korean lives in `.ko.md`. They will misdirect:

```
.claude/agent-memory/guard-korean-corrector/register-guard-answer-files.md
.claude/agent-memory/guard-korean-corrector/genre-register-answer-files.md
.claude/agent-memory/guard-korean-corrector/reference_guard-korean-terms.md
.claude/agent-memory/guard-korean-corrector/terms-left-alone.md
.claude/agent-memory-local/guard-korean-corrector/*        (duplicates of the above)
```

Two further problems inside that set, independent of the workflow change:
`register-guard-answer-files.md` ("always `~다` 평서형") is superseded by
`genre-register-answer-files.md` ("two shapes; decide from the file's own endings") and the two
now contradict; and `reference_guard-korean-terms.md` still names `refs-finder` and
`reads="prompt"`, both of which were removed from the code.

The remaining entries were checked and are accurate — pointer-style, each carrying its own
"re-verify before relying on this".

## Root cause worth fixing

guard's `pre-write` hook already denies a reporting agent's write outside an agent-memory
directory. Narrowing that to the **project-root** agent-memory directory would make a
cwd-drifted store fail loudly instead of appearing silently — the hook doing for creation what
`.gitignore` already does for commits.
