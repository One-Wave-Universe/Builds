# CELL_V1 View / Action Stack

## Canonical paired differentials

The three paired differentials are:

1. **BC–DC** — binary choice / direct polarity relation.
2. **TC–AC** — ternary correction / alternating relation around CENTER.
3. **QC–RC** — quadratic coordination / rotating-current relation.

All three preserve the same active CENTER/(0) reference. They are nested physical relations, not three unrelated controllers.

## BC–DC — binary/direct layer

BC–DC establishes the first opposed relation around CENTER.

- BC presents the balanced binary/polarity relation around `− / (0) / +`.
- DC is the resolved direct signed relation.
- This is the point/state layer: an opposed physical relation resolves direction without a clocked software state machine.

## TC–AC — ternary/alternating layer

TC–AC carries the signed relation through an alternating out-and-back physical traversal around CENTER.

Its local resolution is:

```text
DOWN / HOLD / UP
  −  / (0) / +
```

HOLD is active balance, not OFF. This layer supplies the ternary correction/oscillation relation while preserving the same CENTER reference.

## QC–RC — quadratic/rotating layer

QC–RC is the higher rotating/field relation. It coordinates the lower opposed/alternating relations into a continuously physical orientation/phase/strength state.

The current motor-control implementation candidate places this operation in the **square figure-8 toroidal nucleus**. Two coupled differential/alternating components can be treated as orthogonal components of a magnetic vector. Their combined field can rotate as their relative signed magnitudes/phase change.

For components X and Y:

```text
B_view = X x_hat + Y y_hat
|B_view|^2 = X^2 + Y^2
theta = atan2(Y, X)
```

The quadratic quantity is therefore a candidate physical field relation, not a digital calculation block. Exact winding geometry and whether the square figure-8 realizes the required vector field remain bench/simulation targets.

**No IC/chip implementation is required by this architecture.** The build target is continuous analog electrical/magnetic behavior: windings, differential bias, flux coupling, hysteresis and threshold response.

## Four views UP

QC/RC carries four physical descriptors upward:

1. **Direction**
2. **Phase**
3. **Strength**
4. **Reference**

These are views of the current physical state, not four separate memories.

## Four actions DOWN

The resolved higher/local state returns through four action relations:

1. **Inward**
2. **Outward**
3. **Across**
4. **Over**

Do not collapse these four actions into A/B/C. A/B/C are the three mirrored spatial differential axes / edge-seat pairs of the cell.

## Resolution / closure

The current structural compression is:

```text
BC–DC direct/binary relation
        ↓
TC–AC ternary/alternating relation
        ↓
QC–RC quadratic/rotating relation
        ↓
4 VIEWS UP
Direction / Phase / Strength / Reference
        ↓
higher/local physical resolution
        ↓
4 ACTIONS DOWN
Inward / Outward / Across / Over
        ↓
local ternary resolution
DOWN / HOLD / UP
        ↓
binary / Void closure
        ↓
settled physical state
        ↓
new views UP
```

This is recursive: **UP → resolution → DOWN → NEW STATE → NEW UP**.

The binary/Void closure is the final opposed confirmation/closure step after ternary action resolution; it does not replace CENTER/(0), which remains the active balanced ternary reference.

## Motor-control physical mapping

```text
BC–DC + TC–AC
      ↓
continuous differential / alternating bias
      ↓
square figure-8 toroidal nucleus
      ↓
QC–RC rotating/vector magnetic state
      ↓
4 views UP
      ↓
resolution
      ↓
4 actions DOWN
      ↓
− / (0) / + local ternary
      ↓
binary / Void closure
      ↓
A/B/C physical differential consequences where required
      ↓
two plain round outer/body toroids
      ↓
etched hysteretic lattice paths
= distributed muscle memory
      ↓
protected inductive return → V_BUS
      ↓
next physical state
```

## Memory and energy anti-drift

- Square figure-8 motor-control nucleus: local retained magnetic state candidate.
- Etched hysteretic lattice paths: distributed muscle-memory layer.
- V_BUS: shared energy/readiness/reinjection rail; bus voltage is not the stored muscle memory.
- CENTER/(0): active balanced virtual-ground ternary reference; CENTER is not V_BUS.
- The process/path history is the memory mechanism being tested.
- No MCU, digital state machine, PWM/FOC controller, MTJ memory, or IC multiplier is the intended CELL_V1 decision mechanism.

## Validation boundary

Established analog electromagnetic precedents can support individual operations, but they do not prove this integrated stack. The first useful tests must establish:

1. BC–DC signed differential around CENTER.
2. TC–AC stable alternating/ternary behavior around the same CENTER.
3. two-component magnetic vector/rotation in the square figure-8 nucleus;
4. reproducible Direction/Phase/Strength/Reference readout proxies;
5. four-action projection without a hidden digital controller;
6. ternary action resolution and binary/Void closure;
7. history-dependent response in nucleus and etched lattice paths;
8. protected recovery to V_BUS without corrupting CENTER or retained path state.


## Reference map for this stack

Mechanism-level evidence is centralized in `PROVEN_PARTS_REFERENCES.md`.

- **BC–DC / TC–AC opposed analog relations:** conventional differential/transformer behavior is established; CELL naming and thresholds are architectural mappings.
- **QC–RC rotating/vector magnetic relation:** resolver orthogonal magnetic channels (R1) and rotating-field machinery (R3) are the established precedents. The square figure-8 implementation remains experimental.
- **Direction / Phase / Strength / Reference:** these are CELL's four descriptors of the physical view. Resolver/rotating-field references establish measurable direction/phase/amplitude phenomena, not the CELL semantics.
- **Inward / Outward / Across / Over:** CELL four-action layer; no external reference is claimed to prove this mapping.
- **A/B/C:** synchro 120-degree electromagnetic geometry (R2) and three-half-bridge motor stages (R7) are established precedents for three physical axes/power legs. Four-actions → A/B/C mapping remains experimental.
- **Hysteretic memory:** ferrite hysteresis (R4) and patterned magnetic/domain-wall paths (R5,R6) establish history-dependent magnetic mechanisms. Useful CELL memory remains a measurement.
- **Reinjection:** inductive/DC-link return is established (R8). Useful shared CELL reinjection without disturbing CENTER/memory remains experimental.

**Evidence rule:** never promote a mechanism-level reference into proof of the complete CELL loop.
