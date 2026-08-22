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

**Bold is used functionally** in these answers — the changed table cell and the one
contrast a paragraph exists to make. Two or three `**…**` in a turn file is normal here,
not 볼드 남발.
