# WRITER-TOOLKIT v0.3 — BUILD SPECIFICATION

**Status:** BUILD SPEC / canonical implementation contract  
**Version:** 0.3  
**Schema Version:** 0.3  
**Bootstrap Version:** 0.3  
**Date:** 2026-09-27  
**Source architecture:** `WRITER-TOOLKIT_v0.3_ARCHITECTURE_SPEC.md`  
**Decision basis:** `WRITER_V0.3_FORENSIC_RECONCILIATION.md` + DeepSeek/YandexGPT/GigaChat/Claude forensic findings  
**Purpose:** превратить архитектуру v0.3 в однозначные модули, схемы, триггеры, гейты, outputs и fail conditions.

---

# 0. BUILD PRINCIPLES

## 0.1. Этот документ — не prose skill

Build Spec не содержит литературных рекомендаций как таковых. Он задаёт контракт реализации.

Для каждого механизма должны быть определены:

```text
MODULE
PURPOSE
INPUTS
PRECONDITIONS
TRIGGER
PROCESS
OUTPUTS
STATE CHANGES
GATE
FAIL CONDITIONS
AUTHOR DECISION REQUIRED
ADAPTER DEPENDENCIES
```

## 0.2. One source of truth

Каноническая логика v0.3 должна существовать только в одном архитектурном источнике.

Distribution-specific files:

- Native Skill;
- Universal TXT;
- NEW_CHAT launcher;
- NEW_MODEL launcher;
- templates;

не имеют права создавать собственные противоречащие правила.

## 0.3. Project parameters never become Core defaults

Никакой runtime/test-specific value не может быть перенесён в Core как default.

## 0.4. Read-only audit

Audit не изменяет manuscript/state.

Revision — отдельная операция.

## 0.5. Unknown is a valid state

`UNKNOWN` — не ошибка.

Если параметр не является blocker для текущего шага, проект может продолжаться.

## 0.6. Deferred is not permission

`DEFERRED` означает:

> decision not yet made.

Если decision становится load-bearing:

`MUST STOP`.

## 0.7. Runtime cannot redefine form

Недостаточный response budget не является основанием для молчаливого изменения:

- chapter;
- scene function;
- artistic scope;
- prose texture;
- structure.

Adapter должен использовать chunking/persistence, если это технически возможно.

---

# 1. IMPLEMENTATION LAYERS

Canonical package:

```text
writer-toolkit/
├── SKILL.md
├── core/
├── intake/
├── prose/
├── development/
├── production/
├── revision/
├── audits/
├── conditional/
├── adapters/
├── schemas/
├── templates/
├── reference/
└── tests/
```

## 1.1. Module namespaces

| Prefix | Layer |
|---|---|
| CORE | universal Core |
| BRIEF | Creative Brief |
| FORM | form-dependent |
| PROSE | prose/style |
| DEV | development |
| PROD | production |
| REV | revision |
| AUD | audit |
| STATE | persistence/state |
| ADAPTER | runtime |
| COND | conditional |
| BOOT | bootstrap |
| REF | reference |
| TEST | testing |

---

# 2. MODULE REGISTRY

## CORE MODULES

### `CORE.01_AUTHORITY`
Purpose:
author sovereignty and authority boundaries.

Dependencies:
none.

Activation:
always.

### `CORE.02_STATE`
Purpose:
Authority / Decision / Artifact state semantics.

Activation:
always.

### `CORE.03_EVIDENCE`
Purpose:
artifact-grounded verification.

Activation:
always.

### `CORE.04_CHANGE_CONTROL`
Purpose:
REPAIR / OPTIMIZATION / DEVELOPMENT PROPOSAL / AUTHOR DECISION.

Activation:
always.

### `CORE.05_RUNTIME_LOOP`
Purpose:
UNDERSTAND → INSPECT → PLAN → CREATE → TEST → AUDIT → RECORD → CHECKPOINT.

Activation:
always.

### `CORE.06_KNOWLEDGE_DISCIPLINE`
Purpose:
World Truth / Author Knowledge / Character Knowledge / Reader Knowledge / Belief / Rumor / Evidence / False Interpretation.

Activation:
always.

### `CORE.07_CAUSALITY`
Purpose:
CAUSE → CHOICE/ACTION → CONSEQUENCE → NEW SITUATION.

Activation:
always.

### `CORE.08_PERSISTENCE_POLICY`
Purpose:
MANUSCRIPT / STATE / DIGEST authority separation.

Activation:
always.

---

# 3. CREATIVE BRIEF MODULE

## `BRIEF.01_SCHEMA`

### Required fields

