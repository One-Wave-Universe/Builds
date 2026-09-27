# CELL_V1 + ALGORYTHM-ZER0 — MASTER CURRENT STATE

**Status:** current master handoff for build, review, presentation, and next experiments.

This file is intended to be read first.

It does **not** claim that CELL_V1 is proven or that Algorythm-Zer0 is fully implemented.

Its job is to hold the current architecture together, preserve what is actually locked, identify what is still open, and define the smallest useful next tests.

---

# 1. Current project split

There are two related but distinct systems:

## CELL_V1
The proposed **physical analog body / control cell**.

CELL_V1 is where:
- differential state exists physically;
- CENTER/(0) exists physically;
- hysteresis / retained state must exist physically;
- action returns as consequence;
- inductive energy may return to V_BUS;
- sensor / motor / higher-role nuclei are physically different;
- no software value is allowed to pretend it is the body's retained memory.

## Algorythm-Zer0
The proposed **recursive state-description / routing / rebase grammar**.

Zer0 currently defines:
- how state is organized;
- how lower context is retained at higher levels;
- how Field and Void counter-check;
- how views move up and actions move down;
- how a completed cycle produces a new reference.

Zer0 is **not currently the physical controller**.

That distinction is critical.

---

# 2. Does Algorythm-Zer0 have a part to play yet?

**Yes — but not yet as the final runtime controller.**

Its useful role **right now** is:

1. **Experiment structure**  
   Zer0 defines the sequence that a complete physical test should eventually demonstrate:
   
   ```text
   REFERENCE
   -> CHOICE / POLARITY
   -> MOVE
   -> VIEWS UP / ACTIONS DOWN
   -> STATE / SCALE
   -> RESOLVE / REBASE
   -> NEW REFERENCE
   ```

2. **Traceability / provenance**  
   Every higher level should retain the lower-level state that produced it.

3. **Test oracle**  
   Zer0 can define what counts as a complete cycle without becoming the mechanism that performs the cycle.

4. **Measurement organization**  
   Physical measurements can be tagged against X/Y/Z/T and level 1..6 to see whether the physical system actually supports the intended recursive structure.

5. **Interface contract**  
   Zer0 can specify what information must survive between lower body loops and higher processing layers.

6. **Presentation / explanation**  
   It gives a coherent language for explaining why the architecture is nested, recursive, and reference-updating rather than a simple flat state machine.

7. **Implementation falsification**  
   If a proposed hardware mechanism cannot preserve lower-level context, support HOLD, return consequence, and produce a bounded next reference, it does not satisfy Zer0.

## What Zer0 must NOT do yet

Do not use Zer0 as:

- software memory for CELL_V1;
- a 1,296-entry lookup table;
- a hidden digital controller;
- a pretense that X/Y/Z/T already map cleanly to hardware;
- proof that the current vocabulary is correct;
- proof that the physical cell implements recursion.

The correct current statement is:

> **Zer0 is useful today as a recursive specification, test structure, and interface contract. It becomes part of runtime only after a real physical or analog mechanism can execute at least one complete recursive cycle without hidden digital arbitration.**

---

# 3. CELL_V1 physical lock

## 3.1 Normalized local state

- normalized axis span: **1.00 V**
- CENTER: **0.50 / 50**
- HOLD: **0.45–0.55 / 45–55**
- ternary state: **DOWN / HOLD / UP**
- signed relation: **- / (0) / +**
- HOLD is active balance, not OFF

CENTER/(0) is the active local virtual-ground reference.

CENTER is not V_BUS.

---

## 3.2 Six-sector local geometry

The current basic cell is a point-up hex containing six tapered triangular / pyramidal magnetic sectors:

```text
A+ B+ C+ A- B- C-
```

Opposed mirrors:

```text
A+ <-> A-
B+ <-> B-
C+ <-> C-
```

Current physical intent:

- one winding per sector;
- narrow tips converge toward the local center region;
- broad sector faces form the six cell faces;
- local opposed pairs interact tip-to-tip through the center relation;
- neighboring cells meet base-to-base;
- A/B/C remain three distinct differential axes.

