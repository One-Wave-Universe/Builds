# Repository Reading Protocol for Peer AIs

A peer AI asked to review One-Wave work must inspect repository evidence before offering project-specific conclusions.

## 1. Establish scope
Identify the target repository and question. Do not treat Builds, One-Wave-Science, and Bridge-Comand as interchangeable:
- Builds: engineering implementations, CELL, digital references, dialogue/Foreman.
- One-Wave-Science: hypotheses, assumptions/transformations, simulations, datasets/controls, scientific validation.
- Bridge-Comand: routing, relay, receipts, machine/provider transport.

## 2. Find authority before interpretation
Read repository README/index/map files first. Search for dated corrections, CANON, CONTRACT, GOLD_STANDARD, assumption/transformation contracts, and explicit supersession language. Newer explicit corrections override contradictory older notes. Do not silently merge incompatible versions.

## 3. Follow references
When a document points to another file, assumption ID, transformation ID, fixture, dataset, receipt, issue, or commit needed to understand a claim, inspect it before judging that claim. Distinguish an idea mentioned in prose from an implemented/tested component.

## 4. Evidence classes
Label important statements as one of:
- ESTABLISHED EXTERNAL INGREDIENT
- PROJECT HYPOTHESIS
- SIMULATION RESULT
- BENCH RESULT
- IMPLEMENTATION/REPO EVIDENCE
- UNRESOLVED

A commit or passing software test does not prove a physical theory. A scientific analogy is not evidence of equivalence.

## 5. Science review
For One-Wave-Science, inspect the assumption/transformation contract, controls/nulls, units, parameter freedom, provenance, uncertainty, residuals, held-out tests, and validation status. Prefer attempts that can falsify or discriminate the hypothesis over pattern matching.

## 6. Attack productively
"Attack the science" means identify the highest-leverage weak point and design a discriminating test. Do not optimize for agreement with the project's theory. Look for:
- unconstrained/free parameters;
- missing conventional/null comparator;
- dimensional/unit failures;
- selection effects;
- overfitting;
- non-independent datasets;
- unfalsifiable mappings;
- transforms that manufacture expected structure;
- predictions that differ from standard models;
- the smallest experiment/simulation that can kill or strengthen a claim.

## 7. Output
Return:
- files/contracts actually inspected;
- strongest current scientific claim worth testing;
- weakest dependency beneath it;
- best falsification/discrimination attack;
- required real data and controls;
- pass/fail or comparative metric;
- what result would weaken the hypothesis;
- what result would justify the next test but NOT universal proof;
- concrete next repo job.

If repository access is unavailable, say so and request/use an authorized route. Never pretend to have read files you did not retrieve.
