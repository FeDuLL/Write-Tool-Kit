# WRITER-TOOLKIT v0.3 — ARCHITECTURE SPECIFICATION

**Status:** DRAFT / ARCHITECTURE BASELINE  
**Based on:** WRITER-TOOLKIT v0.2 + four forensic audits + Universality Audit + Forensic Reconciliation  
**Date:** 2026-09-27  
**Language:** Russian documentation; English IDs/labels preserved where they are part of the technical vocabulary.

---

# 0. PURPOSE

Writer-Toolkit v0.3 is a model-independent literary production system whose purpose is to help an AI assist an author in developing, writing, revising, auditing, and packaging literary works without taking ownership of the author's irreversible artistic decisions.

v0.3 is designed to support different:

- forms;
- genres;
- scales;
- narrative modes;
- project scopes;
- author participation modes;
- runtime environments;
- AI models.

The Toolkit itself does **not** prescribe a universal book length, chapter count, genre, language, hidden-world architecture, IP strategy, commercial strategy, or response size.

It provides a system of:

`authority → state → contracts → stages → execution → diagnostics → revision → persistence → handoff`

---

# 1. ARCHITECTURAL NORTH STAR

## 1.1. Core principle

The Toolkit must control the **process of literary creation**, not replace the author's creative sovereignty.

## 1.2. Universalization rule

A project-specific decision MUST NOT migrate into Core simply because it appeared repeatedly during a stress test.

Examples of prohibited Core defaults:

- 4–5 а. л.;
- 160–200K characters;
- 20 chapters;
- 8–9.5K characters per chapter;
- fantasy;
- YA;
- first-person narration;
- hidden ontology;
- mystery/reveal;
- series/IP;
- commercial publishing;
- a specific response limit;
- a specific model/platform.

## 1.3. Runtime neutrality

Core must not assume:

- Python;
- RAG;
- filesystem access;
- API access;
- long context;
- external agents;
- exact counting;
- file export.

Those become capabilities of an Adapter.

---

# 2. LAYER MODEL

v0.3 is composed of the following architectural layers.

## 2.1. ALWAYS ACTIVE CORE

Universal rules required for every project:

- Author Sovereignty;
- Authority / Decision / Artifact State model;
- Core Development Loop;
- Evidence Policy;
- Knowledge Discipline;
- Causality principles;
- Change classification;
- No Unauthorized Artistic Optimization;
- persistence semantics;
- gate semantics;
- runtime status semantics.

## 2.2. PROJECT STATE

Concrete data for the current project:

- form;
- scope;
- genre;
- audience;
- POV;
- tone;
- ending;
- prose texture;
- structural mode;
- participation mode;
- hard requirements;
- active conditional modules;
- current manuscript state.

## 2.3. ENGINES

Reusable operational systems:

- Creative Brief Engine;
- Genre Engine;
- Prose Engine;
- Development Engine;
- Production Engine;
- Revision Engine;
- Audit Engine;
- Prepublication Engine;
- Export/Handoff Engine.

## 2.4. CONDITIONAL MODULES

Loaded only when activated by project properties:

- Reveal / Hidden World;
- Series;
- IP / Cross-Media;
- Commercial;
- Genre-specific;
- Locale;
- Form-specific workflows.

## 2.5. ADAPTERS / RUNTIME

Environment-dependent execution:

- chat-only;
- file-capable;
- RAG-capable;
- tool-capable;
- small-context;
- high-output;
- external-review-capable.

## 2.6. SCHEMAS

Canonical machine-readable representations of:

- Project State;
- Creative Brief;
- Scope Record;
- Style Baseline/Lock;
- Capability Profile;
- Active Modules;
- Hard Requirements;
- Deviation Record;
- Audit Coverage;
- Handoff.

## 2.7. TEMPLATES

Human-readable forms:

- intake questionnaire;
- calibration response;
- synopsis review;
- checkpoint;
- handoff;
- audit finding;
- revision log;
- external audit package.

## 2.8. REFERENCE

Non-operational supporting material:

- literary framework registry;
- bibliography;
- explanatory notes.

