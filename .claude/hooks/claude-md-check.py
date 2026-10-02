#!/usr/bin/env python3
"""SessionStart hook shim — 판정은 scripts/check-claude-md.py 한 곳. 문제 있을 때만 stdout 에 알림(Claude 컨텍스트로 들어감). 항상 종료코드 0."""
import os
import subprocess
import sys

try:
    sys.stdin.read()  # hook 입력 JSON 은 쓰지 않는다
    root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    r = subprocess.run([sys.executable, os.path.join(root, "scripts", "check-claude-md.py"), "--hook",
                        "--file", os.path.join(root, "CLAUDE.md")],
                       capture_output=True, text=True, timeout=15)
    sys.stdout.write(r.stdout)
except Exception:
    pass  # 점검 실패가 세션을 막으면 안 된다
sys.exit(0)
