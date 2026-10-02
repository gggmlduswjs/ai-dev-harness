---
type: reference
status: Draft
owner-of: 프로젝트 위키(_brain/)의 구조·작성 규칙
---

# 프로젝트 위키 규칙

> **시험적 기능입니다.** Karpathy의 LLM Wiki 아이디어를 프로젝트 안에 적용한 새 패턴이며 표준 관행이 아닙니다. 필요 없으면 이 폴더를 통째로 지워도 됩니다(`CLAUDE.md`의 포인터 한 줄도 같이). 개인 브레인과의 역할 구분은 [2-daily-loop-and-second-brain.md](../docs/guides/2-daily-loop-and-second-brain.md) 4장.

> **팀 단위 권장 패턴:** brain 을 코드와 같은 repo·같은 PR 리뷰 흐름에 둔다. 새 결정이 생기면 그 PR 에 `_brain` 노드를 같이 올린다.

이 위키는 **이 프로젝트 전용** 배경 지식(결정 이유, 도메인 규칙, 장애 회고, 슬랙·회의록 정리)을 둡니다. 프로젝트 레포 안에 있으므로 에이전트가 여기서 일할 때 자동으로 읽습니다. 여러 프로젝트에서 쓰는 일반 지식은 개인 브레인(`~/second-brain`)으로 보냅니다.

## 구조

```text
_brain/
  WIKI_SCHEMA.md       이 파일. 규칙
  raw/                 원문. 사람이 넣고 수정하지 않는다. git에 올라가지 않는다(.gitignore)
  wiki/
    index.md           카탈로그. 페이지마다 한 줄 요약
    log.md             추가만 하는 기록. [SETUP] [INGEST] [QUERY] [LINT] [MOVE]
    concepts/          개념·도메인 규칙·결정 이유·장애 회고
    people/            사람·팀·외부 조직(역할만, 개인정보 제외)
    tools/             이 프로젝트가 쓰는 도구·서비스
    sources/           출처 요약. 원본 한 건당 한 페이지
```

`wiki-ingest` 등 스킬은 wiki-template 구조(`raw/` 와 `wiki/` 2층)를 기준으로 하므로 `_brain/` 안에서도 `raw/` 와 `wiki/` 2층을 유지합니다. 평평하게 합치지 않습니다.

## 정본 링크 규칙 (가장 중요)

- Spec·ADR·PRD·Linear에 **이미 있는 내용은 복사하지 않고 링크만** 합니다. 위키는 "왜 그렇게 됐는지 맥락"을 담고, 정본은 정본 자리에 둡니다.
- 위키 내용이 정본과 다르면 정본이 맞습니다. 충돌은 해당 페이지 `## 모순/주의`에 적고 사람이 정합니다.
- 진행·우선순위·일정은 쓰지 않습니다(Linear).
- 위키에서 오래 유효한 사실이 굳으면 `docs/`의 정본으로 올리고 위키에는 링크만 남깁니다([CONVENTIONS](../docs/CONVENTIONS.md) 6장).

## 민감 정보 금지

- 개인정보, 인증정보(키·토큰·비밀번호), 고객 데이터, 인사·보안 사고 내용은 **위키에도 `raw/`에도** 넣지 않습니다.
- `raw/`는 `.gitignore`로 git 이력에서 제외하고 `_brain/wiki/` 쪽(`index.md`, 각 페이지)만 커밋합니다. 그래도 `raw/`에 비밀을 둘 이유는 없습니다.
- 슬랙·회의록은 이름·연락처·금액·계정을 지운 요약만 위키로 옮깁니다.

## 작성 규칙

- 분류 하위 폴더(adr/meeting 등)는 미리 만들지 않습니다. raw 가 쌓이면 ingest 가 필요한 분류를 만듭니다.
- 한국어. 파일명은 `kebab-case.md`, 한 파일 = 한 주제.
- 다른 페이지는 `[[파일명]]`으로 연결합니다.
- 원본에 없는 사실을 확정적으로 쓰지 않습니다. 추측은 "(추론)"으로 표시합니다.
- 충돌하거나 낡은 정보는 지우지 않고 `## 모순/주의`에 출처와 함께 표시합니다.
- 슬랙·회의록은 **의사결정이 있었던 스레드만** 골라 5~10개로 시작합니다. 채널 통째로 넣지 않습니다.

## 프론트매터

```yaml
---
type: concept            # concept | person | tool | source
title: 문서 제목
status: stub             # stub → draft → solid
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/원본파일.md]
---
```

본문 틀: 한 줄 정의 → 핵심 내용 → 모순/주의(있을 때) → 정본 링크 → 관련 페이지.

## 동작

- **Ingest:** 원본 한 건을 읽고 핵심을 말한 뒤 `wiki/sources/`에 요약 페이지를 만들고, 관련 페이지를 병합하거나 새로 만들고, `wiki/index.md`·`wiki/log.md`를 갱신합니다. 한 번에 한 건, 사람이 확인하며 진행합니다.
- **Query:** `wiki/index.md`에서 관련 페이지를 찾아 `[[페이지]]`를 인용해 답합니다. 없으면 "위키에 아직 없음"이라고 말합니다.
- **Lint:** 모순, 고아 페이지, 깨진 링크, index에 없는 페이지, 방치된 stub을 목록으로 보고합니다. 고치기 전에 승인을 받습니다.
- 삭제·이동은 사람이 승인합니다. 자동 삭제는 하지 않습니다.

위 동작은 개인 브레인용 `wiki-ingest`·`wiki-query`·`wiki-lint` 스킬이 같은 구조로 수행할 수 있습니다(스킬 위치는 `docs/guides/2-daily-loop-and-second-brain.md` 3장).
