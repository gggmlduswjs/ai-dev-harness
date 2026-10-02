#!/usr/bin/env python3
"""PreToolUse(Edit|Write) hook — 소스 파일을 고치기 전에 대응 테스트 파일이 있는지 확인하고, 없으면 deny.
존재만 확인한다(테스트를 실행하거나 내용을 보지 않는다). 오류가 나면 통과(fail-open). 끄기: TDD_GUARD_DISABLE=1.
프로젝트에 맞게 고칠 것은 아래 상수뿐이다. 가이드: docs/guides/6-tdd-guard.md"""
import json
import os
import sys

# ── 프로젝트가 고치는 곳 ────────────────────────────────────────────
GUARDED_EXT = {".py", ".js", ".jsx", ".ts", ".tsx", ".vue", ".go", ".java", ".rb", ".rs", ".php", ".cs", ".kt", ".swift"}  # 이 확장자만 검사. 그 외(md·json·yaml·css·lock 등)는 통과
SKIP_DIRS = {".claude", ".git", ".github", ".dev", "_brain", "node_modules", "docs", "templates", "types", "migrations", "dist", "build"}  # 이 폴더 아래는 통과
SKIP_NAMES = {"conftest.py", "setup.py", "manage.py"}  # 이 파일명은 통과 (*.config.*, *.d.ts, __init__.py 는 아래에서 통과)
TEST_DIRS = {"tests", "test", "__tests__"}  # 테스트 폴더 이름 (대상 파일 옆 + 프로젝트 루트에서 찾음)
# 테스트 파일 이름 규칙 — 이름은 소문자·`-`→`_` 로 정규화해 비교. {n}=확장자 뺀 파일명
TEST_PATTERNS = ("test_{n}", "{n}_test", "{n}.test", "{n}.spec")
# ───────────────────────────────────────────────────────────────────


def norm(s):
    return s.lower().replace("-", "_")


def is_test_file(path):
    parts = [norm(p) for p in path.replace("\\", "/").split("/")]
    name = parts[-1]
    return (any(p in TEST_DIRS for p in parts[:-1]) or name.startswith("test_")
            or ".test." in name or ".spec." in name or os.path.splitext(name)[0].endswith("_test"))


def is_skipped(path):
    p = path.replace("\\", "/")
    name = os.path.basename(p)
    ext = os.path.splitext(name)[1].lower()
    return (ext not in GUARDED_EXT or name in SKIP_NAMES or name == "__init__.py" or name.endswith(".d.ts")
            or ".config." in name or any(d in SKIP_DIRS for d in p.split("/")[:-1]))


def find_test(path, root):
    stem = norm(os.path.splitext(os.path.basename(path))[0])
    wanted = {norm(t.format(n=stem)) for t in TEST_PATTERNS}
    here = os.path.dirname(path)
    dirs = [here] + [os.path.join(b, t) for b in (here, root) for t in sorted(TEST_DIRS)]
    for d in dirs:
        try:
            for f in os.listdir(d):
                if norm(os.path.splitext(f)[0]) in wanted:
                    return True
        except OSError:
            pass
    return False


def expected(path):
    stem, ext = os.path.splitext(os.path.basename(path))
    name = f"test_{stem}{ext}" if ext == ".py" else f"{stem}.test{ext}"
    return os.path.join(os.path.dirname(path), name)


def main():
    if os.environ.get("TDD_GUARD_DISABLE") == "1":
        return
    data = json.load(sys.stdin)
    path = (data.get("tool_input") or {}).get("file_path")
    if not path or is_test_file(path) or is_skipped(path):
        return
    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    if find_test(path, root):
        return
    reason = ("테스트 파일이 존재하지 않습니다. 코드를 작성하기 전에 테스트부터 작성하세요. "
              f"예상 경로: {expected(path)}")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                             "permissionDecision": "deny",
                                             "permissionDecisionReason": reason}}, ensure_ascii=False))


try:
    main()
except Exception:
    pass  # 가드 오류가 개발을 막으면 안 된다
sys.exit(0)
