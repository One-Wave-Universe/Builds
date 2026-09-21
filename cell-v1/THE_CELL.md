# The cell (one drawing)

One operator. Six seats on a hex. Three differentials. Three cores. Two references.

---

## Shape and seats

Point-up. Ports at edge centers. Clockwise:

```
                    A+
                 ________
                /        \
           C-  /          \  B+
              |            |
              |   CENTER   |
              |     V0     |
           B-  \          /  C+
                \________/
                    A-
```

`A+ → B+ → C+ → A- → B- → C- → A+`

Opposite sides are one axis:

```
A+ ───[ core A ]─── A-      D_A
B+ ───[ core B ]─── B-      D_B
C+ ───[ core C ]─── C-      D_C
```

Cores sit at A+, B+, C+. Minus seat is the other end of that same core.

---

## Three differentials on one home

Each letter is a pair. Sources star to **one CENTER** inside this hex.

```
     A+ pair          B+ pair          C+ pair
        \                |                /
         \               |               /
          +----------- CENTER ----------+
          |              V0              |
          +--------------+---------------+
         /               |               \
        /                |                \
     A- end           B- end           C- end
```

```
D_A = V(A+) - V(A-)
D_B = V(B+) - V(B-)
D_C = V(C+) - V(C-)
```

All three against this V0. Two-of-three reads D_A, D_B, D_C.
HOLD wobble 0.45–0.55. Commit when two agree and the third is not opposed.

---

## Drive and return (same hex, other metal)

Each axis: half-bridge → winding on that core → local cap → steer to **V_BUS**.

```
  pack --ask-- V_BUS ----+------+------+
  (makeup only)          |      |      |
                      C_BUS   C_BUS  C_BUS   (one reservoir)
                         |      |      |
                      steer  steer  steer
                         |      |      |
                      windA  windB  windC
                         |      |      |
                       HB A   HB B   HB C
```

V_BUS is the **other** reference. Energy, refill ask, redline send-up.
D is never measured on V_BUS. Collapse never dumps on CENTER.

DC = committed stand on an axis.  
AC = shove across the fence.  
RC = leftover on that axis core.

---

## What this hex is

| Piece | Where |
| --- | --- |
| Six seats | hex sides clockwise |
| Three diffs | A, B, C opposite pairs |
| Three cores | at + seats |
| One home | CENTER in the middle |
| One rail | V_BUS around / under, not the middle node |
| Commit | two-of-three on the three D’s |
| Flower | this hex plus six neighbor hexes sharing edges |

Neighbor hex shares one side (one port). Shared edge is the event. Shared V_BUS is readiness. CENTER does not pour into the neighbor.
