# `disable-model-invocation`을 푸는 전제 — 다시 계산한 결과

## 결론

전제를 받으면 말이 됩니다. 다만 제가 앞 턴에서 든 반대 근거 중 하나는 뒤집히고,
하나는 오히려 설계를 결정하는 조건으로 남습니다. 그리고 앞 턴에 추론으로 남겨 뒀던 부분을
실제로 재 봤더니, 그 결과가 구현 방식을 하나로 좁힙니다.

가장 큰 이득은 컨텍스트 절감이 아닙니다. **경로에서 모델의 전사(轉寫) 단계가 사라지는
것**입니다. 지금은 훅이 경로 6줄을 찍고 모델이 그걸 Agent 프롬프트로 옮겨 적습니다.
이번 턴에도 제가 그 6줄을 손으로 다시 쳤습니다. skill 경로에서는 그 값들이 스크립트에서
fork로 바로 들어가고 모델을 거치지 않습니다.

---

## 실측: 두 호출 경로는 다르게 동작한다

`claude` 2.1.240에 일회용 플러그인을 `--plugin-dir`로 물려서 확인했습니다. 같은 스킬,
같은 매처, 프롬프트만 바꾼 두 번의 실행입니다.

| 호출 경로 | `UserPromptExpansion` | 본문 `` !`command` `` 주입 |
| --- | --- | --- |
| 사용자가 `/tp:probeskill` 입력 | 발화 (697바이트 페이로드) | 실행됨 |
| 모델이 `Skill` 도구로 호출 | **발화 안 함** (로그 0바이트) | **실행됨** |

덧붙여, `context: fork`의 `agent:`에 **플러그인 스코프 이름**(`tp:probeagent`)을 넣는 것도
동작했습니다. 문서에는 `.claude/agents/`의 커스텀 서브에이전트까지만 적혀 있어서
미검증으로 남겨 뒀던 부분입니다. 실제로는 fork가 그 에이전트의 시스템 프롬프트로 돌았고,
주입된 마커도 함께 도착했습니다.

