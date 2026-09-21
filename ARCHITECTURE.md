# Proposed architecture

Best current guess for a physical analog cell whose state is a lean in the path that just carried the event.

This is the Builds package. It is a design. It is not a measured device and does not need to be one to be a proposal.

Science cosmology stays in `One-Wave-Science`. Fiction stays in `Mythos-and-Stories`.

---

## 1. What is being proposed

A hex cell with three mirrored axes. No master clock. Ports are bidirectional. When a lean leaves the home band, the cell fires: it drives, it writes a magnetic hold, and leftover field is steered onto a shared DC bus — not onto the floating center.

The weight is that lean. Memory is that lean still in the path. Hardness is how strongly the pair and the core resist being pushed home. Use deepens. Disuse fades.

A corporation can copy the schematic. It cannot copy a lean that was grown.

---

## 2. Layers (do not mash the rails)

| Layer | Rail | Job |
| --- | --- | --- |
| Cell-0 bench | 9 V jellybean FETs | See a lean with parts that exist |
| Analog map | 0–1 V home at 0.50 | Bands, HOLD wobble, ±1 ±2 ±3 |
| Bus | shared DC, separate metal from CENTER | Return of collapse, lattice blood |
| Addressing | Rabbit Hopping (software) | Source fixed, center moves |
| Zer0 lock | four-branch talk | May *name* a settle at T6. Does not remember |

Cell-0 is how you first see `D = DB − DC`. The 1 V map is the intended analog layer. Bidirectional millivolt ports need low-Vt silicon, not a 2N7000 asked to switch at 10 mV.

---

## 3. Geometry

Point-up hexagon. Connections at **edge centers**, not corners.

Clockwise seats: `A+ → B+ → C+ → A− → B− → C−`

Three physical axes, not six independent gates:

- `A+ ↔ A−`
- `B+ ↔ B−`
- `C+ ↔ C−`

On a hex, three seats clockwise is the opposite side. The mirror is the shape.

**Flower (7 cells).** Center plus six. Tiling makes the mirrors:

- Center A+ meets neighbor A−
- Neighbors share an edge so one C+ meets the other C−
- Twelve mirrors per flower, no custom harness
- Outer ring `N1…N6→N1` can circulate without the center (hypothesized under-loop)

**Stack.** Same orientation: plus meets plus (reinforce). Inverted: plus meets minus (differential surface — hypothesized split). Same rule at the next scale: point → flower → stack → volume → next point.

**Gates on an axis.** CHOICE → PIVOT → FLIP → PIVOT → CHOICE. Transistor map is open.

---

## 4. Event, not clock

Nothing says sample-now. The cell waits in HOLD. A crossing of a named band *is* the event. Tempo is how often those crossings finish, including the return of the field onto the bus.

After fire, the path is busy with its own collapse. A second crossing in that window is chatter, not a beat. Enter ≠ exit (hysteresis) plus “this fire owns the path until CENTER is home and the bus kick has settled.” That is refractory without a timer chip.

Pocket = rate of completed loops. Two cells couple when their crossings line up.

---

## 5. Lean = weight = memory

Reference: floating virtual ground. It moves. History sits in that move.

Three properties of one lean:

- Direction — plus or minus of center
- Magnitude — how far
- Hardness — tail current / write depth / how hard to shove home

Pair (subthreshold, intended 1 V layer):

```
Idiff = Iss · tanh(Vd / (2 · n · Vt))
```

`Iss` is hardness. `Vd` is direction and magnitude.

Ternary is the flow, not a register:

- DOWN — net current one way
- HOLD — no net way, tail still flowing, pair sensitive
- UP — net current the other way

HOLD is readiness, not off.

**Home wobble (locked):** `0.45–0.55 V` is 0. Motion inside it is not a commit.

**Commit outside the wobble:**

| | volts |
| --- | --- |
| +3 | 0.80–0.90 |
| +2 | 0.65–0.75 |
| +1 | 0.55–0.60 |
| 0 | 0.45–0.55 |
| −1 | 0.40–0.45 |
| −2 | 0.25–0.35 |
| −3 | 0.10–0.20 |

Gaps stay unnamed. `0.00–0.10` and `0.90–1.00` are terminal, not ±4.

Write depth on the same core: shallow (fades), deep (holds), saturated (protected). Need fade or the lattice freezes its first habit.

Identical probe, different prior lean, different answer — the architecture stands or it does not. That test is proposed as the gate for later measurement, not a claim that it has been run.

---

## 6. Ports

A+ is a port, not an input pin. Same path, either way. Lean picks the way.

Cell-0 uses 2N7000/BS170 to *see* a lean. A both-ways axis is back-to-back N-FETs (body diodes cancel) or later isolated-body / analog-switch silicon. Gate drive must still work when polarity flips. Sense direction, not only size.

---

## 7. Bus (circulatory)

CENTER holds the lean. Waste does not go there.

Collapse of the winding is steered to a DC-link cap, then onto a shared rail every cell may draw. External supply only replaces loss.

