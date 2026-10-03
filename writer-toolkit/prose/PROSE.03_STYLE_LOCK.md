# PROSE.03_STYLE_LOCK

**ID:** `PROSE.03_STYLE_LOCK`

## TRIGGER

Baseline established.

## OUTPUT

```yaml
style_lock:
  baseline_id: ...
  locked_at: ...
  model_profile: ...
  runtime_profile: ...
  permitted_variation: ...
  status: LOCKED | OPEN | SUPERSEDED
```

## LOCK SEMANTICS

Style Lock is an execution reference, not an artistic prison.

Intentional deviation requires:

```text
PROPOSE
→ AUTHOR DECISION
→ UPDATE STYLE LOCK
   OR
  REGISTER LOCAL DEVIATION
```

## GATE

`G3 — STYLE LOCK`

PASS when:

- baseline persisted;
- diagnostic completed;
- required author interaction completed;
- lock record stored.

FAIL:

`STYLE_BASELINE_MISSING`

or

`STYLE_CALIBRATION_NOT_COMPLETE`.
