---
type: guide
status: Draft
owner-of: TDD guard hook를 켜는 법·끄는 법·켜지 말아야 할 때·한계
---

# 6. TDD guard (test-first hook) — 기본 꺼짐, 필요할 때만 켠다

> **목적:** 소스 파일을 고치기 전에 **대응 테스트 파일이 있는지** hook이 확인하고, 없으면 "테스트부터 만들 수 있는지" 묻습니다.
> 근거: 강의 5-6·5-7. 아래 "왜"는 강사 주장이며 검증된 사실이 아닙니다.

## 1. 구조 — 엔진은 한 곳, 이 틀은 shim만

- 엔진(판정 로직): gg-tools 플러그인의 `~/claude/gg-skills/hooks/tdd_guard.py`. **이 레포에 복사하지 않습니다**(원칙: [.claude/README.md](../../.claude/README.md)).
- 이 틀: `.claude/hooks/tdd_guard.py` shim만 있습니다. stdin·인자·stdout·종료코드를 엔진에 그대로 넘깁니다.
- 엔진이 없으면 조용히 통과하지 않고 **확인을 요청**합니다(`guardrail.py` shim과 같음). 처음 한 번 `pwsh ~/claude/bootstrap.ps1`.
- **`.claude/settings.json`에는 등록되어 있지 않습니다.** TDD는 동작이 명확한 작업에 맞고, 모든 프로젝트에 강제하면 안 되기 때문입니다.

엔진이 하는 일(기본 동작은 **확인 요청**): `Write|Edit|MultiEdit`로 소스 파일(`.py .ts .tsx .js .jsx .vue`, 테스트·설정·문서·마이그레이션 제외)을 고치려는데 프로젝트 안에 대응 테스트(`test_<이름>.py`, `<이름>_test.py`, `<이름>.test.*`, `<이름>.spec.*`)가 없으면 사용자에게 확인을 요청합니다.

## 2. 켜는 법

프로젝트의 `.claude/settings.json`에 `PreToolUse` 항목을 추가합니다(기존 `Bash|PowerShell` 항목 옆).

**확인 요청 모드(기본)**

```json
{
  "matcher": "Write|Edit|MultiEdit",
  "hooks": [
    {
      "type": "command",
      "command": "python \"${CLAUDE_PROJECT_DIR}/.claude/hooks/tdd_guard.py\""
    }
  ]
}
```

**차단 모드** — 인자 `--mode deny`를 붙입니다.

```json
"command": "python \"${CLAUDE_PROJECT_DIR}/.claude/hooks/tdd_guard.py\" --mode deny"
```

> 주의: `--mode deny`는 gg-tools에 해당 옵션을 추가하는 PR이 **머지된 뒤에만** 쓸 수 있습니다. 머지 전 엔진에서는 인자가 무시되어 확인 요청으로 동작할 수 있으니, 쓰기 전에 엔진 버전을 확인합니다.

켠 뒤 **세션을 재시작**하고 `/hooks`에서 등록을 확인합니다(5장).

## 3. 끄는 법

- 한 번만: 환경변수 `TDD_GUARD_DISABLE=1`로 Claude Code를 실행합니다(gg-tools PR이 머지돼야 엔진이 이 변수를 읽습니다).
- 계속: `.claude/settings.json`에서 위 `Write|Edit|MultiEdit` 항목을 지웁니다.

## 4. 켜지 말아야 할 때

- **모호한 신규 설계** — 무엇을 만들지 아직 정해지지 않았으면 TDD가 아니라 SDD(설계서 먼저)가 맞습니다. 모든 파일에 걸면 개발이 막힙니다(강의).
- **프로젝트가 TDD shim을 금지하는 경우**(예: Coupang) — 그 프로젝트의 규칙이 정본입니다. 켜지 않습니다.
- 문서·설정·스크립트 위주 작업, 탐색용 프로토타입.

켜도 좋은 경우: 입출력이 분명한 주요 비즈니스 로직(계산·변환·검증)을 고치는 프로젝트.

## 5. 한계

- **존재만 확인**합니다. 빈 테스트 파일만 만들어도 통과합니다(추론 — 코드로 확인한 한계가 아님). 테스트 품질·통과 여부는 보장하지 않습니다. 완료 판정은 [4번 가이드](4-review-and-done.md)의 검증으로 합니다.
- **활성화 시점 미확정.** 같은 세션에서 새로 만든 hook이 언제 켜지는지는 출처가 엇갈립니다(강의: 재시작·`/hooks` 승인 필요 / 문서 요약: 파일 감시로 다음 이벤트부터 반영). 재시작을 권장합니다.
- **bypass 모드에서 PreToolUse hook의 deny가 동작하는지는 확인하지 못했습니다.** hook만 믿고 bypass 모드를 쓰지 마세요.
- **미구현:** 서킷 브레이커(같은 테스트 N회 실패 시 중단), 파일 변경 후 점검(강의의 나머지 hook).

## 6. 확인

shim 자체 검사: `python tests/test_tdd_guard_shim.py` (엔진 없음·엔진 있음, 가짜 HOME 사용 — 실제 엔진 유무와 무관).
엔진 자체 검사: `python .claude/hooks/tdd_guard.py --selftest` (엔진이 없으면 실패 종료코드 1).