Each A/B/C differential has a bidirectional center-gate candidate referencing shared CENTER/(0).

---

## 3.3 FIELD / VOID body-side rule

FIELD and VOID are the **two mirrored sides of the body architecture**.

Each CELL participates in both sides through exactly **two plain round body toroids total**:
- one FIELD-side toroid;
- one VOID-side toroid.

Each toroid carries separate A/B/C coupling windings.

FIELD and VOID are both active information/action sides. Neither is assigned permanently as input-only or output-only.

Both sides have mirrored V_BUS ingress and reinjection return while CENTER remains the shared local balance/reference relation.

# 4. Cell-role geometry

## Common body differential interface — all cells

Every cell role uses:

```text
two plain round outer/body toroids
```

These are:
- common across cell roles;
- the shared body / lattice differential interface;
- **not** figure-8 toroids.

## Specialized nuclei

| Cell role | Current nucleus |
| --- | --- |
| Sensor | one-piece round two-aperture figure-8 hysteretic core |
| Motor-control | one-piece square two-aperture figure-8 hysteretic core |
| M4 | dedicated two-pyramid / double-triangle nucleus |
| Five-mind | double pentagon |
| Six-mind | double hexagon |

There are **two distinct pyramid systems**:
1. **M4 nucleus:** two dedicated triangular/pyramidal toroidal loops base-to-base.
2. **Cluster-routing pyramids:** six tapered A+/B+/C+/A-/B-/C- wedges; opposed tips meet tip-to-tip inside a cell and wedge bases meet base-to-base between neighboring cells.

Do not merge these two structures.

The square figure-8 is **motor-control only**.

The geometry is currently planar / 2D; resulting magnetic fields are 3D.

---

# 5. First flower

Current first seven-cell flower:

- center: one motor-control cell;
- ring: six sensor cells;
- cells connect base-to-base at matching hex faces;
- each retains its own six-sector / three-mirror local geometry;
- the first flower already uses the general six-wedge pyramid-routing lattice;
- an M4 cell, when introduced, also has its own separate two-pyramid nucleus.

---

# 6. Core state rules

Current local decision rules:

```text
two agree -> push
one voice -> wait
opposition -> HOLD
gap -> wait
```

A/B/C are axes.

They are **not** voltage levels.

The seven bands describe expression/compression strength around CENTER.

CHOICE / PIVOT / FLIP remain separate from the seven bands.

POINT / PATH / FIELD are also separate scale concepts.

---

# 7. Seven-band normalized scale

| Range | State | Meaning |
| --- | --- | --- |
| 90–100 | +3 | extreme expression / danger |
| 75–85 | +2 | strong expression |
| 60–70 | +1 | moderate expression |
| 45–55 | 0 | active middle / stable oscillating region |
| 30–40 | -1 | moderate compression |
| 15–25 | -2 | strong compression |
| 0–10 | -3 | extreme compression / danger |

The unnamed gaps are intentional hysteresis / anti-chatter transition regions.

These are normalized bands, not final device voltages.

Do not implement them as a comparator ladder by default.

---

# 8. Hard control constraints

The current intended CELL mechanism does **not** use:

- global clock;
- timing-based commutation as the state authority;
- microcontroller state machine;
- FPGA;
- DSP controller;
- op-amp brain;
- comparator bank;
- LM339;
- software weight memory;
- resistor threshold ladders;
- resistor bleed paths;
- resistor damping returns;
- resistor dump loads as the intended energy return.

The target is discrete analog / magnetic / transistor-level / physical-state control.

Test instruments and computers may observe, simulate, log, and compare.

They must not become the hidden decision-maker.

---

# 9. Reinjection / V_BUS

V_BUS is the shared energy / readiness / reinjection rail.

CENTER is separate.

Recoverable inductive energy is steered toward V_BUS.

Current established basis:

- inductive energy storage;
- capacitive energy storage;
- controlled steering of inductive collapse;
- magnetic hysteresis / remanence.

Current hypotheses:

- return can stay sufficiently isolated from CENTER;
- returned energy can be shared usefully;
- return does not erase retained nucleus state;
- bus condition can provide useful local coordination;
- returned consequence can affect the next physical event.

