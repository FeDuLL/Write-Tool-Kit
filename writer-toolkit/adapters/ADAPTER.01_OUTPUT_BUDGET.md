# ADAPTER.01 — OUTPUT BUDGET

**ID:** ADAPTER.01  
**Purpose:** Separate runtime response capacity from literary form and project scope.

## 1. INPUTS

```text
PRACTICAL_OUTPUT_CAPACITY
RESERVE
CHUNKING_AVAILABLE
FILE_APPEND_AVAILABLE
```

The capacity may be `EXACT`, `ESTIMATED`, or `UNKNOWN`.

## 2. DECISION

### Unit fits

```text
→ SINGLE_OUTPUT
```

### Unit does not fit + chunking is available

```text
→ CHUNKED_OUTPUT
```

The production unit identity remains stable across chunks.

### Unit does not fit + chunking is unavailable

```text
→ BLOCKED
→ report capacity constraint
→ propose a safe structural boundary only as a proposal
```

The adapter does **not** silently shrink the unit or redefine the author's scope.

## 3. CHUNK CONTRACT

Each chunk should carry enough identity to be reassembled unambiguously:

```text
PROJECT_ID
UNIT_ID
CHUNK_INDEX
CHUNK_COUNT (known/unknown)
CONTENT
CONTINUATION_STATUS
```

## 4. PERSISTENCE RULE

Where artifact persistence is available:

```text
WRITE CHUNK
→ APPEND/PERSIST
→ VERIFY
→ NEXT CHUNK
```

A completed production unit is marked complete only after its assembled artifact is persisted.

## 5. NO FORM LEAK

Output budget cannot alter:

- chapter size;
- scene function;
- prose texture;
- artistic scope;
- structural mode.
