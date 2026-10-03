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