절차·원문 인용·판정 근거는 `wiki/ref/claude-code-skill-invocation-paths.md`에 저장했습니다
(출처 https://code.claude.com/docs/en/skills.md, https://code.claude.com/docs/en/hooks.md).

여기서 나오는 설계 제약이 하나입니다. 모델도 부를 수 있는 skill은
`UserPromptExpansion`에서 데이터를 받을 수 없습니다. 호출의 절반은 데이터 없이 도착합니다.
그러니 dynamic injection은 **본문 주입 한 가지**로 가야 하고, 기존
`/guard:claims-auditor` 류가 쓰는 매처 방식과는 구조가 갈라집니다. 둘을 다 달면 사용자가
직접 쳤을 때 훅 stdout과 본문 주입이 이중으로 들어옵니다.

## 다시 계산한 이득

앞 턴에서 "대략 본전"이라고 한 계산은 모델의 전사 비용을 빼먹은 값이었습니다. 이 대화에
실제로 찍힌 블록 길이를 기준으로 다시 세면:

| | 지금 | skill 경로 |
| --- | --- | --- |
| 훅 출력 | 약 650자 | 약 90자 (한 줄) |
| 모델의 라우터 디스패치 | 약 600자 (필드 전사) | 약 30자 (Skill 호출) |
| 라우터 보고서 | 약 400자 | 약 500자 (answer file 경로 포함) |
| 합계 | **약 1,650자** | **약 620자** |

토큰 실측이 아니라 문자 수 계산입니다. 절감분(라우팅 턴당 250토큰 안팎)은 부수입입니다.
본론은 전사가 사라지는 쪽입니다. 경로 하나가 모델의 손을 안 거치면 그 경로에서 오타나
누락이 나올 수 없습니다.

## 설계

### `plugins/guard/skills/routing/SKILL.md`

```yaml
---
name: routing
description: >
  Route the finished turn to guard's audit agents. guard's Stop hook asks for this at the
  end of an audited turn; invoke it then, and not otherwise. Claude Code only.
argument-hint: ''
context: fork
agent: guard:router
background: false
allowed-tools: Bash(uv run --script ${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py route*)
---

!`uv run --script "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" route --session ${CLAUDE_SESSION_ID}`
```

본문이 거의 비어 있는 게 정상입니다. `context: fork`에서는 **에이전트 정의가 시스템
프롬프트, skill 본문이 task**입니다. 판단 방법은 이미 `agents/router.md`에 있습니다.
본문은 이번 턴의 입력만 실어 나르면 됩니다.

`allowed-tools`에 같은 `${CLAUDE_PLUGIN_ROOT}` 문자열을 쓰는 게 필수입니다. 주입 명령은
권한을 묻지 않고, 허용이 아닌 판정이 나오면 **호출 전체가 중단**됩니다.

### `cmd_route()` — `scripts/guard_core/cmd_turn.py`

`cmd_verify()`와 같은 골격이고, `_dispatch_context` 대신 `_router_context`를 부릅니다.
필요한 값은 전부 세션 상태에 있습니다: `pending_verify_prompt_id`, `transcript_path`,
`_eligible_agents`가 쓰는 편집 파일 버킷. 세션 id는 `--session`, 없으면
`CLAUDE_CODE_SESSION_ID` — `cmd_settings`가 이미 쓰는 방식입니다.

절대 0이 아닌 코드로 끝나면 안 됩니다. 문서상 주입 명령이 실패하면 그 placeholder만
비는 게 아니라 skill 호출 전체가 취소되고 모델은 본문을 아예 보지 못합니다. 즉 라우팅이
조용히 사라집니다. 감사할 턴이 없거나 이미 라우팅한 턴이면 그 사실을 한 줄 찍고 0으로
끝내야 합니다.

`cmd_verify`가 스위치를 무시하는 것과 같은 이유로 이것도 스위치를 무시합니다.

### `_ROUTE_LEAD` — `scripts/guard_core/dispatch.py`

```
guard: audit the turn you just finished — invoke the `guard:routing` skill.
```

필드 블록은 `cmd_route`의 stdout으로 옮겨 갑니다. 파일 판독 에이전트
(`comment-corrector` 등) 블록은 라우터를 안 거치므로 지금 자리에 그대로 둡니다.

### `agents/router.md` — 출력에 answer file 경로 추가

이게 놓치기 쉬운 필수 변경입니다. 지금은 메인 에이전트가 훅 블록에서 answer file 경로를
받습니다. skill 경로에서는 그 블록이 fork 안으로만 들어갑니다. 라우터가 보고서에 그
경로를 실어 돌려주지 않으면 메인 에이전트가 감사 에이전트를 디스패치할 수 없습니다.
`Output` 절의 두 템플릿에 한 줄씩 추가하면 됩니다.

## 전제를 받으면 같이 손봐야 하는 것

- **`AGENTS.md`의 불변식.** 지금 문장은 "It names **agents**, never guard's own skills."
  입니다. 이 문장 자체를 고쳐 써야 합니다. 규칙을 어긴 채 두는 것과는 다릅니다. 예: 훅은
  에이전트를 지명하고, 예외는 `routing` 하나 — 라우터의 진입점이자
  `disable-model-invocation`이 없는 유일한 `/guard:*` 파일.
- **`dispatch-playbook.md`의 `Dispatching` 절.** "Never invoke a `/guard:*` skill to do
  it" 에 같은 예외를 명시.
- **`router_model` 설정이 죽습니다.** 지금은 훅이 `- dispatch guard:router with model: …`
  를 찍어 `guard.local.json`의 값을 반영합니다. skill의 `model:`은 프론트매터라 정적입니다.
  설정을 접고 프론트매터에 `opus`를 박든지, 이 한 항목 때문에 Agent 디스패치 경로를
  남기든지 — 전자를 권합니다.

## 남는 위험

- **불려야 할 때 안 불릴 수 있습니다.** 지금도 모델이 라우터를 디스패치해야 하니 실패
  등급은 같습니다. 다만 위의 "주입 실패 = 호출 통째로 소멸"은 새로 생긴 조용한 실패입니다.
  `cmd_route`가 호출될 때마다 trace를 남겨야 사후에 구분이 됩니다.
- **안 불려야 할 때 불릴 수 있습니다.** `disable-model-invocation`을 풀면 description이
  메인 컨텍스트에 상주하고(문서상 그렇습니다), 모델이 임의 시점에 부를 수 있습니다.
  막을 방법은 문구가 아니라 스크립트 쪽입니다. `cmd_route`를 턴당 멱등으로 만들면 됩니다
  (`routed_prompt_id` 같은 마커). 두 번째 호출은 "already routed" 한 줄로 끝냅니다.
  그러면 오호출이 나도 해롭지 않고 비용도 거의 없습니다.
- **fork 보고서를 그 턴에 받으려면 `background: false`** 입니다. 기본값(`true`)이면 결과가
  다음 턴에 도착합니다.
- **Codex는 영향 없습니다.** Codex의 stop 경로는 애초에 라우팅을 하지 않고 적격 집합을
  통째로 권합니다. 파일은 `skills/`에 있어야 Codex 매니페스트에 등록되지만, 이 스킬 자체는
  Claude 전용입니다.

## 제안

실측으로 미검증 항목 두 개(`UserPromptExpansion` 발화 여부, 플러그인 스코프 `agent:`)가
정리됐으니 남은 불확실성은 설계가 아니라 취향 문제입니다. 만들어 볼까요?
