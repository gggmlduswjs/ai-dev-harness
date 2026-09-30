# AI Dev Harness

AI와 함께 개발할 때 **문서·연구·계획·Harness·검증을 일관된 방식으로 관리하기 위한 공통 프로젝트 템플릿**입니다.

이 저장소는 `gggmlduswjs/harness_framework`의 핵심 철학을 실전 프로젝트에 맞게 단순화·확장한 표준입니다.

## Core loop

```text
Linear Issue
    ↓
Repository Context
    ↓
필요하면 Research
    ↓
필요하면 Plan
    ↓
Claude / Codex
    ↓
Code
    ↓
Test / Verification
    ↓
GitHub PR / CI
    ↓
Merge
    ↓
Linear Done
```

## Responsibilities

| System | Responsibility |
|---|---|
| Linear | Project / Milestone / Issue / Status / Priority / Target |
| Repository | Product / Technical knowledge |
| GitHub | Commit / PR / CI / Merge / Release evidence |
| Obsidian | Personal notes / learning / exploratory research |

## Project contract

```text
PROJECT/
├── CLAUDE.md
├── AGENTS.md
├── docs/
│   ├── PRD.md
│   ├── ROADMAP.md
│   ├── ARCHITECTURE.md
│   ├── ADR.md
│   └── UI_GUIDE.md
├── .dev/
│   ├── research/
│   └── plans/
├── .claude/          # add rules/skills/agents/hooks only when justified
├── src/
├── tests/
└── .github/
```

The five top-level documents under `docs/` are the default entry points. Larger projects may add `domains/`, `features/`, `architecture/`, `adr/`, and `reference/` only when needed.

## Rules

1. **Linear is the execution-status SSOT.** Do not duplicate current status, priority, deadlines, or backlog in repository docs.
2. **Repository docs are the product/technical SSOT.**
3. **Research is optional.** Create it only when an important decision requires information you do not yet know.
4. **Plans are optional.** Create them only for complex, multi-layer, multi-day, or high-risk implementation.
5. **Harness grows from real repeated problems.** Do not create rules, skills, hooks, agents, or evals just to fill folders.
6. **AI completion claims are not evidence.** Tests, CI, external re-query, runtime evidence, or human review establish completion as appropriate.
7. **Do not reintroduce phase/step/execute.py orchestration by default.** Linear + plans + agents + GitHub delivery are the default orchestration layer.

## Templates

- Product: `docs/PRD.md`
- Roadmap: `docs/ROADMAP.md`
- Architecture: `docs/ARCHITECTURE.md`
- Decisions: `docs/ADR.md`
- UI: `docs/UI_GUIDE.md`
- Research: `.dev/research/TEMPLATE.md`
- Implementation plan: `.dev/plans/TEMPLATE.md`
- Domain: `templates/DOMAIN.md`
- Feature: `templates/FEATURE.md`
- Linear issue: `templates/LINEAR_ISSUE.md`
- Pull request: `.github/PULL_REQUEST_TEMPLATE.md`

## Scaling rule

Start small. The template is a contract, not a requirement to create every possible folder. Add structure only when the project has enough complexity to justify it.
