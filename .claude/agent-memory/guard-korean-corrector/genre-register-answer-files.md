---
name: genre-register-answer-files
description: guard answer files are either 문서 본문 in ~다 or a 존댓말 session report; read the endings, do not assume ~다
metadata:
  type: project
---

guard's per-turn answer files under `.claude/guard/turns/<session>/<turn>.md` come in two
shapes, and the register is whichever one the file already picked:

- **문서 본문** — a work report with `#` headings, sections and tables, entirely in
  `~다` 평서형. Judged that way, not as 대화 응답.
- **존댓말 세션 보고** — same heading structure, but addressed to the user
  (`말씀하신`, `요청하신`, `~습니다` throughout). Seen on session-summary turns. This is
  a 대화 응답 in report layout; hold it to `-습니다`.

Decide from the file's own endings, never from the fact that it lives under `turns/`.

**Why:** these files are report documents the user reads after the audits finish, not a
chat reply. Converting a whole file to 존댓말 would be a file-wide rewrite driven by a
genre misread, which is exactly the false positive the register axis warns about.

**Bold convention in these files:** a bolded lead sentence opening each paragraph of a
section is this author's structural device and reads as a sub-heading; on the bold count,
strip the *inline* emphasis (`**언급한**`, `**반대**`, `**NO**`) and leave the paragraph
leads, rather than de-bolding a whole section. Bold inside a verbatim English quote is
quoted text — never touched.

**How to apply:** on a guard answer file, register findings are limited to a genuine mix
or a drop out of the file's own register — including telegraphic fragments with no ending
at all (`… 라우터를 거치지 않게.`, `모델은 테스트 후에 정확한 쪽으로.`) inside an
otherwise `-습니다` passage. Consistent register throughout = register 0. If a turn's
file ever contains 존댓말 commentary wrapping a quoted `~다` draft, hold each part to its
own genre. See [[terms-left-alone]].