Reference material must not compete with operational Core on small contexts.

## 2.9. TESTS

Stress tests, regression tests, model comparison protocols, and failure fixtures.

Tests are not part of the production Core.

---

# 3. CANONICAL STATE MODEL

v0.3 preserves the strong three-axis model of v0.2.

## 3.1. Authority Class

Who/what has authority over a proposition:

```text
PROJECT-HARD
DOMAIN-HARD
LITERARY-HARD
SOFT
```

Exact vocabulary may retain v0.2 semantics where already defined.

## 3.2. Decision State

Whether a proposition is decided:

```text
UNKNOWN
OPEN
DEFERRED
PROPOSED
ACCEPTED
REJECTED
```

### Mandatory rule

`DEFERRED` is not permission for the AI to invent a value when the missing value becomes load-bearing.

When a concrete answer becomes necessary:

```text
DEFERRED
→ AI MUST STOP
→ PRESENT ISSUE / OPTIONS
→ AUTHOR DECISION
```

unless the parameter was explicitly marked as authorized for autonomous determination under the project's authority rules.

## 3.3. Artifact State

What exists operationally:

```text
DRAFT
IMPLEMENTED
CHECKED
BLOCKED
STUBBED
SKIPPED-BY-AUTHOR
ARCHIVED
```

Decision State and Artifact State must never substitute for one another.

---

# 4. STATUS SEMANTICS

These labels have separate meanings and must never be conflated.

## PROCEED

Instruction to perform the next already-authorized action.

Not approval.

## AUTHOR APPROVAL

Author explicitly accepts a project artifact/decision for the purpose defined by the relevant gate.

Not proof of objective quality.

## ACCEPTED DEVIATION

Author explicitly accepts a measurable or structural departure from the current project target.

Must record:

```text
parameter
target
actual
deviation
reason
consequence
author authorization
date/checkpoint
```

Silence is never sufficient.

## CHECKED

A specified audit/check was actually performed against specified evidence.

`CHECKED` does not mean excellent.

## AUDIT PASSED

All required checks for that particular audit scope are satisfied.

May be impossible to claim where required independence/capability is unavailable.

## UNVERIFIED

A required check could not be validly performed in the current runtime.

This is not PASS.

## PUBLICATION READY

Only after the defined publication gate is satisfied, including all mandatory audit/revision/export conditions for the project and the required level of independent verification.

A production session must not manufacture this status merely from its own report.

---

# 5. CHANGE AUTHORITY MODEL

Every proposed change is classified before implementation.

## 5.1. REPAIR

AI may perform without new author approval when it is clearly mechanical or already-authorized.

Examples:

- spelling;
- punctuation;
- typographic normalization;
- continuity correction against accepted canon;
- removal of a forbidden term;
- implementation of an already accepted instruction;
- application of an already locked style baseline.

Condition:

`NO CHANGE TO LOAD-BEARING ARTISTIC INTENT`

## 5.2. OPTIMIZATION

AI may detect and propose, but must not silently implement.

Examples:

- changing prose density;
- changing register;
- adding/deleting exposition for aesthetic effect;
- strengthening an image;
- changing scene rhythm;
- rewriting character behavior because it seems better;
- changing ending tone;
- making the work more commercial.

Format:

```text
FINDING
PROPOSED CHANGE
WHY
TRADE-OFF
AUTHOR-VOICE RISK
```

## 5.3. DEVELOPMENT PROPOSAL

AI may originate alternatives where development work is explicitly allowed.

Must provide materially distinct options and trade-offs.

No hidden preference-ranking unless author requested a recommendation.

## 5.4. AUTHOR DECISION

Author-only decisions include:

- premise;
- irreversible canon;
- protagonist identity/essential arc;
- ending;
- core thematic commitment;
- form;
- major scope;
- content boundaries;
- series architecture;
- legal/sensitivity constraints;
- publication strategy;
- adoption of optimization that changes load-bearing aspects.

---

# 6. NO UNAUTHORIZED ARTISTIC OPTIMIZATION

Universal rule:

> AI may improve the execution of an accepted decision, but may not silently replace the decision with what it considers artistically superior.