```text
PROJECT_ID
PROJECT_NAME
FORM
SCOPE_RECORD
GENRE
SUBGENRE
TONE
EMOTIONAL_EFFECT
AUDIENCE
POV
STRUCTURAL_MODE
PROSE_TEXTURE
DARKNESS
HUMOR
ROMANCE
PHILOSOPHICAL_DENSITY
ENDING
SERIES_STATUS
PARTICIPATION_MODE
LANGUAGE
LOCALE
COMMERCIAL_INTENT
CROSS_MEDIA_INTENT
```

### Field state

Every substantive field uses:

```text
DECISION_STATE:
UNKNOWN | OPEN | DEFERRED | PROPOSED | ACCEPTED | REJECTED
SOURCE:
AUTHOR | AI | DERIVED | EXTERNAL
```

`DERIVED` does not mean accepted.

A derived value remains non-authoritative until its authority rules say otherwise.

---

## `BRIEF.02_INTAKE`

### Trigger

New project OR project without valid Creative Brief.

### Preconditions

- no valid current Creative Brief;
- project context available to the extent possible.

### Process

1. inspect user-provided material;
2. extract already-defined author decisions;
3. do not ask for information already present;
4. determine material missing fields;
5. distinguish UNKNOWN from DEFERRED;
6. propose only the minimum material questions;
7. produce BRIEF DRAFT.

### Output

```text
CREATIVE BRIEF DRAFT
AI-DECIDED
MATERIALLY MISSING
DEFERRED
PROPOSED NEXT ACTION
```

### Gate

`BRIEF.READY_FOR_LOCK`

### Fail

- invented author decision presented as known;
- stress-test parameter imported as default;
- omission of load-bearing field;
- closed options presented as exhaustive when they are illustrative only.

---

## `BRIEF.03_LOCK`

### Trigger

User reviews/approves brief.

### Mandatory output

```text
AUTHOR DECISIONS
AI-DECIDED / NOT-YOUR-DECISION-YET
DEFERRED
ACTIVE_MODULES
SCOPE_RECORD
PARTICIPATION_MODE
```

### Gate

`BRIEF.LOCKED`

### Fail

- unresolved author-required decision;
- hidden AI assumption;
- active module missing;
- scope state inconsistent with project.

---

# 4. SCOPE SCHEMA

## `STATE.SCOPE_RECORD`

Canonical structure:

```yaml
scope_record:
  mode: EXACT | RANGE | APPROX | FORM-DERIVED | UNKNOWN | NON-BINDING | DISCOVERY
  metric: AL | CHARACTERS | WORDS | PAGES | MINUTES | OTHER
  target_value: null
  target_min: null
  target_max: null
  current_value: null
  current_exactness: EXACT | ESTIMATED | UNKNOWN
  deviation: null
  deviation_status: NONE | WITHIN | OVER | UNDER | AUTHOR-ACCEPTED
  owner: AUTHOR
  binding: YES | NO
  source: AUTHOR | DERIVED | PROJECT
```

## Rules

1. Toolkit never inserts a numeric target if author did not define one.
2. `UNKNOWN`, `NON-BINDING`, `DISCOVERY` are valid.
3. A target may be derived only if project rules explicitly permit it.
4. Derived target must retain `source=DERIVED`.
5. `AUTHOR-ACCEPTED` deviation requires explicit author act.
6. Silence never changes deviation status.

## Gate

`SCOPE.DECLARED`

This means a mode has been declared. It does NOT require a numeric target.

---

# 5. FORM MODULE

## `FORM.01_CONTRACT`

### Input

`FORM`

### Output

```text
VOLUME_METRIC
STRUCTURAL_UNIT
PRODUCTION_UNIT
LOCK_UNIT
DONE_CRITERIA
AUDIT_PROFILE
PERSISTENCE_PROFILE
```

### Examples

For prose:

```text
STRUCTURAL_UNIT = CHAPTER / SCENE / SEQUENCE
```

For screenplay:

```text
STRUCTURAL_UNIT = SCENE / SEQUENCE
```

No universal chapter requirement.

### Fail

- prose chapter rules applied to screenplay;
- author-sheet metric applied where inappropriate;
- form pipeline conflicts with declared form.

---

# 6. COMPLEXITY MODULE

## `FORM.02_COMPLEXITY`

Allowed:

```text
T1 = COMPACT
T2 = STANDARD
T3 = HIGH-COMPLEXITY
```

### Rule

Complexity controls process depth/resource requirements only.

It does NOT activate:

- mystery;
- hidden world;
- series;
- IP;
- commercial layer.

### Gate

`COMPLEXITY.DECLARED`

---

# 7. ACTIVE MODULES

## `STATE.ACTIVE_MODULES`

