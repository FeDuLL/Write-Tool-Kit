# BRIEF.02_INTAKE

**ID:** `BRIEF.02_INTAKE`

## TRIGGER

New project OR project without valid Creative Brief.

## PRECONDITIONS

- no valid current Creative Brief;
- project context available to the extent possible.

## PROCESS

1. inspect user-provided material;
2. extract already-defined author decisions;
3. do not ask for information already present;
4. determine materially missing fields;
5. distinguish `UNKNOWN` from `DEFERRED`;
6. propose only the minimum material questions;
7. produce `CREATIVE BRIEF DRAFT`.

## OUTPUT

```text
CREATIVE BRIEF DRAFT
AI-DECIDED
MATERIALLY MISSING
DEFERRED
PROPOSED NEXT ACTION
```

## GATE

`BRIEF.READY_FOR_LOCK`

## FAIL

- invented author decision presented as known;
- stress-test parameter imported as default;
- omission of load-bearing field;
- illustrative option set treated as exhaustive.
