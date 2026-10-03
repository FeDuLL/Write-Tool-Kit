# BRIEF ENGINE

**Layer:** ENGINE  
**Activation:** New project OR project without valid Creative Brief  
**Dependencies:** `CORE.01_AUTHORITY`, `CORE.02_STATE`, `CORE.03_EVIDENCE`,
`CORE.04_CHANGE_CONTROL`, `CORE.05_RUNTIME_LOOP`

## PURPOSE

Собрать, проверить и зафиксировать Creative Brief без превращения предположений
модели в авторские решения.

## PROCESS

```text
INSPECT
→ EXTRACT AUTHOR DECISIONS
→ IDENTIFY MISSING / UNKNOWN / DEFERRED
→ PROPOSE MINIMUM QUESTIONS
→ BUILD BRIEF DRAFT
→ AUTHOR REVIEW
→ LOCK
```

## HARD RULES

- Do not ask for information already present.
- `DERIVED` does not mean `ACCEPTED`.
- `DEFERRED` does not mean permission to decide later silently.
- Test/stress-test values never become project defaults.
- Closed option lists are not exhaustive unless the project says so.

## OUTPUTS

- Creative Brief Draft
- AI-DECIDED
- MATERIALLY MISSING
- DEFERRED
- PROPOSED NEXT ACTION
- Locked brief package after author review

## GATE

`BRIEF.READY_FOR_LOCK` → `BRIEF.LOCKED`

## FAIL

- invented author decision presented as known;
- hidden AI assumption;
- omitted load-bearing field;
- active module or scope state inconsistent with the project.
