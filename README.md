# AI 개발 하네스 (AI Dev Harness)

AI 에이전트(Claude Code · Codex)에게 일을 맡겨도 **화면 하나하나가 촘촘하고 일관되게** 나오도록 하는 프로젝트 시작 틀입니다. 새 프로젝트에 복사해서 `docs/` 를 채우고 시작합니다.

## 생각의 뼈대 — 디테일은 산문이 아니라 코드와 표에 둔다

| 층 | 어디 | 누가 정하나 | 무엇으로 지키나 |
|---|---|---|---|
| 무엇을 · 왜 | `docs/PRD.md` · `docs/ROADMAP.md` | 사람 | 단계마다 「끝나는 기준」(실행 명령 · 화면 확인) |
| 업무 규칙(돈 · 상태 · 권한) | `docs/DOMAIN.md` | 사람 | 표 한 줄 = 테스트 하나 |
| 화면 | `docs/SCREENS.md` | 사람이 목록 · 패턴만 고름 | 패턴이 칸 · 상태를 채움 |
| 모양 | `docs/DESIGN_SYSTEM.md` + 토큰 · 패턴 코드 | 한 번 만들고 재사용 | 토큰 밖 값 금지, 패턴마다 상태 5개 |
| 구현 규칙 | `rules/` | 반복된 실수에서 | `rules/INDEX.yaml` 트리거 + 기계 검사 |
| 결정 | `docs/DECISIONS.md` | 사람 | 번호 · 날짜로 덧붙이기만 |

산문 규칙은 잘 안 지켜지고(아래 출처: 산문 규칙 위반 38%, 코드 규칙 4~17%), 코드에는 컴파일러 · 타입 · 테스트라는 공짜 검증기가 있습니다. 그래서 디테일은 가능한 한 **테스트 · 디자인시스템 코드 · 규칙 검사**로 내리고, 문서는 그 바탕이 되는 결정과 목록만 둡니다.

## 폴더

```text
PROJECT/
├── CLAUDE.md              AI 가 처음 읽는 안내(200줄 이하, CI 가 검사)
├── AGENTS.md              Codex 차이만
├── docs/                  제품의 현재 정본 — 읽는 순서는 docs/README.md
│   ├── PRD.md  ROADMAP.md  DECISIONS.md  ARCHITECTURE.md
│   ├── DOMAIN.md          데이터 단위 · 상태전이 · 금액 · 권한
│   ├── SCREENS.md         화면 목록 한 장
│   └── DESIGN_SYSTEM.md   토큰 · 패턴 · 공통 상태 · 금지 목록
├── rules/                 구현 규칙(INDEX.yaml · principles.md · concerns/)
├── templates/             ISSUE.md(작업 하나) · PATTERN.md(화면 패턴 하나)
├── .claude/               훅(위험 명령 · CLAUDE.md 점검 · Baden 슬롯 알림 · TDD guard) — 관제: Baden · gitwatch
├── .github/               PR 양식 · CLAUDE.md 줄 수 검사
├── scripts/  tests/
```

## 새 프로젝트 시작 순서

1. 이 레포를 템플릿으로 새 레포를 만듭니다(`Use this template`).
2. `docs/PRD.md` → `docs/DOMAIN.md` → `docs/SCREENS.md` → `docs/DESIGN_SYSTEM.md` → `docs/ROADMAP.md` 순서로 채웁니다. 모르는 칸은 비워 두지 말고 `?` 를 적습니다.
3. 정한 것은 `docs/DECISIONS.md` 에 번호를 붙여 적습니다.
4. `CLAUDE.md` 의 「안전」 · 「명령」 빈칸을 프로젝트 기준으로 채웁니다.
5. 로드맵 1단계를 GitHub Issue 여러 개로 쪼갭니다(`templates/ISSUE.md`). 이슈 하나 = 화면 하나 또는 흐름 하나.
6. 구현 → PR → 기계 검사 → 리뷰 → 머지. 같은 실수가 두 번 나오면 `rules/` 에 규칙을 더합니다.

## 일의 흐름

```text
GitHub Issue (요구 · 패턴 · 데이터 단위 · 끝나는 기준)
  → 실행 AI 가 구현(worktree)  ── 테스트 먼저: 돈 · 권한 · 상태 · 외부 쓰기
  → PR → CI(테스트 · 규칙 검사 · CLAUDE.md 검사)
  → 리뷰 AI 판정(mergeable / needs_review / blocked) — 구현 AI 와 다른 에이전트
  → 사람 머지 → 이슈 닫힘(PR 본문 Closes #N)
```

- **실행 상태는 GitHub Issues 한 곳.** 진행률 · 우선순위 · 마감을 문서에 적지 않습니다.
- **AI 의 「됐다」는 증거가 아닙니다.** 끝나는 기준의 명령 결과 · CI · 화면 확인이 증거입니다.
- **진짜 병목은 검토하는 사람의 시간입니다.** 기계 검사를 늘려 사람이 볼 것을 줄입니다.

## 출처

이 틀은 세 갈래를 합친 것입니다.

| 출처 | 가져온 것 |
|---|---|
| [jha0313/harness_framework](https://github.com/jha0313/harness_framework) | 시작 문서 틀(PRD · ARCHITECTURE · ADR · UI_GUIDE), 「AC 는 실행 가능한 명령」, 작업 단위 자기완결성 |
| 김민태 [ibare](https://github.com/ibare) — `jindesk` · `aperi21` · `baden` | 문서는 데이터 단위 · 결정 누적 · 읽는 순서 색인, 「결정적인 일은 코드, 판단은 에이전트」, `rules/` 구조(INDEX.yaml 트리거 · principles · concerns), 규칙 준수율 측정. 수치(산문 38% · 코드 4~17%)는 강의 「AI 에이전트 중심 개발 워크플로우」(패스트캠퍼스, 2026) 소개서 |
| 레이시스 디자인시스템(design.leysys.com) 구조 | 토큰 3층(원시 → 의미 → 부품), 강조 4단, 테마 = 속성 몇 개, 화면 디테일은 패턴이 채운다, 기계 판정 UI 계약. 값과 코드는 가져오지 않고 구조만 참고 |