No free-energy claim.

No fixed recovery percentage.

No designed resistor loss-return path.

---

# 10. Memory — local state, muscle memory, and reinjection

Physical memory is not a software receipt.

Current architecture separates three interacting physical roles:

1. **Local retained state** — hysteresis / remanence in the role-specific nucleus or local active path.
2. **Muscle memory / group memory** — a dedicated hysteretic body-state layer laid beneath the connected cells and following the shared lattice / edge routes. Repeated use can leave the preferred path already biased for the next action.
3. **Reinjection / V_BUS** — a separate power/recovery layer carrying returned energy, readiness, and short echo. Reinjection carries consequence back into the continuing loop, but bus voltage alone is not the long-term memory store.

So the process is one loop, but the storage roles are not identical.

Canonical shorthand:

```text
ACTION
-> local magnetic / actuator event
-> consequence + inductive collapse
-> reinjection to V_BUS
-> shared hysteretic lattice/path already carries prior-use bias
-> next traversal sees that changed path
-> next action
```

This is the muscle-memory idea: **the settled hysteretic path means the next event does not start from zero.**

Measure separately:
- local nucleus remanence / threshold bias;
- lattice Br / path bias;
- returned energy;
- V_BUS readiness / short echo;
- next-action bias after repeated use.

Those are separate measurements of one continuing physical process.

---

## Dedicated hysteretic body-state layer

The connected cell lattice requires its own physical hysteresis layer beneath the cells.

```text
cell nuclei / A-B-C / CENTER
          ↓ coupling
shared hysteretic body-state layer
          ↓
V_BUS power/reinjection layer (separate)
```

The layer should:
- span connected cells / flowers;
- follow shared edge and motor-route geometry;
- retain path history as Br / hysteretic bias;
- be writable by repeated action;
- influence later traversal;
- remain separate from CENTER and V_BUS electrically;
- support distributed body state and muscle memory.

This is now a core architecture requirement. Exact material and fabrication remain open.

## Phase-I body-state layer scope

For the current build, use **one connected domain-wall hysteretic body-state layer** under the cell lattice.

Current simple motor scope:
- wheel;
- propeller / rotor-style motion;
- other simple repeated motor paths that do not require independent articulated substructures.

Do **not** add nested body-state layers yet.

Nested muscle-memory layers are reserved for later articulated movement where local habits need to exist at multiple physical scales, for example:

```text
finger
-> hand
-> limb
-> body
```

The higher layer should preserve lower-level history rather than replace it.

Current rule:
- one layer first;
- test whether multiple simple motor routes can coexist without destructive interference;
- add a second / nested layer only when more complex movement requires physically separate retained coordination or measured cross-coupling makes one layer insufficient.

This keeps the first hardware simple while preserving the long-term nested body-memory architecture.

# 11. Best current prior-art anchors

These are comparison targets, not proof.

## Multi-aperture magnetic cores / transfluxors
Useful for:
- history-dependent shared magnetic paths;
- write / probe separation;
- old-state + new-excitation interaction.

Especially relevant to the one-piece two-aperture nuclei.

## Magnetic majority / current-summing logic
Useful for investigating:
- physical two-of-three coherence;
- cancellation around HOLD;
- asynchronous threshold crossing;
- no central digital vote.

This is a candidate precedent only.

## Non-dissipative flyback / regenerative DC-link return
Useful for:
- V_BUS energy return;
- avoiding intentional resistor dumps;
- separating energy recovery from retained magnetic state.

## Multiphase / reluctance / flux-summing magnetic geometry
Useful for:
- comparing six-sector A/B/C geometry;
- coupling;
- leakage;
- rotating field behavior;
- manufacturability.

## Adaptive-reference / moving-equilibrium / attractor systems
Useful only as comparison to Zer0's moving reference.

Do not rename Zer0 by analogy.

---

# 12. Highest-value physical tests

## Test A — retained-history nucleus test

1. apply controlled positive write;
2. remove drive;
3. apply fixed probe;
4. record response;
5. apply equal negative write;
6. apply same fixed probe;
7. compare.

