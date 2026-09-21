# Grant map

Status today: law is written. `cell-v1/LOG.md` is empty. Hardware score is 0%. Do not claim a working cell.

## Pitch (honest)

**Problem.** Digital nets store weights in one place and compute in another. Style and memory can be copied as a file. Analog event-driven hardware that *is* its history is rare, and most of it is still a conductance table next to a processor.

**What we build.** A hex cell, three mirrored axes, event-driven (no clock). A lean off a moving 0.50 V home is the state. HOLD is live current in `0.45–0.55 V`. Commit is ±1 ±2 ±3 outside that wobble. Collapse energy returns on a DC bus through the same magnetic path that just wrote. Neighbor cells share the bus, never CENTER.

**What we do not claim.** Consciousness. Feelings. Free energy. A downloadable brain. Science cosmology.

**Technical risk (the actual research question).** Can one physical axis show: (a) a quiet home under switching, (b) a lean that survives as magnetic state, (c) the same probe answering differently after a different prior lean, (d) measured joules in vs joules back, always less than in?

If (c) fails, stop. That is the Phase I gate.

## Two workstreams only

| Stream | Folder | Phase I job |
| --- | --- | --- |
| Cell | `/cell-v1/` | Solder Cell-0. Log volts. Add bus. Prove lean + recovery numbers. |
| Algorithm | `/algorithms/` | Rabbit Hopping addressing. Zer0 may *name* a T6 settle. It does not hold memory. |

## Work packages

### WP0 — paper lock (done enough to apply)

Geometry, no-clock, lean bands, bus law, readiness language, anti-drift. Repo is the packet.

### WP1 — Cell-0 bench (must start now)

Parts: 9 V pack, 2N7000/BS170 pair, 10k/100k, 100 nF, square-loop core, DMM, breadboard.

T1–T5 in `CELL0.md`. Write every number in `LOG.md`.

Deliverable: photo + table of DB, DC, D, leftover core sign.

### WP2 — one-axis return

Steering onto `C_BUS`. Measure E_in, E_rec, E_loss. Say the percentage you got.

Deliverable: one plot, one number, CENTER did not take the charge.

### WP3 — lean test (Phase I kill-gate)

Identical probe. Different prior write. Different D.

Shallow write vs deep write vs quiet wait. Shallow fades, deep remains.

Deliverable: two traces overlaid. If they match, the model is wrong.

### WP4 — bidirectional port

Back-to-back FETs on one axis. Current both ways. Lean picks the way. No clock.

### WP5 — 1 V layer (not Cell-0 parts)

Low-Vt / subthreshold matched pair. Map `0.45–0.55` wobble and ±1 ±2 ±3. Tail current = hardness.

### WP6 — three axes + flower (Phase II)

Shared bus. No shared CENTER. Rotation A→B→C. Seven-cell flower. 12 mirrors from tiling.

### WP7 — readiness

Show event rate and latency vs bus volts and tail current. Language: the cell *is* sluggish. Not *feels*.

### WP8 — addressing only

Rabbit Hopping stays reversible addressing. Not weights.

## Evidence table (what a reviewer can open)

| Claim | File | Evidence now |
| --- | --- | --- |
| Lean ≠ file | `NOT_SOFTWARE.md` | text |
| Bands / wobble | `WEIGHT_LEAN.md` | text |
| No clock | `NO_CLOCK.md` | text |
| Bus + accounting | `REINJECT_BUS.md` | text |
| Readiness | `READINESS.md` | text |
| Solder steps | `CELL0.md` | text |
| Measured D | `LOG.md` | **empty** |
| Addressing | `algorithms/RABBIT.md` | code in RABBIT-HOPPING |

Until LOG has numbers, the proposal is a feasibility study, not a hardware result.

## Locked vs hypothesis (say it in the pitch)

**Locked as design law:** hex, three axes, 12 flower mirrors from tiling, event-driven, HOLD wobble, ±1±2±3, return ≠ CENTER, no created energy.

**Hypothesis:** flower computes, outer ring is the under-loop, inverted stack is a split, 4×4 brainstem, 3:1 / 6:1 ratios, drummer-scale behavior.

## Words to use / dump

Use: analog cell, event-driven, bidirectional port, measured lean, magnetic hold, DC-link return, energy accounting, system readiness.

Dump: soul, feelings, consciousness, trained weights, neuromorphic neuron chip, backprop, free energy, downloadable style, cosmology.

## Likely doors (not an application)

- NSF SBIR/STTR project pitch first (rolling; full proposal windows). Phase I is a risk-reduction bench, not a product. Pitch wants *the technical risk*, not a brand story.
- Hardware / microelectronics / analog computing frames beat "AI model" frames.
- DoD/DAF neuromorphic topics exist; they usually want SWAP and a task metric. Only apply if you will measure a task, not a vibe.
- University or shop partnership helps WP5 (matched subthreshold silicon).

Register nothing from this file. Read the live solicitation before any submit.

## Ask shape (Phase I, 6–12 months)

People-time: bench + log + one-axis return + lean test.
Stuff: cores with real square-loop / wide coercivity, low-Vt pair or analog array time, scope that can catch events, bus caps, current sense.
Not in Phase I: flower, hemispheres, bucket, speech processor, 1 V production silicon.

Success = WP3 overlay plot + WP2 recovery fraction + a filled LOG.md.

Fail = WP3 traces match. Then rewrite the cell, do not scale it.

## Budget buckets (fill dollars to your shop)

- PI / technician time
- Parts and cores (the core is the special one)
- Instruments (scope, current probe) if you lack them
- Board spin after breadboard
- Foundry / analog-array access only if WP1–3 already speak
- Travel / photos / reporting

No line item named "AI training compute."

## Reviewer one-pager

You can paste this:

> We propose to build and measure a single analog axis in which state is a voltage lean off a 0.50 V home band (0.45–0.55 V wobble). The axis is event-driven and bidirectional. After an event, collapse energy is steered to a DC bus through the same magnetic element that took the write. We will report energy in vs energy recovered (never claiming creation) and the Section-22 test: identical probe, different prior lean, different response. Memory is that lean, not a file. Phase I stops at one axis. Later scale (flower, lattice) is out of scope until that test passes.
