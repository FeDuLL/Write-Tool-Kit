# ADAPTER.00 — ABSTRACT CONTRACT

**ID:** ADAPTER.00  
**Type:** Canonical abstract adapter  
**Activation:** Always

## 1. PURPOSE

Define the logical interface that every runtime adapter must satisfy.

## 2. REQUIRED OPERATIONS

| Operation | Purpose |
|---|---|
| `LOAD_ARTIFACT` | Load persisted manuscript or other required artifact. |
| `SAVE_ARTIFACT` | Persist artifact changes. |
| `LOAD_STATE` | Load Project State and other required state. |
| `SAVE_STATE` | Persist state/checkpoint. |
| `CHECK_CAPABILITIES` | Produce current capability profile. |
| `GET_OUTPUT_BUDGET` | Report usable response/output capacity. |
| `ASSEMBLE_CHUNKS` | Combine chunked outputs into a durable unit/artifact. |
| `VERIFY_ARTIFACT_INTEGRITY` | Check that persisted artifact is intact and addressable. |
| `EXPORT` | Produce requested export from persisted artifacts. |

## 3. OPERATION CONTRACT

Each operation must identify:

```text
operation
status
inputs
artifacts_touched
state_touched
outputs
verification_evidence
error_or_blocker
```

## 4. UNAVAILABLE RULE

When an operation cannot be provided by the runtime:

```text
status = UNAVAILABLE
```

The adapter must not simulate the missing operation.

## 5. SOURCE-OF-TRUTH RULE

`MANUSCRIPT` remains authoritative for literal manuscript content.
`STATE` remains authoritative for project decisions and workflow state.
`DIGEST` is navigation only.

Adapters may transport or persist these artifacts but may not redefine their authority.

## 6. CAPABILITY-DEPENDENT VERDICTS

Any verdict that depends on an unavailable capability must not be presented as a verified result.

Examples:

```text
FULL-MANUSCRIPT-AUDIT + PARTIAL ACCESS
→ UNVERIFIED

SAVE_ARTIFACT + NO PERSISTENCE
→ UNAVAILABLE

EXACT_COUNT + NO EXACT_COUNTING
→ UNVERIFIED
```

## 7. DEPENDENCIES

- Capability Profile;
- Response Output Budget;
- Manuscript/State persistence contracts;
- Audit coverage contract;
- Handoff contract.
