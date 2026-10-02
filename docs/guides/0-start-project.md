---
type: guide
status: Current
owner-of: 새 프로젝트를 아이디어에서 첫 기능 개발까지 시작하는 순서
---

# 0. 새 프로젝트 시작하기

> **목적:** 아이디어 한 줄에서 첫 기능 개발까지의 순서입니다. 순서대로 따라 하면 `docs/`의 핵심 문서가 채워지고 Linear가 준비됩니다.
> **전부 다 채우지 않아도 됩니다.** 작은 프로젝트는 PRD · ARCHITECTURE · ADR · UI_GUIDE만으로 시작하고, 커질 때 `domains/`, `features/`를 추가합니다.

```text
0 아이디어 → 1 틀 복사 → 2 PRD → 3 업무 영역 → 4 ROADMAP → 5 ARCHITECTURE+ADR → 6 UI_GUIDE → 7 Linear → 8 첫 기능
```

★ = 사람이 정하거나 승인하는 지점입니다. 승인 전에는 코드를 쓰지 않습니다.

## 0. 아이디어 한 줄

"누가 어떤 문제를 겪어서 무엇을 만들고 싶다"를 한 줄로 적습니다. 이 한 줄이 2단계 PRD의 출발점입니다.

## 1. 틀 복사

1. 이 저장소를 새 프로젝트 폴더로 복사합니다(clone 후 `.git`을 새로 시작하거나 GitHub의 「Use this template」).
2. 루트 `CLAUDE.md`의 **운영 안전** 항목을 프로젝트에 맞게 채웁니다 — AI가 절대 하면 안 되는 일(운영 데이터 쓰기, 배포, 삭제 등)과 허용 조건을 정합니다.
3. `README.md`를 프로젝트 소개로 바꿉니다.

## 2. PRD — 무엇을, 왜 ★

`docs/PRD.md`를 채웁니다. 가장 오래 다듬을 문서입니다. 아래가 맞아야 이후 단계가 맞습니다.

- 한 줄 정의 · 해결하려는 문제 · 사용자와 관계자 · 제품 목표
- **만들지 않을 것(비목표)** — 범위를 지키는 가장 강한 장치입니다
- 전체 기능 지도 · 핵심 업무 영역 · 대표 업무 흐름 · 범위

AI와 하는 법: `brainstorming`이 질문을 **하나씩** 던지고 접근법을 비교해 줍니다. 답하고, 초안을 고치고, 승인합니다.

## 3. 업무 영역 (필요할 때만)

PRD에 담기 어려운 업무 규칙이 있을 때 [`templates/DOMAIN.md`](../../templates/DOMAIN.md)를 `docs/domains/영역명.md`로 복사해 채웁니다. 영역 이름은 나중에 코드의 도메인 폴더 이름과 **같게** 씁니다.

## 4. ROADMAP — 어떤 순서로 ★

`docs/ROADMAP.md`에 장기 목표(North Star)와 단계별(1·2·3단계)로 **기대 결과 · 포함 범위 · 완료 기준 · 다음 단계로 넘어가는 조건**을 적습니다. 진행 상태와 일정은 쓰지 않습니다(Linear).

## 5. ARCHITECTURE + ADR — 어떤 구조로, 왜 ★

- `docs/ARCHITECTURE.md`: 시스템 개요, 책임 경계(책임지는 것/지지 않는 것), 구성요소, 데이터 흐름, 폴더 지도.
- 기술을 고를 때마다 [`templates/ADR.md`](../../templates/ADR.md)를 `docs/adr/NNNN-제목.md`로 복사해 **왜 골랐는지**를 남기고, `docs/ADR.md` 표에 한 줄을 추가합니다.
- 시작 시점의 ARCHITECTURE는 계획한 구조이므로 `status: Draft`로 두고, 구현되면 `Current`로 바꿉니다.
- 코드 폴더는 `src/backend/<domain>/`, `src/frontend/` 규칙을 따릅니다([CONVENTIONS](../CONVENTIONS.md) 4장).

## 6. UI_GUIDE (화면이 있을 때)

`docs/UI_GUIDE.md`에 디자인 원칙, 레이아웃, 색·글꼴 토큰, 공통 컴포넌트, 접근성을 정합니다. 화면 구현 세부는 코드가 정본이므로 문서에 복제하지 않습니다.

## 7. Linear 준비

| Linear | 이 틀의 대응 |
|---|---|
| Project | 제품(PRD) |
| Milestone | ROADMAP의 단계 하나 |
| Issue | 작업 하나 — [`templates/LINEAR_ISSUE.md`](../../templates/LINEAR_ISSUE.md) |

긴 문서는 Linear에 복사하지 않고 **저장소 경로를 링크**합니다.

## 8. 첫 기능

이제부터는 일상 개발 루프입니다.

```text
Linear 이슈 → (모르면 조사) → brainstorming 설계서 → writing-plans 계획서 → 구현(테스트 먼저) → 검증 → PR → 승인된 머지 → 정본으로 승격 → Linear Done
```

- 설계서는 `docs/features/`, 계획서는 `.dev/plans/`에 저장됩니다(`CLAUDE.md`의 「superpowers 저장 위치」).
- 작은 버그·수정은 설계서·계획서 없이 구현 → 검증 → PR로 갑니다.
- 작업이 끝나면 [CONVENTIONS](../CONVENTIONS.md) 6장대로 정본에 반영합니다.

## 시작 체크리스트

- [ ] `CLAUDE.md` 운영 안전 항목을 채웠다
- [ ] PRD에 **비목표**까지 적고 승인했다
- [ ] ROADMAP 1단계의 **완료 기준**이 있다
- [ ] 고른 기술마다 ADR이 있다
- [ ] Linear에 Project · Milestone이 있고 문서는 링크로만 연결했다