Existing v0.2 taxonomy:

`error / editorial preference / stylistic alternative / optional improvement`

is elevated into Core and mapped to the four classes above.

This rule applies during:

- development;
- drafting;
- auditing;
- revision;
- packaging.

Audit cannot become an unannounced editing channel.

---

# 7. CREATIVE BRIEF ARCHITECTURE

The Creative Brief is the project contract.

## 7.1. Universal project fields

The canonical schema contains at least:

```text
FORM
SCOPE_MODE
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
LANGUAGE / LOCALE
COMMERCIAL_INTENT
CROSS_MEDIA_INTENT
```

Not every field requires a fully determined value at intake.

## 7.2. Prose Texture

This is a first-class load-bearing parameter.

It describes observable literary properties such as:

- sentence movement;
- syntactic density;
- narrative distance;
- descriptive density;
- image density;
- degree of interiority;
- paragraph movement;
- degree of compression.

Do not reduce it to adjectives alone.

It will be anchored by Style Baseline exemplars.

## 7.3. Unknown/deferred handling

The system must distinguish:

```text
UNKNOWN
DEFERRED
PROPOSED
ACCEPTED
REJECTED
```

A skipped question is not an accepted AI decision.

## 7.4. AI-DECIDED block

Before a Development Synopsis can be approved, the model must expose any substantive decisions it made without an explicit author selection.

Format:

```text
AI-DECIDED / NOT-YOUR-DECISION-YET
- field
- current proposal
- why it was introduced
- reversibility
- whether author action is required
```

The author can then accept, revise, defer, or reject.

---

# 8. SCOPE ARCHITECTURE

The Toolkit does not prescribe a universal target.

## 8.1. SCOPE_RECORD

Canonical record:

```text
SCOPE_MODE
TARGET_VALUE
TARGET_MIN
TARGET_MAX
TARGET_METRIC
CURRENT_VALUE
DEVIATION
DEVIATION_STATUS
OWNER
```

## 8.2. Scope modes

```text
EXACT
RANGE
APPROX
FORM-DERIVED
UNKNOWN
NON-BINDING
DISCOVERY
```

## 8.3. Examples are not defaults

A value such as `4–5 а. л.` may appear in documentation only as an explicit example.

It must never be a Core default.

## 8.4. Scope is not a universal Draft exit condition

Draft completion is based on story/structure coverage and project-specific completion conditions.

If a scope target exists, the system reports:

- WITHIN;
- OVER;
- UNDER;
- AUTHOR-ACCEPTED DEVIATION.

It does not pad a finished story merely to reach an arbitrary number.

## 8.5. Discovery mode

A valid project may begin without a numeric target.

In that case:

```text
SCOPE_MODE = DISCOVERY
```

and the system may record an estimate later without treating the estimate as an author decision.

---

# 9. FORM ARCHITECTURE

The same engine cannot impose identical production procedures on every form.

## 9.1. Form-dependent properties

These are selected by the project:

- volume metric;
- structural unit;
- production unit;
- lock unit;
- done criteria;
- audit set;
- persistence assembly strategy.

## 9.2. Supported forms

v0.3 should explicitly account for at least:

- short story;
- novella;
- novella/повесть where the project uses either terminology;
- novel;
- series;
- screenplay.

If support for a form is incomplete, the Toolkit must say so rather than pretend that a prose workflow is a valid screenplay workflow.

## 9.3. Small-form economy

Short works should not be forced through the full long-form apparatus.

The Toolkit can activate a compact path where:

- synopsis is shorter;
- state is lighter;
- chapter locking may disappear;
- production unit may be the whole work;
- audit scope is reduced according to form.

---

# 10. COMPLEXITY TIERS

Tiers are retained only as complexity/resource modes.

They must NOT select narrative features such as mystery, series, or IP.

Possible interpretation:

```text
T1 = compact process
T2 = standard process
T3 = high-complexity process
```

Feature activation comes independently from Project Flags.

Example:

```text
COMPLEXITY = T1
HIDDEN_WORLD = ON
```

is valid.

Also:

```text
COMPLEXITY = T3
HIDDEN_WORLD = OFF
```

