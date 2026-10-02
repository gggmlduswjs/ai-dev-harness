# templates/ — 여러 번 복사해서 쓰는 양식

> **기준:** 한 번만 쓰는 핵심 문서(PRD·ROADMAP·ARCHITECTURE·ADR 목록·UI_GUIDE)는 `docs/`에 **채우는 틀로 이미 있습니다.**
> 같은 종류를 **여러 번** 만드는 문서의 양식만 여기에 둡니다. 양식은 이 폴더 한 곳에서만 관리합니다.

| 양식 | 언제 | 복사해서 둘 곳 | type |
|---|---|---|---|
| [FEATURE.md](FEATURE.md) | 새 기능의 목표·범위·완료 조건을 정할 때 | `docs/features/기능명.md` | spec |
| [DOMAIN.md](DOMAIN.md) | 업무 영역의 규칙이 PRD에 담기 어려워질 때 | `docs/domains/영역명.md` | reference |
| [ADR.md](ADR.md) | 중요한 설계·기술 결정을 남길 때 | `docs/adr/NNNN-제목.md` (+ `docs/ADR.md` 표에 한 줄) | decision |
| [RESEARCH.md](RESEARCH.md) | 중요한 것을 모를 때 | `.dev/research/주제.md` | research |
| [PLAN.md](PLAN.md) | 복잡하거나 위험한 구현 전에 | `.dev/plans/작업명.md` | plan |
| [LINEAR_ISSUE.md](LINEAR_ISSUE.md) | Linear 작업을 만들 때 | Linear (파일로 두지 않음) | — |

**PR 양식**은 GitHub가 정해진 위치만 읽으므로 [`.github/PULL_REQUEST_TEMPLATE.md`](../.github/PULL_REQUEST_TEMPLATE.md)에 있습니다.

복사한 뒤 맨 위 라벨(`type / status / owner-of / linear`)을 채웁니다. 규칙은 [docs/CONVENTIONS.md](../docs/CONVENTIONS.md)입니다.
