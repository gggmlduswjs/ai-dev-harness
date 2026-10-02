---
type: guide
status: Draft
owner-of: TDD test-first guard hook의 동작, 조정법, 끄는 법, 한계
---

# 6. TDD guard (test-first hook)

> **목적:** 소스 파일을 고치기 전에 **대응 테스트 파일이 있는지** hook이 확인하고, 없으면 차단해 "테스트부터 쓰라"고 돌려보냅니다.
> 근거: 강의 5-6. 아래 "왜"는 강사 주장이며 검증된 사실이 아닙니다. 차단 방식(PreToolUse의 `permissionDecision: "deny"`)은 Claude Code hooks 문서(code.claude.com/docs/en/hooks)로 확인했습니다.

## 1. 무엇을 막는가

`.claude/hooks/tdd-guard.py`가 `Edit`·`Write` 직전에 실행됩니다(`.claude/settings.json`의 PreToolUse, matcher `Edit|Write`).

1. 파일 경로가 없으면 통과.
2. **테스트 파일 자체**(`test_*`, `*_test.*`, `*.test.*`, `*.spec.*`, `tests/`·`test/`·`__tests__/` 아래)는 수정 허용.
3. 화이트리스트(소스 확장자가 아닌 파일 — 마크다운·JSON·YAML·CSS·lock 등, `.d.ts`, `*.config.*`, `__init__.py`, `types/`·`docs/`·`.claude/` 등 폴더)는 통과.
4. 그 외 소스 파일은 같은 폴더, 그 아래·프로젝트 루트의 `tests/`·`test/`·`__tests__/`에서 `test_<이름>`, `<이름>_test`, `<이름>.test`, `<이름>.spec` 파일을 찾습니다(`-`와 `_`는 같게 봄).
5. 없으면 **deny** + "테스트 파일이 존재하지 않습니다. 코드를 작성하기 전에 테스트부터 작성하세요." + 예상 경로.

오류가 나면 **통과**합니다(fail-open) — 가드 오류가 개발을 막지 않게 하려는 선택입니다.

## 2. 조정법

고칠 곳은 `tdd-guard.py` 맨 위 상수 한 블록뿐입니다: `GUARDED_EXT`(검사할 확장자), `SKIP_DIRS`(통과 폴더), `SKIP_NAMES`(통과 파일명), `TEST_DIRS`, `TEST_PATTERNS`(테스트 이름 규칙).

- 모든 파일에 TDD를 걸면 개발이 안 됩니다(강의). **주요 비즈니스 로직 폴더만** 걸리도록 `GUARDED_EXT`·`SKIP_DIRS`를 좁히는 것을 권합니다. 이 틀은 그 판단을 대신하지 않습니다.
- 테스트가 `src/` 옆이 아닌 다른 폴더 구조(`spec/` 등)면 `TEST_DIRS`에 추가합니다.

## 3. 끄는 법

- 한 번만: 환경변수 `TDD_GUARD_DISABLE=1`로 Claude Code를 실행합니다.
- 계속: `.claude/settings.json`에서 `Edit|Write` 항목을 지웁니다.

## 4. 한계

- **존재만 확인**합니다. 빈 테스트 파일만 만들어도 통과합니다(위키에 (추론)으로 정리된 한계). 테스트 품질·통과 여부는 보장하지 않습니다 — 완료 판정은 [4번 가이드](4-review-and-done.md)의 검증으로 합니다.
- 서킷 브레이커(같은 테스트 N회 실패 시 중단), 파일 변경 후 점검은 강의의 나머지 hook이며 **미구현**입니다.
- TDD는 동작이 명확한 작업에 맞습니다. 모호한 신규 설계는 SDD(설계서 먼저)가 맞으니 이 hook을 좁히거나 끕니다.

## 5. 활성화

같은 세션에서 새로 만든 hook이 언제 켜지는지는 출처가 엇갈립니다(강의: 재시작·`/hooks` 승인 필요 / hooks 문서 요약: 파일 감시로 다음 이벤트부터 자동 반영 — **미확정**). **세션을 재시작**하고 `/hooks`에서 등록을 확인하는 것을 권합니다.

자체 검사: `python tests/test_tdd_guard.py` (차단·화이트리스트·테스트 파일 수정 허용·테스트 있음 통과·경로 없음, 5케이스).
