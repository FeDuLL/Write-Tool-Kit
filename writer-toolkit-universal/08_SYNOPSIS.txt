# DEV.03_SYNOPSIS_GATE

**ID:** `DEV.03_SYNOPSIS_GATE`

## OUTPUT

```text
APPROVE
APPROVE_WITH_CHANGES
REWORK
RETHINK_CORE
```

The synopsis must expose:

```text
AI-DECIDED
AUTHOR-DECIDED
DEFERRED
OPEN
```

## GATE

Only `APPROVE` or `APPROVE_WITH_CHANGES` after changes are implemented allows
standard production.

`REWORK` and `RETHINK_CORE` block standard production.

## RULE

Approval of the synopsis does not retroactively convert an undisclosed AI
assumption into an author decision.

## AUTHOR RULE

This is an explicit author gate.