Canonical record:

```yaml
active_modules:
  hidden_world: OFF
  reveal: OFF
  series: OFF
  ip: OFF
  cross_media: OFF
  commercial: OFF
  genre_contract: OFF
  locale: RU
  screenplay: OFF
  romance: OFF
```

### Activation inputs

- Creative Brief;
- HARD requirements;
- explicit author decisions;
- form.

### Rule

Memory of an old project is never sufficient to activate a module.

---

# 8. PROSE ENGINE

## `PROSE.01_PROSE_CONTRACT`

Inputs:

- Creative Brief;
- Structural Mode;
- Prose Texture;
- audience;
- POV;
- form.

Output:

```text
PROSE_CONTRACT
```

Contract should describe:

- narrative distance;
- syntactic movement;
- descriptive density;
- interiority;
- image density;
- compression;
- dialogue texture;
- permitted variation;
- forbidden drift patterns where relevant.

No universal numeric targets.

---

## `PROSE.02_STYLE_BASELINE`

### Trigger

- new project;
- no baseline;
- major model/runtime switch;
- intentional style change.

### Process

1. propose calibration material;
2. generate short exemplar(s);
3. audit against brief;
4. author reviews;
5. repair if required;
6. store accepted exemplar(s).

### Output

```yaml
style_baseline:
  baseline_id: ...
  excerpts:
    - type: narrative | dialogue | interiority | description
      text: ...
  target_notes: ...
  permitted_variations: ...
  source_model: ...
  source_runtime: ...
```

### Gate

`STYLE.BASELINE_ESTABLISHED`

### Fail

- baseline is adjective-only;
- baseline was never preserved;
- model calls itself calibrated without artifact;
- baseline silently changes.

---

## `PROSE.03_STYLE_LOCK`

### Trigger

Baseline established.

### Output

```yaml
style_lock:
  baseline_id: ...
  locked_at: ...
  model_profile: ...
  runtime_profile: ...
  permitted_variation: ...
  status: LOCKED | OPEN | SUPERSEDED
```

### Lock semantics

Style Lock is an execution reference, not an artistic prison.

Intentional deviation requires:

`PROPOSE → AUTHOR DECISION → UPDATE STYLE LOCK or register local deviation`.

---

## `PROSE.04_STYLE_DRIFT_AUDIT`

### Input

Current artifact + Style Baseline/Lock.

### Hard diagnostics

- obvious repetitive syntax;
- forbidden production patterns;
- repeated identical images;
- accidental terminology leakage;
- voice reassignment failure where applicable.

### Soft diagnostics

- rhythmic monotony;
- overcompression;
- summary replacing scene;
- excessive declarative emotion;
- flat dialogue voices.

### Output

```text
STYLE DRIFT FINDINGS
EVIDENCE
SEVERITY
RECOMMENDED ACTION
```

### Rule

Soft diagnostic ≠ automatic FAIL.

---

# 9. DEVELOPMENT ENGINE

## `DEV.01_STORY_CORE`

Canonical fields:

```text
PREMISE
CENTRAL_CONFLICT
PROTAGONIST
DESIRE
NEED
STAKES
PROMISE
ENDING
THEMATIC_PRESSURE
```

No field may become universal genre logic.

---

## `DEV.02_DEVELOPMENT_MODE`

Allowed:

```text
ARCHITECT
DISCOVERY
HYBRID
```

### ARCHITECT

Plan before drafting.

### DISCOVERY

Draft/explore first, then extract and stabilize state.

### HYBRID

Alternate between planning and discovery.

### Rule

Discovery is a valid path, not an error.

---

## `DEV.03_SYNOPSIS_GATE`

### Output

```text
APPROVE
APPROVE_WITH_CHANGES
REWORK
RETHINK_CORE
```

The synopsis must expose:

```text
AI-DECIDED
AUTHOR-DECIDED
DEFERRED
OPEN
```

### Gate

Only `APPROVE` or `APPROVE_WITH_CHANGES` after changes are implemented allows standard production.

---

# 10. CORE DEVELOPMENT ENGINES

## `DEV.04_CHARACTER`

Track:

```text
IDENTITY
DESIRE
NEED
FEARS
VALUES
CONTRADICTIONS
ARC
RELATIONSHIPS
VOICE
KNOWLEDGE
CAPABILITIES
LIMITATIONS
```

## `DEV.05_CAUSALITY`

Canonical chain:

```text
CAUSE
→ CHOICE / ACTION
→ CONSEQUENCE
→ NEW SITUATION
```

### Fail

- coincidence performs load-bearing causal work without justification;
- protagonist lacks causal agency where agency is promised.

