# FORM ENGINE

**Layer:** ENGINE
**Dependencies:** Creative Brief, Scope Record, Production, Audit, Persistence, Adapters.

## PURPOSE

Resolve the project form into an executable contract and route it to production, persistence and audit.

## EXECUTION

```text
READ FORM
→ BUILD FORM CONTRACT
→ VALIDATE UNIT / METRIC
→ ROUTE PRODUCTION UNIT
→ ROUTE DONE CRITERIA
→ ROUTE AUDIT PROFILE
→ ROUTE PERSISTENCE PROFILE
```

## SAFETY RULES

No production module may assume `CHAPTER` is universally valid.

No audit may apply prose-only rules when `FORM = SCREENPLAY`.

## RUNTIME RULE

Output budget may cause chunking but may not change the selected structural unit.

## GATE

`FORM.CONTRACT_READY`
