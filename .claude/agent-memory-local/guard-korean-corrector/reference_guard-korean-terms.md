---
name: guard-korean-terms
description: Terms guard's Korean turn answers leave in English/loanword form, and the register each genre uses — do not flag these as 번역체
metadata:
  type: reference
---

Guard turn answers (`.claude/guard/turns/<session>/<turn>.md`) are Korean 대화 응답 in
존댓말 (`-습니다`), with agent/setting names and paths left as identifiers.

**Never flag as 번역체 or translate:**

- agent names: `refs-finder`, `claims-auditor`, `deferrals-auditor`, `clarity-auditor`,
  `korean-corrector`, `comment-corrector`, `router`
- setting values and keys: `off` / `fresh` / `reuse`, `router_model`, `refs_dir`
- paths and commands: `wiki/ref/`, `agents/router.md`, `/guard:settings ...`
- project jargon used bare in Korean: 턴, 스위치, 에이전트, 인스턴스, 라우팅, 커밋,
  fetch (also seen as `재-fetch`)

**Register by genre in these files:** the response body is 존댓말; any quoted issue
body / commit message / KB page fenced inside stays `~다` 평서형. Do not unify them.
Markdown **table cells** and short **bullet-list items** (label — `고침` / 명사형 gloss)
in these answers are terse note style (`~다` / 명사형) and stay that way even when the
surrounding body is 존댓말 — only the running prose is converted.

**Bold is used functionally** in these answers — the changed table cell and the one
contrast a paragraph exists to make. Two or three `**…**` in a turn file is normal here,
not 볼드 남발. In longer recommendation answers, the bolded verdict opener
(`**합치지 않는 쪽을 권합니다.**`) and bolded numbered-list labels are also functional;
count them but do not flag on count alone — up to roughly seven of this kind has been
left in place. In long design-note answers (multi-section, numbered audit-criteria lists),
the bolded item labels act as sub-headings: a total near sixteen was counted and all kept,
since only ~5 were inline emphasis. Judge the inline-emphasis count, not the total.