---

## `DEV.06_COINCIDENCE_AUDIT`

Coincidence can introduce:

- situation;
- encounter;
- information.

It should not silently resolve the central conflict unless intentionally designed and supported.

---

## `DEV.07_SCENE_ENGINE`

Scene fields:

```text
FUNCTION
DESIRE
OBSTACLE
CHOICE
TURN
CONSEQUENCE
PRESSURE
EXIT
```

Not every form requires the same scene model.

---

# 11. KNOWLEDGE ENGINE

## `CORE.06_KNOWLEDGE_DISCIPLINE`

Track separately:

```text
WORLD_TRUTH
AUTHOR_KNOWLEDGE
CHARACTER_KNOWLEDGE
READER_KNOWLEDGE
PUBLIC_BELIEF
RUMOR
EVIDENCE
FALSE_INTERPRETATION
```

### Rule

Knowledge access must be justified.

### Fail

Character/model knows information without an epistemic bridge.

---

# 12. CONDITIONAL HIDDEN-WORLD MODULE

## `COND.01_HIDDEN_WORLD`

Activation:

```text
HIDDEN_WORLD = ON
```

or equivalent HARD-REVEAL requirement.

### Inputs

- hidden truth;
- surface world;
- character knowledge;
- reader knowledge;
- reveal plan.

### Outputs

```text
HIDDEN_ONTOLOGY
SURFACE_MODEL
EPISTEMIC_BRIDGES
REVEAL_STATE
DISCOVERY_CONSTRAINTS
```

This module is completely inactive otherwise.

---

## `COND.02_REVEAL_AUDIT`

### Required independence

If checking first-read inference:

`INDEPENDENT_READER` required.

If unavailable:

`UNVERIFIED`.

Never report:

`PASS`

based on a writer session pretending not to know the hidden truth.

---

# 13. CONDITIONAL SERIES MODULE

## `COND.10_SERIES`

Activation:

`SERIES = ON`

Fields:

```text
BOOK_STATE
SERIES_ARC
RESERVED_REVEALS
ESCALATION
LONG_TERM_CONTINUITY
```

Standalone projects keep module OFF.

---

# 14. CONDITIONAL IP / CROSS-MEDIA

## `COND.20_IP`

Activation:

`IP = ON` or `CROSS_MEDIA = ON`.

Separate:

```text
CORE_WORLD_TRUTH
MEDIUM_ADAPTATION
AUDIENCE_KNOWLEDGE
MARKETING / LICENSE EXPRESSION
```

Novel-first rule remains when literary work is primary.

---

# 15. CONDITIONAL COMMERCIAL MODULE

## `COND.30_COMMERCIAL`

Activation:

explicit author intent.

Commercial hypothesis fields:

```text
HYPOTHESIS
EVIDENCE
STATUS
SUPPORTED
MIXED
WEAKENED
UNTESTED
```

Commercial evidence may influence:

- positioning;
- title/blurb/package;
- target audience;
- channel strategy.

It cannot silently rewrite:

- artistic core;
- psychology;
- ending;
- theme;
- world truth.

---

# 16. LOCALE MODULE

## `COND.40_LOCALE`

Activation:

`LANGUAGE / LOCALE`

For current project defaults:

`RU`

Russian literary authenticity remains a supported target module, not a universal logic requirement for every conceivable language.

---

# 17. GENRE ENGINE

## `COND.50_GENRE_CONTRACT`

Activation:

when author requests or genre materially matters.

### Contract contains

```text
READER PROMISE
EXPECTED EFFECT
CONVENTIONAL ELEMENTS
OPTIONAL CONVENTIONS
DELIBERATE DEVIATIONS
AUDIT RISKS
```

### Rule

Genre conventions are diagnostic lenses, not immutable laws.

---

# 18. PRODUCTION ENGINE

## `PROD.01_PRODUCTION_UNIT`

The project defines its unit:

```text
CHAPTER
SCENE
SEQUENCE
EPISODE
OTHER
```

The runtime does not determine this.

---

## `PROD.02_UNIT_GATE`

Before writing:

Check:

```text
CURRENT STAGE
CURRENT STATE
ACTIVE MODULES
RELEVANT PREVIOUS STATE
AUTHOR DECISIONS
STYLE LOCK
OPEN BLOCKERS
```

### Output

`READY_TO_WRITE` or blocker list.

---
## `PROD.03_WRITE_UNIT`

Allowed only when:

```text
NO BLOCKING HARD CONFLICT
NO REQUIRED UNRESOLVED LOAD-BEARING DECISION
```

AI may proceed if the unit follows accepted plan.

---

## `PROD.04_UNIT_PERSISTENCE`

