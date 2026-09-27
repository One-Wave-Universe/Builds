# CELL_V1 — current prototype parts map

This is a **prototype / validation BOM**, not a claim that the final topology is fixed.

## Architecture constraints

- Core CELL_V1 control is analog and threshold / hysteresis driven.
- No LM339 or op-amp controller is part of the architecture.
- No global clock.
- No software state controller.
- CENTER and V_BUS are separate.
- The common body differential interface is two **plain round toroids**.
- **Motor-control nucleus = square figure-8 toroid.**
- Sensor nucleus = round figure-8 toroid.
- M4 nucleus = double triangle base-to-base.
- Five-mind nucleus = double pentagon.
- Six-mind nucleus = double hexagon.

## Minimum validation hardware

| Part class | Purpose | Status |
| --- | --- | --- |
| Logic-level MOSFETs / matched FET pair | create and steer opposed analog differential | exact part open |
| Precision resistors / bias network | establish stable differential test conditions | bench aid |
| Capacitors | local decoupling and V_BUS reservoir | required |
| Plain round ferrite toroids, pair | common body differential interface | geometry locked, material open |
| Square figure-8 ferrite assembly | motor-control-cell nucleus | geometry locked, material open |
| Round figure-8 ferrite assembly | sensor-cell nucleus | separate sensor role |
| Magnet wire | drive / sense / coupling windings | turns and gauge open |
| Schottky or synchronous recovery path | steer inductive collapse toward V_BUS | implementation open |
| Oscilloscope / DMM | measure differential, hysteresis, return, CENTER stability | required |

## First motor-control prototype

The first motor-control-cell-oriented bench target is:

```text
stable CENTER
-> opposed analog differential
-> square figure-8 motor-control nucleus
-> repeatable retained-state probe
-> common plain-round body pair
-> inductive return to V_BUS
```

Do not add higher-mind nuclei until the lower physical loop survives its measurements.

## What must be measured before scaling

- CENTER stability;
- differential DOWN / HOLD / UP boundaries;
- prior-write-dependent response;
- retention / decay;
- coupling between nucleus and common body pair;
- input energy and recovered energy;
- thermal drift;
- second-cell coupling.

## Not in the BOM as control logic

- LM339 comparator bank;
- op-amp decision controller;
- microcontroller state machine;
- PWM/FOC controller standing in for the cell brain;
- software weight memory.

Test instruments may observe the cell. They do not become the cell.
