# Usable analogue parts — memory / meta / cascade

Brick: YELLOW bench recipes. Uses the existing breadboard only. No MCU learn loop. No chip synapse.

Parents: BREADBOARD.md retained-state test, WEIGHT_LEAN.md, NO_CLOCK.md, REINJECT_BUS.md, METAPLASTICITY_ANALOGUE.md, MEMORY.md (round figure-8 = local lean, square figure-8 = body diary, cap = last kick).

## What you can run with parts already named

Fixture: opposed FET pair, CENTER exposed, V_BUS separate, one nucleus (square figure-8 for motor-control proto). Scope D = V(+) − V(−), V_BUS, write current.

### P0 — two-lean (already in BREADBOARD)

Write +, remove, fixed probe, record.
Write − equal, same probe, record.
If the two probes are not distinguishable past noise/drift: stop. No memory claim.

### P1 — stop-learn in HOLD wobble

Hold the pair inside 0.45–0.55 V for a long dwell. Do not cross a live band.
Then apply the same fixed probe as P0.
If remanence / probe answer moved, HOLD is writing. Fail.

### P2 — fence walk (θ_M analogue)

Dense burst of same-direction fires (stay off terminal 0.00–0.10 / 0.90–1.00).
Wait until analog is back in HOLD.
Sweep lean until the next crossing. Compare to a rested cell's crossing voltage.
Busy history must move the fence or meta is not on this core.

### P3 — palimpsest / cascade-depth

Write route A once. Probe (A1).
Write conflicting B many times. Probe soon (B1). B should dominate visible lean.
Idle (or low V_BUS, tails down). Same probe (A2).
- A gone with no residue → one beaker. Not a cascade.
- Visible B, but A2 still biased vs virgin → hidden depth. Keep.
- A2 = A1 → first habit froze. Fail (saturation).

### P4 — fade / erase

Deep write. Opposite excursion or measured wait/heat.
Probe must walk back toward virgin. Quote τ. No τ, no fade claim.

### P5 — reinjection isolation

Repeat P0 with return to V_BUS enabled vs clamped off.
CENTER must stay in band. Nucleus answer must not invert just because return is on.
Record E_in, E_rec. Never claim 100%.

### P6 — tag-and-capture analogue (only after P0–P3)

Two windings or two seats on the *same* square figure-8 body.
Weak write on seat W. Strong write on seat S within the body's leftover-field window (measure that window; do not invent a timer chip).
Probe W.
If W persists only when S happened nearby in that window, you have a physical tag: S's field/chemistry was captured on W's path.
If W persists with S off the body, it is not tag-and-capture.
No protein. Flux + remanence + shared core only.

### P7 — bounded moving reference

Already in BREADBOARD. Repeated equal writes must not walk monotonically into hard sat. Need a physical release.

## Receipt line (write this or it did not happen)

```text
fixture: …
test: P0..P7
D_before / D_probe / V_BUS / CENTER
pass | fail | skip
note: no processor in the write path
```

## Not usable yet

Flower-scale tag. Inhibitory second species. Lactate-bus as neuromodulator. Intrinsic excitability as a separate channel set. Those wait until P0–P5 exist on one axis.
