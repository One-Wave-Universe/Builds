# Hysteresis

The whole system state after the loop settles. Not three isolated software memories.

Three magnetic / differential axes may lean differently, but they are **parts of one coupled loop**. The hysteresis that matters at cell level is what remains when differential state, nucleus, gates, windings, return path, and V_BUS have all interacted and settled.

Lean → drive → field / winding action → collapse through gated return → V_BUS changes → gates and tails see the resulting condition → **settled physical state**.

That settled offset / retained condition is the memory candidate to measure.

---

## Not this

Three isolated B-H curves in three drawers. A table of three H values. Software OR of three bits.

## This

One coupled physical loop:

```
 three A/B/C differentials
        |
 square figure-8 nucleus
        |
 outer 3+3 windings / magnetic field
        |
 gates → return / reinjection → V_BUS
        |
 next threshold state
```

Remanence in magnetic material is one established mechanism by which the loop can retain a trace. CELL_V1's proposed memory is the behavior of the complete coupled loop, not core A alone.

## Retention regimes are an experimental target

The architecture currently distinguishes **short-, medium-, and long-retention hysteretic behavior as a design goal**, not as a measured result.

Candidate controls include:

- material coercivity / remanence,
- write current and pulse / event energy,
- number of reinforcing events,
- winding turns and geometry,
- magnetic coupling,
- threshold enter / exit spacing,
- leakage and demagnetizing paths,
- bus loading and reinjection conditions.

Do **not** assign durations such as seconds, hours, years, or decades until measured.

## What is established vs what is not

Established physics:
- magnetic hysteresis and remanence,
- dependence of magnetic response on material and applied field history,
- inductive storage / collapse,
- threshold circuits with separate enter / exit points.

Unproven CELL_V1 integration:
- whether one coupled loop produces useful short / medium / long retention bands,
- how cleanly those bands separate,
- whether the same path can support memory and useful reinjection without instability,
- how repeat use changes retention,
- whether disuse produces the desired fade law.

Use may deepen a retained state and disuse may allow it to relax, but the exact CELL_V1 behavior must be measured rather than assumed.
