---
type: reference
status: Current
owner-of: 틀을 만들 때 참고한 외부 레포 목록
---

# 참고 레포

> 별 수와 마지막 push는 **2026-10-02에 `gh`로 조회한 값**입니다. 시간이 지나면 달라집니다.
> 통째로 설치하지 않고 **양식·구조·사고방식만 빌려 옵니다.**

## 문서·기획 양식

| 레포 | ⭐ | 빌려 온 것 | 빌리지 않은 것 |
|---|---|---|---|
| [github/spec-kit](https://github.com/github/spec-kit) | 139,774 | 기능 스펙(`spec-template`: 우선순위 있는 시나리오 + Given/When/Then), 계획(`plan-template`) 양식 | 슬래시 명령 설치, tasks 파일 (작업은 Linear가 관리) |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 70,905 | **현재 동작(`specs/`)과 변경 제안(`changes/`)을 분리**하는 생각 → `status: Current/Draft` | CLI·워크플로 도구 |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 53,721 | `docs/existing-codebases`의 기존 프로젝트 도입 사고방식 | 다중 에이전트 역할 체계 (1인 개발에 과함) |
| [adr/madr](https://github.com/adr/madr) | 2,530 | ADR 양식(상태, 검토한 대안, 결과) | — |
| [architecture-decision-record/architecture-decision-record](https://github.com/architecture-decision-record/architecture-decision-record) | 17,076 | ADR 템플릿 모음 | — |
| [evildmp/diataxis-documentation-framework](https://github.com/evildmp/diataxis-documentation-framework) | 1,243 | 문서를 how-to / reference / explanation으로 나누는 기준 → `type` 라벨 | — |
| [arc42/arc42-template](https://github.com/arc42/arc42-template) | 1,302 | 아키텍처 문서에 빠진 항목을 찾는 **체크리스트**로만 사용 | 12챕터 구조 전체 |

## 폴더 구조

| 레포 | ⭐ | 볼 곳 |
|---|---|---|
| [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | 45,840 | 최상위가 `backend frontend scripts`로 단순한 구조, `.claude`·`.agents` |
| [saleor/saleor](https://github.com/saleor/saleor) | 23,398 | 업무 도메인 하나 = 폴더 하나, 도메인마다 같은 파일 구성, `docs/`는 `adr`·`agents`뿐 |
| [cookiecutter/cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) | 13,613 | `config/settings/{base,local,production,test}`, `docs/`를 읽는 순서로 번호 |
| [PostHog/posthog](https://github.com/PostHog/posthog) | 40,096 | 문서를 독자·수명으로 구분(`internal` `onboarding` `plans` `published`) |
| [getsentry/sentry](https://github.com/getsentry/sentry) | 44,912 | 큰 코드베이스의 개발 환경·스크립트 분리 |
| [zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices) | 18,135 | 도메인별 폴더와 파일 역할 규칙 문서 |
| [kubernetes/enhancements](https://github.com/kubernetes/enhancements) | 3,964 | 기능 기획 문서(`keps/`)의 번호·템플릿·상태 관리 |

## 이 틀의 원본

- [gggmlduswjs/harness_framework](https://github.com/gggmlduswjs/harness_framework) — 강의 원본 하네스
- [obra/superpowers](https://github.com/obra/superpowers) (⭐294,176) — 에이전트의 작업 순서(설계 → 계획 → 구현 → 리뷰)

## 고르는 기준

- **큰 프로젝트가 직접 관리하거나 최근에도 push가 있는** 레포를 우선합니다. 개인이 만든 템플릿 레포는 별 수가 많아도 방치된 경우가 많습니다(예: 마지막 push가 몇 년 전인 Django+Vue 템플릿).
- 도입이 아니라 **참고**합니다. 겹치는 체계를 통째로 들이면 정본이 하나 더 생깁니다.