```
E_in = ∫ V I dt
E_L  = ½ L I²
E_rec = ½ C (V_final² − V_initial²)
E_loss = E_in − E_rec − E_useful
```

Say the percentage you would get. Never 100%. Never more than in. CELL_V1 does not assume energy creation.

Return walks the same magnetic element that just took the write. Recovery and memory are one process.

Bus voltage is lattice state: high / low / rising / falling. Every cell can feel it. No central controller in the proposal.

Shared bus is allowed. Shared CENTER is not.

---

## 8. Readiness (not a soul)

Behavior follows bus, tail current, return timing, threshold walk.

Low rail → fewer crossings, looser timing, the body *is* sluggish. High rail → sharp. After a long set the bus is spent and fields are still coming home. That is the mechanism.

Grant sentence: system readiness changes event rate and latency through those quantities. Measured later. Not a mood flag. Not a feeling-claim. Experience is left unanswered on purpose.

---

## 9. Two machines, under-loop

Brain machine: intent, language, sequence, plan.  
Body machine: motor, balance, hearing, battery.  
Under-loop: reflex, pocket — hypothesized on the flower ring, not routed through deliberation.

Not a software stack. Two peers coupled by a mirror.

Compression (proposed ratios): six edge seats → three axes → one nerve (3:1). Oversight wide and cheap; override rare and expensive (6:1). Oversight is normal.

Brainstem as quadratic (hypothesis): 4 views up × 4 actions down. Classical. Not a qubit.

Locked lexicon for those sixteen:

- X: BASELINE / DELTA / HEADING / RESULT × PULL / PUSH / FLIP / PASS
- Y: ROOT / TRAJECTORY / EXTENT / CONFIGURATION × DRAW / DRIVE / INVERT / TRANSMIT
- Z: PROJECT / COUPLE / TRANSFORM / INTEGRATE × SELECT / ARRANGE / PERMUTE / COLLAPSE
- T: STILL / SLOW_MOTION / ACCELERATED / EXHAUSTED × COINCIDENCE / HOPE / TARGET / STRATEGY

T5 rate (not T4): REST / SLOW / NORMAL / FAST / GLARE  
Lifetime unit (not rate): LIFE / GEOLOGIC / PLANET / GALACTIC / UNIVERSAL

---

## 10. Current kinds

- DC — base flow
- AC — oscillation around center
- RC — not a third PSU. The lean itself
- BC-DC — binary relation picks DC direction
- TC-AC — ternary move picks AC phase
- QC-RC — 4×4 picks path through the recursive lean

---

## 11. Addressing (Rabbit)

Source identity stays put while the generated center moves. Wrappers opposite parity. Families A–D keep operation order. Code: `algorithms/rabbit_hopping.py`.

This is addressing. It is not the weight.

Zer0 may notice a lean and may only treat a proposal as settled at T6. A number in `lean_weight.py` is talk. If the pair has faded, that number is false.

---

## 12. What is locked vs hypothesized

**Locked as the proposal:** hex, three axes, twelve flower mirrors from tiling, event-driven, HOLD wobble, ±1±2±3, lean = memory in the path, return ≠ CENTER, no created energy, no weight file, no clock, readiness is physical state.

**Hypothesis:** flower computes, ring is the under-loop, inverted stack is a split, 4×4 is the brainstem, 3:1 and 6:1 do what we want, bus couples cells usefully, write depth gives the hardness range, millivolt pair stays quiet under switching.

**Open on purpose:** HOLD circuit, magnetic material, fade, CHOICE/PIVOT/FLIP transistors, one core vs A/B/C cores, winding count, flower flip rules, threshold drift with heat.

---

## 13. Scale of the proposal (order, not a promise)

1. One pair, see D (Cell-0)
2. One-axis return onto C_BUS
3. Same probe, different prior lean
4. Both-ways port
5. 1 V pair + tail as hardness
6. Three axes, rotate A→B→C
7. Flower on one bus
8. Nerve compression / override
9. Brainstem
10. Hemispheres / body

The architecture is already the first five sections of this file. Later numbers are scale, not a second invention.

---

## 14. Where the files are

| Topic | File |
| --- | --- |
| This packet | `ARCHITECTURE.md` |
| Grant one-pager | `GRANT.md` / `GRANT_MAP.md` |
| Lean bands | `cell-v1/WEIGHT_LEAN.md` |
| Not a file | `cell-v1/NOT_SOFTWARE.md` |
| No clock | `cell-v1/NO_CLOCK.md` |
| Bus | `cell-v1/REINJECT_BUS.md` |
| Readiness | `cell-v1/READINESS.md` |
| Cell-0 netlist | `cell-v1/CELL0.md` |
| Full cell notes | `cell-v1/CELL_ASSEMBLED.md` |
| Rabbit | `algorithms/rabbit_hopping.py` |
| Ternary toy | `gcac/` |
| Later body loop | `bucket-r2/` |

Do not translate lean → parameter, HOLD → off, memory → checkpoint, T6 → `commit()` as if the body moved. See `ANTI_DRIFT.md`.
