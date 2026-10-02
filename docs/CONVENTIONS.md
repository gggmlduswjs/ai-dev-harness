---
type: guide
status: Current
owner-of: 문서·폴더를 어떻게 정리하는가 (규칙)
---

# 문서·폴더 규칙

> **목적:** 프로젝트가 커져도 "어디에 뭐가 있는지"를 잃지 않게 하는 최소 규칙입니다. 새 틀을 얹는 것이 아니라 **같은 규칙을 계속 지키는 것**이 목적입니다.

## 1. 정본은 하나

- 하나의 주제에는 **정본 문서가 하나**입니다. 같은 내용이 두 곳이면 하나는 지우거나 `docs/_archive/`로 옮깁니다.
- 포인터 문서("자세한 건 여기")는 **한 번까지만** 허용하고, 포인터만 남은 문서는 일정 기간 뒤에 삭제합니다.
- 결정 기록은 프로젝트에서 **한 곳**(`docs/ADR.md` + `docs/adr/`)입니다.
- 실행 상태(진행·우선순위·일정)는 문서에 쓰지 않습니다 → Linear.
- 계산·동작의 정본은 **코드**입니다. 문서에 코드를 복제하지 않고 코드 위치를 가리킵니다.

## 2. 문서마다 라벨 4줄

모든 문서의 맨 위에 둡니다(양식 파일에 이미 들어 있습니다).

```yaml
---
type: product | architecture | decision | spec | plan | research | guide | reference
status: Current | Draft | Historical
owner-of: <이 문서가 정본인 주제 한 줄>
linear: <관련 Issue 링크, 없으면 생략>
---
```

| type | 독자가 하려는 것 | 예 | Diátaxis 대응 |
|---|---|---|---|
| `product` | 무엇을·왜 만드는지 이해 | PRD, ROADMAP | explanation |
| `architecture` | 구조를 이해 | ARCHITECTURE | explanation |
| `decision` | 왜 그렇게 정했는지 확인 | ADR | explanation |
| `spec` | 기능이 무엇을 해야 하는지 확인 | features/* | reference |
| `plan` | 어떻게 만들지 확인 | .dev/plans/* | — |
| `research` | 근거를 확인 | .dev/research/* | explanation |
| `guide` | **따라 한다** | 세팅, 개발, 배포 | how-to |
| `reference` | **찾아본다** | 용어, 표, 규격 | reference |

- **`owner-of`가 같은 문서가 둘이면 중복입니다.** 이 한 줄로 중복을 찾습니다.
- `status`: `Current`(지금 유효) · `Draft`(미승인) · `Historical`(지난 기록 — `_archive/`로).

## 3. 문서 폴더 뼈대

처음엔 입구 5개(`PRD ROADMAP ARCHITECTURE ADR UI_GUIDE`)만 둡니다. 커지면 **필요한 폴더만** 추가합니다.

```text
docs/
├── PRD · ROADMAP · ARCHITECTURE · ADR · UI_GUIDE   입구 5개
├── adr/        개별 결정 기록
├── domains/    업무 영역
├── features/   기능 명세 (기획의 정본)
├── guides/     따라 하는 문서 — 순서가 있으면 번호
├── reference/  찾아보는 문서
└── _archive/   Historical — 일상에서 읽지 않는다
```

폴더 기준은 **주제가 아니라 용도(독자가 무엇을 하려는가)**입니다.

**양식의 자리:** 한 번만 쓰는 문서(입구 5개)는 `docs/`에 채우는 틀로 있고, 여러 번 복사해서 쓰는 양식은 `templates/` 한 곳에서만 관리합니다(`templates/README.md`).

## 4. 코드 폴더 3원칙

1. **업무(도메인) 단위로 폴더를 나눕니다.** `orders`, `inventory`처럼 업무 이름으로 하고 `utils/`, `common/`을 늘리지 않습니다.
2. **도메인 폴더 안의 역할 이름을 통일합니다.** 어느 도메인을 열어도 `models · services · api · tasks · tests`가 같은 자리에 있습니다(`src/backend/README.md`).
3. **루트에는 사람이 읽을 것만 둡니다.** 빌드·로그·백업·임시 출력은 `.artifacts/`로 모으고 git에서 제외합니다.

같은 도메인 이름을 층마다 반복하는 것(`services/orders`와 `api/orders`)은 정상입니다. 대신 **대응 관계를 도메인 `CLAUDE.md`에 한 번 적습니다.**

앱을 쪼개거나 폴더를 크게 옮기는 일은 migration·import·배포 경로에 영향이 큽니다. 문서화로 해결되는지 먼저 보고, 옮길 때는 별도 작업으로 합니다.

## 5. 규칙을 지키게 하는 법

규칙은 쓰는 것보다 **지켜지게 하는 것**이 어렵습니다. 가장 확실한 방법은 CI 검사입니다(선택).

- 라벨 4줄이 빠진 문서가 없는지
- `owner-of`가 중복되는 문서가 없는지
- 입구 문서의 링크가 끊기지 않았는지

검사는 실제로 문서가 흩어지는 문제가 생긴 뒤에 추가합니다. 처음부터 만들지 않습니다.
