# Jetson GPU FIELD Adapter Plan

## Goal
Replace the reference FIELD backend with a Jetson GPU adapter where parallel execution is useful, while preserving identical router/receipt semantics.

## Candidate GPU jobs
- audio filterbank / spectral transforms;
- image local-contrast, edge/orientation and motion fields;
- parallel digital-CELL populations;
- dreamscape sensory rendering/state transforms;
- candidate-state expansion for bounded chooser jobs.

## CPU / VOID remains responsible for
- contracts and permissions;
- provenance checks;
- HOLD/stop decisions;
- memory lookup/rebuild;
- acceptance validation;
- retry/depth budgets;
- Foreman receipts.

## Gold comparison
For every promoted GPU operation:
1. frozen input fixture;
2. CPU reference output;
3. GPU output;
4. numerical tolerance;
5. timing/load receipt;
6. mismatch report;
7. deterministic/reproducibility declaration where achievable.

GPU speed alone does not promote an implementation. It must preserve declared semantics within tolerance.
