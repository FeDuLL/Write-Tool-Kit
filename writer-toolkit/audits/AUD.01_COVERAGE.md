# AUD.01_COVERAGE

**ID:** `AUD.01_COVERAGE`

## SCHEMA

```yaml
audit_coverage:
  audit_id: ...
  scope: CHAPTER | SEQUENCE | MANUSCRIPT | PROJECT
  passes:
    - pass_id: ...
      required: true|false
      executed: true|false
      evidence_available: true|false
      independence_required: true|false
      independence_available: true|false
      result: PASS | FAIL | UNVERIFIED | NOT_APPLICABLE
```

## RULE

No `FULLY_CHECKED` claim until all required passes have a recorded state.

## COVERAGE CHECK

The engine must track:

- what scope was audited;
- which passes were required;
- which passes executed;
- whether evidence exists;
- whether independence was required and available;
- the resulting status.

Chapter-level audits do not automatically count as a full-manuscript audit.
