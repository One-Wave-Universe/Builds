# The cell

CELL_V1 is one coupled physical state machine, but **its magnetic nucleus geometry depends on the cell role**.

## Role-specific core topology

- **Sensor cell:** planar **round figure-8 toroid nucleus**.
- **Motor-control cell:** planar **square figure-8 toroid nucleus** for grid / lattice connection.
- **M4 cell nucleus:** **two triangular toroidal loops base-to-base**.
- **M4 outer field pair:** **two plain round toroids**, not round figure-8 toroids.
- **Five-mind nucleus:** **double pentagon** toroidal geometry.
- **Six-mind nucleus:** **double hexagon** toroidal geometry.
- **Energy / readiness:** V_BUS carries reinjection and lattice readiness. CENTER remains the local lean reference.

All present core hardware is planar / 2D. The magnetic fields are 3D.

All analog. No global clock. No second controller bypasses the local physical decision path.

## Seats

```
                    A+
                 ________
                /        \
           C-  /          \  B+
              |   BRAIN    |
           B-  \          /  C+
                \________/
                    A-
```

The six edge seats are three mirrored axes where that interface is used, not six independent gates.

## Whole-cell loop

```text
sensor / neighbor consequence
→ role-specific nucleus
→ local differential / threshold resolution
→ DOWN / HOLD / UP where applicable
→ role-specific field / motor action
→ collapse / inductive return
→ V_BUS
→ next physical decision
```

For the M4 cell specifically:

```text
double-triangle nucleus
→ local M4 resolution / compression
→ two plain round outer toroids
→ mirrored winding / field response
→ collapse / return
→ V_BUS
```

CENTER stays off the recovery bus. The flower connects neighboring cells on the edge axes while V_BUS provides the shared energy/readiness layer.

This file is detail under `CELL.md`; if wording conflicts, `CELL.md` wins.
