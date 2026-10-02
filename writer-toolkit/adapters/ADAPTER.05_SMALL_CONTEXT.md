# ADAPTER.05 — SMALL-CONTEXT

**ID:** ADAPTER.05  
**Activation:** Full manuscript cannot reliably fit in current context.

## 1. PURPOSE

Permit safe work on large manuscripts without pretending that partial context is complete context.

## 2. REQUIRED BEHAVIOR

Use persisted, addressable manuscript segments or an equivalent indexed representation.

```text
MANUSCRIPT INDEX
→ retrieve relevant segments
→ inspect required context
→ perform task
```

## 3. COVERAGE RULE

Every audit or verification pass declares its actual coverage.

```text
FULL
PARTIAL
TARGETED
UNVERIFIED
```

A small-context runtime must not report a full-manuscript audit when required sections were inaccessible.

## 4. INACCESSIBLE SECTIONS

When required sections cannot be inspected:

```text
RESULT = UNVERIFIED
UNVERIFIED_REASON = inaccessible manuscript coverage
```

The runtime may still produce targeted diagnostics for accessible sections.

## 5. AUTHORITY RULE

Index entries, summaries, and digests are navigation mechanisms.
They do not become substitutes for manuscript text when literal wording matters.

## 6. AUDIT ASSEMBLY

A final manuscript audit requires an explicit coverage record showing which required sections were actually inspected.

## 7. COMPOSITION

Small-context is an execution overlay. It can coexist with:

```text
FILE-CAPABLE
TOOL-ENABLED
```

It does not require a separate project mode.
