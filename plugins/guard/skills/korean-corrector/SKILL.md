---
name: korean-corrector
description: 'On demand, audit the last completed turn''s Korean for whether it reads as something a Korean developer would write, and get the corrected text — guard dispatches the korean-corrector subagent, which counts findings on four axes: tangled sentences (복합문), 번역체, AI literary reflexes (비유·대구·볼드 남발), and register wrong for the genre, then rewrites the response to repair them. A non-Korean response is never flagged. Claude Code only.'
argument-hint: ''
disable-model-invocation: true
---

This command is handled by a guard hook, which targets the last completed turn and
emits the dispatch inputs for the `korean-corrector` subagent, including the path it
should write the corrected text to.

**Follow that dispatch instruction:** dispatch `guard:korean-corrector` with the Agent
tool exactly as the reminder specifies, then act on its verdict. On a pass, state that
the turn passed and stop. On violations, read the rewrite file it names and use that text
as the corrected wording — it repaired the findings in a fresh context, so do not
re-translate or re-style it yourself. Relay the four counts and the phrase-level list so
the user can check the rewrite rather than trust it, and call out anything the corrector
listed as unfixed: those are yours to resolve.

The corrector walks the text once per axis and reports a count for each, so a pass shows
all four were checked rather than only the easy one:

- **복합문** — sentences with too many clauses to read in one pass. Korean puts the
  predicate last, so stacked clauses strand the subject far from its verb. The most
  common failure, and invisible to a translationese check.
- **번역체** — translated-English word order, `~에 대한` noun stacks, literal calques,
  redundant `해당`/`상기`, mismatched particles.
- **AI 문체** — the literary reflexes that betray a model rather than a translation:
  metaphors, 대구 구문, 격언조, bold on every paragraph, a bolded sentence restating the
  point just made. None of it is a calque, so it survives a 번역체-only check.
- **register** — 존댓말 for the assistant talking to the user; `~다` 평서형 for a
  document body such as an issue, commit message, or design doc. One response often
  holds both, and each part is judged against its own genre.

For the other checks, run `/guard:claims-auditor` and `/guard:deferrals-auditor`.

Identifiers, paths, commands and established loanwords are left as they are, in the
rewrite as much as in the findings — the corrector never translates a technical term, and
never flags a `~다` document body as 반말. The rewrite keeps the response's structure and
claims untouched; it repairs how the text reads, never what it says.

If the reminder instead says there is nothing to audit (no completed turn yet), relay
that in one line and take no further action.

Do not read guard's state files or investigate how the pending turn is tracked — the
hook has already selected the turn. Your only job is to dispatch the corrector when the
reminder asks for it, and then to read the one rewrite file it names.
