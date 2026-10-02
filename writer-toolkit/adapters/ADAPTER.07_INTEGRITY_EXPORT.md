# ADAPTER.07 — INTEGRITY / EXPORT

**ID:** ADAPTER.07  
**Purpose:** Define how adapters prove artifact persistence and produce exports.

## 1. VERIFY_ARTIFACT_INTEGRITY

Verification should establish, to the extent supported by the runtime:

```text
artifact exists
artifact is addressable
artifact version is known
content is retrievable
integrity marker/checksum is available when supported
```

The adapter must distinguish:

```text
VERIFIED
UNVERIFIED
FAIL
```

## 2. EXPORT CONTRACT

`EXPORT` must declare:

```text
source_artifact
source_version
export_format
export_location (when available)
export_status
automation/evidence
```

The export source must be persisted project artifacts, not an inferred reconstruction from chat history.

## 3. NO ARTIFACT FABRICATION

The adapter must never report:

```text
FILE SAVED
EXPORT COMPLETE
INTEGRITY VERIFIED
```

unless the corresponding runtime evidence exists.

## 4. PARTIAL EXPORT

When only part of a requested export is accessible:

```text
EXPORT = UNVERIFIED or BLOCKED
```

with the reason recorded.

## 5. HANDOFF COMPATIBILITY

A valid handoff must retain enough artifact identity and state information for a new session/model to re-open the project without relying on hidden conversation memory.