Pass:
- repeatable state-dependent difference beyond noise / drift.

Fail:
- no reliable difference.

---

## Test B — moving-reference boundedness

Apply repeated same-direction events.

Measure:
- reference offset;
- saturation margin;
- repeatability;
- reversal response;
- decay.

Pass candidate:
- useful bounded new reference.

Fail:
- monotonic walk into saturation with no release / rebase mechanism.

---

## Test C — physical triadic coherence

Test A/B/C combinations:

- 2 aligned / 1 opposed;
- 1 aligned / 2 opposed;
- balanced opposition;
- near-HOLD combinations.

Measure:

- summed current / flux;
- CENTER motion;
- threshold crossing;
- chatter;
- history dependence;
- mismatch sensitivity.

Do not assume magnetic majority behavior until measured.

---

## Test D — V_BUS / CENTER isolation

During inductive return:

- measure V_BUS;
- measure CENTER simultaneously;
- vary bus load;
- compare nucleus state before / after return.

Fail:
- return corrupts CENTER or erases retained state beyond acceptable repeatability.

---

## Test E — six-sector mismatch

Perturb one sector thermally or magnetically.

Measure:
- opposed sector;
- neighboring axes;
- CENTER;
- V_BUS;
- next lean.

This shows whether the geometry contains error or spreads it.

---

# 13. Algorythm-Zer0 current canon

Four simultaneous branches:

```text
X = CONTROL
Y = STRUCTURE / ROTATION
Z = DEPTH
T = TIME / CHANGE
```

Six cumulative levels:

```text
L1 = REFERENCE
L2 = POLARITY / CHOICE
L3 = MOVE
L4 = VIEWS UP / ACTIONS DOWN
L5 = STATE / SCALE
L6 = RECURSE / RESOLVE / RETURN
```

Inclusion rule:

```text
L1 ⊂ L2 ⊂ L3 ⊂ L4 ⊂ L5 ⊂ L6
```

Cross-mirror rule:

```text
F1 <-> V6
F2 <-> V5
F3 <-> V4
F4 <-> V3
F5 <-> V2
F6 <-> V1
```

Moving reference:

```text
(0)t
-> interaction
-> consequence
-> resolve
-> (0)t+1
```

The four branches describe one event, not four separate programs.

---

# 14. Zer0's practical role right now

## Use it now for:

### A. Experiment records

Each physical test can record:

```text
X: what action/control relation occurred?
Y: what geometry/orientation/path was active?
Z: what magnitude/depth/relationship was expressed?
T: what changed, persisted, decayed, or rebased?
```

This does not make Zer0 the controller.

It makes Zer0 the **structured description of what the controller physically did**.

### B. Recursive test design

A test should progressively ask:

```text
What was the reference?
What choice appeared?
What move occurred?
What came back?
What state/scale resulted?
What became the next reference?
```

### C. Detecting architecture drift

If a proposed implementation:
- discards prior context;
- cannot distinguish HOLD from no signal;
- requires hidden digital arbitration;
- cannot show returned consequence;
- cannot create a bounded next reference;

then it is not implementing the intended recursive structure.

### D. Future body-to-cortex interface

If CELL hardware works, Zer0 may later become a useful common grammar for translating:

```text
physical body state
<-> compressed recursive state
<-> higher sensory / cortical processing
```

That mapping does **not** exist yet.

---

# 15. Zer0 is not yet allowed to claim

- end-to-end implementation;
- hardware execution of all X/Y/Z/T branches;
- physical realization of the full six levels;
- proven advantage over standard control systems;
- proven completeness of the 168-term vocabulary;
- proven usefulness of every primitive;
- proven 1,296-address physical map.

The address space is conceptual until a real need for those coordinates is demonstrated.

---

# 16. Known Zer0 repo conflict

The newer human-readable canon and the older machine-readable JSON do not fully agree.

Current presentation authority:

