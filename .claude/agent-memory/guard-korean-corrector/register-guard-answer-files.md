---
name: register-guard-answer-files
description: guard answer files under .claude/guard/turns/ are 문서 본문 in ~다 평서형 with first-person sentence headings — never flag as 반말
metadata:
  type: project
---

Answer files at `.claude/guard/turns/<session>/<turn>.md` are the deliverable the user
reads. They are written as **문서 본문** — `~다` 평서형 throughout, first person, with
narrative sentence headings (`## 내 것만 커밋했다`, `## 남은 것`). This is the project's
deliberate convention, matching the repo's commit-message voice.

**Why:** These files are reports, not chat turns. Holding them to 존댓말 would be a
whole-file rewrite of a consistent, intended register — a large false positive.

**How to apply:** Judge these files on axes 1–3 only unless the body genuinely mixes
`~다` and `-습니다`. Do not flag the `~다` endings, and do not flag the sentence-form
headings as 구어체.
