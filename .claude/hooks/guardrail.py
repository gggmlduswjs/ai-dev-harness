#!/usr/bin/env python3
"""가드레일 shim — 위험한 명령(force push, git add -A, 파국적 rm, 인라인 시크릿 등)을 막는다.

판정 로직은 gg-tools 의 공용 엔진 **한 벌**이다. 여기에 복사하지 않는다.
이 프로젝트만의 위험이 생기면 아래 REPO_DENY / REPO_ASK 에 한 줄씩 더한다.

self-test:  python .claude/hooks/guardrail.py --selftest
"""
import json
import os
import runpy
import sys

_HOME = os.path.expanduser("~")
_ENGINE_CANDIDATES = (
    os.path.join(_HOME, "claude", "gg-skills", "hooks", "guardrail.py"),
)
ENGINE = next((p for p in _ENGINE_CANDIDATES if os.path.exists(p)), _ENGINE_CANDIDATES[0])

# (정규식, "deny"|"ask", 사유) — deny 는 ask 보다 앞에 둔다(위→아래 첫 매치가 판정).
REPO_DENY: list = []
REPO_ASK: list = []
REPO_CASES: list = []  # (명령, 기대 판정 또는 None) — selftest 용


def _rules(engine):
    return (REPO_DENY
            + engine["deny_common"](migration_hint="마이그레이션 파일 + PR 로만")
            + REPO_ASK
            + engine["ask_common"]())


if __name__ == "__main__":
    if not os.path.exists(ENGINE):
        # 엔진이 없으면 조용히 통과하지 않는다 — 조용한 통과는 보호가 꺼진 것을 숨긴다.
        # 막지는 않고, 확인을 요청해서 사용자에게 보이게 한다.
        if "--selftest" in sys.argv:
            print("guardrail: 공용 엔진 없음 — 검사 못 함(통과 아님)")
            sys.exit(1)
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": "가드레일 엔진이 없어 위험 명령 검사가 꺼져 있습니다. "
                                        "처음 한 번: pwsh ~/claude/bootstrap.ps1 (.claude/README.md 참고)",
        }}, ensure_ascii=False))
        sys.exit(0)
    _engine = runpy.run_path(ENGINE, run_name="guardrail_engine")
    if "--selftest" in sys.argv:
        sys.exit(_engine["check"](_rules(_engine), REPO_CASES, label="guardrail(harness)"))
    _engine["run"](_rules(_engine))
