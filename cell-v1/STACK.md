# Stack

Bottom to top, one hex:

```
PACK ask
V_BUS copper (circulation)
heavy-metal strip (Ta / W / Pt)     ← actions-down write (SOT later; now just a conductor under)
square-ferrite figure-8             ← CENTER home, views-up read
Permalloy / ferrite skin on hex edges ← hysteresis lattice
three diffs (pairs)                 ← D vs CENTER
V_TOP
```

The heavy-metal strip runs **under the 8 and under the bus lattice**. Same write current that dumps to V_BUS can torque the magnet on the way. Read stays on the 8 / the pairs. Write stays under.

First board: the “heavy metal” can be the copper itself (Oersted only). Swap in Ta/Pt when you plate. Do not wait on a fab to lock the stack.
