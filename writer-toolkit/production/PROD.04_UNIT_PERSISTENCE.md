# PROD.04_UNIT_PERSISTENCE

**ID:** `PROD.04_UNIT_PERSISTENCE`

## COMPLETION CONDITION

A unit is not `DONE` until manuscript text is persisted.

State may not say:

```text
COMPLETED
```

while manuscript artifact is absent.

## GATE

```text
TEXT_PERSISTED = YES
```

plus required state/update bookkeeping.

## RUNTIME PATH

Where output cannot fit in one response:

```text
IF FITS
  → SINGLE OUTPUT
ELSE IF SAFE CHUNKING AVAILABLE
  → CHUNKED OUTPUT
ELSE IF SAFE FILE ASSEMBLY AVAILABLE
  → ASSEMBLED ARTIFACT
ELSE
  → MUST STOP
```

The adapter mechanics must not redefine the production unit.