1. `algorithms/ALGORITHM_ZERO_PRESENTATION.md`
2. `algorithms/FOUR_BRANCHES_AND_UNIVERSAL_RULES.md`
3. `algorithms/thresholds.md`
4. `algorithms/IMPLEMENTATION_STATUS.md`
5. `algorithms/LEAN_INTO_ZER0.md`

`algorithm_zero_locked_canon.json` must not be treated as final authority until reconciled term-by-term.

---

# 17. DC / AC / RC status

Current project shorthand still needs technical reconciliation.

Current working use:

- DC = void / sustained bias / return-side relation;
- AC = field rotation / changing opposed lean;
- RC = remainder / returned consequence / views-up-actions-down relation.

Important:

**RC does not currently mean “resistor-capacitor implementation.”**

There is no locked resistor-based relaxation path in CELL.

The terminology may eventually need to change if established electrical terms describe the actual mechanisms better.

---

# 18. What is locked vs open

## Locked for current architecture

- hardware-first analog control target;
- CENTER != V_BUS;
- active ternary -/(0)/+;
- HOLD is live;
- six-sector A/B/C local geometry;
- common two plain-round body toroids;
- role-specific nuclei;
- square figure-8 is motor-control only;
- no global clock;
- no hidden digital controller;
- no designed resistor-based control / threshold / return path;
- thresholds / hysteresis matter;
- physical memory must remain physical;
- reinjection returns toward V_BUS;
- measure before claiming.

## Open

- exact core materials;
- exact MOSFET topology;
- gate translation method;
- exact turns and winding gauge;
- exact six-sector field geometry;
- exact common-toroid winding pattern;
- exact physical threshold mechanism;
- actual retention time;
- actual recovery fraction;
- actual torque / field strength;
- actual multi-cell coupling;
- exact Zer0-to-hardware mapping;
- whether all six Zer0 levels are physically necessary;
- whether all four branches remain orthogonal in a working system.

---

# 19. Immediate next build question

The highest-value next question is not:

> “How do we build the whole android?”

It is:

> **Can one physical CELL loop create a repeatable, bounded, history-dependent next state around CENTER, return recoverable energy to V_BUS without corrupting CENTER, and preserve enough context that Zer0 can accurately describe one complete recursive cycle?**

If yes, scale.

If no, find which premise failed.

---

# 20. Required review attitude

Question everything.

Do not defend terminology for its own sake.

Do not erase distinctions before understanding them.

Use existing engineering wherever it truly matches.

Use prior art to reduce invention burden.

Prefer a smaller physical mechanism that works.

Treat every unmeasured performance claim as open.

Keep:

```text
change one thing
-> test
-> compare with goal
-> check drift
-> after three failed repeats, change angle
```

---

# 21. Master source references

Current repo authorities:

- `RULES.md`
- `BUILD.md`
- `ARCHITECTURE.md`
- `cell-v1/CELL.md`
- `cell-v1/REINJECT_BUS.md`
- `REAL_WORLD_BUILD_HANDOFF.md` — current builder/engineer handoff for connecting every mechanism to real parts, materials, measurements, and falsifiable tests
- `cell-v1/PARTS.md`
- `cell-v1/BREADBOARD.md`
- `cell-v1/PRIOR_ART_AND_TEST_TARGETS.md`
- `algorithms/README.md`
- `algorithms/ALGORITHM_ZERO_PRESENTATION.md`
- `algorithms/IMPLEMENTATION_STATUS.md`
- `algorithms/FOUR_BRANCHES_AND_UNIVERSAL_RULES.md`
- `algorithms/LEAN_INTO_ZER0.md`
- `algorithms/thresholds.md`

---

**MASTER STATUS**

- CELL_V1: proposed physical architecture, not yet validated
- Zer0: useful specification / experiment grammar now; runtime implementation unresolved
- Reinjection: consequence/energy return path in the same closed process; not the long-term memory store by itself
- Local memory: role-specific nucleus / local hysteretic path
- Muscle memory: hysteretic lattice / shared edge magnetic traces; repeated-use bias to validate
- Triadic coherence: candidate physical mechanism, not yet proven
- Six-sector geometry: current build lock, physical advantage still to test
- Higher-role nuclei: architecture map only until lower cell passes


---

