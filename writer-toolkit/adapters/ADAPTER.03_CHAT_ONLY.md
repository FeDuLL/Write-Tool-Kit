# ADAPTER.03 — CHAT-ONLY

**ID:** ADAPTER.03  
**Activation:** No durable file persistence is available.

## 1. PURPOSE

Provide portable project persistence through explicit chat output when automatic file storage is impossible.

## 2. REQUIRED BEHAVIOR

- use stable, explicitly fenced persistence blocks;
- output manuscript text in identifiable production units;
- output Project State separately from manuscript text;
- require external/user persistence when automatic saving is impossible;
- never claim that a file was saved unless a file was actually created.

## 3. MINIMUM CHECKPOINT

```text
[MANUSCRIPT CHECKPOINT]
[PROJECT STATE CHECKPOINT]
[STYLE STATE]
[ACTIVE MODULES]
[NEXT ACTION]
```

## 4. MANUSCRIPT RULE

The manuscript checkpoint contains the actual text needed to reconstruct the current durable draft.
A prose summary is not a substitute for the manuscript checkpoint.

## 5. STATE RULE

Project State remains separate so that:

```text
MANUSCRIPT ≠ STATE ≠ DIGEST
```

## 6. FAILURE CONDITIONS

### Cannot create file

Report:

```text
SAVE_ARTIFACT = UNAVAILABLE
```

### Context may be lost before checkpoint

The unit must not be reported as durably persisted.

## 7. SAFE USE

Chat-only mode can still support development, drafting, diagnostics, and revision, but persistence claims remain limited to what has actually been emitted and externally retained.
