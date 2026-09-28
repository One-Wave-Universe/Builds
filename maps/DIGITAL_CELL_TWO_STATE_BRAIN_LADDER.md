# Digital CELL + Two-State Brain — Simulation Ladder

## Purpose

Build progressively capable **digital reference models** of the CELL/state-machine architecture. These models are controllers, computational devices, choosers, validators and workers. They are not evidence that the physical analog CELL works; they are executable specifications that can later be compared against hardware receipts.

## Common law at every level

Every capable unit has two explicitly represented sides:

- **FIELD** — expressed/current/external-facing candidate state.
- **VOID** — compressed/latent/internal-facing counterstate.

Neither side is simply input or output. A cycle compares both, resolves a next state, records a receipt, and re-enters.

Canonical software cycle:

```
OBSERVE
→ FIELD candidate
→ VOID counter/candidate
→ DIFFERENCE / RELATION
→ HOLD | CHOOSE | REJECT | REQUEST
→ ACT / EMIT
→ VALIDATE CONSEQUENCE
→ COMPRESS RECEIPT
→ REENTER
```

A unit may expose external Field/Void state and, at higher levels, maintain internal Field/Void state for deliberation. Internal dialogue is a capability of higher levels, not a requirement for simple parsers.

## Capability ladder

### L0 — Digital Cell
One deterministic two-state primitive with ternary resolution: negative / HOLD / positive. Inputs, state transition, history and output are inspectable. No language and no autonomous jobs.

### L1 — Parser Cell
Parses a bounded instruction or artifact into FIELD (present/expressed) and VOID (missing/required/contradicting) structures. Emits parse receipt and unresolved items.

### L2 — Validator Cell
Compares proposed output against declared contract, tests and evidence. Can PASS, HOLD/REQUEST, or REJECT. It never silently repairs evidence.

### L3 — Chooser Cell
Accepts multiple candidate actions, compares consequences/constraints, and chooses or HOLDs. Choice criteria are explicit and logged.

### L4 — Controller Cell
Runs a bounded observe→choose→act→validate loop against an external process. Has timeout, retry budget, stop condition and safe failure state.

### L5 — Worker Cell
Completes a defined job using tools/adapters. Separates task state from long-lived memory. Produces artifact + validation receipt.

### L6 — Recursive Worker
Can decompose one job into child jobs using the same contract. Child results compress back into parent state. Depth/budget is bounded.

### L7 — Field/Void Dialogue Worker
Maintains two internal proposal streams: FIELD develops an expressed solution; VOID searches for omissions, contradictions, alternatives and unexpressed dependencies. A resolver sees both. Dialogue is stored as structured state/claims, not treated as proof.

### L8 — Recall/Rebuild Worker
Retrieves stored references, reconstructs working context, compares reconstruction against source hashes/IDs, and marks uncertainty/missing sources. Recall is not copying an unlimited transcript into context.

### L9 — Persistent Reference Worker
Can nominate crucial information for durable storage. Permanent storage requires a declared reason, provenance, version and validation. New evidence creates a new version; it does not silently rewrite history.

### L10 — Multi-Worker Brain
Specialized parser, validator, chooser, controller, memory/rebuild and domain workers coordinate through the same two-state protocol. No worker has implicit authority; permissions and arbitration are explicit.

### L11 — Embodied State-Machine Brain
Connects real/simulated senses, body state, cortex graphs, memory, chooser/controller and motor/action interfaces. Every sensory source remains tagged real/simulated.

### L12 — Full Digital Reference Brain
Complete executable reference for the proposed two-state architecture: internal/external Field/Void state, recursive workers, sensory cortex, dreamscape adapters, persistent crucial references, reconstruction, action, validation and bounded self-monitoring.

This is the highest digital reference level, not a claim of consciousness or biological equivalence.

## Memory classes

1. **Transient** — current cycle/scratch state; disposable.
2. **Working** — active job graph and current reconstructed context.
3. **Recall index** — addresses/provenance needed to rebuild context from authoritative sources.
4. **Learned summary** — compressed reusable result with source links and confidence.
5. **Crucial permanent reference** — small, explicitly promoted canonical facts/contracts/decisions that must survive restart.

Permanent references require:
- stable ID;
- exact claim/contract;
- provenance/source IDs;
- created/version timestamp;
- validation status;
- supersedes/superseded-by relationship;
- reason it is crucial;
- tests or conditions that would invalidate it.

## Recall vs rebuild

**Recall** finds candidate references.
**Rebuild** reconstructs the current working model from those references and checks it against canonical sources.
**Stored memory** is not automatically current truth.

## Internal dialogue boundary

At L7+, FIELD and VOID may conduct an internal structured debate. The useful artifact is:
- candidate claims;
- counterclaims;
- missing evidence;
- alternatives;
- selected action;
- reason/constraint receipt.

Do not require hidden free-form monologue as an API. The system should expose inspectable structured reasoning state sufficient to test behavior without depending on private chain-of-thought.

## Programming stack

- Python: executable reference/runtime and test harness.
- DCACRC-IR: hardware-neutral state/flow language shared with sensory/cortex work.
- JSON/JSONL: manifests, state, receipts, memory records and replay.
- Later analog backend: compiles only validated DCACRC-IR primitives to physical CELL targets.

## Gold tests at every level

- deterministic replay;
- explicit Field/Void state;
- HOLD is valid;
- malformed/contradictory input fixture;
- bounded loops;
- no silent evidence fabrication;
- state serialization/restart;
- source/provenance retention;
- negative fixture;
- receipt comparison after upgrades.

Higher levels additionally require memory corruption/missing-source tests, worker disagreement tests, external-action permission tests and real-vs-sim sensory provenance tests.

## Relationship to Algorythm-Zer0

The ladder is the executable-worker hierarchy. Algorythm-Zer0 supplies recursive addressing/transform vocabulary where appropriate; it does not replace the state-machine contracts. Integration must be tested level by level rather than assuming the 1→6 conceptual hierarchy automatically implements software control.

## Build order

L0→L1→L2→L3→L4 first. These become reusable primitives.
Then L5/L6 workers.
Then L8/L9 memory reconstruction and permanent-reference mechanics.
Then L7 structured internal Field/Void dialogue.
Then L10 multi-worker brain.
Finally connect L11/L12 to sensory cortex, dreamscape and embodied controller.
