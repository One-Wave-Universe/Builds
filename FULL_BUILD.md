# FULL BUILD — sit this tonight

Repo: https://github.com/One-Wave-Universe/Builds

This is the one packet. Architecture volts **1.00 / 0.50 / 0.45–0.55**.
Bench parts may run at 9 V headroom. You still write 1 V numbers.

Simulator: `algorithms/full_cell.py`

```
python3 algorithms/full_cell.py
```

That file is a model. Empty `cell-v1/LOG.md` still means 0% hardware.

---

## Sentence

A hex sandwich. Three differentials lean off CENTER. Square-ferrite figure-8 holds flux on the home. Leftover current all gates to one V_BUS that feeds everyone. Two-of-three current-sum permits PUSH. Fight holds. Gap waits. Same windings can later turn a shaft.

## Laws

- Event, not clock.
- Home is not the bus. Never one pour.
- HOLD wobble 0.45–0.55 is live, not off.
- Leftover kick → Schottky → bus. Pack only pays loss.
- If the bus is still falling, SEND-UP. Stop pushing.
- Two agrees → PUSH. One voice waits. Fight holds.
- Never both directions ON.
- Actuator = those windings. No extra controller in Phase I.

## BOM — Cell-0 (exists-parts)

| Qty | Part | Job |
| --- | --- | --- |
| 1 | 400-point breadboard | Body |
| 1 | Rechargeable 9 V (map as 1.00) | Pack |
| 2 | 2N7000 or BS170 | Seeing-aid pair |
| 2 | 10 kΩ 1% | Drain loads R1 R2 |
| 2 | 100 kΩ 1% | Gate to 0 V R3 R4 |
| 1 | 100 nF C0G | Across pack |
| 1 | Square-loop / magamp toroid (NOT EMI bead) | Home memory |
| 1 m | 30 AWG magnet wire | 10–20 turns through the core |
| 1 | 1N5819 Schottky | Kick to bus |
| 1 | 10 nF C0G | Local catch |
| 1 | 1 µF film or X7R | Bus reservoir |
| 1 | DMM | Lean meter |

Later: second pair of logic-level N-FETs back-to-back for bidirectional gates, Permalloy foil on edges, 40 mm hex PCB.

## Breadboard rows

- Red rail = pack + (call it 1.00 even if dirty 9 V)
- Blue rail = 0
- Row 15 = CENTER / home only
- Q1 ~row 5, Q2 ~row 8, sources to 15
- Magnet wire 15 through the core back to 15
- Row 22 = BUS. Diode from kick node to 22. Cap 22 to blue
- **Never jumper 15 to 22**

## Netlist

```
VTOP V_TOP 0 DC 9
R1 V_TOP DB 10k
R2 V_TOP DC 10k
R3 GB 0 100k
R4 GC 0 100k
C1 V_TOP 0 100n
MQ1 DB GB CENTER 2N7000
MQ2 DC GC CENTER 2N7000
D1 KICK BUS 1N5819
CBUS BUS 0 1u
* core on CENTER; not a DC element
* CENTER is not 0 and is not BUS
```

## Phase I order (stop at the first fail)

1. Middle 0.50 exists and is quiet under switching.
2. One lean visible against that middle. D = DB − DC.
3. Leftover remanence on the core after you let go. Sign matches last D.
4. Kick moves row 22. Row 15 does not take that charge.
5. Second lean drinks a live bus differently than an empty bus.
6. Write the energy fraction you got. Do not write 99.

Nothing past 5 matters until 5 works.

## Permit

Each axis: DOWN / HOLD / UP from its volts vs 0.45–0.55.

- two UP, zero DOWN → PUSH+
- two DOWN, zero UP → PUSH−
- mixed committed → HOLD
- two in the gap → WAIT
- bus falling while you ask the pack → SEND-UP

Phase I permit is you watching two meters. LM339 later.

## Geometry lock

Point-up hex. Letters are **edges**, clockwise A+ B+ C+ A− B− C−.
Flower = seven hexes. Neighbors share a **side**. Center A+ *is* neighbor A− on the same copper.
Do not start at seven hexes.

## What this is not

Not a drummer. Not a proton. Not a weight file as the memory.
Not software backprop. Memory is the lean in the path plus remanence in the 8 plus skin on the bus edges.

## Grant sentence

One-volt hex. One home. Three leans. Leftover current is the blood. History in the home and in the under-mesh. Coherence instead of a timer. Phase I is steps 1–5.
