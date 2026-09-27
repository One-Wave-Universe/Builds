# Cell — assembled

One-page integration authority beneath `CELL.md`.

**Status:** proposed topology. `LOG.md` remains the hardware evidence gate.

## Common geometry

- Point-up hex edge map where used.
- Six edge connections: A+ -> B+ -> C+ -> A- -> B- -> C-.
- Three mirrored axes: A+<->A-, B+<->B-, C+<->C-.
- Every cell role uses the same **two plain round outer/body toroids**.
- The common outer/body toroids are not figure-8 toroids.

## Nucleus / brain specialization

- Sensor cell -> round figure-8 nucleus.
- Motor-control cell -> **square figure-8 nucleus**.
- M4 cell -> dedicated two-pyramid / double-triangle nucleus.
- Five-mind -> double pentagon.
- Six-mind -> double hexagon.

Separate from the M4 nucleus, the cluster uses six pyramidal A/B/C routing wedges. These meet tip-to-tip inside a cell and base-to-base between cells.

The **square figure-8 nucleus belongs to the motor-control cell**. Do not make it generic.

## Differential state

Each A/B/C axis carries a local ternary lean:

- DOWN = negative lean
- HOLD = centered live balance
- UP = positive lean

Both sides may remain active around CENTER; the state is their differential lean.

No global clock. Threshold crossings, hysteresis, bus condition, retained state, and returned consequences determine transitions.

## Common body field

The two plain round outer/body toroids form the common differential shell used across cell roles.

A mirrored 3+3 winding implementation on that common pair remains a build candidate until measured.

## Local body-state interpretation

The two plain round toroids are the FIELD/VOID nerve/body-control interface. Their combined 3D magnetic field is the current candidate for the cell's local body-state field.

The dedicated domain-wall hysteretic layer beneath connected cells carries longer-lived shared body-state / muscle-memory history.

A separate literal sphere is not locked until measurement shows a distinct spherical structure is needed.

## CENTER and V_BUS

- CENTER = local lean reference.
- V_BUS = shared energy / readiness / reinjection rail.
- CENTER != V_BUS.
- Collapse energy returns toward V_BUS, never intentionally onto CENTER.

## Motor-control cell loop

```text
sensor / neighbor consequence
        ↓
square figure-8 motor-control nucleus
        ↓
A/B/C differential state
        ↓
- / (0) / +
        ↓
common plain-round body toroid pair
        ↓
motor / field action
        ↓
inductive return
        ↓
V_BUS / lattice consequence
        ↓
next physical decision
```

## Phase-I bench gate

Before scale-up demonstrate:

1. stable CENTER;
2. repeatable ternary differential response;
3. state-dependent magnetic response after different prior writes;
4. inductive return to V_BUS with energy accounting;
5. returned consequence changes the next physical decision;
6. common round-toroid body interface can couple a second compatible path / cell.

If identical probes after different writes do not produce distinguishable repeatable responses, stop and revise.

## Still engineering / measurement

Magnetic material, turns, coupling coefficient, transistor map, write depth, fade law, bus impedance, field strength, torque, retention time, recovery fraction, thermal behavior, 3+3 winding implementation, and scale-up performance.

Do not convert unknowns into claims.
