"""tdd_guard shim 최소 자체 검사 — 가짜 HOME 을 쓰므로 실제 엔진 유무와 무관. 실행: python tests/test_tdd_guard_shim.py"""
import json
import os
import subprocess
import sys
import tempfile

SHIM = os.path.join(os.path.dirname(__file__), "..", ".claude", "hooks", "tdd_guard.py")


def run(home, stdin, *args):
    env = {**os.environ, "HOME": home, "USERPROFILE": home}
    return subprocess.run([sys.executable, SHIM, *args], input=stdin, capture_output=True,
                          text=True, encoding="utf-8", env=env)


with tempfile.TemporaryDirectory() as home:
    # 엔진 없음: 통과 아님 — ask 출력, selftest 는 실패
    r = run(home, "{}")
    assert r.returncode == 0 and json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"] == "ask", r
    assert run(home, "", "--selftest").returncode == 1

    # 가짜 엔진: stdin·인자·종료코드가 그대로 전달된다
    d = os.path.join(home, "claude", "gg-skills", "hooks")
    os.makedirs(d)
    with open(os.path.join(d, "tdd_guard.py"), "w") as f:
        f.write("import sys\nprint(sys.stdin.read(), sys.argv[1:])\nsys.exit(7)\n")
    r = run(home, '{"a":1}', "--mode", "deny")
    assert r.returncode == 7 and r.stdout.strip() == "{\"a\":1} ['--mode', 'deny']", r
print("OK")
