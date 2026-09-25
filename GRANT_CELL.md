# Grant cell

## Proposed CELL_V1 analog control cell

CELL_V1 is a proposed event-driven physical control cell intended to combine local state retention, ternary differential decision, motor-field actuation, and inductive energy return in one coupled hardware loop.

It is a feasibility-stage architecture. No working-cell claim is made until the bench log contains measurements.

## Technical problem

Conventional systems commonly separate sensing, state storage, control logic, actuation, and power recovery. CELL_V1 tests whether those functions can be coupled through one physical state path so that prior use changes the next response without requiring a clocked software state table.

## Architecture

### 1. Square figure-8 nucleus

A **square figure-8 toroidal nucleus** forms the brain-side retained-state structure on the lattice-bus / vagus-nerve side of the cell.

The nucleus is neither CENTER nor V_BUS. Its hysteretic state is proposed to bias the next physical decision.

### 2. Three mirrored differential gate pairs

The six edge seats form three opposed axes:

A+↔A−, B+↔B−, C+↔C−.

Their combined physical state resolves a ternary lean:

**DOWN / HOLD / UP = − / (0) / +.**

Transitions are threshold- and hysteresis-driven rather than globally clocked.

### 3. Two outer round figure-8 toroidal structures

Two outer round figure-8 toroidal structures form the combined outer electrical / magnetic field.

They carry **six windings total**, organized as **two mirrored groups of three**. The proposed role of this 3+3 shell is to convert the resolved ternary lean into a larger differential motor-control bias.

### 4. Reinjection and lattice bus

Inductive collapse is steered to **V_BUS**, the shared energy/readiness rail. **CENTER** remains the local lean reference.

Returned energy and neighboring consequences re-enter the same state loop; they do not create a separate controller.

## Closed-loop hypothesis

sensor / neighbor consequence
→ nucleus retained bias
→ mirrored differential gates
→ ternary lean
→ outer 3+3 field
→ motor / field action
→ inductive return
→ V_BUS / lattice consequence
→ next decision.

The Phase-I research question is whether that loop can be demonstrated measurably and repeatably.

## Phase I

Build and instrument the minimum cell path needed to measure:

1. CENTER stability during switching;
2. ternary differential response;
3. different response to an identical probe after different prior magnetic writes;
4. energy into the winding path versus energy recovered to V_BUS;
5. whether reinjected/lattice state measurably changes the next event.

## Success evidence

- oscilloscope traces;
- filled `cell-v1/LOG.md`;
- measured differential values;
- measured retention / decay behavior;
- measured energy accounting;
- repeatable parts and wiring record.

## Stop condition

If an identical probe after different prior writes produces no repeatable state-dependent difference, the retained-state premise fails and the architecture is revised before scaling.

## Do not claim

Consciousness, feelings, free energy, 100% recovery, measured torque, measured efficiency, proven lattice intelligence, or a working full cell before the evidence exists.
