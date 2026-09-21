# Proposed architecture

Physical analog cell. State is the settled loop after an event — hysteresis. Not a weight file. Not a simulation of a cap.

Science stays in One-Wave-Science. Fiction stays in Mythos-and-Stories. No drum. No hear yet.

Start drawing: `cell-v1/THE_CELL.md`

---

## The object

Two faces, both powered.

**Top — ternary.** Point-up hex. Edge-center ports. Clockwise `A+ → B+ → C+ → A- → B- → C-`. Three differentials star to one CENTER. HOLD wobble `0.45–0.55`. Commit ±1 ±2 ±3.

**Between — square ferrite figure-8 per axis.** Two squares, one magnetic loop, + window / − window. Three figure-8s so axes can oppose. Not an EMI bead.

**Bottom — bus-side lattice.** Reinjection. Mirror of the top trit. Every leftover current from all three diffs gates onto V_BUS. The bus is fed by everything and feeds everything. Pack only on ask. Still falling while asking → send up → PASS.

Hysteresis is the **whole loop settled** (top + figure-8s + gates + rail), not three separate widgets.

---

## Three nodes (never shorted)

| Name | Job |
| --- | --- |
| V_TOP | Quiet analog headroom for the pairs. From the pack. Cell-0: 9 V. |
| CENTER | Lean home. Mid of the pairs. Allowed to move a little. |
| V_BUS | Energy home. Living rail. Pulses, sag, ask, redline. |

1 V map = lean bands across the pair. Not the pack voltage.

---

## Lean

`D = V(+) − V(-)` per letter. Direction, magnitude, hardness (Iss / write depth).

```
Idiff = Iss · tanh(Vd / (2 · n · Vt))
```

DOWN / HOLD / UP. HOLD is live tail, not off.
DC = stand. AC = shove. RC = leftover in the settled loop.

No clock. Crossing a named band *is* the event. Path busy until CENTER is home and the bus kick has settled.

---

## Two-of-three → metal

Each axis: HOLD / GAP / IN + sign.
Gated ±Iss into SUM. One unit = one Iss. Trip 1.5, release 1.2.
GAP OR inhibits at the trip (walking third).
PERMIT_UP / PERMIT_DOWN unlock PUSH/FLIP on heading axes only. PULL and PASS always allowed.
Comparators on V_TOP. Buffer PERMIT off SUM.

Law: agree → reinforce. oppose → HOLD. one voice → wait.

---

## Energy

Return walks the figure-8 then the gate then V_BUS. Memory and recovery are one path.

```
E_in  = ∫ V I dt
E_rec = ½ C (V²_after − V²_before)
```

Never claim 100%. Pack is makeup for loss.

---

## Flower

Seven sandwiches. Shared bottom edge + V_BUS. CENTER stays local. Twelve mirrors from tiling.

---

## Addressing vs body

Rabbit Hopping names a place. It does not hold the lean. Zer0 may *name* a settle. The body is the hysteresis.

---

## Locked vs open

**Locked:** sandwich, hex seats, three diffs, figure-8 per axis, settled hysteresis, two-of-three current-sum, PERMIT gating, V_TOP / CENTER / V_BUS, bus fed-by/feeds-all, leftover current gated, no clock, no weight file, no created energy.

**Open:** exact Iss transistors, fade with heat, sync vs Schottky first on a given board, how hard three figure-8s talk in a flat hex.

**Hypothesis:** flower computes, ring is under-loop, inverted stack is a split.

---

## Files

`cell-v1/THE_CELL.md` `HYSTERESIS.md` `SQUARE_FERRITE.md` `BUS_LATTICE.md` `TWO_OF_THREE.md` `PERMIT_DRIVE.md` `TOP_RAIL.md` `REFERENCE.md` `CELL0.md` `BREADBOARD.md` `cad/`
`GRANT_CELL.md` `GRANT.md`
