#!/usr/bin/env python3
"""Stop — 코드는 바뀌었는데 notes/progress.md 가 그보다 오래됐으면 한 번 갱신을 요청한다.

다음 대화가 이어 갈 수 있게 하는 장치다. 같은 멈춤에서 두 번 막지 않는다(stop_hook_active).
git 이 없거나 실패하면 그냥 통과한다(항상 exit 0).
self-test: python .claude/hooks/stop_check.py --selftest
"""
import json
import os
import subprocess
import sys

SKIP = ("notes/", "work/", "briefs/", ".claude/")
REASON = ("코드가 바뀌었는데 notes/progress.md 가 갱신되지 않았다. "
          "지금 상태 · 다음 할 일 · 확인한 것/못 한 것을 갱신하고, 결정이 있었으면 notes/decisions.md 에도 적어라.")


def need_update(changed, progress_mtime, active):
    """changed: [(경로, mtime)] — 바뀐 코드 중 progress 보다 새 것이 있으면 True."""
    if active:
        return False
    code = [m for p, m in changed if not p.startswith(SKIP)]
    return bool(code) and (progress_mtime is None or max(code) > progress_mtime)


def changed_files(root):
    out = subprocess.run(["git", "status", "--porcelain", "-uall"], cwd=root,
                         capture_output=True, text=True, encoding="utf-8", timeout=10).stdout
    res = []
    for line in out.splitlines():
        p = line[3:].split(" -> ")[-1].strip('"')
        full = os.path.join(root, p)
        if os.path.exists(full):
            res.append((p.replace("\\", "/"), os.path.getmtime(full)))
    return res


def selftest():
    assert need_update([("src/a.py", 20)], 10, False) is True          # 코드가 progress 보다 새것 → 요청
    assert need_update([("src/a.py", 5)], 10, False) is False          # progress 를 뒤에 갱신 → 통과
    assert need_update([("src/a.py", 20)], 10, True) is False          # 이미 한 번 막음 → 통과
    assert need_update([("notes/progress.md", 20)], 10, False) is False  # 기록만 바뀜 → 통과
    assert need_update([("src/a.py", 20)], None, False) is True        # progress 없음 → 요청
    print("stop_check selftest OK")


def main():
    data = json.loads(sys.stdin.read() or "{}")
    root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    prog = os.path.join(root, "notes", "progress.md")
    pm = os.path.getmtime(prog) if os.path.exists(prog) else None
    if need_update(changed_files(root), pm, data.get("stop_hook_active", False)):
        print(json.dumps({"decision": "block", "reason": REASON}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        selftest() if "--selftest" in sys.argv else main()
    except AssertionError:
        raise
    except Exception:
        pass
    sys.exit(0)
