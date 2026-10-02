# REVISION ENGINE

**Layer:** ENGINE  
**Activation:** when a finding or author request requires revision  
**Dependencies:** audit findings, Core authority/change control, manuscript,
style baseline/lock, change log

## PURPOSE

Исправить конкретную проблему минимально достаточным изменением, не разрушая
голос, причинность, continuity и другие load-bearing свойства.

## EXACT ORDER

```text
DIAGNOSE
→ LOCATE
→ PROPOSE
→ TEST
→ REWRITE
→ RE-AUDIT
→ RECORD
```

## RULES

- Use smallest effective change.
- Do not rewrite entire text to fix a local issue.
- Do not flatten voice to solve a structural issue.
- Do not convert audit findings directly into silent edits.
- Every substantive applied revision is logged.

## GATE

`G9 — REVISION COMPLETE`

PASS when:

- target defects addressed;
- change log complete;
- relevant audits re-run;
- no silent mutations.
