# ADAPTER.04 — FILE-CAPABLE

**ID:** ADAPTER.04  
**Activation:** Durable file persistence is available.

## 1. PURPOSE

Use persisted artifacts as the durable project substrate instead of relying on conversation reconstruction.

## 2. REQUIRED BEHAVIOR

After an accepted production unit:

```text
PERSIST MANUSCRIPT
→ VERIFY
```

At checkpoint:

```text
PERSIST STATE
→ VERIFY
```

Keep manuscript and state as separate artifacts.

## 3. CHUNK ASSEMBLY

When a production unit is larger than one output:

```text
UNIT
├── CHUNK 1
├── CHUNK 2
├── ...
└── CHUNK N
      ↓
ASSEMBLE
      ↓
VERIFY
      ↓
PERSISTED UNIT
```

Unit completion is not declared merely because the chat produced the final chunk.

## 4. INTEGRITY

Where supported, record an integrity marker such as:

```text
artifact_id
version
byte/character count (when exact)
checksum/integrity marker
last_persisted_unit
```

The exact checksum mechanism is adapter-dependent.

## 5. EXPORT

Exports must be generated from the persisted manuscript/state artifacts, not by reconstructing the project from a conversation transcript.

## 6. FAILURE CONDITIONS

If persistence fails:

```text
SAVE_ARTIFACT = FAIL
```

Do not mark the corresponding artifact or production unit as durably complete.

If integrity cannot be established:

```text
VERIFY_ARTIFACT_INTEGRITY = UNVERIFIED
```

unless the adapter has other explicit evidence that establishes integrity.