# AI 개발 하네스 (AI Dev Harness)

Bookmart, BookEcommerce 및 앞으로 만드는 프로젝트에 **동일한 문서 체계와 AI 개발 방식**을 적용하기 위한 공통 템플릿입니다.

이 저장소는 [강의 원본 하네스](https://github.com/gggmlduswjs/harness_framework)의 핵심 개념을 유지하면서 실전 프로젝트용으로 단순화·확장한 표준입니다.

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
