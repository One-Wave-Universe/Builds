# Build book — the 1 V cell

This is the long packet. Architecture volts: **1.00 / 0.50 / 0.45–0.55**. Ports on hex **sides**. Three leans into the middle. Bus and lattice **under**.

Print this file. About ten pages.

---

## 1. What you are building

A small hex sandwich.

The top face is three leans and a home in the middle. The home is 0.50 V. The wobble around it (0.45–0.55) is live, not off. A figure-8 of square-loop ferrite sits on that home so the middle can remember.

The bottom face is the bus and the lattice. Every leftover current from the three leans is steered onto a 1 V rail that runs the hex edges. That rail feeds every lean. A pack only pays what was lost as heat. If the rail keeps falling, you stop pushing. The edges of that under-hex wear a magnetic skin so the *mesh* can keep a long trace. A capacitor on the rail keeps the short echo.

Two faces. Not one pour. The middle is not the bus.

You look at what you just did. You do the last move. That move plus what came back up *is* the next view. Repeat.

---

## 2. What you are not building in this book

Not a drummer. Not a hearing box. Not a proton. Not a 9 V product. Not a weight file. Not a PCB fab that plates platinum on Friday.

9 V appears only if your FETs will not move at 1 V. Then you run dirty headroom and you still **write 1 V numbers** in the notebook.

---

## 3. Parts — cell top

| Qty | Part | Job |
| --- | --- | --- |
| 1 | 400-point breadboard or the hex PCB | Body |
| 1 | Supply that can sit at 1.00 V, or a bench supply | Pack |
| 2–6 | BSS138 or other logic-level N-FET; 2N7000 only as seeing-aid | Leans and bidirectional switches |
| 2 | 10 kΩ 1% | Drain loads |
| 2 | 100 kΩ 1% | Gate to 0 V |
| 2 | 10 kΩ | Divider that makes 0.50 if the pack is not already a 1 V split |
| 1 | 100 nF C0G | Across the pack |
| 1–2 | Square-loop / magamp toroids | The 8. Two rings touching = figure-8. Not an EMI suppression bead |
| 1 m | 30 AWG magnet wire | 10–20 turns through the 8 |
| 1 | DMM | Middle vs each drain |

TO-92 facing you is usually source-gate-drain. Read the bag anyway.

---

## 4. Parts — bus and lattice under

| Qty | Part | Job |
| --- | --- | --- |
| 1 | 1N5817 / 1N5819 Schottky | Steer leftover current onto the bus |
| 1 | 10 nF C0G | Local catch at the steer |
| 1 | 1 µF film or X7R | Bus reservoir |
| 1 length | Bare copper or insulated wire | Hex edge bus |
| 1 scrap | Permalloy foil, mu-metal foil, or thin ferrite sheet | Magnetic skin under or around those edges |
| tape / epoxy | Hold foil to the underside without shorting the middle |

Later, not this box: electrodeposited NiFe on copper, Ta/W/Pt strip under the 8 for spin-torque write. Phase I is foil + copper + diode.

---

## 5. How the top goes together

Draw a point-up hex. Put six pads on the **midpoints of the sides**, clockwise A+ B+ C+ A− B− C−. Corners stay empty.

In the middle, an island. That island is CENTER at 0.50 V. The figure-8 lives on that island. No via from that island into the bottom bus pour.

Each lean is a pair of FETs whose sources (or the analog-switch commons) meet on the island. Drains go toward the side pads through the 10 k loads to 1.00 V. Gates sit quiet at 0 V through 100 k until something leans them.

On a breadboard the same thing is rows: pack on the red rail, 0 V on blue, **row 15 is CENTER only**, Q1 around row 5, Q2 around row 8, magnet wire from 15 through the toroid back to 15.

Meter the two drains against row 15. The lean is the difference. Wobble inside 0.45–0.55 is not a commit.

---

## 6. How the underside lattice is made

Flip the hex.

Run copper around all six edges. That loop is V_BUS. It is 1 V class. It is allowed to sag. It is not 0.50.

At each edge you may lay a strip of Permalloy or ferrite foil **along** the copper, insulated if the foil would short a pad you do not want shorted. The copper carries current. The foil keeps remanence after the current is gone. That is the lattice skin.

Shared edge with a future neighbor is shared copper **and** shared skin. That is why the long memory is group memory.

Do not let the underside copper flood the CENTER island. Tape or a milled slot or a keep-out. If CENTER and BUS become one metal, the cell is dead as an idea.

---

## 7. How leftover current gets to the bus

When a lean stops being driven, the winding on the 8 still has flux. Flux changing is voltage. That pulse must not dump on CENTER.

Path: winding node → Schottky (or later a sync FET) → bus copper → 1 µF to 0 V.

On the breadboard that is **row 22**. Diode from the kick to 22. Cap 22 to blue. Row 22 is never jumpered to row 15.

All three leans get a diode onto the **same** row 22. One reservoir. Next lean drinks row 22 first. Pack only if row 22 will not come back.

If row 22 is still falling while you are asking the pack, stop pushing. That is send-up.

---

## 8. How the 8 sits on the home

Two square-loop rings side by side, magnet wire through both, is the figure-8. One ring is the baby version.

The wire that is CENTER goes through the iron. The iron is the home remembering. Views live with that home. The last move happens toward the underside. What the bus does (rise, sag, send-up) comes back up and **is** the next view.

You are not building sixteen chips. You are building one 8 and letting use harden which pairings you actually take.

---

## 9. Gates both ways

A single N-FET is one-way because of the body diode. Two N-FETs back-to-back (sources tied, gates tied) pass either way when on, and block both ways when off. That is one bidirectional gate.

Three sides get that treatment when you leave the seeing-aid pair. Off is PASS: current has to go somewhere, it goes to the bus through the Schottky, not through a shorted winding unless you later add a brake on purpose.

Never turn both directions on at once.

---

## 10. Two agrees

Each lean is either in the wobble, walking the gap, or committed one way.

If two committed leans point the same way and the third is not committed the other way, you may push. If the third is still in the gap, wait. If they fight, hold.

That rule can be a current-sum later (LM339 + analog switches). Phase I can be you watching the meters. The law is the same.

---

## 11. Order of work

1. Middle 0.50 exists and is quiet.
2. One lean visible against that middle.
3. Leftover remanence on the 8 after you let go.
4. Kick on the Schottky, bus row moves, middle does not.
5. A second lean that feels a charged bus differently than an empty bus.
6. Skin foil on one edge. See if the leftover lasts longer.
7. Third lean. Then permit. Then six neighbors.

Do not start at seven hexes.

---

## 12. Notebook

Every sitting:

- pack voltage
- middle voltage
- bus voltage before and after a kick
- whether the 8 still had a preferred way after you let go

Energy in vs energy back is a fraction. Write the fraction you got. Do not write 99.

---

## 13. PCB notes

40 mm flat-to-flat hex is enough for Phase I parts. Two layers. Bottom pour = bus, keep-out under CENTER. Pads on side midpoints. Fat trace under the 8 on the bottom is the write strip (copper now, heavy metal later). No KiCad file is in this repo yet. `cad/pcb_hex.svg` is the floorplan to trace.

---

## 14. Grant sentence

One-volt hex. One home. Three leans. Leftover current is the blood. History in the home and in the under-mesh. Coherence instead of a timer. Phase I is steps 1–5 of section 11.

---

## 15. Files

`cell-v1/CELL.md` short lock  
`GRANT.md` submit page  
`cell-v1/PARTS.md` table  
`cell-v1/BREADBOARD.md` rows  
`cad/pcb_hex.svg` board  
This book: `BUILD_BOOK.md`
