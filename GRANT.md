# Grant architecture

**Project:** CELL_V1 event-driven analog control cell with hysteretic state, mirrored 3+3 motor-field actuation, and shared-bus energy return.  
**Repo:** https://github.com/One-Wave-Universe/Builds  
**Ask:** Phase I — build and measure the minimum closed CELL_V1 loop.

## Problem

Sensing, memory, control, actuation, and power recovery are usually implemented as separate subsystems. CELL_V1 tests whether those functions can be coupled through the same physical state path so that prior hardware state changes the next response without a global clock or a software weight table.

## Proposed solution

A 1 V-class hexagonal analog cell with:

- one **square figure-8 toroidal nucleus** on the brain/lattice-bus/vagus side;
- three mirrored differential axes resolving **− / (0) / +**;
- two outer **round figure-8 toroidal structures** carrying **six windings as mirrored 3+3**;
- a distinct local **CENTER** reference;
- a shared **V_BUS** for recovered inductive energy and lattice readiness;
- reinjection that returns into the same decision loop.

The nucleus, gates, outer winding shell, motor response, bus return, and neighbor consequence are treated as one coupled physical state machine.

## Innovation being tested

The novelty claim is the **arrangement**, not a new physical law: retained magnetic state, differential ternary control, mirrored 3+3 field actuation, and energy return are deliberately closed into one event-driven hardware loop.

## Phase I evidence

Phase I will measure:

1. local reference stability;
2. repeatable ternary differential behavior;
3. state-dependent response after different prior writes;
4. energy in versus energy recovered to V_BUS;
5. whether the returned bus/lattice condition changes the next event.

Deliverables: traces, filled bench log, parts/wiring record, and raw energy-accounting results.

## Scaling

Flower, multi-cell lattice, larger motor field, and higher-level control remain Phase-II hypotheses until the single-cell loop passes the retention and reinjection tests.

## Claims boundary

The proposal does not claim consciousness, feelings, free energy, 100% recovery, measured motor performance, or a completed working cell.

## Why Phase I is fundable

The central uncertainty is concrete and falsifiable: **does the physical state of the nucleus and reinjection path produce a repeatable, measurable difference in the next cell response?** The experiment can fail cleanly, and failure prevents premature scale-up.
