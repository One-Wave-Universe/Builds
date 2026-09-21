# THE BUILD

1.00 V hex cell. Letters are edges. Two memories. Bus under. This page is the whole thing.

---

## Volt

Cell **1.00 V**. Home **0.50 V**. HOLD wobble **0.45–0.55 V**, live not off. 9 V is never the architecture.

---

## Shape

Point-up hex. Six letters **are the six edges**, clockwise A+ B+ C+ A- B- C-. Not the points.

A flower is seven hexes. Neighbors share a **side**. Middle A+ *is* neighbor A- on the same copper, same bus, same skin. Corners cannot connect a flower.

Hex is a slice. Seven hexes is still a slice.

---

## Top

Three leans into one home.

**Figure-eight shape = two squares with a shared middle.** That shared middle sits on the 0.50 home. That remanence is **one-cell memory**.

---

## Bottom

Same six edges. 1 V bus copper on those edges. All leftover current gates onto that copper. The bus feeds every lean. Pack only pays loss. If the bus is still falling, stop pushing.

**Lattice skin on those edges = group memory.** Shared side, shared diary.

Cap on the bus = last kick only. Reinject = refresh only. Not diaries.

Home is not the bus. Never one pour.

---

## Loop

New views up → last action down → new state → repeat.
New views **are** last actions plus what came back up.
FLIP is the last move, both ways on the same gate.
Off dumps to the bus.

---

## Gates

Three axes, bidirectional. CHOICE → PIVOT → FLIP, bidirectional. Both readings on. Never both directions ON.
Two agrees → push. One voice waits. Fight holds. Gap waits.
Same windings may throw. No extra controller in Phase I.

---

## Analog nets / crossbars

Steal current-add and no clock. Refuse a downloadable G and a row-column grid. Shared edge is *meant* to be common (group memory), not a sneak error. Isolation we need is home ≠ bus.

---

## Parts

Logic-level N-FETs (2N7000 only as seeing-aid), 10 k loads, 100 k gates to 0 V, 100 nF on pack, two square-loop rings (magamp, not EMI bead), 30 AWG, Schottky 1N5819, 10 nF, 1 µF, copper for edges, Permalloy or ferrite foil for skin, DMM. Divider to 0.50 if the pack is not already split.

---

## Breadboard

Red = 1.00 (or dirty headroom you still *map* as 1 V). Blue = 0. Row 15 = home only. Q1 ~row 5, Q2 ~row 8, sources to 15. Magnet wire 15 through the two rings back to 15. Row 22 = bus. Diode to 22. Cap 22 to blue. Never 15 to 22.

---

## Underside how

Flip hex. Copper on all six **sides**. Foil along that copper. Keep-out under the home island. Each lean's kick → Schottky → that copper loop.

---

## PCB

40 mm flat-to-flat. Pads on side midpoints. Home island + two-square footprint. Bottom pour = bus, not stitched to home. `cad/pcb_hex.svg`.

---

## Phase I

1. See a lean against 0.50.
2. See leftover on the two-square home.
3. Kick moves bus, not home.
4. Second lean feels live bus vs empty bus.
5. Raw energy fraction.

---

## Out

Drum. Hear. Weight file. 99%. Standard Model in this repo. Science C-317 keeps the vortex/tension analogy.

---

## Also

`RULES.md` `GRANT.md` `cell-v1/CELL.md` `cell-v1/FLOWER.md` `cell-v1/MEMORY.md` `cell-v1/PARTS.md` `cell-v1/BREADBOARD.md` `BUILD_BOOK.md`
