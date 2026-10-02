# FORM.02_COMPLEXITY

**ID:** `FORM.02_COMPLEXITY`
**Layer:** FORM
**Activation:** when complexity/resource depth is declared.

## ALLOWED MODES

```
T1 = COMPACT
T2 = STANDARD
T3 = HIGH-COMPLEXITY
```

## RULE

Complexity controls process depth and resource requirements only.

It does not activate:

- mystery;
- hidden world;
- series;
- IP;
- commercial layer.

## GATE

`COMPLEXITY.DECLARED`

## FAIL

`COMPLEXITY_UNDECLARED` when explicit complexity routing is required.
