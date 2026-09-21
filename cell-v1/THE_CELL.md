# The cell

Two faces. Both powered.

**Top:** ternary. Six seats, three pairs, CENTER, three cores between the faces.
**Bottom:** reinjection. Mirror loop + V_BUS + steering + C_BUS + pack ask + send-up.

Bottom is not a ground plane. It is the return of the top trit and the reservoir that drinks the collapse.

---

## Seats (same outline both faces)

```
                    A+
                 ________
                /        \
           C-  /          \  B+
              |   CENTER   |
           B-  \          /  C+
                \________/
                    A-
```

A+ top ↔ A- bottom = axis A (core A in between). Same for B, C.

---

## Bottom — reinjection

```
 pack --ask-- V_BUS =====================
                  |         |         |
               steer A   steer B   steer C
                  |         |         |
                C_A       C_B       C_C
                  |         |         |
               wind A    wind B    wind C   ↑ through cores to top pairs
                  |         |         |
                HB A      HB B      HB C
```

- Collapse of an axis stays on this face → steer → V_BUS.
- Next axis drinks V_BUS first. That is reinjection.
- Pack only fills E_loss.
- Sag → ask. Still falling → send up → PASS.
- Neighbor hex shares this bottom rail and the shared edge. Not top CENTER.

---

## Top — ternary

Three D's against CENTER. HOLD / two-of-three. DC stand, AC shove, RC in the core (between faces).

---

## Side view

```
  top power -- ternary pairs -- CENTER
                 |
               cores
                 |
  bottom power -- HB / wind / steer -- V_BUS reinjection lattice -- pack
```
