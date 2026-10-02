# PROSE.04_STYLE_DRIFT_AUDIT

**ID:** `PROSE.04_STYLE_DRIFT_AUDIT`

## INPUT

Current artifact + Style Baseline/Lock.

## HARD DIAGNOSTICS

- obvious repetitive syntax;
- forbidden production patterns;
- repeated identical images;
- accidental terminology leakage;
- voice reassignment failure where applicable.

## SOFT DIAGNOSTICS

- rhythmic monotony;
- overcompression;
- summary replacing scene;
- excessive declarative emotion;
- flat dialogue voices.

## OUTPUT

```text
STYLE DRIFT FINDINGS
EVIDENCE
SEVERITY
RECOMMENDED ACTION
```

## RULE

Soft diagnostic ≠ automatic FAIL.

Findings are routed to Change Control / Revision as appropriate; the audit itself
does not mutate the manuscript or Style Lock.
