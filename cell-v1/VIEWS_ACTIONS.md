# Views Up & Actions Down — The 4×4 Lattice Couplings

The lattice is the full body state. It is one continuous magnetic medium spanning the entire collective group. Every cell writes to it, every cell reads from it, and its physical magnetization pattern is the body's combined state.

---

## 1. Views Up — Reading the Body State

Each cell's figure-8 read head reads the continuous lattice underneath it. That inductive interrogation is a view up.

| View | Meaning | Memory Read | Strain Read |
|:---|:---|:---|:---|
| **BASELINE** | Resting magnetization | Lattice resting pattern at node | Baseline load / resting flux density |
| **DELTA** | Change rate | Excursion since last event ($d\Phi/dt$) | Rate of change of mechanical / electrical load |
| **HEADING** | Trajectory | Direction of movement (deepening/fading) | Trajectory of strain (rising or falling toward saturation) |
| **RESULT** | Committed state | Remanence state post-write | Residual committed strain level |

Views up = the cell interrogating the body state across four angles on the same lattice.

---

## 2. Actions Down — Writing the Body State

The cell's collapse pulse and drive current write back to the lattice. That physical write is an action down.

| Action | Meaning | Physical Write | Strain Impact |
|:---|:---|:---|:---|
| **PULL** | Route inward | Draw from lattice, reinforce toward center | Relieves outward strain, consolidates charge |
| **PUSH** | Route outward | Drive into lattice, deepen trace past $H_c$ | Incurs high strain, risks driving toward saturation |
| **FLIP** | Invert polarity | Invert magnetic domain orientation | Rapid excursion, high instantaneous $\mathrm{d}\Phi/\mathrm{d}t$ |
| **PASS** | Continue | No write, let state stand (coast) | Zero strain addition, allows thermal/bus relaxation |

Actions down = the cell modifying the body state through four physical operations.

---

## 3. The 4×4 Coupling Matrix

Four views up $\times$ four actions down = sixteen physical couplings.

```
              VIEWS UP (reading lattice)
              BASE  DELTA  HEAD  RESULT
              │      │      │      │
    PULL ─────┼──────┼──────┼──────┤
              │      │      │      │
    PUSH ─────┼──────┼──────┼──────┤
ACTIONS       │      │      │      │
DOWN          │      │      │      │
    FLIP ─────┼──────┼──────┼──────┤
              │      │      │      │
    PASS ─────┼──────┼──────┼──────┤
              │      │      │      │
```

These sixteen couplings are not a software lookup table. They are sixteen physical analog routing paths through the figure-8 read/write stack.

---

## 4. The Recursive Closure

The last action down becomes the new view up:

$$\text{View Up} \longrightarrow \text{Action Down} \longrightarrow \text{Lattice Changes} \longrightarrow \text{New View Up} \longrightarrow \text{New Action Down} \dots$$

The cycle closes because the cell is always reading what it just wrote, and the lattice is always carrying the latest state.

---

## 5. Full Body State, Fully Connected

- A write at cell 1 propagates across the shared medium to cell 7.
- A read at cell 7 includes cell 1's history.
- Every cell's action down is part of every cell's view up.

The body state is one connected medium. Views up read it. Actions down write it. Sixteen couplings. One recursion. One body.
