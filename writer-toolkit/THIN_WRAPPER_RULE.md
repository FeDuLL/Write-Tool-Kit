# THIN WRAPPER RULE

Launch wrappers are convenience entry points only.

They may identify:
- the trigger;
- the canonical branch;
- the persisted package to load.

They must not redefine:
- authority;
- state;
- prose;
- capabilities;
- audit;
- persistence;
- deviations;
- module activation;
- publication status.

Canonical source: `BOOTSTRAP.md`

If a wrapper conflicts with the canonical bootstrap, the wrapper is defective.