# 22. What validation looks like

Passing these tests validates the **Phase-I premises** of CELL_V1. It does **not** by itself prove the full cell, flower, higher nuclei, intelligence, or complete Zer0 runtime.

The tests are run in order. A failed prerequisite stops scale-up until the failure is understood.

## Test A — retained-history nucleus

**Question:** Does prior physical state measurably change the response to the same later probe?

**Method:**
1. apply a controlled write in one direction;
2. remove the write;
3. apply a fixed probe;
4. record response;
5. apply an equal write in the opposite direction;
6. apply the same probe;
7. compare repeated trials.

**Measure:**
- write current / voltage;
- probe response;
- remanence / inferred retained bias;
- thermal drift;
- repeatability;
- decay with time.

**Pass criterion:** a repeatable prior-state-dependent difference that remains separable from noise, drift, and measurement error.

**Fail criterion:** nominally different prior writes produce no repeatable difference.

**Fallbacks to test, one at a time:**
- different hysteretic material;
- different write amplitude / duration within safe limits;
- different turn count;
- different aperture / flux-path geometry.

Do not add software memory to rescue a failed physical-memory test.

## Test B — bounded moving reference

**Question:** Can the physical state influence the next reference without drifting blindly into saturation?

**Method:** repeat equal-direction events, then reverse and release.

**Measure:**
- cycle-to-cycle CENTER / effective reference shift;
- saturation margin;
- reversal response;
- relaxation / decay;
- hysteresis-loop displacement;
- repeatability.

**Pass criterion:** the next reference is measurably history-dependent **and bounded** over the tested operating range.

**Fail criterion:** the reference walks monotonically into saturation or becomes irrecoverable without an external hidden controller.

**Fallbacks to investigate:**
- different coercivity / loop shape;
- alternate physical release / rebasing path;
- separate magnetic path for retained bias;
- geometry changes that reduce accumulation.

A reset winding or other release mechanism is a **candidate experiment**, not locked architecture.

## Test C — physical triadic coherence

**Question:** Can A/B/C produce stable physical agreement / opposition outcomes without a digital arbiter?

Test:
- 2 aligned / 1 opposed;
- 1 aligned / 2 opposed;
- balanced opposition;
- one active / two near HOLD;
- all near HOLD;
- polarity-reversed equivalents.

**Measure:**
- summed current / flux;
- threshold crossing;
- CENTER motion;
- chatter;
- switching latency;
- history dependence;
- mismatch sensitivity.

**Pass criterion:** equivalent input relations resolve reproducibly, with HOLD physically distinguishable from OFF / missing signal.

**Fail criterion:** component mismatch or uncontrolled cross-coupling dominates the intended relation.

**Candidate precedents:** magnetic majority / current-summing systems, parametron-style analog summation, saturable magnetic thresholds.

These precedents do not prove the CELL geometry performs the function automatically.

## Test D — V_BUS / CENTER isolation and reinjection

**Question:** Can recoverable inductive energy return toward V_BUS without corrupting CENTER or erasing retained state?

**Method:**
- perform the same controlled drive / collapse event with return enabled and disabled;
- vary V_BUS loading within the safe test range;
- measure CENTER simultaneously;
- compare nucleus state before and after return.

**Measure:**
- E_in;
- E_rec;
- peak flyback voltage;
- V_BUS ripple;
- CENTER disturbance;
- return timing;
- retained-state change.

**Pass criterion:** measurable recovery with CENTER remaining within the allowed operating band and retained-state behavior remaining repeatable.

**Fail criterion:** return repeatedly corrupts CENTER, destabilizes the local differential, or erases / dominates the retained state.

**Fallbacks to investigate:**
- different steering topology;
- greater magnetic / electrical isolation;
- local reservoir changes;
- separate return path geometry.

No resistor dump / bleed / damping path is introduced as the intended solution.

## Test E — six-sector mismatch and cross-coupling

**Question:** Does the A/B/C geometry preserve usable opposed-axis behavior under real mismatch?

**Method:** perturb one sector thermally, magnetically, geometrically, or by controlled winding variation.

