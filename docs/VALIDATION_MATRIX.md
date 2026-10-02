# Validation Matrix

| Area | Status | Meaning |
|---|---|---|
| Architecture | VERIFIED | Canonical architecture contract exists |
| Build contract | VERIFIED | Build requirements and acceptance boundaries are documented |
| Schemas | VERIFIED | Canonical schema layer materialized |
| Native Skill | VERIFIED | Entrypoint and canonical bootstrap are present |
| Universal TXT | VERIFIED | Portable distribution and load order are defined |
| FORM | VERIFIED | Form-aware routing is implemented, including screenplay profile |
| Phase H | VERIFIED | TEST-01..TEST-13 regression passed |
| Synthetic E2E | VERIFIED | Lifecycle contracts exercised with controlled fixtures |
| Anti-drift | VERIFIED | Variant validation checks that core assumptions do not drift |
| Arbitrary LLM behavioral compliance | UNVERIFIED | External model behavior cannot be proven from static files |
| Cross-model behavioral portability | UNVERIFIED | Requires runtime testing on the target model/runtime |
| Independent reader verification | CONDITIONAL | Requires an actually independent reviewer |

## Important interpretation

`VERIFIED` means the corresponding package artifact or controlled validation exists. It does not mean that every external LLM will obey the contract without runtime enforcement.
