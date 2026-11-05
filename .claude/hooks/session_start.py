#!/usr/bin/env python3
"""SessionStart — notes/progress.md 의 순서 · 지금 상태 · 다음 할 일을 대화 맥락에 싣는다.

새 대화가 「하던 일 · 다음 할 일」을 파일에서 바로 알게 한다. 실패해도 세션을 막지 않는다(항상 exit 0).
self-test: python .claude/hooks/session_start.py --selftest
"""
import os
import sys

KEEP = ("순서", "지금 상태", "다음 할 일")
MAX_LINES = 60


def pick(text):
    out, on = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            on = any(k in line for k in KEEP)
        if on:
            out.append(line)
    return "\n".join(out[:MAX_LINES]).strip()


def selftest():
    sample = "# 진행\n## 순서\n1. 뼈대\n## 확인한 것\n- 비밀\n## 다음 할 일\n- 로그인\n"
    got = pick(sample)
    assert "1. 뼈대" in got and "- 로그인" in got and "비밀" not in got, got
    assert pick("") == ""
    print("session_start selftest OK")


def main():
    root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    path = os.path.join(root, "notes", "progress.md")
    if not os.path.exists(path):
        print("notes/progress.md 가 없다 — 하던 일을 파일에서 알 수 없다. 만들어 두자.")
        return
    with open(path, encoding="utf-8") as f:
        body = pick(f.read())
    if body:
        print("[notes/progress.md 요약 — 먼저 확인]\n" + body)


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        selftest() if "--selftest" in sys.argv else main()
    except AssertionError:
        raise
    except Exception:
        pass
    sys.exit(0)
