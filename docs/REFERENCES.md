---
type: reference
status: Current
owner-of: 틀을 만들 때 참고한 외부 레포와 실제 반영 여부
---

# 참고 레포

> 별 수와 마지막 push는 **2026-10-02에 `gh`로 조회한 값**입니다. 시간이 지나면 달라집니다.
> 통째로 설치하지 않고 **양식·구조·사고방식만 빌려 옵니다.**
>
> - **반영함** = 이 틀의 파일에 실제로 들어간 것
> - **참고만** = 읽고 판단했지만 파일에는 넣지 않은 것 (필요해지면 그때 반영)

## 문서·기획 양식

| 레포 | ⭐ | 상태 | 내용 |
|---|---|---|---|
| [evildmp/diataxis-documentation-framework](https://github.com/evildmp/diataxis-documentation-framework) | 1,243 | **반영함** | 문서를 how-to / reference / explanation으로 나누는 기준 → `type` 라벨과 `guides/`·`reference/` 분리 ([CONVENTIONS](CONVENTIONS.md) 2·3장) |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 70,905 | **반영함** (개념만) | 현재 동작과 변경 제안을 구분하는 생각 → `status: Current / Draft / Historical`. CLI·도구는 쓰지 않음 |
| [adr/madr](https://github.com/adr/madr) · [ADR 모음](https://github.com/architecture-decision-record/architecture-decision-record) | 2,530 · 17,076 | **반영함** (규칙만) | 번호 재사용 금지, 상태 `대체됨` 관리 → [docs/adr/README.md](adr/README.md). ADR 양식 자체는 기존 양식에 같은 항목(상태·검토한 대안·영향)이 이미 있어 바꾸지 않음 |
| [github/spec-kit](https://github.com/github/spec-kit) | 139,774 | 참고만 | 기능 스펙의 우선순위 시나리오 + Given/When/Then, plan 양식. `templates/FEATURE.md`에는 아직 넣지 않음. 슬래시 명령·tasks 파일은 쓰지 않음(작업은 Linear) |
| [arc42/arc42-template](https://github.com/arc42/arc42-template) | 1,302 | 참고만 | 아키텍처 문서에 빠진 항목(품질 요구, 리스크, 배포 뷰) 점검 용도. `docs/ARCHITECTURE.md`에는 아직 넣지 않음 |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 53,721 | 참고만 | 기존 프로젝트 도입 방식(`docs/existing-codebases`). 다중 에이전트 역할 체계는 1인 개발에 과해서 쓰지 않음 |

## 폴더 구조

| 레포 | ⭐ | 상태 | 내용 |
|---|---|---|---|
| [saleor/saleor](https://github.com/saleor/saleor) | 23,398 | **반영함** | 업무 도메인 하나 = 폴더 하나, 도메인마다 같은 역할 이름 → [src/backend/README.md](../src/backend/README.md), CONVENTIONS 4장 |
| [zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices) | 18,135 | **반영함** | 도메인별 폴더와 파일 역할 규칙 (위와 같은 방향) |
| [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | 45,840 | **반영함** | `backend` / `frontend` 분리, `scripts/`, `.claude/` → `src/` 구조 |
| [cookiecutter/cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) | 13,613 | **반영함** | 설정을 환경별로 분리(`base/local/production/test`), `docs/guides`를 읽는 순서로 번호 |
| [PostHog/posthog](https://github.com/PostHog/posthog) | 40,096 | 참고만 | 문서를 독자·수명으로 나누는 방식(`internal` `onboarding` `plans` `published`) |
| [getsentry/sentry](https://github.com/getsentry/sentry) | 44,912 | 참고만 | 큰 코드베이스의 개발 환경·스크립트 분리 |
| [kubernetes/enhancements](https://github.com/kubernetes/enhancements) | 3,964 | 참고만 | 기능 기획 문서(`keps/`)의 번호·템플릿·상태 관리 |

## 이 틀의 원본·작업 방식

| 레포 | ⭐ | 상태 | 내용 |
|---|---|---|---|
| [gggmlduswjs/harness_framework](https://github.com/gggmlduswjs/harness_framework) | 1 | **반영함** | 강의 원본 하네스 (이 틀의 출발점) |
| [obra/superpowers](https://github.com/obra/superpowers) | 294,176 | **반영함** | 설계 → 계획 → 구현 → 리뷰 흐름. 저장 위치 지정, `.superpowers/` 제외 → [CLAUDE.md](../CLAUDE.md) |

## 고르는 기준

- **큰 프로젝트가 직접 관리하거나 최근에도 push가 있는** 레포를 우선합니다. 개인이 만든 템플릿 레포는 별 수가 많아도 방치된 경우가 많습니다(예: 마지막 push가 몇 년 전인 Django+Vue 템플릿).
- 도입이 아니라 **참고**합니다. 겹치는 체계를 통째로 들이면 정본이 하나 더 생깁니다.
