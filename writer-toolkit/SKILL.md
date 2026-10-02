---
name: writer-toolkit
version: "0.3"
schema-version: "0.3"
bootstrap-version: "0.3"
description: Model-independent literary production system for author-controlled writing, development, persistence, revision, auditing, and handoff.
---

# WRITER-TOOLKIT v0.3

This file is the Native Skill entrypoint/router.

## Startup
1. Execute `BOOTSTRAP.md`.
2. Determine NEW CHAT or NEW MODEL.
3. Load persisted manuscript/state.
4. Load only active modules.
5. Restore Style Baseline/Lock.
6. Check current capabilities.
7. Identify blockers and the next authorized action.

## Load order
```
core/
intake/
form/
prose/
development/
production/
revision/
audits/
conditional/   (only active modules)
adapters/
schemas/
templates/
reference/
tests/         (only for testing/validation work)
```

## Non-negotiable runtime rules
- AI supports the author; it does not own irreversible artistic decisions.
- `DERIVED` does not mean accepted.
- `DEFERRED` is not permission.
- `AI MAY PROCEED` is not `AUTHOR APPROVAL`.
- Audit is read-only.
- Revision is a separate manuscript-changing operation.
- Runtime limits must not silently redefine literary form.
- Unavailable capability is not fabricated PASS.
- Full-manuscript audit requires explicit coverage.

## Canonical source
`reference/WRITER-TOOLKIT_v0.3_ARCHITECTURE_SPEC.md`
`reference/WRITER-TOOLKIT_v0.3_BUILD_SPEC.md`

## Form routing
Every project must establish `FORM.CONTRACT_READY` before standard production.

Screenplay projects activate `FORM.03_SCREENPLAY_PROFILE`; prose projects do not inherit screenplay-only rules.