is valid.

---

# 11. FEATURE FLAGS / ACTIVE MODULES

Canonical state must contain:

```text
ACTIVE_MODULES
```

Examples:

```text
HIDDEN_WORLD = ON/OFF
REVEAL = ON/OFF
SERIES = ON/OFF
IP = ON/OFF
COMMERCIAL = ON/OFF
GENRE_CONTRACT = ON/OFF
LOCALE = RU/OTHER
SCREENPLAY = ON/OFF
ROMANCE = ON/OFF
```

Activation is derived from Creative Brief + Hard Requirements + explicit author decisions.

No module becomes active merely because the model remembers that it exists.

---

# 12. STYLE SYSTEM

## 12.1. STYLE BASELINE

A baseline is an actual textual exemplar, not only an adjective list.

Recommended long-form baseline:

- 2–3 short fragments;
- at least one narrative passage;
- at least one dialogue-heavy passage;
- optionally one interiority/description passage.

The exact composition is form-dependent.

## 12.2. STYLE CALIBRATION

Required before mass production when:

- project is new;
- no baseline exists;
- model/runtime changes significantly;
- prose register intentionally changes.

Calibration cycle:

```text
PROPOSE
→ WRITE SAMPLE
→ DIAGNOSTIC
→ AUTHOR REVIEW
→ REPAIR if necessary
→ RE-CHECK
→ STYLE BASELINE
→ STYLE LOCK
```

## 12.3. Exit condition

`STYLE LOCKED` requires:

- baseline exists;
- source/exemplar is preserved;
- approved target is explicit enough to reproduce;
- permitted deviations are known;
- active model/runtime is recorded.

## 12.4. No universal numeric style KPI

Do not require:

- fixed share of long sentences;
- fixed show/tell percentage;
- fixed fragment ratio;
- fixed lexical diversity.

Use objective diagnostics only where they are genuinely falsifiable and context-independent.

---

# 13. PRODUCTION BUDGET ARCHITECTURE

## 13.1. RESPONSE OUTPUT BUDGET

Runtime capability:

```text
PRACTICAL_OUTPUT_CAPACITY
RESERVED_MARGIN
CHUNKING_AVAILABLE
FILE_APPEND_AVAILABLE
```

## 13.2. CHAPTER / SCENE SIZE

Project/form property.

It may be:

- exact;
- approximate;
- flexible.

## 13.3. Assembly rule

If an intended production unit does not fit into one output:

1. use chunked production if persistence/assembly is available;
2. preserve unit identity across chunks;
3. update state only after the complete unit is persisted;
4. only if chunking is impossible, propose a structural boundary change;
5. do not silently reduce artistic scope solely because the runtime is constrained.

---

# 14. CAPABILITY PROFILE

At session start, runtime should declare:

```text
CAPABILITY PROFILE

FILE_PERSISTENCE: YES/NO
MANUSCRIPT_ACCESS: YES/NO
FULL_MANUSCRIPT_IN_CONTEXT: YES/NO/PARTIAL
EXACT_COUNTING: YES/NO
OUTPUT_CAPACITY: ...
INDEPENDENT_REVIEW: YES/NO
STATE_TRANSFER: YES/NO
EXTERNAL_TOOLS: ...
```

Capability values are not project decisions.

They describe the current execution environment.

---

# 15. PERSISTENCE ARCHITECTURE

## 15.1. Primary artifact

`MANUSCRIPT`

The manuscript is authoritative for what is physically written.

## 15.2. Secondary state

`PROJECT_STATE`
`DOMAIN_STATE`
`CHARACTER_STATE`
`CONTINUITY_STATE`
`STYLE_STATE`
`ACTIVE_MODULES`
`HARD_REQUIREMENTS`
`SCOPE_RECORD`
`AI_DECIDED`
`DEVIATIONS`

State is authoritative for what has been decided, not for what the text literally says.

## 15.3. Tertiary navigation memory

`STABLE_DIGEST`

A digest is a navigation aid.

It is not a source of canon by itself.

## 15.4. Conflict handling

Never resolve:

```text
MANUSCRIPT
vs
STATE
```

by blanket precedence.

Instead:

```text
INSPECT CONFLICT
→ identify which artifact is stale or incorrect
→ revise manuscript OR update state
→ record correction
```

## 15.5. Durable package

Minimum:

```text
MANUSCRIPT
PROJECT_STATE
DOMAIN_STATE
CONTINUITY
STYLE_STATE
HARD_REQUIREMENTS
ACTIVE_MODULES
SCOPE_RECORD
CHANGE_LOG
ARCHIVE
```

---

# 16. AUDIT ARCHITECTURE

## 16.1. Audit types

### Internal Falsifiable

Examples:

- chronology;
- terminology;
- continuity;
- forbidden terms;
- explicit HARD requirements;
- epistemic bridge presence.

### Internal Soft Diagnostic

Examples:

- repetition;
- voice similarity;
- scene stagnation;
- prose drift.

Output is diagnostic, not proof of literary superiority.

### Independent Reader Audit

Required when the audit depends on not knowing the hidden answer.

Examples:

- reveal fairness;
- earliest reader inference;
- first-read effect;
- discovery convergence.

If independence is unavailable:

`UNVERIFIED`

not:

`PASS`.

### Full Manuscript Audit

Covers the complete persisted manuscript.

Chapter audits do not count as a substitute.

### Prepublication Audit

Final integrated pass after revision and full re-audit.

---

# 17. EVIDENCE POLICY

Universal rule:

> Intent is not evidence. A production report is not evidence. A previous PASS is not evidence.

Evidence must come from the relevant artifact.

For HARD-* and reveal-critical claims, PASS should contain:

```text
SOURCE
LOCATOR
EVIDENCE
RESULT
```

This makes auditing reproducible.

---

# 18. AUDIT MUTATION FIREWALL

Auditor may:

- inspect;
- classify;
- compare;
- flag;
- propose.

Auditor must not silently:

- rewrite manuscript;
- change state;
- change style baseline;
- accept deviation;
- alter authority;
- close an open decision.

Revision is a separate operation.

---

# 19. STAGE MODEL

v0.3 retains the production lifecycle but makes stage exits explicit.

## STAGE 0 — INTAKE

Input:
- author idea;
- constraints;
- available information.

Exit:
- minimum Creative Brief exists;
- unknowns correctly marked;
- no hidden AI decision masquerades as author choice.

## STAGE 1 — CREATIVE BRIEF LOCK

Exit:
- project fields recorded;
- AI-decided items exposed;
- author decisions recorded;
- active modules determined;
- scope mode declared;
- capability profile known or marked unknown.

## STAGE 2 — GENRE / PROSE CONTRACT

Exit:
- genre contract exists where relevant;
- prose contract exists;
- style calibration trigger known.

## STAGE 3 — STYLE CALIBRATION

Exit:
- STYLE BASELINE exists;
- diagnostics performed;
- corrections completed if needed;
- STYLE LOCK recorded.

## STAGE 4 — DEVELOPMENT

Possible paths:

```text
ARCHITECT
DISCOVERY
HYBRID
```

Exit:
- approved development artifact exists;
- planned material is represented;
- AI-decided items are visible;
- synopsis approval semantics are satisfied.

## STAGE 5 — PRODUCTION

Exit for a unit:
- unit persisted;
- artifact state updated;
- local continuity checked;
- allowed diagnostics completed;
- no unresolved blocking hard conflict.

Author checkpoint frequency depends on participation mode.

## STAGE 6 — DRAFT COMPLETION

Exit:
- all intended production units exist;
- synopsis/plan coverage checked;
- HARD requirements checked;
- ending/promise condition satisfied where relevant;
- scope record updated if scope is active.

## STAGE 7 — FULL MANUSCRIPT AUDIT

Exit:
- all required passes executed;
- coverage recorded;
- independent-only passes either completed or explicitly UNVERIFIED.

## STAGE 8 — REVISION

Cycle:

```text
DIAGNOSE
→ LOCATE
→ PROPOSE
→ TEST
→ REWRITE
→ RE-AUDIT
→ RECORD
```

