# Grant map

## Current status

CELL_V1 topology is consolidated in `cell-v1/CELL.md`.

Hardware evidence remains incomplete. `cell-v1/LOG.md` is the measurement gate. Do not claim a working full cell until it contains repeatable bench results.

## Canonical architecture

1. **Square figure-8 toroidal nucleus** — retained-state brain-side structure on the lattice-bus / vagus-nerve side.
2. **Three mirrored differential gate pairs** — resolve one − / (0) / + ternary lean.
3. **Two outer round figure-8 toroidal structures** — combined outer electrical / magnetic field.
4. **Six outer windings** — mirrored 3+3 motor-field system.
5. **CENTER** — local lean reference.
6. **V_BUS** — shared reinjection / energy / readiness rail.
7. **Closed loop** — returned energy and neighbor consequence must feed the next physical decision.

## Phase-I research question

Can one physical CELL_V1 path demonstrate all of the following in a repeatable measurement sequence?

- stable local reference under switching;
- ternary differential resolution;
- state-dependent response after different prior writes;
- inductive energy return to V_BUS;
- a measurable effect of returned/lattice state on the next event.

If the state-dependent probe test fails, stop and revise before scaling.

## Work packages

### WP0 — canonical lock

Keep `cell-v1/CELL.md` authoritative. Detail and grant files must agree with it.

### WP1 — minimum differential bench

Demonstrate DOWN / HOLD / UP around the local reference and record raw voltages/currents.

### WP2 — nucleus retention test

Apply controlled prior writes to the square figure-8 nucleus, then use an identical probe.

Deliverable: overlaid traces showing whether prior physical state changes the response.

### WP3 — reinjection accounting

Measure winding-path energy in and recovered energy returned to V_BUS.

Deliverable: E_in, E_rec, E_loss with no energy-creation claim.

### WP4 — closed-loop test

Feed the returned bus/lattice consequence into the next cell event and test whether it changes the next physical decision in a repeatable way.

### WP5 — outer 3+3 motor-field shell

Connect the two outer round figure-8 structures and their mirrored six windings. Demonstrate the larger differential field response to the resolved ternary lean.

Torque and efficiency claims require measurement.

### WP6 — scale only after single-cell pass

Three-axis integration, flower, neighboring-cell coupling, and larger lattice field are Phase II.

## Reviewer evidence map

| Claim | Authority / evidence |
| --- | --- |
| Canonical topology | `cell-v1/CELL.md` |
| Nucleus role | `cell-v1/SQUARE_FERRITE.md` |
| Differential logic | `cell-v1/DIFFERENTIALS.md` |
| No-clock rule | `cell-v1/NO_CLOCK.md` |
| Reinjection / energy accounting | `cell-v1/REINJECT_BUS.md` |
| Outer motor-field shell | `cell-v1/ACTUATORS.md` |
| Bench evidence | `cell-v1/LOG.md` |
| Full integration view | `cell-v1/CELL_ASSEMBLED.md` |

## Locked design topology

- hex edge geometry;
- three mirrored axes;
- square figure-8 nucleus;
- two outer round figure-8s;
- mirrored 3+3 outer windings;
- ternary − / (0) / + lean;
- no global clock;
- CENTER separate from V_BUS;
- reinjection re-enters the same state loop.

## Still hypothesis / engineering

Material selection, winding turns, coupling coefficient, exact transistor implementation, retention depth, decay/fade law, field strength, torque, recovery fraction, thermal behavior, multi-cell usefulness, and higher-level behavior.

## Grant language

Use: event-driven analog control cell, hysteretic retained state, mirrored differential axes, ternary lean, mirrored 3+3 winding shell, inductive energy return, measurable state-dependent response, falsifiable Phase-I test.

Avoid: consciousness, feelings, free energy, guaranteed efficiency, proven intelligence, proven motor performance, or claims that bench data does not support.
