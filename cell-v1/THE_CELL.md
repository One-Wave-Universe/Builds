# The cell

Two faces of one hex. Both powered.

**Top:** ternary. Three differentials. Six seats. CENTER.
**Under:** mirror loop of that ternary. Same six seats, opposite polarity through the lattice. V_BUS lives here too.

The under lattice is not a dead ground pour. It is the mirror of the top trit.

---

## Seats (same on both faces)

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

Clockwise both faces: A+ → B+ → C+ → A- → B- → C-

Top A+ is mirrored under to A-. That via / lattice path *is* axis A.

---

## Side view — one axis (all three look like this)

```
   TOP power
        |
     pair top     A+ trit (DOWN / HOLD / UP)
        |
     [ core A ]
        |
     pair under   A- trit (mirror)
        |
   UNDER power + V_BUS lattice
```

Top ternary and under ternary are one loop. Flip on top is the opposite seat under. That is the mirror, not a second brain.

```
D_A = V(A+ top) - V(A- under)
D_B = V(B+ top) - V(B- under)
D_C = V(C+ top) - V(C- under)
```

CENTER is the top home for those reads. Under home is the lattice mid on V_BUS *class*, not the same node as CENTER.

---

## Power on both sides

Top rail feeds the top pairs.
Under rail feeds the mirror pairs + half-bridges + steering.
Pack asks **under** (V_BUS sag → refill). Top rail can be derived from under or a second tap from the pack. Two powered faces. Still only two *references*: CENTER (top home) and V_BUS (under home / energy).

Do not short top rail to V_BUS as CENTER.

---

## What the under lattice does

- Closes each axis: + seat on top to - seat under (and the reverse on the next event).
- Tiles neighbor hexes: shared edge is shared mirror metal.
- Carries V_BUS so collapse stays under. Reinjection stays under.
- Sends up (redline) from under when the loop cannot refill.

Top never dumps an event into CENTER. Under takes the collapse.

---

## Event

1. Top HOLD. Under HOLD.
2. AC on the loop (top and under are the two ends).
3. Two-of-three on the three D's.
4. Collapse stays under → V_BUS.
5. RC in the core between the faces.

Flower = seven of these sandwiches. Shared under-edge is the neighbor mirror.