Exit:
- targeted issues resolved;
- no silent substantive changes;
- relevant audits re-run.

## STAGE 9 — PREPUBLICATION

Exit:
- final full manuscript audit passed;
- required independent checks passed;
- change ledger complete;
- export artifact successfully assembled;
- no blocking UNVERIFIED conditions.

Only then may:

`PUBLICATION READY`

be assigned.

---

# 20. AUTHOR PARTICIPATION MODES

The author should not be forced into one interaction pattern.

Possible modes:

```text
HIGH-COLLABORATION
BALANCED
AUTONOMOUS-WITH-GATES
```

## HIGH-COLLABORATION

Frequent checkpoints.

## BALANCED

AI proceeds through routine work and pauses at major decision gates.

## AUTONOMOUS-WITH-GATES

AI may proceed across routine production units but MUST STOP on load-bearing decisions and hard conflicts.

Changing participation mode is an author decision and is recorded in Project State.

---

# 21. AI MAY PROCEED / MUST STOP / PROPOSE

## AI MAY PROCEED

Only already-authorized or mechanical actions:

- write the next scene/unit from accepted plan;
- maintain state;
- persist text;
- run allowed diagnostics;
- perform mechanical repairs;
- apply locked prose baseline;
- update navigation notes without changing canon.

## AI MUST STOP

- unresolved HARD conflict;
- load-bearing decision not authorized;
- DEFERRED decision becomes necessary;
- requested scope changes materially;
- ending changes;
- protagonist identity/core arc changes;
- form changes;
- reveal architecture changes;
- authority class changes;
- unavailable capability makes a required gate unverifiable.

## AI PROPOSES

When a better solution is possible but not already authorized.

It presents:

- problem;
- options;
- trade-offs;
- consequences;
- voice risk.

---

# 22. CONDITIONAL MODULES

## 22.1. HIDDEN WORLD / REVEAL

Activate only if:
- hidden truth exists;
- reveal timing matters;
- audience knowledge differs materially from world truth.

Contains:
- hidden ontology;
- reader knowledge;
- discovery fairness;
- reveal integrity;
- epistemic bridges;
- blind reader audit;
- ontology persistence.

## 22.2. SERIES

Activate when:
- continuation architecture is intended.

Contains:
- book state;
- series arc;
- escalation;
- reserved reveals;
- long-term continuity.

## 22.3. IP / CROSS-MEDIA

Activate when:
- explicit cross-media intent exists.

Contains:
- core world truth;
- medium adaptation;
- audience knowledge;
- license/marketing expression;
- asset register.

## 22.4. COMMERCIAL

Activate when author requests commercial analysis.

Commercial data may influence:
- positioning;
- packaging;
- audience targeting;
- marketing hypotheses.

It must not silently rewrite:
- artistic core;
- character psychology;
- theme;
- ending;
- world truth.

## 22.5. GENRE MODULES

Activated by genre.

Genre contract is a diagnostic lens, not an absolute artistic law.

## 22.6. LOCALE MODULE

Language/cultural production rules belong here.

For the current user workflow, Russian is the primary target locale.

---

# 23. BOOTSTRAP ARCHITECTURE

## 23.1. One canonical bootstrap

The system has one source of truth:

`BOOTSTRAP CORE`

It contains two branches.

### NEW CHAT

Used when the model/runtime is essentially unchanged but the chat context is new.

Sequence:

```text
VERIFY VERSION
→ VERIFY ARTIFACT INTEGRITY
→ LOAD MANUSCRIPT / STATE
→ DETERMINE CURRENT STAGE
→ LOAD ACTIVE MODULES
→ RESTORE STYLE LOCK
→ CHECK BLOCKERS
→ STATE NEXT AUTHORIZED ACTION
```

### NEW MODEL

All above plus:

```text
PROFILE CAPABILITIES
→ RECALCULATE OUTPUT BUDGET
→ RE-ANCHOR STYLE FROM STYLE BASELINE
→ VERIFY ACTIVE MODULE COMPATIBILITY
→ RECHECK CAPABILITY-DEPENDENT VERDICTS
→ MARK UNSUPPORTED VERDICTS UNVERIFIED
```

