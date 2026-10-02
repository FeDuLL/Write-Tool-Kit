# FORM.01_CONTRACT

**ID:** `FORM.01_CONTRACT`
**Layer:** FORM
**Activation:** always at project setup/restore because every project has a declared form.

## PURPOSE

Translate the project `FORM` into an operational contract without imposing a universal literary shape.

## INPUT

```
FORM
SCOPE_RECORD
PARTICIPATION_MODE
CURRENT_PROJECT_STATE
```

## OUTPUT

```
VOLUME_METRIC
STRUCTURAL_UNIT
PRODUCTION_UNIT
LOCK_UNIT
DONE_CRITERIA
AUDIT_PROFILE
PERSISTENCE_PROFILE
```

## FORM RULE

The declared project form determines the legal structural and production units.

The runtime does not choose the literary form.

### Prose forms

Allowed structural/production units may include:

```
CHAPTER
SCENE
SEQUENCE
EPISODE
OTHER
```

The exact unit remains project-defined.

### Screenplay

```
STRUCTURAL_UNIT = SCENE / SEQUENCE
PRODUCTION_UNIT = SCENE / SEQUENCE
```

A screenplay has no mandatory chapter model.

Its volume metric remains project-defined and may use:

```
PAGES
MINUTES
SCENES
SEQUENCES
OTHER
```

## GATE

`FORM.CONTRACT_READY`

## FAIL CONDITIONS

```
FORM_UNDECLARED
FORM_PIPELINE_CONFLICT
PROSE_RULE_APPLIED_TO_SCREENPLAY
INAPPROPRIATE_VOLUME_METRIC
```

## INVARIANTS

- No universal chapter requirement.
- No universal numeric volume target.
- Response budget cannot redefine structural unit.
- Production, persistence and applicable audit routing use the form contract.
