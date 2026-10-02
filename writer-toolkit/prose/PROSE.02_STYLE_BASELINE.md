# PROSE.02_STYLE_BASELINE

**ID:** `PROSE.02_STYLE_BASELINE`

## TRIGGER

- new project;
- no baseline;
- major model/runtime switch;
- intentional style change.

## PROCESS

1. propose calibration material;
2. generate short exemplar(s);
3. audit against brief;
4. author reviews;
5. repair if required;
6. store accepted exemplar(s).

## OUTPUT

```yaml
style_baseline:
  baseline_id: ...
  excerpts:
    - type: narrative | dialogue | interiority | description
      text: ...
  target_notes: ...
  permitted_variations: ...
  source_model: ...
  source_runtime: ...
```

## GATE

`STYLE.BASELINE_ESTABLISHED`

## FAIL

- baseline is adjective-only;
- baseline was never preserved;
- model calls itself calibrated without artifact;
- baseline silently changes.
