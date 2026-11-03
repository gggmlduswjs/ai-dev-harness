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

## Baden 연결

[Baden](https://github.com/ibare/baden) = 에이전트 행동 · 규칙 준수를 실시간으로 쌓는 로컬 모니터(:3800). 판정은 `scripts/baden.py` 한 곳.

| 무엇 | 어디 |
|---|---|
| 프로젝트 이름(정본) | `CLAUDE.md` 「Baden Monitoring」 의 `Project Name` |
| 슬롯 구분 | 세션 시작 훅(`scripts/baden.py session`)이 worktree 폴더 이름을 알려 주고, `baden_start_task` prompt 앞에 `[slot]` 을 붙인다. 대시보드 등록은 프로젝트당 한 번 |
| 서버 꺼짐 알림 | 같은 훅이 :3800 에 1초 물어보고, 응답이 없으면 세션에 알린다(보고가 조용히 버려지는 것을 막음) |
| 서브에이전트 보고 | `python scripts/baden.py report '<JSON>'` (settings.json 에 허용 등록됨) |

처음 한 번(PC 마다):

```bash
git clone https://github.com/ibare/baden.git && cd baden && npm run build
# MCP 는 PC 경로가 들어가서 레포에 넣지 않고 사용자 범위로 등록한다
claude mcp add --scope user baden -e BADEN_API_URL=http://localhost:3800 -- node <baden 경로>/mcp/dist/index.js
node bin/baden.js start          # macOS 는 `baden install` 로 로그인 때 자동 실행
```

Codex 는 `~/.codex/config.toml` 에:

```toml
[mcp_servers.baden]
command = "node"
args = ["<baden 경로>/mcp/dist/index.js"]
env = { BADEN_API_URL = "http://localhost:3800" }
```

프로젝트마다: 대시보드(http://localhost:3800) 「+ Add Project」 에 `CLAUDE.md` 의 Project Name 과 **똑같은 이름**으로 등록한다(모르는 이름의 보고는 버려진다). 규칙 추적을 쓰려면 Rules Path 에 `rules/` 를 넣는다.

Windows 는 baden 의 자동 실행(launchd)을 지원하지 않는다. 로그인 때 `node <baden 경로>/bin/baden.js start` 를 작업 스케줄러에 걸어 둔다.

## 워크트리 관제 — gitwatch

[gitwatch](https://github.com/gggmlduswjs/gitwatch) = 여러 worktree 의 브랜치 · 커밋 안 된 변경 · 앞섬/뒤짐 · 마지막 커밋을 한 화면에 보는 **읽기 전용** 관제판(:3810, 의존성 0, Node 20+). 김민태 GitWatcher(macOS, 비공개)의 Windows 판.

```bash
git clone https://github.com/gggmlduswjs/gitwatch.git
node gitwatch/server.mjs <레포 경로> [다른 레포 ...]   # → http://127.0.0.1:3810
```

- **두 화면은 같은 이름으로 맞춰 본다.** gitwatch 의 행 = worktree 폴더 이름 = Baden 의 `[slot]`. gitwatch 로 「어느 슬롯이 무엇을 바꿨나」를, Baden 으로 「그 슬롯의 에이전트가 무엇을 했고 규칙을 지켰나」를 본다.
- gitwatch 는 git 조회만 한다(fetch 도 안 함). 조회 실패는 0 이 아니라 「조회 실패」로 보인다.
- 로그인 때 자동으로 띄우려면 Baden 과 같이 작업 스케줄러에 건다.

## TDD guard 켜기

돈 · 권한 · 상태 코드가 많은 프로젝트에서만 켠다. `settings.json` 의 `hooks.PreToolUse` 에 `Edit|Write` matcher 로 `python "${CLAUDE_PROJECT_DIR}/.claude/hooks/tdd_guard.py"` 를 더한다. 확인: `python .claude/hooks/tdd_guard.py --selftest`.

## 더할 때

에이전트 · 스킬 · 훅은 **같은 실수가 반복될 때만** 더한다. 구현 규칙은 여기가 아니라 루트 `rules/` 에 둔다.
