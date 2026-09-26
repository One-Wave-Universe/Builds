# Reinjection bus

A shared DC / analog bus spans the lattice. Every cell may draw from it. Every cell may return recovered inductive energy and physical consequences to it through gated / steered paths.

**CENTER / virtual ground and V_BUS are different nodes.**

- CENTER = fixed virtual-ground center reference for the differential structure.
- V_BUS = live shared analog / energy / readiness / reinjection state.
- V_BUS is not assumed to be neutral or zero; when read, it is whatever value the coupled system physically has at that moment.

Both mirrored sides can read V_BUS and, through their gated return paths, contribute to its next state.

## Conceptual topology

```
       V_BUS shared live rail
            |
   ┌────────┼────────┐
 [A stage] [B stage] [C stage]
   |         |        |
  WA        WB       WC
   |         |        |
   └────────┼────────┘
            |
    steering / gated return
            |
       DC-link storage
            |
       back to V_BUS
```

Per axis:

- bidirectional drive / switching path,
- winding or coupled magnetic path,
- steering / synchronous return on collapse,
- local storage / DC-link element,
- gated return to V_BUS,
- sensing relative to CENTER plus the present shared bus condition.

The exact voltage level and implementation are bench choices. Do not confuse an early prototype supply with the architectural meaning of V_BUS.

## Recovery

Drive releases. Field collapses. Current wants to continue. A controlled return path can steer some of that energy toward local storage and V_BUS:

1. active drive changes state,
2. winding field collapses,
3. steering / synchronous path conducts,
4. current charges storage / returns to bus,
5. V_BUS changes,
6. both sides can read that resulting state on the next interaction.

Useful accounting:

- E_in = ∫ V(t)·I(t) dt at the source / bus
- E_L = ½ L I² at a measured instant
- E_C = ½ C V²
- E_rec = measured returned energy
- E_loss = input − recovered − useful output − stored change, within measurement uncertainty

CELL_V1 does not assume created energy. Recovery fraction must be measured.

## Memory and return are coupled, not automatically identical

The proposed architecture routes return through state-bearing magnetic / electrical structures so prior state may condition the return path.

That makes memory and recovery **coupled parts of one loop**, but bench work must determine whether they can share enough physical path to produce the desired behavior without unwanted saturation, oscillation, or cross-coupling.

Do not claim that every write necessarily deepens memory or that a given write depth maps to a specific lifetime until measured.

## Bus state

V_BUS is more than a power reservoir if the experiment shows cells can usefully respond to its instantaneous value.

Possible measurable descriptors include:

- absolute bus voltage / current,
- rising vs falling tendency,
- local impedance,
- returned-energy pulses,
- cross-cell perturbation,
- recovery fraction,
- settling after an event.

The labels ready / depleted / recovering are engineering interpretations of those measurements, not fixed metaphysical states.

## Proven / ordinary bench / hypothesis

Established mechanisms:
- ½LI² and ½CV² energy storage,
- steering of inductive collapse,
- MOSFET switching,
- hysteresis / remanence,
- differential sensing,
- shared-rail power distribution.

Ordinary bench work:
- half-bridge / bidirectional switching,
- synchronous steering,
- cap sizing,
- rail sensing,
- current-direction sensing,
- decoupling and impedance control.

Hypothesis until measured:
- shared V_BUS couples cells usefully,
- returned energy can participate in the next state without destabilizing the lattice,
- desired short / medium / long retention regimes emerge,
- one coupled arrangement supports both useful memory and useful recovery,
- A/B/C cross-coupling remains controllable.

## Hard parts

1. Steer recovery without moving CENTER.
2. Keep V_BUS distinct from virtual ground.
3. Prevent one branch from swamping the other A/B/C branches.
4. Characterize short / medium / long hysteresis rather than naming durations prematurely.
5. Determine winding gauge, turn count, spacing, geometry, and coupling experimentally.
6. Control saturation / erase / fade so the lattice does not freeze.
7. Measure or do not claim.

## Build order

1. One axis recovery — one winding, steering, storage. Measure E_in vs E_rec.
2. Characterize threshold / return waveform.
3. Add magnetic state element. Measure hysteresis.
4. Same probe, different prior state, compare response. Stop if no reproducible state dependence.
5. Characterize retention over progressively longer intervals.
6. Add three axes A/B/C on one shared V_BUS. Measure cross-coupling.
7. Add threshold-driven A→B→C field progression; no global clock.
8. Tune winding gauge / turns / spacing / coupling.
9. Flower / multi-cell lattice only after the single-cell loop is reproducible.

Nothing above the single-cell validation matters until that validation works.
