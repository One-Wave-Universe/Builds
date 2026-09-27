# Build packet

Repo: https://github.com/One-Wave-Universe/Builds

## Sentence

CELL_V1 is a hardware-first analog control-cell family with a **common two-round-toroid body differential shell**, a **role-specific magnetic nucleus**, live -/(0)/+ state around CENTER, and measured inductive return to V_BUS.

## Geometry lock

- common outer/body interface for every cell role = **two plain round toroids**;
- sensor nucleus = round figure-8;
- **motor-control nucleus = square figure-8**;
- five-mind nucleus = double pentagon;
- six-mind nucleus = double hexagon;
- **M4 = the pyramidal routing/connection layer, not a nucleus:** tip-to-tip inside each cell; base-to-base between cells.

The square figure-8 is motor-control nucleus only.

## Shared electrical rules

- CENTER = local differential reference;
- V_BUS = shared energy / readiness / reinjection rail;
- CENTER != V_BUS;
- DOWN / HOLD / UP = - / (0) / +;
- HOLD is live;
- no global clock;
- no hidden software / comparator / op-amp controller;
- no designed resistor ladder, bleed, damping, or dump path in the intended CELL mechanism.

## First motor-control build

```text
one differential
-> square figure-8 motor-control nucleus
-> retained-state write / probe test
-> V_BUS recovery
-> common two-round-toroid body interface
-> second compatible path
-> full A/B/C
-> actuator test
```

Stop at the first failed premise.

## Evidence

- scope traces;
- current / voltage measurements;
- exact core material and winding record;
- retained-state A/B tests;
- retention / decay;
- CENTER stability;
- input versus recovered energy;
- thermal drift;
- coupling between two compatible paths.

## Maximize without lying

Say:
- most pieces are established engineering technologies;
- the novelty is the proposed integration and recursive physical loop;
- the build is explicitly falsifiable;
- exact performance is not claimed before measurement.

Do not claim:
- free energy;
- fixed recovery percentage;
- measured torque or efficiency without data;
- proven intelligence / consciousness;
- a full working cell before the hardware log proves it.

## Read next

`RULES.md`  
`cell-v1/CELL.md`  
`cell-v1/NUCLEUS_TOROID_TYPES.md`  
`cell-v1/CELL_ASSEMBLED.md`  
`GRANT_CELL.md`  
`FULL_BUILD.md`
