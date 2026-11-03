# .claude/ — Claude Code 설정

| 파일 | 하는 일 | 켜짐 |
|---|---|---|
| `settings.json` | 플러그인 · 훅 연결 | — |
| `hooks/guardrail.py` | 위험 명령(force push · `git add -A` · 파국적 rm · 인라인 시크릿) 막기 | 예 |
| `hooks/claude-md-check.py` | 세션 시작 때 `CLAUDE.md` 줄 수 · 오래됨 알림(판정은 `scripts/check-claude-md.py`) | 예 |
| `hooks/tdd_guard.py` | 소스 수정 전 대응 테스트 파일 확인 | 아니요 — 아래 |

훅의 판정 엔진은 [gg-tools](https://github.com/gggmlduswjs/gg-tools) 한 곳에 있고, 여기 파일은 얇은 shim 이다. 엔진이 없으면 조용히 통과하지 않고 확인을 요청한다.

```powershell
gh repo clone gggmlduswjs/gg-tools ~/claude
pwsh ~/claude/bootstrap.ps1
python .claude/hooks/guardrail.py --selftest
```

## TDD guard 켜기

돈 · 권한 · 상태 코드가 많은 프로젝트에서만 켠다. `settings.json` 의 `hooks.PreToolUse` 에 `Edit|Write` matcher 로 `python "${CLAUDE_PROJECT_DIR}/.claude/hooks/tdd_guard.py"` 를 더한다. 확인: `python .claude/hooks/tdd_guard.py --selftest`.

## 더할 때

에이전트 · 스킬 · 훅은 **같은 실수가 반복될 때만** 더한다. 구현 규칙은 여기가 아니라 루트 `rules/` 에 둔다.
