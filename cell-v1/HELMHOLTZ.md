# Shared Helmholtz field

Candidate common magnetic weather for a flower, and later for the two opposed flowers.

Not locked as measured. Not a nucleus. Not a body toroid. Not RC.

Added as an open build claim. Bench has to earn it.

## Job

Put every cell of a connected flower in one shared magnetic field so the lattice has a common bias volume, not only edge-to-edge gates.

The implementation candidate is a Helmholtz pair: two matched coils on a common axis, separated by about one coil radius, driven so the field between them is approximately uniform.

```text
coil +
  |  approximately uniform B
  |  flower sits in this volume
  |  second flower, inverted, may share the same volume
coil -
```

Both flowers can sit in that volume. Opposite polarity stays in the cells: FIELD against VOID, A+ against A−. The Helmholtz pair does not replace those mirrors.

## What it is not

- Not CENTER. CENTER stays the local differential reference.
- Not V_BUS. V_BUS stays the energy / readiness / reinjection rail.
- Not the square figure-8 nucleus. That stays the middle motor-control cell only.
- Not the round figure-8 nuclei. Those stay on the sensor ring.
- Not the two plain round body toroids. Those stay the FIELD/VOID differential interface, three windings each, A/B/C unshorted.
- Not the six wedge windings. Those stay on A+ B+ C+ A− B− C−.
- Not RC. RC is what a round core still holds after an event.
- Not the domain-wall / hysteretic body-state layer. That layer is path memory. A Helmholtz field is uniform on purpose. Uniform bias is a bad scar map.

Shared weather and shared scars are different jobs. Do not series them and call both the body.

## Relation to the rest of the stack

```text
Helmholtz pair
  shared approximately uniform B
        |
  flower volume
  center: square figure-8 motor-control nucleus
  ring: round figure-8 sensor nuclei
        |
  two plain round body toroids per cell
  FIELD side against VOID side
        |
  six wedge windings, three differentials, one CENTER
        |
  hysteretic under-layer keeps path memory
  V_BUS takes inductive return
```

The second flower is the inverted side. Upper A+ still meets lower A−. That joint stays a differential surface. The shared field does not hard-short the two flowers.

## Bench, or it is only a drawing

Record before any claim:

- coil radius, turns, wire, spacing, current, direction;
- measured B at center and at the flower edge;
- uniformity across one cell and across the seven-cell flower;
- CENTER drift with the pair on versus off;
- whether an identical probe still discriminates a prior write;
- whether V_BUS recovery changes when the pair is energized;
- whether the inverted flower sees the same sign or the opposite sign.

Fail if the shared field walks CENTER into the bus, erases retained state, or forces every cell to the same lean.

## Order

Do not build this before one differential, one nucleus, and one flower layer have a log.

Helmholtz is a later common-volume test. It does not skip Cell One.
