# AUDIT ENGINE

**Layer:** ENGINE  
**Activation:** when diagnostics or formal audit are required  
**Dependencies:** Core authority/state/evidence, manuscript/state artifacts, applicable engines, capability profile, FORM contract

## PURPOSE

Проводить проверку в явном scope с соответствующей evidence policy,
различать falsifiable checks, soft diagnostics и independent-reader checks,
и не использовать аудит как скрытый канал редактирования.

## FORM ROUTING

Every formal audit loads the current `AUDIT_PROFILE` from the Form Contract.

For:

```text
FORM = SCREENPLAY
```

the form-specific set includes:

```text
FORM_UNIT_INTEGRITY
SCENE_SEQUENCE_CONTINUITY
SCREENPLAY_FORMAT_CONSISTENCY
DIALOGUE_ACTION_SEPARATION
CHAPTER_RULE_CONTAMINATION
```

Generic audits remain applicable where relevant.

## AUDIT SCOPES

```text
CHAPTER
SCENE
SEQUENCE
MANUSCRIPT
PROJECT
```

For screenplay, `CHAPTER` is not a required scope.

## RESULT SEMANTICS

```text
PASS
FAIL
UNVERIFIED
NOT_APPLICABLE
```

For soft diagnostics:

```text
FINDING
NO_SIGNIFICANT_FINDING
```

## FULL CHECK RULE

No `FULLY_CHECKED` claim until all required passes have a recorded state.

## ROLE MODEL

```text
AUTHOR
WRITER
AUDITOR
```

One model may perform multiple roles sequentially.

Role switching does not automatically create independence.

## FORM SAFETY

A form-specific audit profile may add checks, but it may not silently redefine the generic Core.
