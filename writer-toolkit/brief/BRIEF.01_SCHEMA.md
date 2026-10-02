# BRIEF.01_SCHEMA

**ID:** `BRIEF.01_SCHEMA`

## Required fields

```
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

## Field state

Every substantive field uses:

```
DECISION_STATE:
UNKNOWN | OPEN | DEFERRED | PROPOSED | ACCEPTED | REJECTED

SOURCE:
AUTHOR | AI | DERIVED | EXTERNAL
```

`DERIVED` does not mean accepted.

A derived value remains non-authoritative until the applicable authority rules
make its status explicit.

## Acceptance conditions

A brief field may be used as an author decision only when its decision state is
`ACCEPTED` under the applicable authority rules.

`UNKNOWN`, `OPEN`, `DEFERRED` and `PROPOSED` remain unresolved/non-authoritative.

## Scope boundary

This schema describes brief data. It does not select a genre, prose style,
scope, or structural mode on the author's behalf.
