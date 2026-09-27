# CELL_V1 — current prototype parts map

This is a **prototype / validation BOM**, not a claim that the final topology is fixed.

## Architecture constraints

- **No designed resistors in the CELL control, threshold, CENTER, or reinjection architecture.**
- Do not create a resistor-based bias ladder, dead band, damping path, bleed path, or loss-return path.
- Real copper/core/device losses are measured as losses; they are not intentionally created as the return mechanism.
- Core CELL_V1 control is analog and threshold / hysteresis driven.
- No LM339 or op-amp controller is part of the architecture.
- No global clock.
- No software state controller.
- CENTER and V_BUS are separate.
- The common body differential interface is two **plain round toroids**.
- **Motor-control nucleus = square figure-8 toroid.**
- Sensor nucleus = round figure-8 toroid.
- Five-mind nucleus = double pentagon.
- Six-mind nucleus = double hexagon.
- **M4 nucleus = two triangular/pyramidal toroidal loops base-to-base.**
- **Cluster-routing pyramids = separate six pyramidal/wedge magnetic routes. Tip-to-tip inside the cell, base-to-base between cells.**

## Minimum validation hardware

| Part class | Purpose | Status |
| --- | --- | --- |
| Logic-level MOSFETs / matched FET pair | create and steer opposed analog differential | exact part open |
| Capacitors | local decoupling and V_BUS reservoir | required |
| Plain round ferrite toroids, pair | FIELD/VOID body differential interface | geometry locked, material open |
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

- resistor threshold ladders;
- resistor damping / bleed / dump returns;
- LM339 comparator bank;
- op-amp decision controller;
- microcontroller state machine;
- PWM/FOC controller standing in for the cell brain;
- software weight memory.

Test instruments may observe the cell. They do not become the cell.


## Bidirectional nerve-gate requirement

Each mirror gate requires a **bidirectional analog wave path** around CENTER/(0). The prototype target is discrete MOSFET/passive/magnetic gating, not an IC switch or digital gate.

Electrical target: **CELL normalized signal span ≤1 V**, oscillating about CENTER at every gate step.

Part-selection requirements:
- bidirectional signal/current handling in the chosen topology;
- usable conduction with the *actual* available gate-source overdrive;
- low enough RDS(on) in that operating region;
- matched/opposed behavior around CENTER;
- low leakage relative to HOLD-band currents;
- parasitic capacitance small enough not to dominate the wave/phase relation;
- no assumption that datasheet VGS(th) means the device is fully ON;
- characterize transfer curve and RDS(on) on the bench before locking the MOSFET.

A back-to-back MOSFET arrangement is a candidate when true off-state blocking in both current directions is required; exact topology remains open until the nerve-gate current direction and body-diode behavior are measured.


## A/B/C differential cell — physical build skeleton

A/B/C are **three physical winding/power axes**, not the four action states. The established power-stage skeleton is three discrete half-bridges (six power MOSFETs total):

```text
                         MAIN ENERGY / V_BUS
                                |
                +---------------+---------------+
                |               |               |
              QAH             QBH             QCH
          A high MOSFET    B high MOSFET    C high MOSFET
                |               |               |
                A               B               C
                |               |               |
           A winding       B winding       C winding
                |               |               |
              QAL             QBL             QCL
           A low MOSFET     B low MOSFET     C low MOSFET
                |               |               |
                +---------------+---------------+
                                |
                         RETURN / V_BUS
```

The three phase/axis midpoints A, B and C feed the CELL winding/actuator geometry. Their magnetic vector sum is the proven physical precedent for a rotating field. The exact CELL winding placement on the square figure-8 nucleus and common body toroids remains experimental.

### What drives the six MOSFET gates

The power MOSFETs are **not the decision-maker**. Gate intent comes from the CELL's analog process:

```text
new VIEWS UP
      ^
      | bidirectional wave around CENTER
mirror gate 3
      <-> CENTER/(0)
mirror gate 2
      <-> CENTER/(0)
mirror gate 1
      | bidirectional wave around CENTER
      v
old ACTIONS DOWN
      |
analog nerve-gate / gate-bias translation
      |
A/B/C six-MOSFET power stage
      |
windings / actuator / load
      |
back-EMF + hysteretic consequence + reinjection
      |
next VIEWS UP
```

**Three mirror gates = one complete loop = one FLIP.** Old actions down and new views up coexist during the loop. Every mirror-gate relation oscillates around CENTER/(0).

### <=1 V nerve signal boundary

The CELL nerve/wave signal target is <=1 V normalized span. That is a **signal/state domain**, not permission to connect it blindly to six power-MOSFET gates. Datasheet VGS(th) marks channel onset, not guaranteed low RDS(on). The build therefore requires either power devices characterized for the actual available VGS or a discrete analog gate-bias/translation stage that supplies the required gate-source swing without inserting a digital/IC decision controller.

### Memory through the actuator loop

Memory is the history dependence of the same analog process at multiple persistence scales:
- short: live winding current, charge, phase, flux and back-EMF;
- mid: local nucleus/core hysteresis and remanence;
- long: the single Phase-I domain-wall hysteretic body-state layer / connected path network beneath the body grid.

The actuator is part of the loop: load changes current/flux/back-EMF, so physical action returns a changed view. V_BUS carries shared energy/reinjection; retained history belongs to the hysteretic process/path, not bus voltage alone.
