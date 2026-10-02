#!/usr/bin/env python3
"""TDD guard shim — 소스 수정 전 대응 테스트 파일이 있는지 확인하는 hook. **기본 꺼짐**(settings.json 에 등록 안 함).

판정 로직은 gg-tools 의 공용 엔진 **한 벌**이다. 여기에 복사하지 않는다.
stdin·인자·stdout·종료코드를 엔진에 그대로 넘긴다(예: --mode deny, --selftest).
켜는 법: docs/guides/6-tdd-guard.md

self-test:  python .claude/hooks/tdd_guard.py --selftest
"""
import json
import os
import runpy
import sys

ENGINE = os.path.join(os.path.expanduser("~"), "claude", "gg-skills", "hooks", "tdd_guard.py")

if not os.path.exists(ENGINE):
    # guardrail shim 과 같다: 조용히 통과하지 않고 확인을 요청한다(selftest 는 실패).
    if "--selftest" in sys.argv:
        print("tdd_guard: 공용 엔진 없음 — 검사 못 함(통과 아님)")
        sys.exit(1)
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": "TDD guard 엔진이 없어 검사가 꺼져 있습니다. "
                                    "처음 한 번: pwsh ~/claude/bootstrap.ps1 (.claude/README.md 참고)",
    }}, ensure_ascii=False))
    sys.exit(0)
runpy.run_path(ENGINE, run_name="__main__")  # 엔진이 sys.argv·stdin 을 직접 읽고 sys.exit 한다
