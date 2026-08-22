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

**Some turn answers are record documents, not 대화 응답.** A file that opens as a status
record (e.g. `# … 재검증 — 착수 상태`, with a line like `이 파일은 착수 시점의 사실만 담는다`)
is 문서 본문 end to end and is correctly `~다` 평서형 throughout. Same for **work-report
answers** — a title naming what changed, `## 반영: …` / `## 반영하지 않았다 …` / `## 버전` /
`## 남은 것` sections, uniform `~다` with no 존댓말 anywhere. Judge as 문서 본문; converting
the whole file to 존댓말 would be a re-authoring, not a correction. In these reports the
noun-fragment enumeration style (`… 돌려 봐도 된다는 것. … 값싸다는 것.`) listing what was
added to a paragraph is deliberate — keep it when splitting a long sentence, and do not
flag it as a fragment. Do not flag it as 반말 or
convert it to 존댓말. Also seen bare in such notes and left alone: `deferral`,
`resolvable` / `legitimate` / `pass` (verdict tokens), `픽스처`, `디스패치`, `auditor`.

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
left in place. In work-report answers a bolded lead sentence opening a finding paragraph
(`**신뢰 대화상자는 그대로 뜬다.**`, `**앞서 적은 이유는 틀렸다.**`) is functional; four of
this kind in one report was normal, not 볼드 남발.
In long design-note answers (multi-section, numbered audit-criteria lists),
the bolded item labels act as sub-headings: a total near sixteen was counted and all kept,
since only ~5 were inline emphasis. Judge the inline-emphasis count, not the total.
