# Ternary windings — motors and actuators

The actuator is not a second brain. It is the outer field expression of the same CELL_V1 decision.

## Outer motor-field shell

The common outer/body field uses **two plain round toroids**.

A candidate implementation places **six windings total** across that common pair:

- round toroid A: three windings
- round toroid B: three mirrored windings

Together they may form a **mirrored 3+3 differential field system**, subject to bench validation.

For a motor-control cell, the **square figure-8 nucleus** and the live differential state resolve locally first. The common plain-round body pair then expresses the resolved state into the larger motor-field response.

## State map

| Cell state | Motor-field meaning |
| --- | --- |
| UP / PUSH | bias field in the resolved positive direction |
| DOWN / PULL | bias field in the resolved negative direction |
| HOLD / PASS | no new net drive; permit inductive return |
| FLIP | reverse the resolved axis relation |
| bus redline | prefer HOLD / PASS and reduce new drive |

HOLD is not a clocked pause. It is the physical center condition.

## Reinjection

When drive falls, winding energy is steered back to V_BUS. The returning energy and its consequence re-enter the same cell loop; they do not bypass the nucleus or create a second controller.

## Anti-drift

- Do not reduce the architecture to an ordinary three-phase inverter.
- Do not call the common outer/body round toroids figure-8s.
- The square figure-8 nucleus is motor-control-cell specific.
- Do not call the six windings six independent phases.
- Do not add a separate PWM/FOC controller as the CELL_V1 brain.
- Do not claim torque, efficiency, field strength, or recovery percentage until measured.
