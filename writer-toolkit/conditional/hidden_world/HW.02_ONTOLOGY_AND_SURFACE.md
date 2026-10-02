# HW.02 — Ontology and Surface

## Purpose

Keep the actual world model distinct from the model that characters and readers can reasonably construct before the reveal.

## Required separation

```text
HIDDEN_ONTOLOGY
SURFACE_MODEL
PUBLIC_BELIEF
CHARACTER_INTERPRETATION
READER_INTERPRETATION
```

## Rule

The model may use knowledge of hidden ontology for planning, but prose generation must respect the active character/reader epistemic state.

## Check

For every hidden element ask:

```text
Could the current viewpoint legitimately know this?
Could the current character infer this from available evidence?
Does the wording leak ontology through terminology or authorial framing?
```

An answer of `NO` to the first two questions is a block against direct assertion, not a license to invent a different fact.
