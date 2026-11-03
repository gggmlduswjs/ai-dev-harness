#!/usr/bin/env python3
"""Baden 연결 — 표준 라이브러리만. 판정은 이 한 파일(SessionStart 훅 · 서브에이전트 보고 공용).

  python scripts/baden.py session          세션 시작 안내(프로젝트 · 슬롯 · 서버 상태)를 출력. 항상 종료코드 0
  python scripts/baden.py report '<JSON>'  서브에이전트가 MCP 대신 HTTP 로 보고. 예: '{"action":"rule_check","ruleId":"C1","taskId":"…"}'
                                           projectName 은 자동으로 채운다. 실패해도 종료코드 0(에이전트를 막지 않는다)
  python scripts/baden.py --selftest

프로젝트 이름의 정본 = CLAUDE.md 의 「- Project Name: `이름`」 한 줄.
슬롯 = 이 체크아웃이 git worktree 면 그 폴더 이름, 본 체크아웃이면 main.
  baden 에는 슬롯 칸이 없어서, baden_start_task 의 prompt 맨 앞에 [슬롯] 을 붙여 구분한다.
  그러면 대시보드에 프로젝트를 한 번만 등록해도 슬롯마다 작업이 갈린다.
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

API = os.environ.get("BADEN_API_URL", "http://localhost:3800").rstrip("/")
NAME = re.compile(r"^\s*-\s*Project Name:\s*`([^`]+)`", re.M)


def root():
    return os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def project(text):
    """CLAUDE.md 본문 → 프로젝트 이름. 없거나 아직 {placeholder} 면 None."""
    m = NAME.search(text)
    return m.group(1) if m and not m.group(1).startswith("{") else None


def slot(top, git_dir, common_dir):
    """git 값 → 슬롯 이름. 보조 worktree 는 git-dir 과 common-dir 이 다르다."""
    if not top:
        return None
    same = os.path.normcase(os.path.abspath(git_dir)) == os.path.normcase(os.path.abspath(common_dir))
    return "main" if same else os.path.basename(os.path.normpath(top))


def git(*args):
    try:
        return subprocess.run(["git", *args], cwd=root(), capture_output=True, text=True, timeout=5).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def read_project():
    try:
        with open(os.path.join(root(), "CLAUDE.md"), encoding="utf-8") as f:
            return project(f.read())
    except OSError:
        return None


def alive():
    try:
        urllib.request.urlopen(API, timeout=1)
        return True
    except urllib.error.HTTPError:
        return True  # 응답이 왔으면 서버는 떠 있다
    except Exception:
        return False


def session():
    name = read_project()
    if not name:
        return  # Baden 을 쓰지 않는 프로젝트 — 조용히
    top = git("rev-parse", "--show-toplevel")
    s = slot(top, git("rev-parse", "--absolute-git-dir"), os.path.join(top, git("rev-parse", "--git-common-dir")) if top else "") or "main"
    print(f"Baden: project={name} slot={s}. baden_start_task 의 prompt 맨 앞에 [{s}] 를 붙인다.")
    if not alive():
        print(f"Baden 서버가 응답하지 않는다({API}). 보고는 버려진다 — 사람에게 알리고 작업은 계속한다.")


def report(raw):
    name = read_project()
    try:
        body = {**json.loads(raw), "projectName": name}
        req = urllib.request.Request(API + "/api/query", data=json.dumps(body).encode(), method="POST",
                                     headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=3)
    except Exception:
        pass  # 보고 실패가 작업을 막으면 안 된다


def selftest():
    assert project("- Project Name: `shop`\n") == "shop"
    assert project("- Project Name: `{projectName}`") is None and project("no block") is None
    assert slot("/r/app", "/r/app/.git", "/r/app/.git") == "main"
    assert slot("/wt/dev-2", "/r/app/.git/worktrees/dev-2", "/r/app/.git") == "dev-2"
    assert slot("", "", "") is None
    print("selftest OK")
    return 0


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "--selftest":
        return selftest()
    try:
        if cmd == "session":
            session()
        elif cmd == "report" and len(sys.argv) > 2:
            report(sys.argv[2])
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
