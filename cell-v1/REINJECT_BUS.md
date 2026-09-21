# Reinjection bus

A shared DC bus that spans the whole lattice. Every cell draws from it. Every cell returns to it. Collapsing fields are steered back to it instead of dumped as heat. Recovered energy is available to any other cell that needs it.

Not just efficiency. Circulatory. Blood does not belong to one organ. Same here.

CENTER / V0 stays quiet. The bus is other metal.

## Topology

```
       +1V rail (shared DC bus)
            |
   ┌───────┼───────┐
 [HB-A]  [HB-B]  [HB-C]     3 half-bridges
   |        |       |
  WA       WB      WC       windings
   |        |       |
   └───────┼───────┘
            |
     steering / clamp
            |
       DC-link cap
            |
     ──→ back to +1V rail
```

Per axis:

- Half-bridge — two MOSFETs, winding forward or reverse
- Winding — field stores the event
- Steering — diode or synchronous switch on the collapse
- DC-link cap — local reservoir
- Return — cap feeds the main bus

Cell-0 is still one pair at 9 V. This +1 V rail is the analog-brain / lattice bus layer. Do not mash the two supplies into one node.

## Recovery

Drive off. Field collapses. Current wants to keep going. Steered to the cap:

1. Drive MOSFET off
2. Winding spikes (L·di/dt)
3. Steering conducts
4. Current into DC-link cap
5. Cap voltage rises
6. Energy on the cap: E = ½ C V²

Any cell may draw bus first, external supply second. Only losses get replaced by the source.

## Accounting — no created energy

- E_in = ∫ V(t)·I(t) dt at the rail
- E_L = ½ L I² at peak winding current
- E_rec = ½ C (V_final² − V_initial²)
- E_loss = E_in − E_rec − E_useful

If you recover 40%, say 40%. Never 100%. Never more than in.
CELL_V1 does not assume energy creation.

## Memory and return are the same path

The return goes through the same state-bearing magnetic element that just took the write. The path that wrote is the path the energy comes home on. Return is conditioned by the write.

- The cell keeps direction, phase, magnitude of that use
- Every write deepens the lean
- Every return walks the same lean
- Memory and recovery are one process, not two boxes

Write depth is how hard the lean sits:

- Shallow — low current, partial alignment, fades
- Deep — high current, consolidated
- Saturated — protected, decades

Same core. Same path. Different write energy.

## Bus voltage is lattice state

Not just power. Every cell can feel it. No central controller.

- High — charged, ready to drive
- Low — depleted, conserve
- Rising — recovering
- Falling — spending faster than return

## Proven / ordinary bench / hypothesis

Proven: ½LI², ½CV², steering of collapse, hysteresis, deeper alignment with repeat write.

Ordinary bench: half-bridge, synchronous steering, cap sizing, sense the rail.

Hypothesis until measured:

- Return stays off V0 / CENTER
- Shared bus couples cells usefully
- Write depth gives the hardness range we want
- Bus voltage is enough local coordination

## Hard parts

1. Steer recovery without moving CENTER
2. Shared bus impedance — local decoupling, layout
3. Saturation — need fade / erase or the lattice freezes its first habit
4. Material — wide coercivity range, not a random EMI bead
5. Measure or do not claim

## Build order

1. One axis recovery — one winding, steering, cap. E_in vs E_rec.
2. Say the number you got.
3. Magnetic core on that winding. Hysteresis. Write depth.
4. Identical probe, different prior lean, different response. Stop here if this fails.
5. Three axes A B C. Shared bus. Cross-coupling.
6. Sequence A→B→C. Field rotates. Recovery during rotation.
7. Flower. Seven cells, one bus. Aggregate recovery.
8. Volume / hemisphere / body.

Nothing above 4 matters until 4 works.

## Cell-0 hook

`CELL0.md` pair first (9 V, DB/DC, CENTER, core).
After T5: leftover drain and kick to this bus, not to CENTER.
Shared bus later. Shared CENTER never.
