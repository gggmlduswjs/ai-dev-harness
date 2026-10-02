"""scripts/check-claude-md.py 최소 자체 검사 (경계 199/200/201줄). 실행: python tests/test_check_claude_md.py"""
import os
import subprocess
import sys
import tempfile

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "scripts", "check-claude-md.py")

with tempfile.TemporaryDirectory() as d:
    for n, want in ((199, 0), (200, 0), (201, 1)):
        p = os.path.join(d, "CLAUDE.md")
        open(p, "w", encoding="utf-8").write("x\n" * n)
        rc = subprocess.run([sys.executable, SCRIPT, "--lines-only", "--file", p], capture_output=True).returncode
        assert rc == want, f"{n}줄: 종료코드 {rc}, 기대 {want}"
print("OK")
