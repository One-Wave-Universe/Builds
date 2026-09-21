# PARTS — Phase I (1 V cell)

Architecture volts are **1.00 / 0.50 / 0.45–0.55**. If you only have 2N7000s, you may run 9 V *hardware* and **write every number as 1 V map**. Do not call 9 V the cell.

## Buy now

| Qty | Item | Notes |
| --- | --- | --- |
| 1 | 400-point breadboard | |
| 1 | Adjustable 1.0 V supply **or** 9 V pack + divider later | Prefer a bench supply set to 1.0 V if FETs allow |
| 2 | 2N7000 or BS170 TO-92 | Seeing-aid FETs. Confirm S-G-D on the bag |
| 2 | BSS138 or similar logic-level N-FET | Better at 1 V gates |
| 2 | 10 kΩ 1% 1/4 W | Drain loads |
| 2 | 100 kΩ 1% 1/4 W | Gate leak to 0 V |
| 2 | 10 kΩ trim or 2×10 k | CENTER 0.50 divider if pack ≠ 1 V |
| 1 | 100 nF C0G | Across pack |
| 1 | 10 nF C0G | Local steer cap |
| 1 | 1 µF film or X7R | C_BUS |
| 1 | 1N5817 or 1N5819 Schottky | Bus steer |
| 1–2 | Square-loop / magamp toroid | Magnetics magamp, VAC tape, MEGAMP. Not Fair-Rite EMI-61 if you can help it |
| 1 m | 30 AWG magnet wire | 10–20 turns |
| 1 | DMM (two if you have them) | Home and bus at once |
| 1 pack | Dupont jumpers |
| 1 | Permalloy or mu-metal foil scrap | Under-bus skin experiment |

## Next (permit / second axis)

| Qty | Item |
| --- | --- |
| 1 | LM339 or LMV339 (1 V–friendly if possible) |
| 1 | TS5A3166 or CD4066 |
| 4 | Extra BSS138 / 2N7000 |
| 1 handful | 10 k / 100 k for sum node |

## PCB later (not Phase I required)

2-layer 1.6 mm, 1 V pour on bottom as V_BUS, top signal, hex outline 40 mm flat-to-flat, pads at **edge midpoints**, CENTER pad island not tied to bus pour, figure-8 footprint in the island.
