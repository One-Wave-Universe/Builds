# Breadboard — minimum validation fixture

This fixture is only for proving the first electrical / magnetic relations. It is **not** the final CELL_V1 geometry.

## Rails

- V_TOP / test supply = bench headroom.
- CENTER = local differential reference.
- V_BUS = separate recovery / readiness rail.
- Never short CENTER to V_BUS.

## First differential

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
