# The cell

Two layers. Same hex. Do not draw them as unrelated parts.

**Top:** three differentials, six seats, one CENTER, three cores.
**Under:** lattice metal + V_BUS reservoir + steering + pack ask.

---

## Top — lean

Point-up hex. Ports at edge centers. Clockwise:

```
                    A+
                 ________
                /        \
           C-  /          \  B+
              |   CENTER   |
              |     V0     |
           B-  \          /  C+
                \________/
                    A-
```

Walk: A+ → B+ → C+ → A- → B- → C- → A+

Three pairs on that same face, sources starred to CENTER:

```
A+ ---- pair A ---- A-     D_A = V(A+) - V(A-)
B+ ---- pair B ---- B-     D_B = V(B+) - V(B-)
C+ ---- pair C ---- C-     D_C = V(C+) - V(C-)
```

Core A at A+ (A- is the other end of core A). Same for B, C.

```
     pair A     pair B     pair C
         \         |         /
          +----- CENTER ----+
                    V0
```

HOLD 0.45–0.55. Two-of-three commit. Third walking → wait. Opposed → HOLD.

DC = stand. AC = shove. RC = leftover on that axis core.

---

## Under — lattice + bus

Same six sides, lower metal. Not CENTER.

```
 pack --ask-- V_BUS ==========================
                  |         |         |
               steer A   steer B   steer C
                  |         |         |
                C_A       C_B       C_C
                  |         |         |
               wind A    wind B    wind C     (through the cores above)
                  |         |         |
                HB A      HB B      HB C
```

V_BUS is the second reference: energy, refill, redline send-up.
Neighbor hexes share **under** (V_BUS + the edge port). They do not share top CENTER.

Tile under: hex lattice of those rails and edge metals. Top cells sit on that lattice.

---

## Stack (side view)

```
   A+  B+  C+  A-  B-  C-     seats
    |   |   |   |   |   |
  [ pairs + CENTER V0 ]       TOP  lean / RC
    |   |   |   |   |   |
  [ cores on A B C axes ]
    |   |   |   |   |   |
  [ HB, windings, steer ]     UNDER  AC drive / return
    |   |   |   |   |   |
  [ V_BUS + C_BUS lattice ]   UNDER  DC rail / ask / up
              |
            pack
```

Drive goes down through the core into the bus. Lean is read on top against CENTER.

---

## One event through both layers

1. Top HOLD.
2. AC on under half-bridges. D walks on top.
3. Two-of-three on top. DC stand or back to HOLD.
4. Field collapses under → steer → V_BUS. CENTER does not take it.
5. RC stays in that axis core (between the layers).
6. Bus quiet → loop. Sag → ask pack. Still falling → send up → PASS.

---

## Flower

Seven of these stacked hexes. Center hex + six outers. Shared sides are shared **ports + under rail**. Twelve mirrors from tiling. Same law.
