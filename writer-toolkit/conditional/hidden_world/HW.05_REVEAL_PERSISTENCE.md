# HW.05 — Reveal Persistence

## Purpose

Persist hidden-world state so a new chat or model does not lose the distinction between truth, belief, and reveal status.

## Persistence fields

```text
HIDDEN_ELEMENT_ID
WORLD_TRUTH_REF
CURRENT_REVEAL_STATE
CHARACTER_KNOWLEDGE_STATE
READER_KNOWLEDGE_STATE
PUBLIC_BELIEF_STATE
RESERVED_REVEAL
LAST_CHECKED_UNIT
OPEN_RISKS
```

## Authority

`STATE` is authoritative for decisions and reveal status.

`MANUSCRIPT` remains authoritative for literal prose.

`DIGEST` is navigation only.

Conflicts are resolved by inspection; there is no blanket rule that a snapshot overrides the manuscript.
