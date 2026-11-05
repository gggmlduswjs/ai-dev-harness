# AGENTS.md — Codex · 다른 에이전트

`CLAUDE.md` 를 먼저 읽는다. 규칙 · 안전 · 완료 조건은 거기가 정본이다.

- `.claude/settings.json` 의 권한과 훅은 Claude Code 에서만 돈다. 세션을 시작할 때 `notes/progress.md` 를 직접 읽고, 끝날 때 직접 갱신한다.
- `.env` 읽기 금지 · force push 금지 · `git add -A` 금지는 스스로 지킨다. 막히면 우회하지 말고 보고한다.
