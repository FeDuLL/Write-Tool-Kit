# Forensic Reconciliation

This document records the final reconciliation principles used to stabilize WRITER-TOOLKIT v0.3.

## Resolved areas

- universal volume assumptions were removed;
- response budget was separated from chapter size;
- hidden-world behavior became conditional rather than universal;
- manuscript/state precedence was made explicit;
- DEFERRED gained a load-bearing decision firewall;
- style calibration and Style Lock became explicit;
- audit mutation was separated from revision;
- runtime capability assumptions were isolated in adapters;
- conditional modules were separated from Core;
- bootstrap portability was formalized;
- numeric literary KPIs were rejected as universal requirements;
- status language was tightened so UNVERIFIED is not silently converted into PASS.

## Reconciliation principle

The architecture must distinguish mechanism, project parameter, domain rule, runtime capability, and experiment.

A successful stress test may reveal a defect. It may not, by itself, define a universal rule.

## Evidence boundary

Static package validation can prove the presence and internal consistency of files and contracts. It cannot prove that an arbitrary external model will behave correctly under every runtime condition.