**Measure:**
- opposed partner response;
- neighboring-axis response;
- coupling matrix;
- leakage flux;
- CENTER shift;
- next-cycle lean;
- temperature dependence.

**Pass criterion:** intended axis relation remains distinguishable and repeatable under measured mismatch.

**Fail criterion:** all sectors collapse into uncontrolled common coupling or CENTER becomes dominated by one sector.

**Fallbacks to investigate:**
- revised taper / spacing;
- alternate flux guides;
- increased magnetic isolation;
- simpler geometry if it produces the same required function.

## Phase-I validation statement

If Tests A through E pass their measured criteria, the correct conclusion is:

> **The five Phase-I CELL_V1 premises survived bench validation in the tested configuration.**

Do **not** replace that with:

> “The whole CELL_V1 architecture is proven.”

The next scale step must add only one new claim at a time.

---

# 23. Candidate physical mechanisms for currently locked functions

These are **implementation candidates**, not new locks.

## CENTER distinct from V_BUS

Required function:
- CENTER remains the local differential reference;
- V_BUS carries shared energy / readiness / reinjection;
- return events must not redefine CENTER unintentionally.

Candidate mechanisms:
- physically separate conductors / rails;
- separate magnetic paths with measured coupling;
- local magnetic or transistor-level isolation;
- a dedicated physical buffer stage only if direct isolation fails.

Do not claim a specific square-loop isolation mechanism until it is built and measured.

## HOLD is live

Required function:
- current / field activity may remain present;
- no directional commit occurs inside the HOLD band.

Candidate mechanisms:
- coercive / hysteretic threshold;
- saturable magnetic threshold;
- opposed-current cancellation;
- paired physical thresholds creating a dead zone.

HOLD must not be defined merely as “drive disappeared.”

## Active ternary - / (0) / +

Required function:
- negative lean;
- live balanced HOLD;
- positive lean.

Candidate mechanisms:
- opposed current / flux paths around CENTER;
- dual physical thresholds around CENTER;
- magnetic threshold plus bidirectional steering;
- transistor-level current steering whose bias is set by the physical state rather than a resistor ladder.

## No global clock

Required function:
- transitions occur from physical state / threshold / consequence.

Candidate mechanisms:
- hysteretic threshold crossing;
- asynchronous magnetic switching;
- passive propagation / delay;
- physical ring / propagation structures if sequencing is later proven necessary.

A delay line is a candidate fallback, not a current lock.

## No designed resistor path

Required function:
- control thresholds and reinjection are not implemented by resistor ladders or resistor dump branches.

Candidate mechanisms:
- magnetic threshold;
- semiconductor junction threshold;
- diode steering;
- self-driven synchronous switching;
- inductive / capacitive / magnetic state.

Bench protection may use external current-limited equipment, but that protection does not become the architecture.

---

# 24. First bench target — corrected

The smallest useful first build is **one hysteretic multi-aperture / figure-8 nucleus under write-and-probe measurement**.

Do not lock arbitrary turn counts, pulse widths, currents, or pass percentages before the actual core material and safe operating region are known.

Minimum functions required:

- one controlled write winding / path;
- one probe / sense path;
- reversible write polarity;
- externally current-limited drive for safe characterization;
- oscilloscope measurement;
- repeated identical-probe comparison after opposite prior writes.

The first experiment is Test A.

Its purpose is not to prove the whole cell.

Its purpose is to answer one question:

> **Does this chosen physical nucleus retain enough measurable state that prior write history changes the response to the same later probe?**

If no, change material / geometry / winding conditions before building the full hex.

If yes, proceed to bounded-reference and triadic tests.

---

# 25. Prior-art interpretation guardrails

Verified historical mechanism classes worth studying include multi-aperture magnetic cores / transfluxors and parametron majority-style analog summation.

Use them as mechanism precedents only.

Do not infer from their existence that:
- CELL's semantics are already solved;
- HOLD has already been demonstrated in CELL;
- the six-sector geometry is validated;
- Zer0 is implemented;
- reinjection and memory are the same state variable.

Higher-role nucleus shapes remain project hypotheses until they have their own physical validation.
