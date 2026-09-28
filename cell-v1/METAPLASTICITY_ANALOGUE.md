# Metaplasticity — analogue only

Brick: YELLOW mapping. Biology is Gray catalog. CELL does not get a chip, a weight file, or an STDP ASIC.

`NOT_SOFTWARE.md` still holds. `algorithms/lean_weight.py` may *name* a commit. It may not be the store.

## Ban

No digital allowed in this layer:
- no parameter file
- no backprop table
- no neuromorphic chip as the memory
- no sampled clock that decides “now learn”
- no memristor crossbar as a substitute body

Allowed: voltage, current, field, remanence, coercivity, threshold bias, chemistry in the path, heat, fade.

## What metaplasticity is (Gray)

Abraham and Bear: activity at time 1 that persists and changes whether LTP or LTD happens at time 2. Not a change in the present EPSP. A change in the *rule*.

BCM: θ_M slides with a running history of activity. Busy cell → LTP harder, LTD easier. Quiet cell → opposite. Stops Hebb runaway.

Two geometric moves of that curve:
- Horizontal slide of θ_M (induction threshold)
- Vertical / pull-push (LTP-only vs LTD-only state), often neuromodulator / Gs vs Gq

Three biological places the slide is implemented (catalog, not CELL parts):
1. How release is coupled to the next pulse (residual Ca, depletion) — short, usually not called meta.
2. How receptor current makes Ca (NR2A/NR2B ratio, NMDA kinetics, SK / I_h / AHP).
3. How kinases vs phosphatases read that Ca (CaMKII T286 vs T305/306, CaN, PP1).

Heterosynaptic / tag-and-capture: one path's protein synthesis can be stolen by a weakly written neighbor. Cell-wide priming can exist without a spike (store-released Ca, mAChR).

Cascade / Benna-Fusi: hidden states so fast write and slow keep are not the same variable. Bidirectional chain. Palimpsest overwrite.

Homeostatic scaling is a cousin, not the same: scaling changes gain now; meta changes what the next protocol will do.

## Analogue translation on CELL

Visible lean = present efficacy (Field).
Threshold fences = θ_M.
Hidden remanence / body trace = cascade depth.
Bus + tail = readiness / short echo. Not the long store.

| Gray mechanism | Analogue slot on CELL | Forbidden stand-in |
|---|---|---|
| Slide θ_M after a busy epoch | Crossing fences walk with recent event rate and leftover Br | Software θ |
| NR2A/NR2B “current duration” | How long the winding / path stays above the write coercivity | Timed MCU pulse |
| Kinase vs phosphatase | Write vs erase bias of the same core (same H, different prior B) | Two flags in RAM |
| Vertical pull-push | Neuromodulator analogue = bus height + local chemistry, not a mode bit | FSM |
| Tag-and-capture | Shared under-hex trace captures a weak local write | Packet bus protocol |
| Cascade depth | Local nucleus (labile) under body lattice (resistant) | n-bit counter |
| Spacing / delayed expression | Reinjection revisits the path; deep lean re-biases later fire | Scheduled task |
| Stop-learn | HOLD 0.45–0.55 V wobble writes nothing | Clocked sample-and-hold |
| Fade / un-freeze | Thermal / demag / opposite excursion; required or first habit locks | `q *= 0.99` loop |

## Analogue-only tests (do these or do not claim)

1. **Fence walk.** After a dense burst of fires, the next identical probe needs more lean to leave HOLD (or less). Scope it. That is θ_M.
2. **Two-lean probe.** Same schematic, two histories, two responses. Path memory. Stop the stack if this fails.
3. **Palimpsest.** Write A, then B many times. Soon: B. Later / idle / low bus: A bias still there or A leaks back. One beaker if A is gone without residue.
4. **Stop-learn in wobble.** Drive that stays inside 0.45–0.55 V must not deepen remanence. If it does, HOLD is a lie.
5. **CENTER isolation.** Meta write via reinjection must not shove V0 out of band.
6. **Fade.** A deep lean must be erasable by opposite excursion or time/heat in a measured τ. Frozen first habit is failure.
7. **No chip in the loop.** If the only way the fence moves is a processor writing a register, this file does not apply.

Build order remains REINJECT_BUS.md: one axis → quote E_rec → core on the winding → two-lean probe. Meta is test 2 plus test 1. Nothing digital inserted between them.

## What we refuse

Memristor papers and STDP ASICs are Gray *cousins*. They may be read. They may not be imported as CELL. The moat is the raised body. A chip is a drawing you can copy.
