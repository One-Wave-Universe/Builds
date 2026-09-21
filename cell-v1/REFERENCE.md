# References connect — at the right scale

D = DB − DC only means something if both sides share a home.
Three D’s in one flower only mean something if they share **one** home.

That home is CENTER. It must connect. It must not connect everywhere.

---

## Inside one flower: one CENTER

Seven pairs, three cores, one virtual ground.

```
   pair A    pair B    pair C
      \        |        /
       +---- CENTER ----+
                 |
            quiet V0
```

All DB/DC in that flower are measured against this node. Two-of-three is illegal if each axis invents its own 0.50.

CENTER is **electrical**. It is not a fourth core. No ferrous bar through the three cores using CENTER as the yoke — that would magnetically merge H again.

How V0 is made (proposal): resistive divider or a quiet buffer from V_BUS, then left to float a little so history can sit in the pair. Stiff lab ground as CENTER kills the moving-home idea. Stiff V_BUS *as* CENTER dumps collapse into the lean. Separate pin.

---

## Between flowers: do not pour CENTER

Neighbor flowers share **V_BUS** and share an **edge (axis port)**.
They do **not** share a fat CENTER pour.

If you stitch every CENTER together with thick copper, every lean in the field is one node. Fights become shorts. Memory becomes the rail.

Allowed between flowers:

- V_BUS common (readiness)
- axis metal at the shared edge (the event)
- a *weak* bias (high-Z) so homes sit in the same voltage *class* (all near mid-rail), not the same instantaneous volt

High-Z tie: large resistors from each flower CENTER toward a mid reference derived from V_BUS. Enough to stop homes wandering to the rails. Not enough to equalize a live D.

---

## Three metals again

| Net | Connects |
| --- | --- |
| AXIS | neighbor to neighbor at edges |
| V_BUS | every cell, whole lattice |
| CENTER | **star inside one flower only** |

CENTER vias do not hop to the next flower.

---

## Sense of three cores

Center cell reads D_A, D_B, D_C against **that flower’s** CENTER. That is the connection you wanted: references meet at the integrator, not in the iron.
