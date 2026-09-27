# THE BUILD

This is the compact current CELL_V1 build map.

## One sentence

A hardware-first analog cell uses a common pair of plain round body toroids for differential connection, a role-specific magnetic nucleus for retained local state, a live -/(0)/+ differential around CENTER, and a shared V_BUS for measured inductive return and readiness — with no global clock and no software controller replacing the physical loop.

## Common body interface

Every cell role uses **two plain round outer/body toroids**.

Those two round toroids are the common body / lattice differential interface so sensor, motor-control, M4, five-mind, and six-mind cells remain physically compatible.

They are **not figure-8 toroids**.

## Role-specific nuclei

- Sensor -> round figure-8 nucleus.
- Motor-control -> **square figure-8 nucleus**.
- M4 -> double triangle, base-to-base.
- Five-mind -> double pentagon.
- Six-mind -> double hexagon.

The square figure-8 is **motor-control-cell specific**.

## Volt

- normalized axis: **1.00 V**
- CENTER: **0.50 V**
- HOLD band: **0.45–0.55 V**
- HOLD is live, not OFF.

## Differential

Three opposed axes where used:

```text
A+ <-> A-
B+ <-> B-
C+ <-> C-
```

Local state:

```text
DOWN / HOLD / UP = - / (0) / +
```

No clock. Physical thresholds, hysteresis, returned state, and bus condition drive events.

## Motor-control cell

```text
plain round body toroid
        |
square figure-8 motor-control nucleus
        |
A/B/C live differential
        |
- / (0) / +
        |
plain round body toroid
        |
motor / field consequence
        |
V_BUS return
```

## Reinjection

- CENTER is the local differential reference.
- V_BUS is the shared energy / readiness / reinjection rail.
- CENTER != V_BUS.
- Inductive collapse returns toward V_BUS.
- Supply replaces losses.
- Measure recovery; never assume 100%.

## Phase I

1. Stable CENTER.
2. One visible opposed differential.
3. State-bearing magnetic nucleus.
4. Identical probe after different writes gives repeatably different response.
5. Inductive kick reaches V_BUS without moving CENTER.
6. Returned bus state changes the next physical event.
7. Add the common two-round-toroid body interface.
8. Couple a second compatible path / cell.

Stop at the first failed premise and revise before scaling.

## Out

No software state controller in the core cell. No comparator controller. No op-amp brain. No weight-file memory. No global clock. No free-energy claim.

## Read next

`RULES.md`  
`cell-v1/CELL.md`  
`cell-v1/NUCLEUS_TOROID_TYPES.md`  
`cell-v1/CORES.md`  
`GRANT_CELL.md`
