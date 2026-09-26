# Reinjection bus / vagus circulation

The CELL_V1 vagus system is a paired lattice circulation:

- **arterial / feed side** distributes available energy and the present live bus condition toward cells;
- **venous / return side** receives recovered inductive energy and physical consequences from cells and returns them toward shared storage / the live bus state.

Every cell participates in both sides.

**CENTER / virtual ground remains separate from both.**

- CENTER = fixed virtual-ground center reference for the differential structure.
- arterial/feed = outward distribution side of the vagus circulation.
- venous/return = recovery / consequence side of the vagus circulation.
- V_BUS live state = the shared physical condition produced by the coupled feed/return system.

V_BUS is not assumed to be neutral or zero; when read, it is whatever value the coupled system physically has at that moment.

## Conceptual topology

```
        shared storage / live V_BUS state
                   │
          arterial/feed rail
                   │
       ┌───────────┼───────────┐
    [A stage]   [B stage]   [C stage]
       │           │           │
      WA          WB          WC
       │           │           │
       └───────────┼───────────┘
                   │
        steering / gated return
                   │
          venous/return rail
                   │
        local / shared storage
                   │
          updates live V_BUS
```

Per axis:

- bidirectional drive / switching path,
- winding or coupled magnetic path,
- steering / synchronous return on collapse,
- local storage / DC-link element where useful,
- gated connection to the venous return side,
- sensing relative to CENTER plus the present feed-side bus condition.

The exact voltage level and implementation are bench choices. Do not confuse an early prototype supply with the architectural meaning of the vagus system.

## Recovery loop

1. arterial/feed side presents the current shared condition / available energy,
2. local threshold and hysteresis state determines action,
3. winding stores magnetic energy during action,
4. active drive changes state,
5. winding field collapses,
6. steering / synchronous path routes return onto the venous side,
7. returned energy / consequence changes shared storage / live V_BUS,
8. the updated state is redistributed on the arterial/feed side.

Useful accounting:

- E_in = ∫ V(t)·I(t) dt at the source / feed
- E_L = ½ L I² at a measured instant
- E_C = ½ C V²
- E_rec = measured energy arriving on the venous return
- E_loss = input − recovered − useful output − stored change, within measurement uncertainty

CELL_V1 does not assume created energy. Recovery fraction must be measured.

## Memory and return are coupled, not automatically identical

The proposed architecture routes return through state-bearing magnetic / electrical structures so prior state may condition the return path.

That makes memory and recovery **coupled parts of one loop**, but bench work must determine whether they can share enough physical path to produce the desired behavior without unwanted saturation, oscillation, or cross-coupling.

Do not claim that every write necessarily deepens memory or that a given write depth maps to a specific lifetime until measured.

## Why split feed and return

A paired feed/return architecture gives the vagus system a cleaner physical role:

- the feed side does not have to absorb every collapse event directly,
- the return side can be steered, measured, buffered, and gated separately,
- returned energy can be accounted for before being reintroduced,
- one cell's collapse is less likely to swamp another cell's immediate feed path,
- and flower-scale circulation can merge recursively without using CENTER as a dump node.

Whether the two sides should be separate conductors everywhere, partially shared through switched elements, or locally combined through storage is a bench design question.

## Proven / ordinary bench / hypothesis

Established mechanisms:
- ½LI² and ½CV² energy storage,
- steering of inductive collapse,
- MOSFET switching,
- hysteresis / remanence,
- differential sensing,
- paired supply/return distribution,
- local decoupling and shared-rail impedance control.

Ordinary bench work:
- half-bridge / bidirectional switching,
- synchronous steering,
- cap sizing,
- feed and return current sensing,
- current-direction sensing,
- decoupling and impedance control.

Hypothesis until measured:
- the paired vagus circulation couples cells usefully,
- returned energy can participate in the next state without destabilizing the lattice,
- desired short / medium / long retention regimes emerge,
- one coupled arrangement supports both useful memory and useful recovery,
- A/B/C cross-coupling remains controllable,
- recursive artery/vein merging remains stable at flower scale.

## Hard parts

1. Steer recovery without moving CENTER.
2. Keep both circulation paths distinct from virtual ground.
3. Prevent venous return spikes from swamping the arterial/feed side.
4. Characterize short / medium / long hysteresis rather than naming durations prematurely.
5. Determine winding gauge, turn count, spacing, geometry, and coupling experimentally.
6. Control saturation / erase / fade so the lattice does not freeze.
7. Determine optimum feed/return impedance and local storage.
8. Measure or do not claim.

## Build order

1. One axis with separate feed and return nodes.
2. One winding, steering, storage. Measure E_in vs E_rec.
3. Characterize feed-side disturbance when return fires.
4. Add magnetic state element. Measure hysteresis.
5. Same probe, different prior state, compare response. Stop if no reproducible state dependence.
6. Characterize retention over progressively longer intervals.
7. Add three axes A/B/C on one paired feed/return circulation. Measure cross-coupling.
8. Add threshold-driven A→B→C field progression; no global clock.
9. Tune winding gauge / turns / spacing / coupling.
10. Flower / multi-cell lattice only after the single-cell circulation is reproducible.

Nothing above the single-cell validation matters until that validation works.
