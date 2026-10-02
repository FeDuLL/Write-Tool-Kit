# PRODUCTION ENGINE

**Layer:** ENGINE  
**Activation:** when draft production is authorized  
**Dependencies:** Core + Brief + Prose + Development + active conditional modules

## PURPOSE

Produce the defined production unit without allowing runtime response limits to
define the literary unit or scope.

## PRODUCTION UNIT

Project-defined:

```text
CHAPTER
SCENE
SEQUENCE
EPISODE
OTHER
```

The runtime does not determine the unit.

## PROCESS

```text
UNIT GATE
→ WRITE UNIT
→ DIAGNOSTICS
→ PERSIST MANUSCRIPT
→ UPDATE STATE
→ UNIT COMPLETE GATE
```

## HARD RULE

A unit is not complete while its manuscript text is not persisted.

## SCOPE RULE

Response Budget ≠ Chapter Size.

Where output limits exist, use a safe chunking/assembly path when available;
do not silently shrink or reshape the literary unit.


## FORM ROUTING

Before `PROD.01_PRODUCTION_UNIT`:

```text
FORM CONTRACT → PRODUCTION UNIT
```

When `FORM = SCREENPLAY`, route to `FORM.03_SCREENPLAY_PROFILE`.

The production engine must never infer `CHAPTER` solely from prose habits or runtime constraints.
