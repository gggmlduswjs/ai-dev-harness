# AI 개발 하네스 (AI Dev Harness)

Bookmart, BookEcommerce 및 앞으로 만드는 프로젝트에 **동일한 문서 체계와 AI 개발 방식**을 적용하기 위한 공통 템플릿입니다.

이 저장소는 [강의 원본 하네스](https://github.com/gggmlduswjs/harness_framework)의 핵심 개념을 유지하면서 실전 프로젝트용으로 단순화·확장한 표준입니다.

## 관련 저장소의 역할 — 코드 중복 금지

| 역할 | 정본 | 여기에 복사하지 않을 것 |
|---|---|---|
| 프로젝트 초기 구조·공식 문서 양식·공통 운영 원칙 | **이 저장소 `ai-dev-harness`** | 실행 중인 제품의 현재 문서 |
| 개발 프로세스(Brainstorming·계획·TDD·디버깅·검증) | 외부 [Superpowers](https://github.com/gggmlduswjs/superpowers) 플러그인 | 외부 스킬 본문·별도 phase 실행기 |
| 공통 전문 스킬·공통 Hook 엔진·Eval·PC 설치 | [gg-tools](https://github.com/gggmlduswjs/gg-tools) | 플러그인 코드·설치 스크립트 |
| 제품별 정책·전용 스킬·Hook 연결 | Bookmart / Coupang_v2 각 레포 | 프로젝트 전용 비즈니스 규칙 |
| 현재 Project·Issue·Status·일정·우선순위 | Linear | 두 번째 실행 보드 |

**이 레포는 설치 가능한 Claude 플러그인 자체가 아니라 프로젝트를 시작할 때 참고·복사하는 표준 템플릿입니다.** `gg-tools`가 이미 플러그인 배포를 담당하므로 이 저장소에 별도 마켓플레이스나 Superpowers 사본을 만들지 않습니다.

기존 운영 프로젝트는 자료를 새 경로로 일괄 복사하지 않고 **현재 실제 정본에 이 표준의 논리적 역할을 대응**시킵니다. 예를 들어 Coupang_v2의 상세 계약 `docs/v2/`와 Bookmart의 현재 표준 입구는 유지하고 필요한 연결만 정리합니다.

## 개발의 기본 흐름

```text
Linear 작업(Issue)
    ↓
저장소에서 관련 문서·코드 확인
    ↓
모르는 것이 중요하면 Research
    ↓
복잡하거나 위험하면 Plan
    ↓
Claude / Codex 구현
    ↓
테스트 및 검증
    ↓
GitHub PR / CI
    ↓
승인된 병합(Merge)
    ↓
Linear 완료(Done)
```

**매 작업마다 Research·Plan을 만들지 않습니다.** 필요한 경우에만 사용합니다.

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
├── docs/                       # 제품의 현재 공식 지식
│   ├── PRD.md                  # 제품의 무엇과 왜
│   ├── ROADMAP.md              # 제품 발전 순서
│   ├── ARCHITECTURE.md         # 시스템 구조
│   ├── ADR.md                  # 중요한 결정과 그 이유
│   └── UI_GUIDE.md             # 공통 UI 규칙
├── .dev/
│   ├── research/               # 중요한 것을 모를 때만
│   └── plans/                  # 복잡하고 위험할 때만
├── .claude/                    # 실제 필요할 때 AI 규칙/스킬/Agent/Hook 추가
├── src/                        # 실제 제품 코드
├── tests/                      # 검증 코드
└── .github/                    # PR 템플릿 및 CI/CD
```

작은 프로젝트는 강의 원본처럼 `PRD / ARCHITECTURE / ADR / UI_GUIDE` 중심으로 시작합니다. 제품이 복잡해질 때에만 `docs/domains/`, `docs/features/`, `docs/architecture/`, `docs/adr/`, `docs/reference/`를 추가합니다.

**이 저장소는 템플릿이라 `src/`, `tests/`, `.claude/`의 빈 폴더는 일부러 만들지 않았습니다.** 실제 프로젝트에서 필요할 때 구성합니다.

## 복사해서 사용할 양식

| 목적 | 파일 |
|---|---|
| 제품 요구사항 | [PRD](docs/PRD.md) |
| 제품 발전 순서 | [로드맵](docs/ROADMAP.md) |
| 시스템 구조 | [아키텍처](docs/ARCHITECTURE.md) |
| 주요 결정 | [ADR](docs/ADR.md) |
| 공통 화면 설계 | [UI 가이드](docs/UI_GUIDE.md) |
| 공식 조사 | [Research 양식](.dev/research/TEMPLATE.md) |
| 구현 계획 | [Plan 양식](.dev/plans/TEMPLATE.md) |
| 업무 영역 | [Domain 양식](templates/DOMAIN.md) |
| 기능 명세 | [Feature 양식](templates/FEATURE.md) |
| Linear 작업 | [Issue 양식](templates/LINEAR_ISSUE.md) |
| 코드 변경 설명 | [PR 양식](.github/PULL_REQUEST_TEMPLATE.md) |

## 반드시 지킬 원칙

1. **실행 상태는 Linear만 관리합니다.** 현재 진행률·우선순위·마감·백로그를 저장소 문서에 중복해서 적지 않습니다.
2. **제품과 기술의 공식 지식은 저장소가 관리합니다.** 하나의 질문에는 현재 정본 하나가 있어야 합니다.
3. **Research와 Plan은 선택 사항입니다.** 작은 버그마다 문서를 만들지 않습니다.
4. **AI 하네스는 반복된 실수나 위험을 줄일 때만 확장합니다.** 폴더를 채우기 위해 Rule/Skill/Hook을 만들지 않습니다.
5. **AI가 완료했다고 말하는 것만으로 완료 처리하지 않습니다.** 작업의 위험도에 맞는 테스트·CI·외부 재조회·운영 근거를 확인합니다.
6. **강의 원본의 `phases/step/execute.py` 실행기를 기본 구조로 복원하지 않습니다.** Linear + 필요한 Plan + AI + GitHub가 실행 관리를 맡습니다.

## 적용 방법

기존 프로젝트에서는 바로 폴더를 이동하거나 기존 문서를 덮어쓰지 말고 **현재 정본 → 이 공통 역할**을 먼저 대응합니다. 업무와 코드 폴더는 달라도 개발 흐름을 통일하는 것이 목적입니다.