A unit is not `DONE` until its manuscript text is persisted.

State may not say:

```text
COMPLETED
```

while manuscript artifact is absent.

### Gate

```text
TEXT_PERSISTED = YES
```

---

# 19. RESPONSE OUTPUT ADAPTER

## `ADAPTER.01_OUTPUT_BUDGET`

Inputs:

```text
PRACTICAL_OUTPUT_CAPACITY
RESERVE
CHUNKING_AVAILABLE
FILE_APPEND_AVAILABLE
```

### Behavior

If unit fits:

`SINGLE OUTPUT`

If unit does not fit and chunking is available:

`CHUNKED OUTPUT`

If file append is available:

`ASSEMBLED ARTIFACT`

If no persistence/chunking:

`MUST STOP before silently changing artistic unit`.

---

# 20. STATE ENGINE

## `STATE.01_PROJECT_STATE`

Minimum:

```yaml
project_state:
  toolkit_version: 0.3
  schema_version: 0.3
  project_id: ...
  project_name: ...
  current_stage: ...
  current_unit: ...
  form: ...
  scope_record: ...
  participation_mode: ...
  complexity: ...
  active_modules: ...
  hard_requirements: ...
  style_lock: ...
  capability_profile: ...
  ai_decided: ...
  deviations: ...
  blockers: ...
  last_checkpoint: ...
```

---

## `STATE.02_MANUSCRIPT`

Primary artifact record:

```yaml
manuscript:
  manuscript_id: ...
  version: ...
  form: ...
  persisted: true|false
  location: ...
  current_length:
    value: ...
    metric: ...
    exactness: EXACT|ESTIMATED|UNKNOWN
  completed_units: [...]
  checksum_or_integrity_marker: ...
```

The exact checksum mechanism is adapter-dependent.

---

## `STATE.03_STABLE_DIGEST`

Digest purpose:

navigation only.

Required disclaimer:

```text
DIGEST IS NOT AUTHORITATIVE FOR LITERAL MANUSCRIPT CONTENT.
```

---

# 21. DEVIATION RECORD

## `STATE.04_DEVIATION`

Schema:

```yaml
deviation:
  id: ...
  parameter: ...
  target: ...
  actual: ...
  deviation: ...
  reason: ...
  consequence: ...
  status: PROPOSED | AUTHOR-ACCEPTED | REJECTED
  author_authorized: true|false
  checkpoint: ...
```

### Rule

`PROPOSED` never equals `ACCEPTED`.

---

# 22. AI-DECIDED RECORD

## `STATE.05_AI_DECIDED`

Schema:

```yaml
ai_decided:
  id: ...
  field: ...
  proposal: ...
  reason: ...
  source_context: ...
  reversible: true|false
  author_action_required: true|false
  decision_state: PROPOSED | ACCEPTED | REJECTED | DEFERRED
```

This record prevents AI assumptions from disappearing into prose.

---

# 23. CAPABILITY ADAPTER

## `ADAPTER.10_CAPABILITY_PROFILE`

Schema:

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

Capability profile may change between sessions/models.

---

# 24. AUDIT ENGINE

## `AUD.01_COVERAGE`

Schema:

```yaml
audit_coverage:
  audit_id: ...
  scope: CHAPTER | SEQUENCE | MANUSCRIPT | PROJECT
  passes:
    - pass_id: ...
      required: true|false
      executed: true|false
      evidence_available: true|false
      independence_required: true|false
      independence_available: true|false
      result: PASS | FAIL | UNVERIFIED | NOT_APPLICABLE
```

### Rule

No `FULLY_CHECKED` claim until all required passes have a recorded state.

---

# 25. AUDIT PASS CLASSIFICATION

## HARD FALSIFIABLE

Examples:

- forbidden terms;
- chronology;
- continuity;
- hard requirement;
- exact state match;
- explicit epistemic bridge.

Result:
`PASS/FAIL`.

## SOFT DIAGNOSTIC

Examples:

- repetition;
- prose drift;
- monotony.

Result:
`FINDING / NO_SIGNIFICANT_FINDING`.

Not a universal binary quality verdict.

## INDEPENDENT READER

Examples:

- reveal inference;
- first-read effect.

Result:

```text
PASS
FAIL
UNVERIFIED
```

`UNVERIFIED` if independent capability unavailable.

---

# 26. AUDITOR ROLE

## `AUD.02_ROLE`

Roles:

```text
AUTHOR
WRITER
AUDITOR
```

One model may perform multiple roles sequentially.

The current role must be explicit.

### Example

```text
ROLE = WRITER
ACTION = DRAFT
```

then:

```text
ROLE = AUDITOR
ACTION = HARD_CONTINUITY_CHECK
```

Role switch does not automatically create independence.

---

# 27. AUDIT EVIDENCE

For every HARD-* PASS:

```yaml
evidence:
  source: ...
  locator: ...
  excerpt: ...
  interpretation: ...
  result: PASS
```

A production report alone is invalid evidence.

---

# 28. AUDIT MUTATION FIREWALL

Forbidden during audit:

```text
MANUSCRIPT EDIT
STATE EDIT
AUTHORITY EDIT
DEVIATION ACCEPTANCE
STYLE LOCK UPDATE
CANON UPDATE
```

Allowed:

```text
FIND
DESCRIBE
CLASSIFY
PROPOSE
```

Only Revision or explicit Author action can commit changes.

---

# 29. REVISION ENGINE

## `REV.01_REVISION_LOOP`

Exact order:

```text
DIAGNOSE
→ LOCATE
→ PROPOSE
→ TEST
→ REWRITE
→ RE-AUDIT
→ RECORD
```

### Rule

Use smallest effective change.

Do not rewrite entire text to fix local issue.

Do not flatten voice to solve structural issue.

---

# 30. CHANGE LOG

## `STATE.06_CHANGE_LOG`

Every substantive revision:

```yaml
change:
  id: ...
  artifact: ...
  location: ...
  before: ...
  after: ...
  reason: ...
  category: REPAIR | OPTIMIZATION | DEVELOPMENT_PROPOSAL | AUTHOR_DECISION
  severity: ...
  author_voice_risk: LOW | MEDIUM | HIGH
  authorized_by: AUTHOR | PRE_AUTHORIZED | N_A
  status: PROPOSED | APPLIED | REJECTED
```

No silent substantive revision.

---

# 31. AUTO-PROCEED CONTRACT

## `CORE.09_INTERACTION`

### MAY PROCEED

- already approved plan;
- mechanical repairs;
- persistence;
- state bookkeeping;
- allowed diagnostics;
- application of Style Lock;
- routine production.

### MUST STOP

- load-bearing new decision;
- hard conflict;
- unresolved DEFERRED;
- major scope change;
- ending change;
- form change;
- authority change;
- capability blocker;
- required independent audit unavailable.

### MUST PRESENT

When optimization could help but is not already authorized.

---

# 32. PARTICIPATION MODE

Schema:

```text
HIGH-COLLABORATION
BALANCED
AUTONOMOUS-WITH-GATES
```

## High collaboration

Author checkpoint at frequent production boundaries.

## Balanced

Author checkpoints at defined major gates.

## Autonomous

Routine production proceeds without per-unit approval.

Still requires:

- MUST STOP gates;
- state persistence;
- revision/audit controls.

Silence never equals approval.

---

# 33. BOOTSTRAP CORE

## `BOOT.01_CANONICAL`

### Universal preflight

```text
1. VERIFY TOOLKIT VERSION
2. VERIFY SCHEMA VERSION
3. VERIFY ARTIFACT INTEGRITY
4. LOAD MANUSCRIPT
5. LOAD PROJECT STATE
6. LOAD ACTIVE MODULES
7. LOAD STYLE LOCK
8. LOAD CAPABILITIES
9. IDENTIFY CURRENT STAGE
10. IDENTIFY BLOCKERS
11. IDENTIFY NEXT AUTHORIZED ACTION
```

### Fail

- version mismatch;
- missing required artifact;
- manuscript unavailable when required;
- state corruption;
- schema mismatch;
- incompatible audit status.

---

## `BOOT.02_NEW_CHAT`

Trigger:

new conversation, same project/model/runtime.

Additional behavior:

```text
RESTORE
→ VERIFY INTEGRITY
→ DETERMINE LAST STABLE CHECKPOINT
→ CONTINUE NEXT AUTHORIZED ACTION
```

Do not reinterpret settled decisions from scratch.

---

## `BOOT.03_NEW_MODEL`

Trigger:

same project moves to different model/runtime.

Additional:

```text
PROFILE CAPABILITIES
→ RECHECK OUTPUT LIMIT
→ RE-ANCHOR STYLE FROM BASELINE
→ CHECK ACTIVE MODULE COMPATIBILITY
→ INVALIDATE CAPABILITY-DEPENDENT VERDICTS IF UNSUPPORTED
→ CONTINUE
```

Style descriptions are not considered sufficient for transfer; preserved exemplars are.

---

# 34. FORM OF HANDOFF

## `STATE.07_HANDOFF`

Canonical order:

