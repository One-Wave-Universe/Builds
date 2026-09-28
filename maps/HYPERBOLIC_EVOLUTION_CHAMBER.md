# Hyperbolic Evolution Chamber — Product / Simulation Map

## Purpose

Build a visual, downloadable simulation environment in which validated physics primitives can be combined into a working simulated space and bounded worker “goblins” can explore candidate silicon-CELL architectures.

The chamber is an engineering search environment. A simulated survivor is a **build candidate**, not proof that the physical device works.

## Entry gate

A primitive may enter the chamber only with:
- stable primitive/version ID;
- equations/algorithm and units;
- parameter bounds;
- source/implementation provenance;
- controls/nulls where applicable;
- validation status and receipts;
- declared numerical limitations.

The chamber must consume the One-Wave Science assumption/transformation contracts rather than silently changing physics.

## Simulated world

The physics engine owns authoritative state. Rendering never changes solver state.

Required capabilities grow modularly:
- geometry and lattice;
- fields / potentials;
- electrical differential state;
- magnetic / hysteretic state;
- thermal state;
- mechanical strain/load;
- coupling between enabled primitives;
- time/history;
- energy/accounting residuals;
- uncertainty/error ledger;
- 2D first, 3D where scientifically meaningful.

Hyperbolic geometry is a chamber/search visualization and topology capability unless a specific physical model explicitly requires hyperbolic geometry. Do not silently impose hyperbolic spacetime/physics on ordinary CELL simulations.

## Evolution object

A candidate architecture is a versioned genome/manifest, not opaque generated code.

It records:
- geometry;
- materials;
- connections;
- primitive versions;
- parameters;
- constraints;
- parent candidate IDs;
- mutation/operator;
- random seed;
- simulation fixtures;
- scores/measurements;
- failure modes;
- validation receipts;
- buildability notes.

## Goblin ladder

### G0 Probe Goblin
Runs one fixed fixture against one candidate. No mutation.

### G1 Parameter Goblin
Explores bounded parameter ranges without changing topology.

### G2 Geometry Goblin
Proposes bounded geometry changes using allowed primitives.

### G3 Circuit/Connection Goblin
Explores legal routing, gating and coupling variants.

### G4 Coupling Goblin
Explores interactions among validated electrical, magnetic, thermal and mechanical primitives.

### G5 Builder Goblin
Evaluates manufacturability, component availability, tolerances, instrumentation and bench-test accessibility.

### G6 Adversary / Validator Goblin
Searches for instability, hidden energy/accounting errors, overfitting, numerical artifacts and failed controls. Cannot silently repair a candidate.

### G7 Evolution Foreman
Schedules populations and experiments, enforces budgets, compares receipts, preserves diversity and promotes only candidates satisfying declared acceptance gates.

Higher goblins use the same FIELD/VOID worker contracts as the digital brain ladder. They are bounded workers, not unconstrained autonomous agents.

## Evolution cycle

`SEED → SIMULATE → MEASURE → CHALLENGE → MUTATE/RECOMBINE → REPLAY → VALIDATE → HOLD|REJECT|PROMOTE → REENTER`

Promotion requires reproducibility under frozen fixtures plus held-out tests. Failed candidates remain inspectable rather than disappearing.

## Real-world lock gate

Simulation may produce:
- REJECTED
- HOLD / unresolved
- SIMULATION-SUPPORTED
- BUILD-CANDIDATE

Only physical receipts can later produce bench-supported status.

A BUILD-CANDIDATE packet must contain exact BOM/material targets, geometry, tolerances, wiring/netlist, expected traces, instrumentation, safety/limits, falsification tests and simulation receipts.

## Visual program

Desktop application target:
- downloadable installer;
- chamber/world viewport;
- CELL/lattice geometry;
- live field/state overlays;
- goblins visible as named workers with current bounded job;
- candidate family tree;
- timeline/replay;
- FIELD/VOID state;
- measurements/residuals;
- failure visualization;
- compare two candidates;
- pause/step/run;
- inspect exact assumptions and primitive versions;
- export a BUILD-CANDIDATE packet.

The visual representation is explanatory. Scientific measurements come from solver state, never pixel positions.

## App-store/mobile version

Mobile is an observer/controller first:
- watch chamber runs;
- inspect goblin jobs and receipts;
- pause/resume/queue bounded jobs;
- compare candidates;
- receive promoted-candidate notifications;
- inspect replay and build packet;
- originate jobs through the GitHub Device Lattice.

Heavy simulation may execute on laptop/Jetson/other authorized workers. The app must preserve the same request IDs and provenance.

A later device-capable build may run lightweight local simulations where practical.

## Persistence

Every run must be restartable from:
- engine version;
- primitive versions;
- candidate genome;
- seed;
- fixture;
- solver settings;
- worker/goblin versions;
- receipts.

No evolutionary result counts if it cannot be replayed.

## Product architecture

Keep separate layers:
1. Physics Core
2. Candidate/Genome Store
3. Experiment Runner
4. Goblin Worker Runtime
5. Validator/Promotion Gate
6. Replay/Receipt Store
7. Visual Chamber
8. Desktop Packaging
9. Mobile/App-Store Client
10. Device-Lattice Adapter

## Build order

Do not begin with the animated chamber.

1. accumulate validated primitive modules;
2. establish common physics-engine interface;
3. combine enough primitives into deterministic CELL-space fixtures;
4. implement candidate manifests + replay;
5. add G0/G1 exploration;
6. add adversarial validation;
7. add geometry/coupling/buildability goblins;
8. add evolution Foreman;
9. add visual desktop chamber;
10. package downloadable desktop application;
11. add mobile observer/controller and app-store packaging.

The visual product grows around an inspectable engine; it must never become a visual demo disconnected from the scientific solver.
