# ADAPTER RUNTIME ENGINE

**ID:** ADAPTER-ENGINE  
**Layer:** Runtime Adapter  
**Phase:** E

## 1. PURPOSE

Provide a single execution boundary between canonical Writer-Toolkit logic and the current model/runtime.

## 2. CORE PRINCIPLE

The toolkit defines literary/project semantics.

The adapter defines what the current environment can actually do.

```text
CANONICAL TOOLKIT
      ↓
ADAPTER CONTRACT
      ↓
CURRENT CAPABILITY PROFILE
      ↓
RUNTIME EXECUTION
```

Runtime capability is not project authority.

## 3. ADAPTER COMPOSITION

The canonical adapter is always present. Runtime profiles are overlays:

```text
BASE ADAPTER
├── CHAT_ONLY
├── FILE_CAPABLE
├── SMALL_CONTEXT
└── TOOL_ENABLED
```

The overlays may coexist.

Examples:

```text
CHAT-ONLY
FILE-CAPABLE + TOOL-ENABLED
FILE-CAPABLE + SMALL-CONTEXT
FILE-CAPABLE + SMALL-CONTEXT + TOOL-ENABLED
```

A profile must never activate a literary/project module merely because a runtime capability exists.

## 4. SESSION START

At session start:

```text
CHECK_CAPABILITIES
→ GET_OUTPUT_BUDGET
→ LOAD_ARTIFACT (when required)
→ LOAD_STATE
→ verify adapter/module compatibility
```

Capability values describe the current execution environment only.

## 5. OPERATION RESULT RULE

Every adapter operation must expose whether it actually succeeded.

Minimum semantic outcomes:

- `SUCCESS` — operation completed and evidence exists;
- `UNAVAILABLE` — operation is not supported in this runtime;
- `BLOCKED` — operation is supported but cannot proceed because a required condition is absent;
- `FAIL` — operation was attempted and failed;
- `UNVERIFIED` — result cannot be established with available evidence.

`UNAVAILABLE` must never be translated into `SUCCESS` by inference.

## 6. LITERARY-SCOPE FIREWALL

Adapter logic must not silently:

- shorten a chapter because of output capacity;
- change the scene function;
- rewrite prose texture;
- alter planned structure;
- convert a deferred decision into canon;
- claim persistence without persistence evidence;
- claim full-manuscript audit without full coverage.

When technical limits prevent the requested operation, the adapter reports the condition and uses the smallest safe technical alternative, such as chunking or persistence.

## 7. STATE UPDATE RULE

Production state is updated only after the corresponding artifact state is actually durable enough for the current adapter.

For chunked production:

```text
WRITE CHUNK
→ PERSIST CHUNK
→ VERIFY CHUNK
→ continue
→ complete UNIT
→ update UNIT STATE
```

A conversation-only draft must not be reported as persisted manuscript.