```text
VERSION
PROJECT_ID
CURRENT_STAGE
CURRENT_UNIT
PROJECT_STATUS
AUTHOR_DECISIONS
AI_DECIDED
DEFERRED
OPEN_BLOCKERS
SCOPE_RECORD
STYLE_LOCK
ACTIVE_MODULES
CAPABILITY_PROFILE
RECENT_MANUSCRIPT_CONTEXT
CONTINUITY
NEXT_AUTHORIZED_ACTION
DO_NOT_DO
```

`DO_NOT_DO` is especially useful for model switching.

---

# 35. STAGE GATES — EXACT BUILD CONTRACT

## Gate G0 — INTAKE

PASS when:

- project identity exists;
- minimum brief fields known or marked;
- no hidden hard assumption;
- no test value imported.

FAIL:
`BRIEF_INCOMPLETE`

---

## Gate G1 — BRIEF LOCK

PASS when:

- author decisions recorded;
- deferred/unknown separated;
- AI-decided exposed;
- active modules determined;
- scope mode declared;
- participation mode declared.

FAIL:
`BRIEF_AUTHORITY_UNCLEAR`

---

## Gate G2 — PROSE CONTRACT

PASS when:

- prose texture exists or is validly deferred;
- form-compatible prose contract exists;
- style calibration trigger determined.

FAIL:
`PROSE_TARGET_UNRESOLVED`

if writing cannot proceed without it.

---

## Gate G3 — STYLE LOCK

PASS when:

- baseline persisted;
- diagnostic completed;
- author interaction completed where required;
- lock record stored.

FAIL:
`STYLE_BASELINE_MISSING`

or:

`STYLE_CALIBRATION_NOT_COMPLETE`

---

## Gate G4 — DEVELOPMENT READY

PASS when:

- development path selected;
- approved synopsis/architecture exists;
- AI assumptions exposed;
- active conditional modules loaded.

FAIL:
`DEVELOPMENT_NOT_AUTHORIZED`

---

## Gate G5 — PRODUCTION UNIT READY

PASS when:

- current unit defined;
- no blocker;
- state loaded;
- style lock available;
- required previous context accessible;
- no unresolved load-bearing deferred decision.

FAIL:
`UNIT_NOT_READY`

---

## Gate G6 — UNIT COMPLETE

PASS when:

- manuscript text persisted;
- artifact state updated;
- required diagnostics performed;
- continuity checked;
- no blocking finding.

FAIL:
`UNIT_NOT_PERSISTED`

---

## Gate G7 — DRAFT COMPLETE

PASS when:

- production coverage complete;
- synopsis/plan diff checked;
- HARD requirements checked;
- story completion criteria met;
- scope status recorded if active.

FAIL:
`DRAFT_INCOMPLETE`

---

## Gate G8 — FULL AUDIT COMPLETE

PASS when:

- all required passes executed;
- coverage record complete;
- independent-required passes verified or explicitly accepted as unresolved according to project policy.

Normal publication gate should not accept blocking `UNVERIFIED`.

FAIL:
`AUDIT_INCOMPLETE`

---

## Gate G9 — REVISION COMPLETE

PASS when:

- target defects addressed;
- change log complete;
- relevant audits re-run;
- no silent mutations.

FAIL:
`REVISION_UNVERIFIED`

---

## Gate G10 — PREPUBLICATION

PASS when:

- final manuscript persisted;
- final audit complete;
- required independent checks passed;
- blocking findings resolved;
- export/package complete.

FAIL:
`PREPUBLICATION_BLOCKED`

---

# 36. FAILURE CODE REGISTRY

```text
BRIEF_INCOMPLETE
BRIEF_AUTHORITY_UNCLEAR
SCOPE_MODE_MISSING
SCOPE_CONFLICT
DEFERRED_BLOCKER
AI_DECISION_HIDDEN
PROSE_TARGET_UNRESOLVED
STYLE_BASELINE_MISSING
STYLE_CALIBRATION_NOT_COMPLETE
STYLE_DRIFT_UNRESOLVED
MODULE_MISSING
MODULE_NOT_AUTHORIZED
CAPABILITY_PROFILE_MISSING
MANUSCRIPT_MISSING
MANUSCRIPT_NOT_PERSISTED
STATE_INTEGRITY_ERROR
STATE_MANUSCRIPT_CONFLICT
UNIT_NOT_READY
UNIT_NOT_PERSISTED
DRAFT_INCOMPLETE
AUDIT_INCOMPLETE
AUDIT_UNVERIFIED
AUDIT_MUTATION_DETECTED
REVISION_UNVERIFIED
PREPUBLICATION_BLOCKED
VERSION_MISMATCH
SCHEMA_MISMATCH
BOOTSTRAP_INTEGRITY_ERROR
```

