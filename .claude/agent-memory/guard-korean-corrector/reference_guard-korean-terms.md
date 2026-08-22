---
name: guard-korean-terms
description: Terms and register conventions to leave alone when auditing Korean guard turn answers in studykit-plugins
metadata:
  type: reference
---

Leave untouched in this project's Korean turn answers:

- Agent / switch / plugin identifiers: `refs-finder`, `ext-docs-fetcher`, `_eligible_agents`,
  `reads="prompt"`, `SessionStart`, `WebFetch`, `Glob`, `guard:*`.
- English status strings quoted from reports: `already saved`, `fetched and saved`, `none`,
  `maybe`.
- Bare English nouns the answers mix into Korean sentences: subject, payload, primary source,
  grep, fetch, refs, pod. These are what the repo says; do not translate.

Register per genre in these answers:

- Assistant commentary → 존댓말 (`-습니다`). Trailing 해요체 tails (`~인데요`, `~이었고요`) show
  up in this user's voice and are still 존댓말 — not a register violation.
- Quoted agent-file text, bullet lists restating a shipped Method, and blockquoted instruction
  text → `~다` 평서형, and stays that way. Rewriting a quotation also misquotes it, so metaphors
  inside quoted shipped text (e.g. `인덱스는 지도지 경계가 아니다`) are left as written.
