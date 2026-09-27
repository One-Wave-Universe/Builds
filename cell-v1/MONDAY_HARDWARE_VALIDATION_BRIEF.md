# Monday Hardware Validation Brief — CELL_V1

## Purpose

This is the engineering handoff for the Monday hardware-validation discussion. CELL_V1 is the working name of the first hardware cell, not a company or finalized product name.

The near-term goal is not to claim a complete artificial brain. It is to build and measure one physical analog control primitive assembled from established electrical and magnetic mechanisms, then identify whether the proposed integration produces the intended behavior.

## Full motor-control cell

```text
DC supply / V_BUS reservoir
        ↓
CENTER virtual-ground reference
        ↓
three opposed A/B/C differential axes
        ↓
− / (0) / + physical ternary lean
        ↓
square figure-8 motor-control nucleus
        ↓
threshold + local nucleus hysteresis
        ↓
two plain round outer/body toroids
        ↓
etched hysteretic lattice paths / distributed muscle memory
        ↓
field / actuator / load consequence
        ↓
inductive recovery / reinjection
        ↓
V_BUS
        ↓
next physical decision
```

CENTER and V_BUS have different jobs. CENTER/(0) is the active balanced virtual-ground reference used to construct the physical ternary state. V_BUS is the energy/readiness/reinjection rail.

## Magnetic center — the missing coupled-field test

The motor-control build is not just "nucleus then outer toroids." The **square figure-8 nucleus sits in the coupling region of the two outer/body magnetic structures**, so the three magnetic elements must be characterized as one 3-D field problem.

Use classical coil systems only as references:
- a Helmholtz pair demonstrates how matched outer excitation can create a comparatively uniform central field;
- anti-Helmholtz excitation demonstrates how reversing one side creates a central zero / gradient;
- Maxwell three-coil arrangements demonstrate that a middle coil can materially reshape the field of an outer pair.

CELL_V1 is not automatically any of those geometries. The present outer/body hardware is two plain round toroids and the middle is a hysteretic square figure-8 nucleus. Therefore **field shape, coupling and symmetry are measurements, not names**.

Test both outer-pair modes where the winding arrangement permits:
1. **common/additive excitation** — ask what field reaches the middle;
2. **opposed/differential excitation** — ask what gradient / cancellation / asymmetry reaches the middle.

Then repeat each test with the nucleus prepared in controlled negative, near-center and positive prior states. The critical result is whether the same outer/differential stimulus produces a reproducibly different response because of retained nucleus state.

### Coupled state loop

```text
A/B/C signed differential around CENTER/(0)
              +
outer-pair common/opposed field
              +
square figure-8 nucleus prior hysteretic state
              ↓
      coupled 3-D magnetic state
              ↓
 threshold / body / actuator consequence
              ↓
 inductive collapse + protected V_BUS return
              ↓
retained nucleus state + new bus condition
              ↓
          next event
```

### Magnetic measurements

Capture:
- 3-D/axial field samples through the center and around the outer pair;
- outer current and ampere-turns;
- nucleus drive and sense-winding voltage/flux proxy;
- additive versus opposed outer excitation;
- major and minor hysteresis behavior;
- remanence and coercive threshold;
- saturation onset;
- mutual coupling / induced voltage between each magnetic element;
- threshold shift versus prior nucleus state;
- retention/decay versus time;
- heating and drift;
- whether outer excitation disturbs or erases the nucleus state;
- whether V_BUS recovery perturbs CENTER or the retained state.

A Hall/gauss probe, current probe, sense winding, oscilloscope and DMM are instrumentation only; they do not become control elements.


## Established building blocks vs CELL_V1 experiment

| CELL_V1 function | Established engineering basis | What CELL_V1 must prove |
| --- | --- | --- |
| Opposed analog differential | differential pairs / bridge drive | stable signed lean on all three axes |
| CENTER / (0) | split-rail / virtual-ground and differential reference practice | active balanced middle remains stable under coupled load |
| − / (0) / + | signed differential around a reference; multilevel/ternary circuits exist | robust physical DOWN/HOLD/UP boundaries without a software state machine |
| Ferrite/toroidal magnetic path | inductors, transformers, magnetic cores | selected geometry gives useful coupling |
| Hysteresis / remanence | magnetic-core memory and hysteretic magnetic devices | previous physical state measurably shifts the next response |
| Threshold switching | analog/magnetic threshold behavior | repeatable threshold-driven transition without a global clock |
| Outer magnetic field / actuator coupling | wound magnetic actuators and motor windings | two-round-toroid body interface produces useful measurable coupling |
| Inductive return | flyback, regenerative drives, DC-link energy recovery | recovered energy can return to V_BUS without corrupting CENTER or destabilizing state |
| Etched hysteretic lattice paths | patterned magnetic/domain-wall paths provide physical precedent | repeated traversal can write/retain a measurable path bias without unacceptable crosstalk |
| Shared V_BUS | conventional DC buses / reservoirs | carries energy/readiness/reinjection while remaining distinct from stored path memory |
| Multi-cell scaling | networked/distributed control is established broadly | CELL_V1 neighbor coupling and lattice behavior remain unproven |

