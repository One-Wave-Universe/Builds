# Hysteresis

Known physics. New arrangement.

**Hysteresis** — state depends on history, not only the live input.
**Remanence** — what stays when drive is gone. The trace.
**Write depth** — how deep that trace is. Shallow to deep, not 0/1.
**Lean** — this event.
**Trace** — the path that kept it.

We did not discover hysteresis. We use it as **graded write depth** on three axes.

---

## Where it lives

On the **bus-side lattice path** — the same winding/core the collapse walks through to V_BUS.

Top pair makes D. Under steer dumps leftover current to the rail. Between them the core is on that loop. Return does not go around the memory. Return goes *through* it.

```
 TOP lean (D)
      |
   [ core — hysteresis / remanence / write depth ]
      |
 BOTTOM lattice → gate → V_BUS
```

Three cores, three loops, one bus. Each axis keeps its own loop. Use deepens. Disuse fades.

---

## Pitch line

Remanence, hysteresis, and inductive recovery are old. The cell uses them as graded state on the bus-side lattice, not as a bit in a table. The trace depth is the memory.
