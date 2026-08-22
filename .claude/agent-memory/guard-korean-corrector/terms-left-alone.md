---
name: terms-left-alone
description: terms in this repo's Korean answer files that look like 번역체 but are correct as written — leave them alone
metadata:
  type: project
---

Terms this project leaves in place inside Korean prose:

- Identifiers and agent names — `ext-docs-auditor`, `ext-docs-fetcher`, `PreToolUse`,
  `SubagentStart`, `agent_id`, `agent_type`, `default`, `bypassPermissions`
- Model names in lowercase — `opus`, `sonnet`, `haiku`
- git vocabulary kept in English — `git status`, `git add`, `rename`, HEAD
- Korean dev usage that is idiomatic here: 스테이지/언스테이지(하다), 인덱스, 미추적,
  개명, 빚 (for technical debt), 커밋, 리마인더

**Why:** Translating any of these makes the text wrong rather than smoother.

**How to apply:** Never raise these on axis 2. See [[register-guard-answer-files]] for the
register these files use.