## 23.2. Thin launch wrappers

For usability, distribution may provide:

```text
NEW_CHAT
NEW_MODEL
```

as thin wrappers around the canonical bootstrap.

They must not contain divergent rules.

---

# 24. SCHEMA SET

v0.3 requires explicit schemas rather than fields described only in prose.

Minimum schemas:

```text
creative_brief.schema
project_state.schema
scope_record.schema
style_baseline.schema
style_lock.schema
capability_profile.schema
active_modules.schema
hard_requirements.schema
deviation_record.schema
audit_coverage.schema
change_log.schema
handoff.schema
```

Schemas should be portable plain text / Markdown / JSON-compatible where appropriate.

---

# 25. UNIVERSAL TXT DISTRIBUTION

For weak or context-limited models, provide a deterministic sequence.

Recommended:

```text
00_START_HERE.txt
01_CORE.txt
02_RUNTIME.txt
03_CREATIVE_BRIEF.txt
04_GENRE.txt
05_PROSE.txt
06_DEVELOPMENT.txt
07_SYNOPSIS.txt
08_PRODUCTION.txt
09_REVISION.txt
10_AUDIT.txt
11_PREPUBLICATION.txt
12_STATE.txt
13_EXPORT.txt
20_CONDITIONAL_HIDDEN_WORLD.txt
21_CONDITIONAL_SERIES.txt
22_CONDITIONAL_IP.txt
23_CONDITIONAL_COMMERCIAL.txt
30_TEMPLATES.txt
40_SCHEMAS.txt
90_REFERENCE.txt
```

`20+` conditional modules are loaded only when active.

The TXT distribution must not require a model to load the entire system into a single context.

---

# 26. NATIVE SKILL DISTRIBUTION

Canonical native structure:

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

`SKILL.md` is an entrypoint/router, not the entire system.

---

# 27. VERSIONING

Single source:

```text
WRITER-TOOLKIT VERSION = 0.3
SCHEMA VERSION = 0.3
BOOTSTRAP VERSION = 0.3
```

Change history is stored outside the operational Core.

No automatic state migrations are required at this architectural stage.

Bootstrap must detect:

- Toolkit version mismatch;
- Schema mismatch;
- missing required artifacts;
- stale project state;
- incompatible capability-dependent audit results.

---

# 28. MIGRATION v0.2 → v0.3

Migration is conceptual first; exact migration scripts come later.

## Keep

- Author Sovereignty;
- Authority/Decision/Artifact separation;
- Core Development Loop;
- Causality;
- Character architecture;
- Knowledge discipline;
- Form-scale principle;
- Framework-as-lens rule;
- Anti-AI prose principles;
- Revision protocol;
- Commercial firewall;
- evidence policy.

## Move

- Hidden-world → conditional module;
- Locale → locale module;
- Commercial/IP → conditional modules;
- Framework bibliography → reference;
- Runtime budget → adapter;
- form-specific production logic → form modules.

## Replace

- RESPONSE-BUDGET / CHAPTER-SIZE → separate contracts;
- vague Style Calibration → Style Baseline/Lock;
- state precedence list → split manuscript/decision authority;
- DEFERRED loophole → explicit firewall;
- implicit capability assumptions → capability profile.

## Add

- MANUSCRIPT persistence;
- SCOPE_RECORD;
- STYLE_BASELINE;
- STYLE_LOCK;
- AI-DECIDED;
- DEVIATION_RECORD;
- CAPABILITY_PROFILE;
- ACTIVE_MODULES;
- role model;
- audit independence class;
- canonical bootstrap;
- schemas.

## Remove from Core

- stress-test journal;
- hidden-world material as always-loaded instruction;
- universal one-response chapter rule;
- universal numeric volume assumptions;
- test-specific narrative parameters.

---

# 29. ACCEPTANCE CRITERIA FOR v0.3 ARCHITECTURE

Before implementation, the architecture specification itself is accepted only if a reviewer can answer “YES” to all:

