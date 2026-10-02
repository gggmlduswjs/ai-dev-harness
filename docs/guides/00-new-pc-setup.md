---
type: guide
status: Draft
owner-of: 아무것도 설치되지 않은 Windows PC에서 이 틀과 gg-tools로 개발을 시작하기까지의 순서
---

# 00. 새 PC에서 처음 시작하기

> **목적:** 아무것도 설치되지 않은 PC에서 **두 저장소**만으로 개발을 시작합니다. 아래를 위에서부터 그대로 복사해 붙여 넣으면 됩니다.
> **상태:** Draft — 명령은 실제 이 PC에서 확인했지만 **빈 PC에서 처음부터 끝까지 돌려 본 적은 없습니다.** 막히면 맨 아래 표를 보고, 고친 내용은 이 문서에 반영합니다.

| 저장소 | 역할 | 공개 여부 |
|---|---|---|
| [ai-dev-harness](https://github.com/gggmlduswjs/ai-dev-harness) | **프로젝트 틀.** 문서 양식, 폴더 구조, 개발 규칙. 프로젝트마다 한 벌씩 받아 그 위에서 개발 | 공개 |
| [gg-tools](https://github.com/gggmlduswjs/gg-tools) | **도구 모음.** Claude Code 스킬과 자동 검사(hook). **PC마다 한 번** 설치 | 비공개 (GitHub 로그인 필요) |

```text
PC 준비(1회) → GitHub 로그인(1회) → Claude Code 로그인(1회) → gg-tools 설치(1회) → 프로젝트 만들기(프로젝트마다) → 채팅으로 개발
```

## 준비물

- Windows 10 또는 11
- **GitHub 계정** (gg-tools 저장소에 접근 권한이 있는 계정)
- **Claude 계정** (Claude Code를 쓸 수 있는 요금제)

## 1. 프로그램 설치 (PC에 한 번)

시작 메뉴에서 **PowerShell**을 열고 한 줄씩 실행합니다. 설치 중 "허용하시겠습니까?"가 나오면 허용합니다.

```powershell
winget install --id Git.Git -e
winget install --id GitHub.cli -e
winget install --id Microsoft.PowerShell -e
winget install --id Python.Python.3.12 -e
winget install --id Anthropic.ClaudeCode -e
```

| 프로그램 | 왜 필요한가 |
|---|---|
| Git | 저장소를 받고 변경을 기록 |
| GitHub CLI(`gh`) | GitHub 로그인과 저장소 받기 |
| PowerShell 7(`pwsh`) | gg-tools 설치 스크립트를 실행 |
| Python | 자동 검사(hook)가 파이썬으로 동작 |
| Claude Code | 채팅으로 개발하는 도구 |

**모두 끝나면 PowerShell 창을 닫고 새로 엽니다.** 새 프로그램이 인식되려면 필요합니다. 확인:

```powershell
git --version; gh --version; pwsh --version; python --version; claude --version
```

다섯 줄 모두 버전이 나오면 됩니다. 하나라도 "찾을 수 없다"가 나오면 그 프로그램만 다시 설치하고 창을 새로 엽니다.

처음 한 번 Git에 이름을 알려 줍니다(커밋 기록에 쓰임).

```powershell
git config --global user.name "내 이름"
git config --global user.email "내 이메일"
```

## 2. 로그인 (PC에 한 번)

```powershell
gh auth login
```

질문이 나오면 `GitHub.com` → `HTTPS` → `Login with a web browser`를 고르고, 화면의 코드를 브라우저에 입력합니다. 끝나면:

```powershell
gh auth status
```

`Logged in to github.com`이 나오면 됩니다.

다음은 Claude Code 로그인입니다.

```powershell
claude
```

처음 실행하면 로그인 안내가 나옵니다. 브라우저에서 로그인하고 돌아오면 채팅 화면이 뜹니다. `/exit`로 나옵니다.

## 3. gg-tools 설치 (PC에 한 번)

폴더 위치는 **반드시 `~\claude`**(사용자 폴더 아래 `claude`)로 합니다. 프로젝트의 자동 검사가 이 경로에서 엔진을 찾습니다.

```powershell
gh repo clone gggmlduswjs/gg-tools $env:USERPROFILE\claude
pwsh $env:USERPROFILE\claude\bootstrap.ps1 -SkipPcWiring
```

- `bootstrap.ps1`이 Claude Code 플러그인(Superpowers, gg-skills 등)을 설치합니다.
- `-SkipPcWiring`은 **작성자 개인 PC 전용 배선**(구글 드라이브 메모리 연결, 북마트·쿠팡 개발 단축키)을 건너뜁니다. 처음 시작하는 PC에는 필요 없습니다.
- 끝나면 Claude Code를 새로 시작해야 새 스킬이 보입니다.

## 4. 프로젝트 만들기 (프로젝트마다)

```powershell
cd $env:USERPROFILE\Desktop
gh repo clone gggmlduswjs/ai-dev-harness my-project
cd my-project
Remove-Item -Recurse -Force .git
git init -b main
```

`my-project`는 원하는 이름으로 바꿉니다. 틀의 옛 기록을 지우고 **내 프로젝트의 새 저장소**로 시작하는 과정입니다.

그다음 Claude Code를 엽니다.

```powershell
claude
```

처음 열면 "이 폴더를 신뢰하시겠습니까?"가 나옵니다. 내 프로젝트이므로 신뢰합니다.

## 5. 채팅으로 시작하기

Claude Code 화면에서 이렇게 말하면 됩니다.

```text
새 프로젝트를 시작할게. 아이디어는 "____" 이야. docs/guides/0-start-project.md 순서대로 진행해줘.
```

Claude가 질문을 하나씩 하고, 답하면 `docs/PRD.md` 같은 기획 문서를 채웁니다. **PRD·ROADMAP·설계서·계획서·머지는 내가 승인해야 다음으로 넘어갑니다.** 승인 전에는 코드를 쓰지 않습니다. 이후 흐름은 [0-start-project.md](0-start-project.md)와 [2-daily-loop-and-second-brain.md](2-daily-loop-and-second-brain.md)를 봅니다.

## 6. 잘 설치됐는지 확인

| 확인 | 명령 | 기대 결과 |
|---|---|---|
| 플러그인 설치됨 | Claude Code 안에서 `/plugin` | `superpowers`, `gg-skills`가 보임 |
| 자동 검사 엔진 있음 | `python .claude/hooks/guardrail.py --selftest` | `selftest OK (57 cases …)` |
| 틀이 온전함 | `dir docs` | `PRD.md`, `ROADMAP.md`, `ARCHITECTURE.md` 등이 보임 |

## 막힐 때

| 증상 | 원인과 해결 |
|---|---|
| `winget`을 찾을 수 없다 | Windows 10 오래된 버전. Microsoft Store에서 "앱 설치 관리자"를 업데이트 |
| 설치 직후 `git`·`gh`·`claude`를 찾을 수 없다 | PowerShell 창을 **닫고 새로** 연다 |
| `gh repo clone gggmlduswjs/gg-tools`가 "not found" | 로그인한 GitHub 계정에 gg-tools 접근 권한이 없음. 저장소 소유자에게 초대를 요청 |
| `bootstrap.ps1`에서 `claude`를 찾을 수 없다 | Claude Code 설치 후 창을 새로 열지 않음 |
| `bootstrap.ps1`이 마켓플레이스 추가 실패 | `gh auth status`로 로그인 확인, 인터넷 확인 후 다시 실행(여러 번 돌려도 안전) |
| `guardrail.py --selftest`에서 "공용 엔진 없음" | gg-tools를 `~\claude`가 아닌 곳에 받음. 위치를 `$env:USERPROFILE\claude`로 |
| Claude가 위험 명령 검사가 꺼져 있다고 확인을 요청 | 같은 원인(엔진 없음). 3단계를 다시 확인 |

## 알아 둘 것

- 이 문서의 명령은 **Windows 전용**입니다(PowerShell).
- 이 틀의 프로젝트는 처음에 **GitHub에 올리지 않은** 로컬 저장소입니다. 올릴 때는 `gh repo create 이름 --private --source . --push`를 씁니다.
- Vue 화면을 만드는 프로젝트라면 이후 Node.js가 필요합니다(`winget install --id OpenJS.NodeJS.LTS -e`). 처음 시작에는 필요 없습니다.
