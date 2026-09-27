# Reinjection bus

A shared DC bus that spans the whole lattice. Cells may draw from it and may return recoverable inductive energy to it. The return path must be deliberately steered and protected; losses remain losses. Any sharing of recovered energy between cells is a system-level behavior to measure, not assume.

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

**Architecture rule:** there is no intentional resistor dump / bleed / damping branch in the CELL reinjection path. Recoverable inductive energy is steered toward V_BUS. Copper loss, core loss, transistor loss, imperfect coupling, radiation, and useful mechanical work remain real losses / outputs and must be measured rather than represented by a designed resistor return.

Closest established precedent to investigate: **non-dissipative flyback / regenerative clamp networks and DC-link energy recovery**. These are precedent classes only; CELL's self-gating and state-coupled use remain unproven.

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

## Memory and return interact, but are not assumed identical

The hysteretic nucleus and the inductive return path participate in the same physical event, but they are **not automatically the same energy path or the same state variable**.

A drive event can:
- change magnetic state in the nucleus;
- store energy in inductive fields;
- perform useful mechanical / field work;
- dissipate heat and magnetic loss;
- return part of the remaining inductive energy to V_BUS.

The retained part is tested through remanence / later threshold bias. The recovered part is tested through rail energy accounting. CELL_V1 must measure whether reinjection preserves, perturbs, strengthens, or erases the retained state.

Do not infer memory depth from recovered energy alone.

## Bus voltage is lattice state

Not just power. Every cell can feel it. No central controller.

- High — charged, ready to drive
- Low — depleted, conserve
- Rising — recovering
- Falling — spending faster than return

## Proven / ordinary bench / hypothesis

Established basis: ½LI², ½CV², controlled steering/clamping of inductive collapse, and magnetic hysteresis/remanence. How repeated writes affect this selected nucleus and whether that produces useful CELL_V1 state must be measured.

Ordinary bench: half-bridge, synchronous steering, cap sizing, sense the rail.

Hypothesis until measured:

- Return stays off V0 / CENTER
- Shared bus couples cells usefully
- Etched path state is writable and retained with the useful range we want
- Prior path history measurably biases a later traversal
- Reinjection does not unintentionally erase/corrupt the path state
- Bus condition provides useful local coordination without being confused with stored muscle memory

## Failure tests added from independent review

1. **CENTER-corruption test:** heavily load V_BUS during a controlled inductive return and measure whether CENTER/(0) shifts outside its allowed band.
2. **Recovery-isolation test:** repeat identical writes with return enabled and disabled; determine whether reinjection perturbs or erases retained nucleus state.
3. **Bus-ripple test:** measure V_BUS ripple, return peak, and next-event bias to distinguish useful returned consequence from simple supply noise.

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