1. Can a short story use it without receiving a novel pipeline?
2. Can a novel use it without assuming a fixed length?
3. Can the author leave scope UNKNOWN?
4. Can the author use discovery mode?
5. Can a screenplay avoid prose-only rules?
6. Can hidden-world modules remain completely inactive?
7. Can commercial/IP remain completely inactive?
8. Can Russian remain the current target locale without making the architecture logically Russian-only?
9. Can a model with no file system still persist state in portable form?
10. Can a file-capable runtime assemble a chapter across multiple outputs?
11. Can a model proceed without asking approval for every routine step?
12. Can it never silently convert a load-bearing unresolved decision into canon?
13. Can audit findings be produced without changing the manuscript?
14. Can an audit report UNVERIFIED instead of fabricating PASS?
15. Can a new model re-enter the project without relying on hidden previous chat memory?
16. Can manuscript text survive context loss?
17. Can style be re-anchored after model change?
18. Can the system distinguish a project decision from a runtime limitation?
19. Can a project remain smaller or larger than any previous test without breaking the Toolkit?
20. Can no prior stress-test decision leak into Core?

---

# 30. ANTI-DRIFT TESTS

Before calling v0.3 complete, run at least these project variants:

### Test A — short literary story
No mystery, no series, no IP, unknown initial volume.

### Test B — long commercial genre novel
Defined scope, explicit genre contract, no hidden ontology.

### Test C — hidden-world story
Short form, complex epistemic reveal.

This verifies that complexity and feature activation are independent.

### Test D — screenplay
No chapters, screenplay-specific production units and volume metric.

### Test E — discovery writer
Scope initially UNKNOWN, architecture emerges during production.

### Test F — model switch
Same project moved to another model/runtime.

### Test G — context loss
Old chat disappears; only persisted package remains.

### Test H — constrained runtime
Small response budget requires chunked manuscript assembly.

---

# 31. NON-GOALS

v0.3 does not attempt to:

- quantify artistic quality with one score;
- guarantee commercial success;
- guarantee publication success;
- replace an editor or human reader;
- decide author's artistic goals;
- create a universal theory of literature;
- force one narrative structure;
- force one prose style;
- make every audit independent;
- eliminate all model-specific behavior.

---

# 32. FINAL ARCHITECTURAL FORMULA

The intended v0.3 system is:

```text
AUTHOR
  ↓
PROJECT CONTRACT
  ↓
CORE AUTHORITY + STATE
  ↓
FORM / PROJECT FLAGS
  ↓
ACTIVE MODULES
  ↓
PROSE BASELINE / STYLE LOCK
  ↓
DEVELOPMENT
  ↓
PRODUCTION
  ↓
PERSISTED MANUSCRIPT
  ↓
DIAGNOSTICS
  ↓
FULL AUDIT
  ↓
REVISION
  ↓
RE-AUDIT
  ↓
PUBLICATION PACKAGE
```

Runtime sits beside the process:

```text
RUNTIME
  ├── capabilities
  ├── output budget
  ├── persistence
  ├── chunking
  └── external review
```

Runtime constraints are not allowed to silently redefine literary form.

---

# 33. IMPLEMENTATION ORDER

The actual v0.3 build should proceed in this order:

1. Canonical Core.
2. Canonical state schemas.
3. Creative Brief schema.
4. Scope Record.
5. Style Baseline/Lock.
6. Runtime/Capability Adapter contract.
7. Bootstrap Core.
8. Production/persistence contract.
9. Audit role and evidence model.
10. Conditional module contracts.
11. Universal TXT distribution.
12. Native Skill distribution.
13. Templates.
14. Regression tests.
15. New stress tests.

Do not write the final giant `SKILL.md` first.

Build the canonical architecture and schemas first, then compile distributions from it.

---

# 34. IMPLEMENTATION STATUS

This document is an architecture specification, not yet the final v0.3 Skill.

Canonical next artifact:

`WRITER-TOOLKIT_v0.3_BUILD_SPEC.md`

That build specification should turn every item above into:

- exact module contract;
- exact schema;
- exact trigger;
- exact gate;
- exact output;
- exact fail condition.

Only after that should the v0.3 modules be written.
