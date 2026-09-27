# CELL_V1 lock list

If it is here, stop re-litigating it unless a deliberate architecture change is made.

## Common shell

- Every cell role uses the same **two plain round outer/body toroids**.
- The common outer/body toroids are **not figure-8 toroids**.
- Common shell = compatibility / body differential layer.
- Nucleus = role specialization layer.
- Point-up hex edge map where used: A+ B+ C+ A- B- C-.
- Opposed edges form three differential axes.

## Nucleus by role

- Sensor cell -> **round figure-8 toroid nucleus**.
- Motor-control cell -> **square figure-8 toroid nucleus**.
- M4 cell -> **double triangle**, two triangular toroidal loops base-to-base.
- Five-mind cell -> **double pentagon**.
- Six-mind cell -> **double hexagon**.

The **square figure-8 nucleus is motor-control-cell specific**.

All present core geometry is planar / 2D. Magnetic fields are 3D.

## Electrical state

- Normalized cell axis: 1.00 V.
- CENTER: 0.50.
- HOLD: 0.45–0.55 and live, not OFF.
- CENTER != V_BUS.
- A/B/C are spatial differential axes, not voltage levels.
- Ternary: DOWN / HOLD / UP = - / (0) / +.
- No global clock.
- No comparator or software controller becomes the hidden state machine.

## Retained state

- Processing and retained state are intended to share the active physical path.
- Hysteresis / remanence must be measured.
- Software state is not CELL_V1 memory.
- Identical probe + different prior write must produce a repeatable difference or the retained-state premise fails.

## Reinjection

- Inductive collapse returns toward V_BUS, not CENTER.
- The supply replaces losses.
- Energy accounting is mandatory.
- No created energy and no fixed recovery percentage may be claimed.

## First build order

1. One differential around CENTER.
2. Add one role-appropriate nucleus.
3. Prove retained-state discrimination.
4. Route one inductive return into V_BUS without corrupting CENTER.
5. Show returned state changes the next event.
6. Add the common two-round-toroid body interface.
7. Couple a second compatible path / cell.
8. Then expand to three axes, motor field, flower, or higher-mind nuclei.

## Still open engineering

- exact magnetic materials;
- turns and wire gauge;
- coupling coefficients;
- transistor topology;
- thermal fade / relaxation;
- write depth;
- bus impedance and local storage;
- exact 3+3 winding implementation;
- torque / field strength / recovery fraction;
- scale-up behavior.

No op-amp controller, no comparator controller, no global clock, and no software weight file in the core cell.
