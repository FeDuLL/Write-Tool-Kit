# BRIEF.03_LOCK

**ID:** `BRIEF.03_LOCK`

## TRIGGER

Author reviews/approves the brief.

## PRECONDITIONS

- brief draft exists;
- all material author decisions are explicitly visible;
- unresolved items are labeled.

## MANDATORY OUTPUT

```
AUTHOR DECISIONS
AI-DECIDED / NOT-YOUR-DECISION-YET
DEFERRED
ACTIVE_MODULES
SCOPE_RECORD
PARTICIPATION_MODE
```

## GATE

`BRIEF.LOCKED`

## FAIL

- unresolved author-required decision hidden;
- AI assumption is not exposed;
- required active module missing;
- scope state inconsistent with project.

## AUTHOR RULE

Locking the brief is an author gate.

Silence is not approval.
