---
name: terms-left-alone
description: project terms that look like 번역체 or English intrusion but are what this repo says — never rewrite them
metadata:
  type: project
---

Terms this project leaves alone in Korean prose. They are identifiers, scope names or
established loanwords, not 번역체.

- memory scope names: `project`, `local` — used bare inside Korean sentences
  (`local` 저장소, `project`는 루트만 추적하고). These are the scope identifiers, not
  English words standing in for Korean ones.
- paths and globs quoted as-is: `.claude/agent-memory-local/`,
  `**/.claude/agent-memory-local/`, `plugins/<name>/.claude/agent-memory/`, `!` prefix
- `.gitignore`, `diff`, `PR`, 커밋, 리뷰, 스코프, 에이전트, 트리
- `git check-ignore` verdict strings shown in tables: `IGNORED`, `WOULD-BE-COMMITTED`

**Why:** a rewrite that translates a scope name or renames a path makes the text wrong
rather than merely awkward — the damage is worse than the phrasing it fixed.

**How to apply:** when a Korean sentence reads oddly because of one of these, fix the
Korean around it and leave the term byte-identical. See [[genre-register-answer-files]].
