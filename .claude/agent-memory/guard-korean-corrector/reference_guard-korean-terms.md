---
name: guard-korean-terms
description: Terms and register conventions in this repo's Korean guard answers — what looks like 번역체 but is house style and must be left alone
metadata:
  type: reference
---

Terms this project leaves alone in Korean prose (never "translate" or flag them):

- English-as-is: `guard`, `PreToolUse`, `UserPromptSubmit`, `SessionStart`, `Stop`,
  `payload`, `agent_type`, `deny`, `fetch`, `pod`, plugin/agent names such as
  `guard:ext-docs-fetcher`, `guard:refs-finder`, and file paths like
  `wiki/ref/...`, `cmd_write_guard.py`.
- Settled loanwords: 훅, 라우터, 서브에이전트, 프롬프트, 커밋, 리마인더, 컨텍스트,
  버킷, 스냅샷, 플러그인.
- Verb idioms that are normal dev Korean here, not 의인화: "훅이 돈다 / 라우터가
  Stop에서 돕니다", "훅이 뜬다", "줄을 낸다" (emit a line of injected context).

Register by genre in this repo:

- guard turn answers (`.claude/guard/turns/**.md`) are 대화 응답 → 존댓말 throughout.
- Quoted directive strings inside them ("직접 fetch하지 마라", "…라우터를 띄워라")
  are quoted instruction text, not 반말. Never flag.
- Issue bodies / commit messages / doc drafts quoted inside an answer stay `~다` 평서형.
- Some guard answers are written end-to-end as a record/note (`## 기록`, `## 미커밋`
  headings, tables) in uniform `~다` 평서형. Treat that as 문서 본문 and do NOT convert it
  to 존댓말 — a whole-file register flip is a diff that buries the real findings. Flag
  register only on a genuine `~다` / `-습니다` mix inside one part.

Bold usage: guard answers use `**…**` sparingly as list labels (e.g. `**fail open.**`).
Around five in a document-length answer is house style, not 볼드 남발.
