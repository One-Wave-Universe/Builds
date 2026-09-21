# Hex bus architecture

Two different buses live on the same tiling. Do not merge them.

1. **Axis bus** — signal / lean. Three directions. A, B, C. Mirrors at opposite edges.
2. **Power bus** — shared DC rail. Every cell draws and returns. Not CENTER.

---

## Why hex (not a square mesh)

A square grid has two wiring directions. A hex has **three**. That is the same count as the three mirrored axes.

Cube / axial addressing for a hex tile:

```
q + r + s = 0
```

Neighbors are one step on two of those axes. Distance is half the taxicab on (q,r,s). This is standard hex-grid law (Red Blob Games / cube coords). It is how you *name* cells. It is not the lean.

On silicon, hex tiles show up as NoC / many-core layouts: six neighbors, shorter average hop than a 4-neighbor mesh, ~3% more area per tile, often less total application area because interconnect is denser. Power on those chips is still a *separate* grid (P/G mesh or hex TSV bundle). Same split we want: neighbor links ≠ supply.

Honeycomb *magnetic* lattices (recent patents) use the hex as a reservoir you current-drive. Different job. Do not steal their “the lattice is the neuron.”

---

## Axis bus (A / B / C)

Six edge seats, three physical channels:

```
        B+
     A+    C+
     A−    C−
        B−
```

Clockwise: A+ → B+ → C+ → A− → B− − C−.

Each pair is one bidirectional port. Lean picks direction.

**Flower wiring (automatic):**

- Center A+ meets neighbor A− (and same for B, C). Six center–outer mirrors.
- Two outers that share an edge: one’s leftover axis meets the other’s opposite. Six outer–outer mirrors.
- Total 12. No extra harness.

**Outer ring** N1→N2→…→N1 does not have to go through the center. That is a second path on the *axis* bus, not a second power rail.

Routing on the axis bus is local: a cell only talks to edge neighbors. No packet router in the proposal. If a later scale needs a name for a cell, use (q,r,s) with q+r+s=0. Rabbit addressing is the *logical* hop, not a third metal layer.

---

## Power bus (shared DC)

One rail spans the flower, then the volume.

```
  +V_BUS --------+-----+-----+-----+
                 |     |     |     |
               cell  cell  cell  …
                 |     |     |     |
  return --------+-----+-----+-----+
                 C_BUS local, then the rail
```

Every cell:

- draws from V_BUS to run the pair and the half-bridges
- steers winding collapse into its C_BUS, then back onto V_BUS
- does **not** dump that charge onto CENTER

CENTER is per-cell (or per-axis) floating reference. Sharing CENTER would short every lean together. Sharing V_BUS is how the lattice couples *readiness* without coupling *memory*.

Hex-tile compute papers already share power on the edges of the tile and keep IO as separate point-to-point. That is the right split. Their IO is digital. Ours is the A/B/C ports.

**Sag is a feature in the proposal:** V_BUS is a lattice state variable (high / low / rising / falling). It is not a precision lab supply that must stay flat. External feed only replaces loss.

**Star vs ring on the power bus**

- Flower: one local rail ring around seven cells is enough. Center and six outers tap the same metal.
- Volume: stack flowers; run V_BUS as vias at edge-centers (same seats as the signal ports, different layer).
- Do not run V_BUS down the same winding as A+.

Three metal kinds, minimum:

| Layer | Carries |
| --- | --- |
| AXIS | A, B, C ports |
| BUS | V_BUS / return |
| REF | CENTER, local only |

---

## What hex does *not* give you for free

- A clock. Still event-driven.
- A packet NoC. Six neighbors are analog ports, not routers.
- Isolated grounds if you pour one copper pour for BUS and REF.
- Equal current in all six neighbors. Lean is allowed to be asymmetric.

---

## Proposal sentence

The interconnect is a hex lattice with three bidirectional axes and a fourth, shared DC rail. Axes carry leans. The rail carries recovered energy and lattice readiness. References stay local. The flower’s twelve mirrors are the tiling, not extra wire.
