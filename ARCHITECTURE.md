# Proposed CELL_V1 architecture

Physical analog cell family. State is carried by the settled physical loop after an event — differential bias, magnetic history, bus condition, and returned consequence. Not a weight file.

Science stays in One-Wave-Science. Build claims stay here.

## Common body shell

Every cell role uses the same **two plain round outer/body toroids** as its body differential / interconnect layer.

That common shell lets sensor, motor-control, five-mind, and six-mind cells connect through one shared physical language.

The common outer/body toroids are **not figure-8 toroids**.

## Nucleus specialization

- Sensor cell -> round figure-8 toroid nucleus.
- Motor-control cell -> **square figure-8 toroid nucleus**.
- Five-mind cell -> double pentagon nucleus.
- Six-mind cell -> double hexagon nucleus.

## Two distinct pyramid systems

### M4 nucleus
The M4 cell has a dedicated **two-pyramid / double-triangle toroidal nucleus** arranged base-to-base.

### Cluster-routing pyramids
Separately, the general CELL lattice uses six tapered pyramidal/wedge routes:
- inside a cell, opposed wedges meet **tip-to-tip** through the local center relation;
- between neighboring cells, wedge bases meet **base-to-base** across the shared hex face;
- the six routes carry A+/B+/C+/A-/B-/C- connectivity between local differential resolution and neighboring cells.

The M4 nucleus and cluster-routing pyramids are separate structures.

The square figure-8 nucleus is **motor-control specific**.

Current hardware geometry is planar / 2D. Magnetic fields are 3D.

## Differential state

Where the A/B/C interface is used:

```text
A+ <-> A-
B+ <-> B-
C+ <-> C-
```

The local state is:

```text
DOWN / HOLD / UP = - / (0) / +
```

HOLD is active balance, not OFF.

CENTER is the local differential reference. V_BUS is the shared energy / readiness / reinjection rail. They are not the same node.

No global clock. Physical thresholds, hysteresis, returned state, and bus condition drive transitions.

## Motor-control cell

```text
common plain-round body toroid
        ↕
square figure-8 motor-control nucleus
        ↕
live A/B/C differential
        ↕
- / (0) / +
        ↕
common plain-round body toroid
        ↕
motor / field consequence
        ↕
V_BUS return
```

A candidate mirrored 3+3 winding implementation may live on the common round-toroid body pair, but that remains a bench variable until measured.

## Energy / reinjection

Inductive collapse is routed toward V_BUS.

```text
E_in  = integral V(t) I(t) dt
E_rec = 1/2 C (V_after^2 - V_before^2)
```

Pack / source replaces losses. No created energy and no fixed recovery percentage.

## First validation sequence

1. stable CENTER;
2. one opposed differential;
3. motor-control square figure-8 nucleus;
4. identical-probe / different-prior-write retained-state test;
5. return one inductive event to V_BUS without corrupting CENTER;
6. show returned state affects the next event;
7. add common two-round-toroid body interface;
8. couple a second compatible path / cell;
9. only then expand to three axes, motor actuation, flower scale, or higher nuclei.

## No hidden controller

No comparator bank, op-amp controller, microcontroller state machine, software weight file, resistor threshold ladder, resistor damping/bleed return, or global clock may substitute for the intended CELL_V1 physical control loop.

Test instruments may observe the cell. They do not become the cell.

## Locked versus open

**Locked:** common plain-round body pair, role-specific nuclei, M4 pyramidal routing geometry, motor-control square figure-8 nucleus, -/(0)/+ differential, CENTER distinct from V_BUS, threshold / hysteresis-driven events, reinjection into V_BUS, hardware-first control, and no designed resistor path for thresholding or energy return.

**Open:** exact materials, winding turns, transistor topology, thermal fade, coupling coefficient, bus impedance, 3+3 winding implementation, field strength, torque, recovery fraction, retention time, scale-up behavior.

Do not promote open engineering variables into claims.
