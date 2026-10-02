# PROD.01_PRODUCTION_UNIT

**ID:** `PROD.01_PRODUCTION_UNIT`

## PRECONDITION

`FORM.CONTRACT_READY`

## UNIT

The project form contract defines the legal production unit.

Examples:

```text
PROSE:
  CHAPTER / SCENE / SEQUENCE / EPISODE / OTHER

SCREENPLAY:
  SCENE / SEQUENCE
```

## RULE

The runtime does not determine the literary production unit.

The form contract is authoritative for structural/production unit selection.

The unit may be implemented through one or more runtime outputs where the adapter supports safe persistence/assembly.

## SCREENPLAY SAFEGUARD

When `FORM = SCREENPLAY`:

```text
CHAPTER_MODEL = OFF
PRODUCTION_UNIT = SCENE / SEQUENCE
```

Applying chapter-only production logic is a `FORM_PIPELINE_CONFLICT`.

## GATE

The current form contract and current unit must be explicit before production begins.

`PRODUCTION_UNIT.READY`