---

# 37. SCHEMA INVENTORY

The following files must exist before v0.3 can be called implementation-complete:

```text
schemas/
├── creative_brief.schema
├── project_state.schema
├── scope_record.schema
├── style_baseline.schema
├── style_lock.schema
├── capability_profile.schema
├── active_modules.schema
├── hard_requirements.schema
├── deviation_record.schema
├── ai_decided.schema
├── audit_coverage.schema
├── evidence.schema
├── change_log.schema
├── manuscript.schema
└── handoff.schema
```

---

# 38. TEMPLATE INVENTORY

```text
templates/
├── creative_brief.txt
├── ai_decided.txt
├── synopsis_review.txt
├── style_calibration.txt
├── checkpoint.txt
├── audit_finding.txt
├── audit_coverage.txt
├── revision_log.txt
├── handoff.txt
├── external_audit_package.txt
└── bootstrap_status.txt
```

---

# 39. CONDITIONAL FILE INVENTORY

```text
conditional/
├── hidden_world/
│   ├── MODULE.txt
│   ├── reveal_state.schema
│   ├── discovery_fairness.txt
│   └── blind_reader_audit.txt
│
├── series/
│   ├── MODULE.txt
│   ├── series_state.schema
│   └── escalation.txt
│
├── ip/
│   ├── MODULE.txt
│   └── ip_asset_register.schema
│
├── commercial/
│   ├── MODULE.txt
│   └── commercial_hypothesis.schema
│
├── genre/
│   ├── MODULE.txt
│   └── genre_contract.schema
│
└── locale/
    ├── MODULE.txt
    └── locale_rules.schema
```

---

# 40. ADAPTER CONTRACT

Every adapter must provide the same logical interface, regardless of implementation.

Required operations:

```text
LOAD_ARTIFACT
SAVE_ARTIFACT
LOAD_STATE
SAVE_STATE
CHECK_CAPABILITIES
GET_OUTPUT_BUDGET
ASSEMBLE_CHUNKS
VERIFY_ARTIFACT_INTEGRITY
EXPORT
```

Unavailable operation must return:

```text
UNAVAILABLE
```

not a fabricated success.

---

# 41. CHAT-ONLY ADAPTER

When no file system exists:

- use explicit fenced persistence blocks;
- output manuscript text in stable units;
- output state separately;
- require user persistence when automatic persistence is impossible;
- never claim file saved when no file was created.

Minimum checkpoint:

```text
[MANUSCRIPT CHECKPOINT]
[PROJECT STATE CHECKPOINT]
[STYLE STATE]
[ACTIVE MODULES]
[NEXT ACTION]
```

---

# 42. FILE-CAPABLE ADAPTER

When file persistence exists:

- persist manuscript immediately after accepted production units;
- persist state at checkpoint;
- keep manuscript and state separately;
- support chunk assembly;
- produce integrity marker if possible;
- export from persisted manuscript, not conversation reconstruction.

---

# 43. SMALL-CONTEXT ADAPTER

When full manuscript cannot fit:

- use indexed persisted manuscript;
- retrieve only relevant segments;
- do not claim full-manuscript audit without full coverage;
- mark inaccessible sections;
- use `UNVERIFIED`;
- assemble final audit coverage explicitly.

---

# 44. AUDIT COVERAGE CONTRACT

An audit pass must specify:

```text
PASS_ID
TARGET_SCOPE
REQUIRED_SECTIONS
INPUT_ARTIFACTS
INDEPENDENCE_REQUIRED
INDEPENDENCE_AVAILABLE
EVIDENCE_MODE
RESULT
UNVERIFIED_REASON
```

No generic:

`AUDIT PASSED`

without scope.

---

# 45. PUBLICATION READINESS CONTRACT

`PUBLICATION READY` requires:

```text
DRAFT_COMPLETE = PASS
FULL_AUDIT = PASS
REVISION = COMPLETE or NOT_REQUIRED
REQUIRED_INDEPENDENT_CHECKS = PASS
NO_BLOCKING_UNVERIFIED = TRUE
CHANGE_LOG_COMPLETE = TRUE
MANUSCRIPT_PERSISTED = TRUE
EXPORT_COMPLETE = TRUE
```

Additional project-specific publication requirements may be added.

Commercial success is never implied.

---

# 46. TEST SPECIFICATION

Minimum regression suite:

## TEST-01 Short literary story

Properties:

```text
SHORT FORM
NO HIDDEN WORLD
NO SERIES
NO IP
SCOPE = UNKNOWN initially
```

Must verify:

- compact process;
- no forced novel pipeline;
- no forced target volume;
- style baseline works.
