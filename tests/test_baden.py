"""scripts/baden.py 최소 검사 — 순수 판정(selftest) + 실제 git worktree 에서 슬롯 · 꺼진 서버 알림. 실행: python tests/test_baden.py"""
import os
import subprocess
import sys
import tempfile

SCRIPT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts", "baden.py"))
assert subprocess.run([sys.executable, SCRIPT, "--selftest"]).returncode == 0


def session(cwd):
    env = {**os.environ, "CLAUDE_PROJECT_DIR": cwd, "BADEN_API_URL": "http://127.0.0.1:9"}  # 9 = 닫힌 포트
    r = subprocess.run([sys.executable, SCRIPT, "session"], cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0, r
    return r.stdout


with tempfile.TemporaryDirectory() as d:
    main, wt = os.path.join(d, "app"), os.path.join(d, "dev-2")
    os.makedirs(main)
    run = lambda *a: subprocess.run(["git", *a], cwd=main, capture_output=True, check=True)
    run("init", "-q")
    open(os.path.join(main, "CLAUDE.md"), "w", encoding="utf-8").write("- Project Name: `shop`\n")
    run("add", "CLAUDE.md")
    run("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "init")
    run("worktree", "add", "-q", wt)

    out = session(main)
    assert "project=shop slot=main" in out and "응답하지 않는다" in out, out
    assert "slot=dev-2" in session(wt), session(wt)

    open(os.path.join(main, "CLAUDE.md"), "w", encoding="utf-8").write("- Project Name: `{projectName}`\n")
    assert session(main) == ""  # 아직 안 채운 템플릿은 조용히

print("test_baden OK")
