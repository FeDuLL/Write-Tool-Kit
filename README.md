# Write-Tool-Kit

## WRITER-TOOLKIT v0.3

Model-independent operational system for long-form literary development, production, persistence, revision, and audit.

This repository contains the canonical documentation and runtime distribution of **WRITER-TOOLKIT v0.3**. The system is designed to work across different LLMs and runtimes without transferring authorship of irreversible artistic decisions to the model.

### Architecture

```
AUTHOR
→ PROJECT CONTRACT
→ CORE AUTHORITY + STATE
→ FORM / PROJECT FLAGS
→ ACTIVE MODULES
→ PROSE BASELINE / STYLE LOCK
→ DEVELOPMENT
→ PRODUCTION
→ PERSISTED MANUSCRIPT
→ DIAGNOSTICS
→ FULL AUDIT
→ REVISION
→ RE-AUDIT
```

### Core principles

- **Author Sovereignty** — the author retains final authority over canon and irreversible artistic decisions.
- **MANUSCRIPT / STATE / DIGEST separation** — literal text, accepted decisions/execution state, and navigation summaries are distinct artifacts.
- **DEFERRED ≠ permission** — an unresolved load-bearing decision blocks continuation unless autonomous determination is explicitly authorized.
- **AI MAY PROCEED ≠ AUTHOR APPROVAL** — routine authorization is not acceptance of artistic content.
- **Audit Mutation Firewall** — audit is read-only; manuscript-changing revision is a separate operation.
- **Style Baseline + Style Lock** — style is restored from project evidence, not silently replaced by model preference.
- **Response Budget ≠ Chapter Size** — runtime limits are handled by chunking/persistence/assembly, not by redefining literary form.
- **Conditional Modules** — hidden world, commercial, series, cross-media, locale, and genre rules activate only when the project requires them.
- **UNVERIFIED is a valid result** — unavailable evidence or capabilities are never fabricated as PASS.
- **Project parameters do not become universal Core rules** — stress-test assumptions remain test data.

### Repository layout

```
docs/                       Development record and validation
writer-toolkit/             Native Skill / canonical runtime distribution
writer-toolkit-universal/   Model-independent TXT distribution
tests/                      Validation material
```

### Native Skill

Entry point: `writer-toolkit/SKILL.md`

Canonical startup: `writer-toolkit/BOOTSTRAP.md`

Canonical architecture:
`writer-toolkit/reference/WRITER-TOOLKIT_v0.3_ARCHITECTURE_SPEC.md`

Canonical build contract:
`writer-toolkit/reference/WRITER-TOOLKIT_v0.3_BUILD_SPEC.md`

### Universal distribution

The Universal TXT package is intended for environments that cannot load a native skill directory. It uses a canonical load order and thin wrappers so that model changes do not silently create a second architecture.

### Validation status

The v0.3 package has passed structural/schema validation, FORM validation, Phase H regression, synthetic end-to-end runtime tests, and anti-drift variant testing.

Behavioral portability across arbitrary external models remains a separate verification question. In particular, the toolkit does not claim that any LLM will automatically obey every contract merely because the files are present.

### What this project does not claim

- no universal numeric KPI for literary quality;
- no guarantee of commercial or publishing success;
- no guarantee that a model's self-audit is epistemically independent;
- no elimination of model-specific behavior;
- no replacement of author judgment.

### Development rule

Architecture changes are made only after a reported issue is reproduced and classified as:

`REAL DEFECT` / `FALSE POSITIVE` / `DESIGN CHOICE` / `UNVERIFIED`

This prevents external audit suggestions or model behavior from silently becoming architecture.

## Status

**Version:** 0.3  
**Baseline:** 2026-10-02  
**State:** canonical v0.3 package being transferred to GitHub

## License

No license is declared yet. The repository owner should choose the license before treating the project as an open-source distribution.
