#!/usr/bin/env python3
"""CLAUDE.md 점검 — 판정은 이 한 파일에서만 한다 (SessionStart hook · GitHub Action 공용). 표준 라이브러리만 사용.

  python scripts/check-claude-md.py                 줄 수 + 마지막 git 수정일 점검, 문제 있으면 종료코드 1
  python scripts/check-claude-md.py --lines-only    줄 수만 (CI: shallow clone 은 수정일을 못 믿음)
  python scripts/check-claude-md.py --hook          문제 있어도 종료코드 0 (SessionStart hook 용)
  git diff --name-only ... | python scripts/check-claude-md.py --drift
                                                    stdin 의 변경 파일에 컨벤션 파일은 있고 CLAUDE.md 는 없으면 종료코드 3
  python scripts/check-claude-md.py --selftest      경계값 자체 검사 (종료코드 0 = 통과)
"""
import argparse
import os
import subprocess
import sys
import tempfile
import time

MAX_LINES = 200
MAX_AGE_DAYS = 14
CONVENTION_PREFIXES = ("docs/", "templates/", ".claude/rules/")  # 바뀌면 CLAUDE.md 도 봐야 하는 곳


def check(path, lines_only=False, max_lines=MAX_LINES, max_age_days=MAX_AGE_DAYS, now=None):
    """문제 문장 목록을 돌려준다. 파일이 없으면 점검할 것이 없으므로 빈 목록."""
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8", errors="replace") as f:
        n = len(f.read().splitlines())
    problems = []
    if n > max_lines:
        problems.append(f"{os.path.basename(path)} 가 {n}줄입니다(상한 {max_lines}). docs/ 로 링크하고 낡은 항목을 지우세요.")
    if not lines_only:
        age = last_modified_days(path, now)
        if age is not None and age > max_age_days:
            problems.append(f"{os.path.basename(path)} 를 마지막으로 수정한 지 {age}일 지났습니다(기준 {max_age_days}일).")
    return problems


def last_modified_days(path, now=None):
    """git 기준 마지막 수정 후 경과일. git 이력이 없으면 None(판정 생략)."""
    try:
        d = os.path.dirname(os.path.abspath(path))
        out = subprocess.run(["git", "log", "-1", "--format=%ct", "--", os.path.basename(path)],
                             cwd=d, capture_output=True, text=True, timeout=10).stdout.strip()
        return int(((now or time.time()) - int(out)) // 86400) if out else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def drift(changed):
    """컨벤션 파일만 바뀌고 CLAUDE.md 는 안 바뀌었으면 True."""
    changed = [c.strip().replace("\\", "/") for c in changed if c.strip()]
    return any(c.startswith(CONVENTION_PREFIXES) for c in changed) and "CLAUDE.md" not in changed


def selftest():
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "CLAUDE.md")
        for n, bad in ((199, False), (200, False), (201, True)):
            with open(p, "w", encoding="utf-8") as f:
                f.write("x\n" * n)
            assert bool(check(p, lines_only=True)) == bad, f"{n}줄 판정 틀림"
        assert not check(os.path.join(d, "none.md"))
    assert drift(["docs/A.md"]) and not drift(["docs/A.md", "CLAUDE.md"]) and not drift(["src/a.py"])
    print("selftest OK (199/200 통과, 201 실패, drift 판정)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="CLAUDE.md")
    ap.add_argument("--lines-only", action="store_true")
    ap.add_argument("--hook", action="store_true")
    ap.add_argument("--drift", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.drift:
        return 3 if drift(sys.stdin.read().splitlines()) else 0
    problems = check(a.file, a.lines_only)
    if problems:
        print("CLAUDE.md 점검 필요 — " + " ".join(problems) + " claude-md-improver 를 돌리세요(리포트 확인 후 승인한 항목만 수정).")
    return 0 if a.hook else (1 if problems else 0)


if __name__ == "__main__":
    sys.exit(main())
