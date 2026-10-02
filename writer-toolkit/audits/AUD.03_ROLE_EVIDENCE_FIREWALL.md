# AUD.03_ROLE_EVIDENCE_FIREWALL

**ID:** `AUD.03_ROLE_EVIDENCE_FIREWALL`

## ROLE MODEL

```text
AUTHOR
WRITER
AUDITOR
```

A single model may perform several roles sequentially.

Current role must be explicit.

Example:

```text
ROLE = WRITER
ACTION = DRAFT
```

then:

```text
ROLE = AUDITOR
ACTION = HARD_CONTINUITY_CHECK
```

Role switch alone does not create independence.

## EVIDENCE

For every `HARD-* PASS`:

```yaml
evidence:
  source: ...
  locator: ...
  excerpt: ...
  interpretation: ...
  result: PASS
```

A production report alone is invalid evidence.

## MUTATION FIREWALL — FORBIDDEN DURING AUDIT

```text
MANUSCRIPT EDIT
STATE EDIT
AUTHORITY EDIT
DEVIATION ACCEPTANCE
STYLE LOCK UPDATE
CANON UPDATE
```

## ALLOWED DURING AUDIT

```text
FIND
DESCRIBE
CLASSIFY
PROPOSE
```

Only Revision or explicit Author action can commit changes.

## REQUIRED BEHAVIOR WHEN INDEPENDENCE IS UNAVAILABLE

Where independence is required for a valid result and the capability is not
available:

```text
RESULT = UNVERIFIED
```

Never fabricate PASS.

## OUTPUT

- findings;
- evidence records;
- coverage status;
- explicit UNVERIFIED where required;
- proposals routed to Revision / Author.
