# ADAPTER.02 — CAPABILITY PROFILE

**ID:** ADAPTER.02  
**Purpose:** Describe the current runtime, not the literary project.

## 1. CANONICAL SCHEMA

```yaml
capabilities:
  file_persistence: true|false
  manuscript_access: true|false
  full_manuscript_context: YES|NO|PARTIAL
  exact_counting: true|false
  output_capacity:
    value: ...
    exactness: EXACT|ESTIMATED|UNKNOWN
  independent_review: true|false
  state_transfer: true|false
  external_tools: []
  chunking: true|false
  append_to_artifact: true|false
```

## 2. SEMANTICS

### `file_persistence`
Whether the runtime can durably save project artifacts.

### `manuscript_access`
Whether the runtime can retrieve the current manuscript artifact.

### `full_manuscript_context`
Whether the full manuscript can be held in the current working context at once.

### `exact_counting`
Whether the runtime can provide exact counts required by a task rather than estimates.

### `output_capacity`
Current practical output capacity. This is a runtime value, not a chapter-size target.

### `independent_review`
Whether a genuinely independent review capability is available to the current workflow.

### `state_transfer`
Whether required project state can be transferred into the current session without hidden prior memory.

### `external_tools`
The tools actually available to the runtime. An empty list means no declared external tools.

### `chunking`
Whether the runtime can safely produce and assemble a logical unit across multiple outputs.

### `append_to_artifact`
Whether the runtime can append/persist content to the target artifact between chunks.

## 3. CAPABILITY FIREWALL

Capability declarations must not become project decisions.

```text
CAPABILITY = runtime fact
DECISION = project fact
```

Example:

`FULL_MANUSCRIPT_CONTEXT = NO` does not mean that the manuscript is short.
It means the current runtime cannot hold the whole manuscript in context simultaneously.

## 4. CHANGE RULE

Capability profile may change between sessions or models.

On model/runtime switch:

```text
LOAD STATE
→ RECHECK CAPABILITIES
→ RECHECK OUTPUT BUDGET
→ INVALIDATE UNSUPPORTED CAPABILITY-DEPENDENT VERDICTS
```
