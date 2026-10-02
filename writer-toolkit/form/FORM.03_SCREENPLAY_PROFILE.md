# FORM.03_SCREENPLAY_PROFILE

**ID:** `FORM.03_SCREENPLAY_PROFILE`
**Layer:** FORM
**Trigger:**

```
FORM = SCREENPLAY
```

## PURPOSE

Provide the required screenplay routing without importing prose chapter logic.

## OPERATIONAL PROFILE

```
STRUCTURAL_UNIT = SCENE / SEQUENCE
PRODUCTION_UNIT = SCENE / SEQUENCE
LOCK_UNIT = SCENE / SEQUENCE / SEQUENCE_BATCH
VOLUME_METRIC = PROJECT-DEFINED
CHAPTER_MODEL = OFF
SCREENPLAY_AUDIT_PROFILE = ON
```

## PRODUCTION RULES

- Do not require chapters.
- Do not measure completion by chapter count.
- Do not force prose chapter transitions.
- Preserve scene/sequence identity across chunked output.
- A scene/sequence may be produced across multiple runtime outputs when the adapter requires it.

## SCREENPLAY AUDIT SET

At minimum:

```
FORM_UNIT_INTEGRITY
SCENE_SEQUENCE_CONTINUITY
SCREENPLAY_FORMAT_CONSISTENCY
DIALOGUE_ACTION_SEPARATION
CHAPTER_RULE_CONTAMINATION
```

Generic causality, continuity, character, knowledge and manuscript audits remain applicable where relevant.

## DONE CRITERIA

A screenplay unit is complete when:

- its declared scene/sequence function is fulfilled;
- required form representation is present;
- continuity with adjacent units is preserved;
- the unit is persisted;
- applicable diagnostics are complete.

## GATE

`SCREENPLAY.FORM_READY`

## FAIL

```
SCREENPLAY_CHAPTER_CONTAMINATION
SCREENPLAY_UNIT_UNDEFINED
SCREENPLAY_AUDIT_PROFILE_MISSING
```
