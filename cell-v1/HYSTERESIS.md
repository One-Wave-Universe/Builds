# Hysteresis — CELL_V1 retained-state loop

Hysteresis is the **history dependence of the physical magnetic/state loop**. It is not software memory and it is not three isolated core memories.

For the current motor-control cell there are **two scales of the same history-dependent process**:

- **local nucleus hysteresis:** the planar square figure-8 nucleus can retain local magnetic state;
- **distributed muscle memory:** the **etched hysteretic lattice paths** retain the history of the physical routes repeatedly traversed by cell/body current and field activity.

The lattice-memory layer and the muscle-memory layer are therefore the **same physical path layer**. V_BUS travels through/supports this network as the energy/readiness/reinjection rail, but instantaneous V_BUS voltage is not the stored muscle memory.

## Physical basis

For a magnetic core:

```text
H = N I / l_e
B = B(H, history)
Phi = B A_e
lambda = N Phi
v = d(lambda)/dt
```

A hysteretic material can retain remanent flux after drive is reduced. Coercivity defines the reverse drive needed to cross/erase/flip that retained state. Minor loops, major loops, saturation and loss are ordinary magnetic behavior.

That known behavior does **not** prove that CELL_V1's geometry supplies useful memory. The experiment must show that the nucleus retains a reproducible state and that the retained state changes a later response.

## CELL_V1 loop

```text
A/B/C differential lean around CENTER/(0)
        ↓
nucleus magnetizing drive
        ↓
history-dependent nucleus state
        ↓
coupled field with outer/body pair
        ↓
threshold / actuator / lattice consequence
        ↓
field collapse + protected return to V_BUS
        ↓
new electrical + retained magnetic starting condition
        ↓
next physical decision
```

CENTER/(0) is the active virtual-ground ternary reference. V_BUS is the separate energy/readiness/reinjection rail.

## Etched-path muscle memory

The intended distributed memory is not a separate register written after an action. **The process path is the memory:** traversal changes the hysteretic state of the etched path, and that retained path state can bias a later traversal.

Research precedent exists for magnetic domain-wall/path devices in patterned soft magnetic structures, including Permalloy nanostripes; that supports the physical plausibility of writable magnetic paths, but it does not validate CELL_V1's proposed etched lattice geometry. The exact film/laminate material, thickness, path width, coercivity and write mechanism remain bench-design variables.

Required path experiment:
**same present stimulus + different controlled path histories -> measurably different later path response.**

Measure path-local coercive threshold, remanence/domain state proxy, write current/field, repeatability, neighboring-path crosstalk, thermal drift, decay, and whether reinjection disturbs or reinforces the written path.

## What counts as memory

The minimum useful claim is not merely that a B-H curve exists.

Run the **same probe from different controlled prior writes**. If the measured next threshold, flux/sense response, or differential response changes reproducibly with prior state, the cell has demonstrated a history-dependent physical bias.

Measure:
- remanence after positive and negative writes;
- coercive/switching threshold;
- minor-loop response around HOLD;
- major-loop response for deliberate reversal;
- retention/decay versus time;
- repeatability across cycles;
- temperature dependence;
- next-threshold shift versus prior state;
- disturbance caused by the outer/body field;
- whether V_BUS return changes or erases the retained state.

## HOLD and lean

HOLD is not OFF. Around CENTER/(0), the opposed electrical sides remain active while net lean is inside the HOLD band.

A small excitation may trace a minor magnetic loop without flipping the retained state. Larger excitation may walk farther around the hysteresis curve. A deliberate reversal may cross coercivity and produce a major state change. The exact mapping between the seven electrical bands and magnetic loop depth is **not locked until measured**.

## Whole-loop hysteresis

There are two related things to keep distinct:

1. **Material hysteresis:** the nucleus B-H history and remanence.
2. **System hysteresis:** the complete cell's next response depends on its previous settled magnetic/electrical condition.

Material hysteresis is established physics. Useful CELL_V1 system hysteresis is an experimental claim.

## Pass condition

The retention stage passes only if:
**controlled prior state + identical later probe -> reproducibly different measured response**, with the difference larger than noise, drift and thermal variation.

If that does not happen, do not call the nucleus a memory element.

## Anti-drift

- Current motor-control nucleus = one planar square figure-8 toroid.
- Current universal outer/body interface = two plain round toroids.
- Do not restore the obsolete “three independent cores” description.
- CENTER/(0) is not V_BUS.
- Hysteresis is physical history dependence, not a software table.
- Etched hysteretic lattice paths = distributed muscle-memory layer.
- V_BUS voltage = instantaneous energy/readiness condition, not the stored muscle memory.
- Do not claim decades of retention, learning, habit, consolidation, or useful memory without measurements.
