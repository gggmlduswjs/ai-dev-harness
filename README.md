# AI 개발 하네스 (AI Dev Harness)

Bookmart, BookEcommerce 및 앞으로 만드는 프로젝트에 **동일한 문서 체계와 AI 개발 방식**을 적용하기 위한 공통 템플릿입니다.

이 저장소는 [강의 원본 하네스](https://github.com/gggmlduswjs/harness_framework)의 핵심 개념을 유지하면서 실전 프로젝트용으로 단순화·확장한 표준입니다.

> **빈 PC에서 처음 시작한다면** [docs/guides/00-new-pc-setup.md](docs/guides/00-new-pc-setup.md)부터 보세요. 이 틀과 [gg-tools](https://github.com/gggmlduswjs/gg-tools) 두 저장소로 개발을 시작하는 순서입니다.

## 관련 저장소의 역할 — 코드 중복 금지

| 역할 | 정본 | 여기에 복사하지 않을 것 |
|---|---|---|
| 프로젝트 초기 구조·공식 문서 양식·공통 운영 원칙 | **이 저장소 `ai-dev-harness`** | 실행 중인 제품의 현재 문서 |
| 개발 프로세스(Brainstorming·계획·TDD·디버깅·검증) | 외부 [Superpowers](https://github.com/obra/superpowers) 플러그인 | 외부 스킬 본문·별도 phase 실행기 |
| Claude Code에서 Codex 작업 위임·리뷰 | [codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 플러그인 런타임·명령 본문 |
| 공통 전문 스킬·공통 hook 엔진(`guardrail`·`tdd_guard`·`secret_guard` 등)·온보딩 점검 스킬 `onboard`(`--structure`·`--catalog`·`--adopt`·`--impact`)·PC 설치 | [gg-tools](https://github.com/gggmlduswjs/gg-tools) | 플러그인 코드·hook 엔진·점검 스크립트·설치 스크립트 (이 레포의 `.claude/hooks/`는 shim만, [원칙](.claude/README.md)) |
| 제품별 정책·전용 스킬·Hook 연결 | Bookmart / Coupang_v2 각 레포 | 프로젝트 전용 비즈니스 규칙 |
| 현재 Project·Issue·Status·일정·우선순위 | Linear | 두 번째 실행 보드 |

Superpowers는 직접 설치하지 않고 `gg-tools`의 bootstrap(`pwsh ~/claude/bootstrap.ps1`)으로 설치합니다. 마켓플레이스가 다르면 중복 설치되고 `onboard` 점검이 감지합니다.

**이 레포는 설치 가능한 Claude 플러그인이 아니라 프로젝트를 시작할 때 참고·복사하는 표준 템플릿입니다.** 플러그인 배포는 `gg-tools`가 맡으므로 이 저장소에 별도 마켓플레이스나 Superpowers 사본을 만들지 않습니다.

기존 운영 프로젝트는 자료를 새 경로로 일괄 복사하지 않고 **현재 실제 정본에 이 표준의 논리적 역할을 대응**시킵니다.

## 이 틀의 적용 범위

| 구분 | 내용 | 적용 대상 |
|---|---|---|
| **어디서나 쓰는 것** | 기획 순서(PRD → ROADMAP → ARCHITECTURE/ADR → Linear), 문서 규칙(정본 하나·라벨·승격), 개발 루프, `templates/` 양식, 폴더 원칙 | 모든 프로젝트 |
| **웹서비스에 맞춘 것** | `src/backend`·`src/frontend` 분리, 도메인 폴더의 `models services api tasks tests`, `UI_GUIDE.md` | 서버 + 화면이 있는 프로젝트 |
| **스택 전용** | Element Plus·`refactoring-ui` 규칙 (`UI_GUIDE.md`, `CLAUDE.md`, `src/frontend/README.md`의 이름표 붙은 절) | Vue 3 + Element Plus 프로젝트 |

받은 뒤 **웹서비스·스택 전용 부분이 맞지 않으면 그 부분만 바꾸거나 지웁니다.** 어디서나 쓰는 것은 그대로 둡니다.

## 개발의 기본 흐름

```text
Linear 작업(Issue)
    ↓
관련 문서·코드 확인 및 범위 결정 (Claude 또는 Codex)
    ↓
모르는 것이 중요하면 Research
    ↓
복잡하거나 위험하면 Plan
    ↓
승인된 범위를 Codex가 구현
    ↓
Codex의 관련 검증 → 계약·diff·실행 근거 검수
    ↓
GitHub PR / CI
    ↓
승인된 병합(Merge)
    ↓
Linear 완료(Done)
```

**매 작업마다 Research·Plan을 만들지 않습니다.** 필요한 경우에만 사용합니다.

기본은 **Claude 기획 → Codex 구현·검증**입니다. Claude Code에서 `/codex:rescue`로 작업을 넘기며, **Codex 단독으로 기획부터 검증까지 수행할 수도 있습니다.** Claude 한도가 소진되면 같은 작업의 기존 결정·계획·브랜치를 이어받습니다. 실행 방식·인계 계약·명령 예시는 [일상 가이드의 작업 절차](docs/guides/2-daily-loop-and-second-brain.md#작업-절차)가 정본입니다.

## 도구별 책임

| 도구 | 유일하게 관리하는 것 |
|---|---|
| Linear | Project, Milestone, Issue, 진행 상태, 우선순위, 목표일 |
| Repository | 제품과 기술의 공식 지식 |
| GitHub | 커밋, PR, CI, 병합 및 배포 이력 |
| Obsidian | 개인 생각, 학습, 자유로운 조사 메모 |

## 공통 폴더 구조

```text
PROJECT/
├── CLAUDE.md                   # AI가 처음 읽는 프로젝트 안내서
├── AGENTS.md                   # Codex/다른 Agent용 보충 지침
├── README.md
├── docs/                       # 제품의 현재 공식 지식
│   ├── PRD.md  ROADMAP.md  ARCHITECTURE.md  ADR.md  UI_GUIDE.md   # 입구 5개
│   ├── CONVENTIONS.md          # 문서·폴더 규칙
│   ├── ADOPTION.md             # 기존 프로젝트에 적용하는 순서
│   ├── REFERENCES.md           # 참고한 외부 레포
│   ├── adr/                    # 개별 결정 기록 (결정은 이 한 곳)
│   ├── domains/                # 업무 영역
│   ├── features/               # 기능 명세 (기획의 정본)
│   ├── guides/                 # 따라 하는 문서 (0-start-project.md 부터)
│   ├── reference/              # 찾아보는 문서
│   └── _archive/               # Historical — 일상에서 읽지 않는다
├── .dev/
│   ├── research/               # 중요한 것을 모를 때만
│   └── plans/                  # 복잡하고 위험할 때만
├── .claude/                    # agents / rules / skills / hooks — 실제 필요할 때만 채움
├── src/
│   ├── backend/<domain>/       # 업무별 폴더: models · services · api · tasks · tests
│   └── frontend/               # 화면 코드
├── tests/                      # 도메인을 가로지르는 테스트
├── scripts/                    # 운영·CI 스크립트 (이 한 곳)
├── templates/                  # 여러 번 복사해서 쓰는 양식 (양식은 이 한 곳)
├── .artifacts/                 # 빌드·로그·백업·임시 출력 (git 제외)
└── .github/                    # PR 템플릿 및 CI/CD
```

폴더마다 안내 `README.md`가 있습니다. 규칙은 [docs/CONVENTIONS.md](docs/CONVENTIONS.md)입니다.

작은 프로젝트는 강의 원본처럼 `PRD / ARCHITECTURE / ADR / UI_GUIDE` 중심으로 시작합니다. 제품이 복잡해질 때에만 `docs/domains/`, `docs/features/`, `docs/architecture/`, `docs/adr/`, `docs/reference/`를 추가합니다.

**`src/`·`tests/`·`.claude/`는 폴더의 역할과 이름 규칙만 안내하는 뼈대입니다.** 언어와 프레임워크는 프로젝트가 정하고, `.claude/` 내용은 반복된 실수나 위험이 생길 때 채웁니다.

## 복사해서 사용할 양식

**한 번만 쓰는 문서(PRD 등 5개)는 `docs/`에서 채우고, 여러 번 만드는 문서는 [`templates/`](templates/README.md)의 양식을 복사합니다.**

| 목적 | 파일 |
|---|---|
| 제품 요구사항 | [PRD](docs/PRD.md) |
| 제품 발전 순서 | [로드맵](docs/ROADMAP.md) |
| 시스템 구조 | [아키텍처](docs/ARCHITECTURE.md) |
| 주요 결정 목록 | [ADR](docs/ADR.md) |
| 개별 결정 기록 | [ADR 양식](templates/ADR.md) |
| 공통 화면 설계 | [UI 가이드](docs/UI_GUIDE.md) |
| 공식 조사 | [Research 양식](templates/RESEARCH.md) |
| 구현 계획 | superpowers `writing-plans` → [.dev/plans/](.dev/plans/README.md) |
| 업무 영역 | [Domain 양식](templates/DOMAIN.md) |
| 기능 명세 | [Feature 양식](templates/FEATURE.md) |
| Linear 작업 | [Issue 양식](templates/LINEAR_ISSUE.md) |
| 코드 변경 설명 | [PR 양식](.github/PULL_REQUEST_TEMPLATE.md) |
| 새 프로젝트 시작 순서 | [0-start-project](docs/guides/0-start-project.md) |
| Linear·GitHub 이슈 활용법 | [1-linear-and-github-issues](docs/guides/1-linear-and-github-issues.md) |
| 문서·폴더 규칙 | [CONVENTIONS](docs/CONVENTIONS.md) |
| 기존 프로젝트 적용 순서 | [ADOPTION](docs/ADOPTION.md) |
| 참고한 외부 레포 | [REFERENCES](docs/REFERENCES.md) |

## 반드시 지킬 원칙

1. **실행 상태는 Linear만 관리합니다.** 현재 진행률·우선순위·마감·백로그를 저장소 문서에 중복해서 적지 않습니다.
2. **제품과 기술의 공식 지식은 저장소가 관리합니다.** 하나의 질문에는 현재 정본 하나가 있어야 합니다.
3. **Research와 Plan은 선택 사항입니다.** 작은 버그마다 문서를 만들지 않습니다.
4. **AI 하네스는 반복된 실수나 위험을 줄일 때만 확장합니다.** 폴더를 채우기 위해 Rule/Skill/Hook을 만들지 않습니다.
5. **AI가 완료했다고 말하는 것만으로 완료 처리하지 않습니다.** 작업의 위험도에 맞는 테스트·CI·외부 재조회·운영 근거를 확인합니다.
6. **강의 원본의 `phases/step/execute.py` 실행기를 기본 구조로 복원하지 않습니다.** Linear + 필요한 Plan + AI + GitHub가 실행 관리를 맡습니다.

## 적용 방법

기존 프로젝트에서는 바로 폴더를 이동하거나 기존 문서를 덮어쓰지 말고 **현재 정본 → 이 공통 역할**을 먼저 대응합니다. 업무와 코드 폴더는 달라도 개발 흐름을 통일하는 것이 목적입니다.
