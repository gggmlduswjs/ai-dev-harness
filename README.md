# AI 개발 하네스

AI(Claude Code · Codex)에게 일을 맡길 때 쓰는 프로젝트 시작 틀이다. 처음 만들 때도 유지보수할 때도 **같은 파일, 같은 흐름**을 쓴다.

## 바닥 3층

AI 는 대화가 끝나면 잊고, 적어 둔 지시는 빠지고, 「됐다」는 말은 증거가 아니다. 그래서 세 가지를 파일로 둔다.

| 층 | 무엇으로 | 왜 |
|---|---|---|
| **기억** | `CLAUDE.md`(규칙 5개) + `notes/`(progress · requests · decisions) | 새 대화가 파일만 읽고 하던 일을 이어 간다 |
| **권한** | `.claude/settings.json` deny · allow | 「읽지 마라」라고 적는 것과 권한으로 막는 것은 다르다 |
| **검증** | `work/<일>/acceptance.md`(합격선) + `plan.md`(「금지할 변경」 칸) | 코드를 고친 것과 사람이 결과를 본 것은 다르다 |

훅 두 개가 바닥을 받친다. 세션 시작 때 `progress.md` 를 대화에 싣고(`session_start.py`), 코드만 바뀌고 `progress.md` 가 그대로면 멈추기 전에 갱신을 요청한다(`stop_check.py`).

**합격 시험:** `/clear` 뒤 새 대화에 「하던 일 · 다음 할 일」을 물었을 때 파일만으로 맞게 답한다.

## 폴더

```text
PROJECT/
├── CLAUDE.md            목적 · 파일 안내 / 확인 방법 / 작업 규칙 5 / 안전 / 「구조 바꾸지 않는다」
├── AGENTS.md            Codex 차이만
├── .claude/             settings.json(권한 · 훅) · hooks/(session_start · stop_check)
├── notes/               progress(순서 · 지금 · 다음) · requests(요청 원문) · decisions(무엇을 왜)
├── work/                일 하나 = 폴더 하나(acceptance · plan). 양식은 work/_양식/
├── briefs/              받은 자료 원본 — 고치지 않는다
├── docs/                오래 가는 설명만: PRD · DOMAIN(업무 규칙) · ARCHITECTURE · UI_GUIDE
└── .github/             PR 양식
```

진행 상태는 `notes/progress.md` 한 곳. `docs/` 에는 쓰지 않는다.

## 처음 개발

1. 이 레포를 템플릿으로 새 레포를 만들고 `CLAUDE.md` 의 `{ }` 를 채운다.
2. `docs/PRD.md` → `docs/DOMAIN.md` 를 채운다. 모르는 칸은 `?` 와 확인 질문으로 남긴다.
3. `notes/progress.md` 「순서」에 단계와 단계마다 끝나는 기준을 적는다.
4. 첫 일은 `work/_양식/` 을 `work/<번호-이름>/` 으로 복사해서 한다. **합격선을 먼저**, 그다음 계획.
5. plan mode 로 계획을 받아 검토한다(범위 · 확인 방법 · 지어낸 정보 · 금지할 변경) → 구현 → 검사 명령 → 사람 확인 → `decisions` · `progress` 갱신 → PR.

## 요청 쓰는 법

AI(또는 Codex)에게 일을 맡길 때 매번 같은 칸을 채운다.

| 칸 | 예 |
|---|---|
| 자료 | `@work/12-login/plan.md` |
| 목적 | 담당자가 무엇을 하려고 쓰나 |
| 바꿀 곳 · 그대로 둘 곳 | 「조건만 고치고 나머지는 그대로」 · 「새 함수는 만들지 마」 |
| 기대값 | 사람이 정해 박는다. 「기대값은 바꾸지 마」 |
| 실패하면 | 「멈춘 단계와 다음 조치만 말해. 임의로 고치지 마」 |
| 기록 시점 | 「기록 · 커밋은 내가 확인한 뒤에」 — 커밋 전에 notes 를 실제 결과와 대조한다 |

## 유지보수

- 요청이 오면 `notes/requests.md` 에 한 줄. 작은 일은 바로 고치고 `progress` 에 한 줄, 큰 일(돈 · DB · 여러 날)은 `work/` 폴더.
- 같은 실수가 두 번 나오면 **하나만 더한다**: `CLAUDE.md` 규칙 한 줄 · `settings.json` deny 한 줄 · 훅 하나.
- 끝난 `work/` 폴더는 남길 결정을 `decisions` 로 옮기고 지운다(git 이력에 남는다).
- **구조는 바꾸지 않는다.** 새 강의 · 새 도구를 배워도 위 「더하기」로만 넣는다. 구조를 바꿔야 하면 `decisions` 에 이유를 적고 승인받는다.

## 출처

- 바닥 3층 · 작업 규칙 5개 · notes · 합격선 · 「금지할 변경」: 송태영 「문제 정의부터 해결까지, AI Agent 로 끝내는 FDE 실무」 2~3장(moreon-lab 실습)
- 업무 규칙 표(표 한 줄 = 테스트 하나) · UI 가이드 8칸: [jha0313/harness_framework](https://github.com/jha0313/harness_framework), 김민태 강의
