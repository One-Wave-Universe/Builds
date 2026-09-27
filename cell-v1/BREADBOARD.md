# Breadboard — minimum validation fixture

This fixture is only for proving the first electrical / magnetic relations. It is **not** the final CELL_V1 geometry.

## Rails

- V_TOP / test supply = bench headroom.
- CENTER = local differential reference.
- V_BUS = separate recovery / readiness rail.
- Never short CENTER to V_BUS.

## First differential

**No resistor bias ladder is part of this fixture or architecture.** Establish the differential with the selected discrete device / magnetic topology and expose all relevant nodes so CENTER formation is measurable rather than imposed by a resistor network.

Build one opposed FET pair and measure both sides relative to CENTER.

Required observation:

```text
D = V(+) - V(-)
```

The first goal is simply to establish a repeatable negative / balanced / positive differential around CENTER.

## Nucleus fixture

Choose the nucleus for the role being tested.

For the **motor-control-cell prototype**, use the **square figure-8 nucleus**.

For a later sensor-cell prototype, use the round figure-8 nucleus instead.

Do not treat the nucleus fixture as the common body toroid pair.

## Retained-state test

1. Apply a controlled write in one direction.
2. Remove the write.
3. Apply a fixed probe.
4. Record response.
5. Apply equal write in the opposite direction.
6. Apply the same fixed probe.
7. Compare responses.

If the responses are not repeatably distinguishable beyond noise / drift, stop and revise the retained-state premise.

## V_BUS recovery fixture

After retained-state discrimination works:

- steer one inductive collapse toward V_BUS;
- measure V_BUS rise;
- verify CENTER remains stable;
- record input and recovered energy.

## Common body interface

Only after the local nucleus / differential loop passes, add the **two plain round toroids** that form the common body differential interface shared by all cell roles.

The common round toroids are not figure-8s.

## Rule

Change one thing -> test -> compare -> record.

Do not add the next layer until the present relation is measurable.


## Added falsification tests

### Moving-reference boundedness
Apply repeated equal-direction write events. Measure whether the effective next-cycle reference:
- approaches a bounded repeatable offset; or
- walks monotonically into hard saturation.

Monotonic runaway without a physical release / rebase mechanism is a fail for the moving-reference implementation candidate.

### Triadic coherence candidate
When three A/B/C contributions are available, test a **physical-summing candidate** rather than a digital majority gate:
- 2 aligned / 1 opposed;
- 1 aligned / 2 opposed;
- balanced opposition;
- all near HOLD.

Measure summed flux/current, CENTER motion, threshold crossing, chatter, and retained-state dependence. Magnetic-majority behavior is a **candidate precedent**, not a locked CELL mechanism.

### Sector mismatch
Perturb one sector thermally or magnetically and measure:
- its opposed partner;
- both neighboring axes;
- CENTER;
- V_BUS;
- next-cycle lean.

This directly measures whether the six-sector geometry contains mismatch or spreads it through the cell.
