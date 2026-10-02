# PROD.03_WRITE_UNIT

**ID:** `PROD.03_WRITE_UNIT`

## ALLOWED WHEN

```text
NO BLOCKING HARD CONFLICT
NO REQUIRED UNRESOLVED LOAD-BEARING DECISION
```

## MAY PROCEED

AI may write the unit when it follows an accepted plan and current Style Lock.

## MUST STOP

- new load-bearing decision required;
- hard conflict;
- unresolved blocking deferred item;
- capability blocker;
- required context unavailable.

## RULE

Production execution must not silently alter premise, form, ending, major scope,
protagonist architecture, or other author-only decisions.

## OUTPUT

Manuscript text for the current unit, subject to persistence.
