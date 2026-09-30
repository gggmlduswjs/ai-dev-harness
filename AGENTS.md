# Agent Guidance

Read `CLAUDE.md` first. This file adds only agent-specific guidance and must not duplicate the entire project context.

## Agent behavior

- Inspect existing canonical context before creating new documentation.
- Prefer updating an existing canonical source over creating a competing document.
- Keep research findings, product decisions, implementation plans, and production truth distinct.
- Use the smallest workflow that safely fits the task.
- Verify work with evidence appropriate to the risk.
- Surface conflicts between docs, code, and runtime state instead of silently choosing one.
- Do not create new management frameworks, registries, status systems, or ID namespaces unless explicitly required.

## Context discipline

For a task, load only the relevant product/domain/feature/architecture/decision context. Historical and archived material is reference-only unless the task specifically needs it.

## Completion

Report separately when relevant:

- research complete
- implementation complete
- tested
- merged
- deployed
- verified
- operating

Do not collapse these into a single ambiguous "done".
