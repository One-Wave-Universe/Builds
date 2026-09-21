# Hysteresis loop × ferrite per axis

Square ferrite figure-8. Square B–H. Br stays near Bm after H is gone. That leftover B *plus* the bus coming home *is* the cell's settled hysteresis — one state, three pieces of iron.

## The loop (old physics)

- Drive H up → B climbs, saturates (flat top).
- H back to 0 → B does **not** go to 0. Remanence Br. Old state.
- Drive the other way → must beat coercivity Hc before it flips. New state.
- Inner loops = shallow write. Outer loop = deep write.

Squareness Br/Bm high (≥ ~0.9 on magamp / square-ferrite family) is why a trace survives the settle. Round power ferrite slumps. EMI bead slumps.

We use that. We did not discover it.

## Figure-8 per axis

Two square windows, shared leg. + winding / − winding = the two seats.

Same current that writes Br is the current that, when the drive drops, collapses through the gate onto V_BUS. Memory and recovery share the iron.

Three figure-8s (A B C). They are not three separate memories. After V_BUS and the pairs come home there is **one** settled cell state. The three loops are how that state can have a heading.

## Minor loops vs saturation

HOLD / wobble → stay on a minor loop or on Br, little new write.
±1 → shallow inner loop.
±2 ±3 → deeper. Saturation is protected habit — hard to flip, also hard to fade. Need some fade or the first day freezes the cell.