The novelty claim is therefore the **integration**, not invention of each underlying component.

## Highest-risk interfaces

1. **CENTER under load** — can the active virtual-ground ternary reference remain sufficiently stable while the magnetic/actuator paths move energy?
2. **Differential → nucleus coupling** — does signed lean reliably produce a measurable nucleus response without an external digital controller?
3. **Hysteresis → next decision** — does a previous write/state produce a repeatable, useful shift in the next threshold crossing?
4. **Nucleus → outer/body pair** — is coupling strong and selective enough to influence the body/actuator path?
5. **Return → V_BUS** — can inductive energy be recovered while keeping CENTER separate and avoiding unstable positive feedback?
6. **Thermal/component drift** — do the three states remain distinguishable across realistic component and temperature variation?
7. **Etched path → later traversal** — after controlled writes, does the same later stimulus follow a measurably history-dependent response, beyond noise/drift?
8. **Second-cell coupling** — only after one cell passes: does an adjacent cell see the intended opposed differential consequence?

## First validation sequence

### V0 — reference
Build CENTER and verify its unloaded and loaded stability. No magnetic-memory claim.

### V1 — one differential
Build one opposed differential axis and demonstrate repeatable negative lean, active balanced HOLD, and positive lean around CENTER.

### V2 — nucleus
Couple that axis to the square figure-8 motor-control nucleus. Sweep the differential and record current, voltage, flux/sense response, threshold crossings, and heating.

### V3 — retention
Apply controlled writes in both directions, remove/reduce drive, then probe again. Quantify retention, decay, repeatability, and whether prior state changes the next threshold.

### V4 — coupled outer pair + hysteretic middle
Add the two plain round outer/body toroids. Characterize common/additive and opposed/differential outer excitation where physically supported. Map the center field, then repeat with controlled prior nucleus states. Measure whether the outer pair disturbs the nucleus and whether nucleus history changes the coupled response.

### V5 — return
Add the protected inductive recovery path to V_BUS. Measure input energy, recovered energy, bus excursion, CENTER disturbance, and temperature. Do not claim net recovery efficiency until measured.

### V6 — three axes
Replicate the validated differential path for A/B/C and test interaction/crosstalk. The axes operate in parallel; they are not three sequential voltage levels.

### V7 — etched-path muscle memory
Add one deliberately simple writable hysteretic path test coupon before a full lattice. Apply controlled traversals in both directions, return energy through the protected V_BUS path, then apply an identical probe. Measure coercive/write threshold, retained path-state proxy, next-response shift, decay, thermal drift, neighboring-path crosstalk, and whether reinjection reinforces, erases, reverses, or leaves the path unchanged.

### V8 — second cell
Only after V0–V7 pass, connect a second cell/opposed seat and measure whether the intended neighbor consequence survives loading and coupling.

## Bench traces to bring back

- V_BUS(t)
- CENTER(t)
- each signed differential D_A, D_B, D_C
- winding current
- nucleus sense/flux proxy
- outer-pair sense/flux proxy
- threshold entry/exit values
- prior-state-dependent threshold shift
- nucleus retention/decay vs time
- etched-path retained-state proxy and write/erase threshold
- identical-probe response after different path histories
- path-to-path crosstalk
- input and returned energy
- temperature vs run time
- crosstalk between axes
- center/outer field samples for common and opposed excitation
- nucleus disturbance/retention after outer-field events

## Pass/fail principle

A diagram is not a pass. A simulation is not a physical pass. A component precedent is not an integrated-system pass.

For each stage record:
**stimulus → measured state → expected range → observed range → pass/fail → next smallest change.**

If three repetitions fail for the same reason, change the experimental angle rather than repeating the same setup.

## What help is needed from EE / ME collaborators

- select real core material, dimensions, winding gauge and turns;
- choose a practical matched differential/drive implementation;
- calculate CENTER source/sink and impedance requirements;
- design safe clamp/recovery hardware around V_BUS;
- model magnetic saturation, coupling and thermal limits;
- define sense winding / Hall / current-probe measurement strategy;
- fixture the square figure-8 nucleus and two round body toroids repeatably;
- review failure modes before energizing the full coupled assembly.

## Scope boundary

The motor-control cell is the immediate validation target. Sensor, M4, five-mind and six-mind nucleus geometries remain later role-specific extensions. Do not let those later layers block validation of the first physical cell.

**Memory lock:** local nucleus hysteresis is local retained state; etched hysteretic lattice paths are the distributed muscle-memory layer; V_BUS is the energy/readiness/reinjection rail and is not itself the stored muscle memory.

No measured claim is made for useful retention, etched-path memory, torque, coupling, reinjection efficiency, lattice behavior, or higher cognition until the corresponding experiment exists.
