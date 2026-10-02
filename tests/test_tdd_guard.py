"""hook(.claude/hooks/tdd-guard.py) 최소 자체 검사 5케이스. 실행: python tests/test_tdd_guard.py"""
import json
import os
import subprocess
import sys
import tempfile

HOOK = os.path.join(os.path.dirname(__file__), "..", ".claude", "hooks", "tdd-guard.py")


def run(root, file_path):
    payload = {"tool_name": "Edit", "cwd": root, "tool_input": {} if file_path is None else {"file_path": file_path}}
    env = {**os.environ, "CLAUDE_PROJECT_DIR": root}
    env.pop("TDD_GUARD_DISABLE", None)
    r = subprocess.run([sys.executable, HOOK], input=json.dumps(payload), capture_output=True, text=True,
                       encoding="utf-8", env=env)
    assert r.returncode == 0, r.stderr
    return r.stdout


with tempfile.TemporaryDirectory() as d:
    os.makedirs(os.path.join(d, "tests"))
    src = os.path.join(d, "calc.py")
    out = run(d, src)  # 1 차단 (테스트 없음)
    deny = json.loads(out)["hookSpecificOutput"]
    assert deny["permissionDecision"] == "deny" and "test_calc.py" in deny["permissionDecisionReason"], out
    assert run(d, os.path.join(d, "README.md")) == ""  # 2 화이트리스트(문서)
    assert run(d, os.path.join(d, "tests", "test_calc.py")) == ""  # 3 테스트 파일 자체 수정 허용
    open(os.path.join(d, "tests", "test_calc.py"), "w").close()
    assert run(d, src) == ""  # 4 대응 테스트 있음 → 통과
    assert run(d, None) == ""  # 5 경로 없음 → 통과
print("OK")
