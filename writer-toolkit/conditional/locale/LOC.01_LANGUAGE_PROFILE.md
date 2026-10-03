# LOC.01 — Language Profile

## Required fields

```text
PRIMARY_LANGUAGE
SECONDARY_LANGUAGES
SCRIPT
REGISTER
DIALECT / SOCIOLECT REQUIREMENTS
ORTHOGRAPHY / SPELLING CONVENTION
PUNCTUATION CONVENTION
TRANSLATION POLICY
TERMINOLOGY POLICY
```

## Runtime rule

Language profile is part of project state and must survive chat/model transitions.

A model may use local linguistic knowledge, but unresolved project-specific terminology remains open rather than silently canonicalized.
