# Project

This repository defines the shared AI-native development harness used as a reference/template for projects.

## Where to Look

- Product template: `docs/PRD.md`
- Roadmap template: `docs/ROADMAP.md`
- Architecture template: `docs/ARCHITECTURE.md`
- Decision template: `docs/ADR.md`
- UI guide template: `docs/UI_GUIDE.md`
- Research template: `.dev/research/TEMPLATE.md`
- Plan template: `.dev/plans/TEMPLATE.md`
- Domain / Feature / Linear templates: `templates/`

## Default Workflow

```text
Linear Issue
→ Repository Context
→ Implementation
→ Verification
→ PR / CI
→ Merge
→ Linear Done
```

Escalate only when needed:

- Important unknown → Research.
- Complex or high-risk implementation → Plan.
- Durable product truth → docs.
- Repeated AI failure/risk → rule, skill, hook, agent, or eval as appropriate.

## Critical Principles

1. Linear owns execution status.
2. Repository docs own product and technical context.
3. GitHub owns change evidence.
4. Obsidian/personal notes are not repository truth.
5. Do not create duplicate canonical sources.
6. Do not require Research, Spec, or Plan for every issue.
7. Do not treat an AI statement of completion as verification.
8. Do not add harness machinery without a demonstrated repeated need.

## Safety

Project-specific repositories must define their own safety constraints for:

- production database writes
- migrations
- money/inventory calculations
- destructive operations
- external API writes
- deployment

Do not assume this template grants permission for any of them.

## Verification

Each consuming project must define concrete commands for its stack:

- unit tests
- integration tests
- browser/E2E tests
- lint/build/type checks
- external or production verification when required

## Git / PR

Prefer small, reviewable changes. Keep documentation cleanup, feature implementation, and architecture refactors separate when practical.

## Harness

Add `.claude/rules`, `.claude/skills`, `.claude/agents`, and `.claude/hooks` only when real project needs justify them.
