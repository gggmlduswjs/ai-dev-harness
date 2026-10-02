# 프로젝트 안내

이 저장소는 여러 프로젝트에서 공통으로 사용할 **AI 개발 하네스의 기준과 문서 양식**을 제공합니다.

실제 서비스에 적용할 때는 이 파일을 프로젝트 환경과 안전 규칙에 맞게 수정해야 합니다.

## 필요한 정보는 어디서 찾는가?

- 제품 요구사항 양식: `docs/PRD.md`
- 로드맵 양식: `docs/ROADMAP.md`
- 아키텍처 양식: `docs/ARCHITECTURE.md`
- 중요한 결정 양식: `docs/ADR.md`
- UI 공통 규칙 양식: `docs/UI_GUIDE.md`
- 조사 양식: `templates/RESEARCH.md`
- 설계서·구현 계획서: superpowers 스킬이 만든다 → 저장 위치는 아래 「superpowers 저장 위치」
- 업무·기능·결정(ADR)·Linear 양식: `templates/` (목록: `templates/README.md`)
- 문서·폴더 규칙(정본 하나·라벨·폴더 3원칙): `docs/CONVENTIONS.md`
- 새 프로젝트 시작 순서(아이디어 → PRD → ROADMAP → ARCHITECTURE → Linear → 첫 기능): `docs/guides/0-start-project.md`
- Linear·GitHub 이슈 활용법(상태 정의·라벨·GitHub 연동): `docs/guides/1-linear-and-github-issues.md`
- 기존 프로젝트에 적용하는 순서: `docs/ADOPTION.md`
- 참고한 외부 레포: `docs/REFERENCES.md`
- 배경 지식·결정 이유(시험적, 필요 없으면 삭제): @_brain/wiki/index.md 먼저. 정본(Spec·ADR·Linear)은 복사하지 않고 링크

## 기본 개발 흐름

```text
Linear Issue
→ 관련 저장소 문서와 코드 확인
→ 구현
→ 검증
→ GitHub PR / CI
→ 승인된 병합
→ Linear Done
```

상황에 따라 다음 절차를 추가합니다.

- 중요한 정보가 부족함 → Research.
- 구현이 복잡하거나 고위험임 → Plan.
- 앞으로도 유효해야 할 제품 규칙 → docs.
- AI가 같은 실수를 반복함 → 필요에 따라 Rule / Skill / Hook / Agent / Eval.

## 화면(UI) 작업 (Vue + Element Plus 프로젝트일 때)

화면을 만들거나 고칠 때는 이 순서로 합니다. 규칙의 정본은 `docs/UI_GUIDE.md`입니다. 다른 스택이면 부품 선택 단계를 그 스택의 규칙으로 바꿉니다.

1. **부품 선택** — Element Plus 공식 컴포넌트에서 고릅니다(`element-plus` 스킬).
2. **디자인 판단** — 간격·위계·색·그림자는 `refactoring-ui` 스킬로 정해진 단계에서 고릅니다.
3. **토큰** — 값은 토큰 파일 한 곳에서만 바꿉니다. 컴포넌트마다 스타일을 덮지 않습니다.

## 작업이 끝났을 때

머지 전에 앞으로도 유효한 내용을 정본(`docs/`)으로 올리고, 끝난 설계서·계획서는 `status: Historical`로 바꿔 `docs/_archive/`로 보냅니다. 올릴 것이 없는 작업은 건너뜁니다. 절차: `docs/CONVENTIONS.md` 6장.

## superpowers 저장 위치

superpowers 스킬의 기본 저장 위치(`docs/superpowers/…`)는 쓰지 않습니다. 정본이 둘이 되기 때문입니다.

| 산출물 | 저장 위치 | 만드는 스킬 |
|---|---|---|
| 설계서(spec) | `docs/features/YYYY-MM-DD-기능명.md` | `brainstorming` |
| 구현 계획서 | `.dev/plans/YYYY-MM-DD-기능명.md` | `writing-plans` |
| 작업 장부·검토 패키지 | `.superpowers/` (git 제외) | `executing-plans` 등 |

저장할 때 위 경로를 사용자 설정으로 지정하고, 맨 위에 `docs/CONVENTIONS.md`의 라벨 4줄을 붙입니다.

## 핵심 규칙

1. **Linear가 실행 상태의 유일한 정본**입니다.
2. **Repository 문서가 제품과 기술 지식의 정본**입니다.
3. **GitHub가 코드 변경과 검증 이력**을 보관합니다.
4. 개인 Obsidian 메모를 검증 없이 프로젝트 공식 사실로 취급하지 않습니다.
5. 같은 주제의 공식 정본을 중복 생성하지 않습니다.
6. 모든 작업에 Research·Feature Spec·Plan을 강제하지 않습니다.
7. AI의 완료 선언만으로 검증 완료라 판단하지 않습니다.
8. 실제 반복 문제나 위험을 해결하지 못하는 하네스 구성요소는 만들지 않습니다.

## 운영 안전

**실제 프로젝트**에서는 다음 항목에 대한 구체적인 허용·금지 조건을 별도로 정의해야 합니다.

- 운영 DB 쓰기
- 마이그레이션
- 돈·재고 계산
- 삭제·초기화 등 파괴적 작업
- 외부 API 쓰기
- 배포

이 템플릿이 어떤 운영 변경도 자동 승인하는 것은 아닙니다.

## 검증 명령

실제 프로젝트의 기술 스택에 맞춰 다음 명령을 기입합니다.

- 단위 테스트:
- 통합 테스트:
- 브라우저/E2E:
- 린트/빌드/타입 검사:
- 외부 시스템/운영 상태 확인:

## Git 및 PR

작고 검토 가능한 변경을 우선합니다. 문서 정리, 기능 개발, 대규모 구조 변경은 가능한 한 별도 작업과 PR로 구분합니다.

## AI 하네스 구성요소

실제로 필요할 때에만 `.claude/rules/`, `.claude/skills/`, `.claude/agents/`, `.claude/hooks/`를 추가합니다.
