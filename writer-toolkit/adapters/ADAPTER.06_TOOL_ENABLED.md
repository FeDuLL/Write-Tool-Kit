# ADAPTER.06 — TOOL-ENABLED

**ID:** ADAPTER.06  
**Activation:** One or more external runtime tools are actually available.

## 1. PURPOSE

Expose verified tool capability to the Writer-Toolkit without allowing tools to redefine project authority.

## 2. DECLARATION

Tools are declared through:

```yaml
external_tools:
  - tool_identifier
  - tool_identifier
```

Only tools actually available in the current runtime may be declared.

## 3. TOOL USE RULE

A tool result is evidence or an execution result. It is not automatically:

- author approval;
- canon;
- quality approval;
- a completed audit;
- a saved artifact.

These distinctions remain governed by the Core/state contracts.

## 4. EXAMPLES OF VALID TOOL USE

A tool may be used to:

- load a persisted manuscript;
- save an artifact;
- count exact characters when exact counting is available;
- assemble chunks;
- verify an integrity marker;
- export a file;
- obtain an explicitly independent review when such capability is actually available.

The adapter must record what the tool actually returned.

## 5. UNAVAILABLE TOOL

If a requested tool operation is not available:

```text
UNAVAILABLE
```

Do not replace it with an inferred success.

## 6. AUTHORITY FIREWALL

Tool output cannot silently mutate:

- canon;
- manuscript;
- Project State;
- Style Lock;
- author decisions.

Mutation requires the normal governed operation and its required evidence.

## 7. INDEPENDENT REVIEW

Having tools does not by itself mean that an audit is independent.
Independence remains a separate capability claim in the Capability Profile.
