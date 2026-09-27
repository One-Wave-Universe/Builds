# FULL BUILD — current validation path

This file is the interview-readable build sequence. It intentionally separates **what is locked**, **what is a prototype aid**, and **what still requires measurement**.

## Locked architecture

- hardware-first analog control;
- no global clock;
- CENTER distinct from V_BUS;
- DOWN / HOLD / UP around - / (0) / +;
- common outer/body interface = **two plain round toroids for every cell role**;
- sensor nucleus = round figure-8;
- **motor-control nucleus = square figure-8**;
- M4 nucleus = double triangle base-to-base;
- five-mind nucleus = double pentagon;
- six-mind nucleus = double hexagon.

## First target: motor-control cell

The first coherent motor-control validation path is:

```text
stable CENTER
    ↓
one opposed analog differential
    ↓
square figure-8 motor-control nucleus
    ↓
retained-state write / probe test
    ↓
common two-round-toroid body interface
    ↓
field / actuator coupling
    ↓
inductive return
    ↓
V_BUS
    ↓
effect on next event
```

The square figure-8 is **not** the generic nucleus. It is the motor-control-cell nucleus.

## Evidence gate

Before calling the first cell path successful, obtain:

1. stable CENTER under the tested switching event;
2. repeatable negative / balanced / positive differential;
3. prior-write-dependent response to an identical probe;
4. retention / decay curve;
5. inductive return to V_BUS without corrupting CENTER;
6. measured energy accounting;
7. repeatable coupling through the common plain-round body pair;
8. same result over repeated trials.

## Stop rules

Stop and revise if:

- prior-write response cannot be separated from noise / thermal drift;
- CENTER instability creates the apparent ternary state;
- V_BUS return destabilizes the differential;
- common body coupling is not repeatable;
- energy accounting does not close within measurement error.

## Build order

```text
one differential
-> motor-control square figure-8 nucleus
-> retained-state test
-> V_BUS return
-> common two-round-toroid body interface
-> second compatible path / cell
-> full A/B/C
-> actuator / motor test
-> flower
-> M4 / higher nuclei
```

## Established constituent technologies

The build deliberately starts from familiar engineering pieces: differential analog circuits, magnetic hysteresis, ferrite / toroidal cores, inductive energy storage, regenerative return paths, DC-link buses, and multi-winding magnetic systems.

The proposed part is their integration into this particular recursive, state-bearing control loop.

## Not claimed yet

No measured torque, efficiency, intelligence, recovery percentage, higher-mind function, or full-cell success until the bench evidence exists.
