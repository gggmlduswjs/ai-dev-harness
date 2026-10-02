---
type: guide
status: Draft
owner-of: 설치된 스킬·플러그인을 언제, 어떤 상황에서, 어떤 주기로 쓰는가
---

# 3. 어떤 스킬을 언제 쓰나

> **목적:** `bootstrap.ps1`로 설치한 스킬이 많아서, **상황별로 무엇을 부르고 얼마나 자주 돌리는지**를 한곳에 정합니다.
> **상태:** Draft — 주기는 권장 기본값이며, 써 보고 맞게 고칩니다. 스킬 목록은 [gg-tools](https://github.com/gggmlduswjs/gg-tools)의 `plugins.json`이 정본입니다.

## 1. 기본 원칙

- **한 요청에 스킬 하나.** 같은 일을 하는 스킬을 여러 개 부르지 않습니다. 헷갈리면 Claude에게 "ask-gg" 또는 "어떤 스킬 써야 해?"라고 묻습니다.
- **대부분은 말만 하면 자동으로 골라집니다.** 스킬 이름을 외우지 않아도 됩니다. 이름을 불러야 하는 경우는 아래 표의 "직접 부르기"입니다.
- **무거운 점검은 정해진 시점에만** 돌립니다(PR 전, 주간, 배포 전). 매 작업마다 돌리면 시간과 토큰만 듭니다.

## 2. 항상 켜져 있는 것 (따로 부르지 않음)

| 이름 | 하는 일 |
|---|---|
| `ponytail` | 가장 단순한 해법을 우선하게 만듦(없는 기능을 만들지 않음) |
| `claude-mem` | 세션이 바뀌어도 맥락을 이어 가는 기억 |
| `headroom` | 시작 시 걸리는 hook |
| 위험 명령 차단 hook | 프로젝트의 `.claude/hooks/guardrail.py`가 위험한 명령을 막음 |
| 상태줄 `ccstatusline` | 화면 아래에 컨텍스트 사용량 등을 표시 |

## 3. 상황별로 무엇을 쓰나

### 개발 흐름 (매 작업)

| 상황 | 말하는 법 | 쓰는 스킬 | 주기 |
|---|---|---|---|
| 새 기능·아이디어를 정리 | "이 기능 설계하자" | `brainstorming` (Superpowers) | 기능마다 1번 |
| 계획 구멍 찾기 | "내 계획 grill해줘" | `grill-me` | 계획서 승인 전, 큰 결정마다 |
| 계획서 작성 | "계획서 써줘" | `writing-plans` | 설계 승인 뒤 1번 |
| 구현 | "계획대로 구현해줘" | `executing-plans` 또는 `subagent-driven-development` | 계획서마다 |
| 테스트 먼저 | (구현 중 자동) | `test-driven-development` | 구현마다 |
| 버그 원인 찾기 | "왜 안 되는지 찾아줘" | `systematic-debugging` | 버그 발생 때 |
| 완료 주장 전 확인 | (자동) | `verification-before-completion` | 완료 직전 |
| 도메인 용어·모델 정리 | "도메인 모델링 하자" | `domain-modeling`, `grilling` (mattpocock) | 새 도메인이 생길 때 |
| 기존 운영 기능을 바꿀 때 | "기존 시스템 영향 조사부터" | `existing-system-modernization` | 운영 중인 기능 변경 때마다 |

### 마무리·리뷰 (PR마다)

| 상황 | 쓰는 스킬 | 주기 |
|---|---|---|
| 코드 리뷰 | 내장 `/code-review`, `requesting-code-review` | **PR마다** |
| 커밋 전 보안 확인 | 내장 `/security-review` | 인증·결제·개인정보를 건드린 PR마다 |
| 변경분 상세 보안 리뷰 | `differential-review` (Trail of Bits) | 위험도 높은 PR |
| 기본값이 불안한 설정 | `insecure-defaults` | 설정·배포 파일을 바꿀 때 |
| 브랜치 마무리 | `finishing-a-development-branch` | 기능 끝날 때 |
| 코드를 더 단순하게 | `code-simplification` (agent-skills) | 기능이 끝난 뒤 필요할 때 |

### 점검 (주기적으로)

| 점검 | 스킬 | 권장 주기 |
|---|---|---|
| 프로덕션 준비 종합(성능·보안·데이터·관측성) | `production-readiness-5axis` | 배포 전, 분기마다 |
| 레포 전체 보안 | `owasp-security-scan` | 배포 전, 월 1회 |
| 공급망·의존성 위험 | `supply-chain-risk-auditor` | 의존성을 크게 바꿀 때, 월 1회 |
| 정적 분석(CodeQL·Semgrep) | `static-analysis` 플러그인, 같은 유형 탐색은 `variant-analysis` | 보안 이슈를 하나 찾았을 때 같은 유형 탐색 |
| 성능(웹 지표) | `lighthouse-performance-loop` | 화면을 크게 바꾼 뒤, 배포 전 |
| 에러·분석·SEO | `observability-posthog-seo` | 출시 전, 분기마다 |
| DB 진단(Supabase) | `supabase-db-advisor-readonly` | 마이그레이션 뒤, 월 1회 |
| AI가 코드를 읽기 좋은지 점수 | `ai-readiness-cartography` | 월 1회, 구조를 크게 바꾼 뒤 |
| 토큰·비용 낭비 | `improve-token-efficiency` | 월 1회 |
| 스킬·CLAUDE.md 회귀 | `harness-eval` | 스킬·규칙을 고친 뒤 |
| 스킬 평가 | `eval-writer`, `skill-evaluator` | 새 스킬을 만들었을 때 |

### 화면·문서·기타

| 상황 | 스킬 |
|---|---|
| 화면 디자인 | `ui-ux-pro-max`, `refactoring-ui` |
| 실제 브라우저로 확인·자동화 | `dev-browser`, `browser-testing-with-devtools` |
| docx·pdf·pptx·xlsx 만들기·읽기 | `document-skills` |
| Claude API로 앱 개발 | `claude-api` |
| 기능 기획 문서 묶음(PRD·유저플로우 등) | `product-spec-kit` |
| CI/CD·API 설계·마이그레이션·ADR | `agent-skills`(addyosmani)의 해당 스킬 |
| 다른 모델에게 두 번째 의견 | `codex` |
| 위키에 넣기·묻기·점검 | `wiki-ingest` · `wiki-query` · `wiki-lint` (`second-brain`에서만) |
| 옵시디언 노트 다루기 | `obsidian` |
| 작업 중 반복되는 패턴·교정을 관찰해 스킬 후보로 기록(작업 폴더에 관찰 파일을 씀) | `task-observer` |

## 4. 하루·주·월 루틴 (권장)

| 주기 | 할 일 |
|---|---|
| **매 작업** | 설계 → 계획서 → 구현(TDD) → 검증. 새 세션은 한 작업만 |
| **매 PR** | 코드 리뷰 + (위험하면) 보안 리뷰. 머지는 내가 승인 |
| **저녁(5분)** | 한 일·못한 일·개선점을 `second-brain`에 기록 |
| **주 1회(30분)** | 열린 PR·Linear **증거 대기** 확인, 반복된 실수를 규칙·스킬로 올릴지 결정 |
| **월 1회** | `owasp-security-scan`, `improve-token-efficiency`, `ai-readiness-cartography`, `supply-chain-risk-auditor` |
| **배포 전** | `production-readiness-5axis` + 보안 점검 + `lighthouse-performance-loop` |
| **스킬·규칙을 바꾼 뒤** | `harness-eval`로 회귀 확인 |

"같은 일을 3번 시키게 되면 스킬로, 같은 실수를 3번 하면 규칙(`CLAUDE.md`)으로" 올립니다.

## 5. 스킬이 너무 많다고 느껴질 때

- 스킬 설명은 매 세션 컨텍스트에 올라갑니다. **안 쓰는 플러그인은 `plugins.json`에서 빼고** `bootstrap`을 다시 돌리면 됩니다.
- Cybersecurity Skills 818개는 일부러 기본 설치에서 뺐습니다. 필요할 때만 설치합니다.
- 컨텍스트가 길어졌다면 새 세션을 열거나 `/compact`를 합니다([2-daily-loop-and-second-brain.md](2-daily-loop-and-second-brain.md) 5장).
