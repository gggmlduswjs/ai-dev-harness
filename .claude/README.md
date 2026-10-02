# .claude/ — AI 규칙·스킬·에이전트·훅

**반복된 실수나 위험이 실제로 있을 때만** 채웁니다. 폴더를 채우려고 만들지 않습니다.

```text
.claude/
├── agents/    역할이 정해진 서브에이전트 (예: executor, investigator)
├── rules/     항상 지킬 규칙
├── skills/    반복 작업 절차
└── hooks/     자동 검사
```

## 외부 스킬 설치 — refactoring-ui (화면이 있는 프로젝트)

[s0xDk/refactoring-ui-skill](https://github.com/s0xDk/refactoring-ui-skill) (MIT)은 책 *Refactoring UI*의 규칙을 담은 스킬입니다. **파일을 복사해 넣지 않고** git으로 설치해야 업데이트를 추적할 수 있습니다. **폴더 이름은 반드시 `refactoring-ui`**여야 합니다(스킬 이름과 맞춤).

```sh
# 이 프로젝트에만 (팀과 공유) — 권장
git submodule add https://github.com/s0xDk/refactoring-ui-skill.git .claude/skills/refactoring-ui

# 모든 프로젝트에서 (개인)
git clone https://github.com/s0xDk/refactoring-ui-skill.git ~/.claude/skills/refactoring-ui
```

설치 후 **새 세션**을 시작해야 스킬이 로드됩니다. UI를 만들거나 고칠 때 자동으로 쓰이고, `/refactoring-ui …`로 직접 부를 수도 있습니다.
스킬에 들어 있는 `assets/tokens.css`는 시작용 토큰이므로, 프로젝트의 토큰 파일에 **값을 옮겨 쓰고** Element Plus 변수와 맞춥니다.

