# Transfluxor — mechanism (Gray prior art)

Rajchman and Lo, 1956. Multi-aperture square-loop ferrite. Name = transfer of flux between legs.

This is a comparison class for the square figure-8 nucleus. It does not prove CELL_V1, Zer0, or flower geometry.

No chip. No software weight. Flux continuity and remanence only.

## Geometry

Two unequal apertures → three legs.

- Leg 1 (wide): cross-section ≈ leg2 + leg3. Long path around *both* holes.
- Leg 2 (center).
- Leg 3 (narrow read side): short path around the *small* hole only.

Square-loop material: Br ≈ Bs. Once a leg is saturated a way, it stays until H exceeds Hc on a path that can actually reverse that leg.

## Blocked vs unblocked

**Block / reset.** Large current through the big hole, long path. Legs 2 and 3 saturate the *same* way around the small hole. After the pulse, remanence holds that.

Prime the small hole either polarity: you would need to *increase* flux in an already-saturated leg. Impossible. No flux change, no output voltage. **Blocked.** That is a stored 0 that readout does not destroy.

**Set / unblock.** Opposite pulse through the big hole, *smaller* amplitude. H falls with radius (Ampère). Only material inside a critical radius switches. Leg 2 reverses; distant leg 3 stays. Around the small hole the two legs now point *opposite* ways.

Prime the small hole: flux can slosh between 2 and 3. Output winding sees a voltage. Amount of slosh = how much of leg 2 was set. **Unblocked**, and analog: set amplitude chooses the effective area of a one-hole core from ~0 to max.

Read / prime pair on the small hole transfers that set flux back and forth. The write on the large hole is not required again. **NDRO** if the prime is bounded so it cannot walk the long path and re-block.

## Why thresholds exist without a clock

- Block current: must close the *longest* path (outer circumference). Lower bound, no tight upper bound.
- Set current: enough to reverse leg 2, not enough to reach leg 3 around both holes.
- Read current: enough for the *short* path, not the long path.

Path length *is* the decoder. Same square-loop Hc, different l, different I = Hc·l / n.

## Multi-aperture extras Rajchman already ran

- Three holes in a row: sequential gate. Output only if A then B, not B then A. Order is flux state, not a timer.
- Five-aperture “flower”: four-input AND by flux paths. Name collision with CELL flower is historical, not identity.

## Overlap with CELL / mismatch

Overlap: one body, two apertures, write and probe on different paths, remanence is the store, readout can be non-destructive, analog set amount, no RAM cell.

Mismatch:
- Transfluxor blocked/unblocked is a *gate on AC transfer*, not DOWN/HOLD/UP lean on a differential pair.
- Set radius is analog amplitude, not AZ0 bands.
- CELL square figure-8 is a specific nucleus proposal; it is not automatically a transfluxor unless block/set/read currents and leg areas are measured as such.
- Reinjection to V_BUS has no 1956 counterpart.
- CENTER must stay quiet; a transfluxor has no CENTER rail.

## Bench that would earn the word

On the actual square figure-8:

1. Long-path write. Prime short path both ways. Output ≈ 0 → blocked.
2. Opposite intermediate write on long path. Prime short path. Output ≠ 0 → unblocked.
3. Repeat prime many times. Output stays; long-path state stays → NDRO.
4. Sweep set amplitude. Output grows then plateaus → analog set radius.
5. Over-set (too much current on long path). If read dies or flips, the set window is real.

If 1–2 fail, do not call this core a transfluxor. It may still pass Test A (two-lean) by remanence without blocked/unblocked geometry.
