# Parts — worked out

## Cell-0 (buy this first)

| Qty | What | Why | Buy-class |
| --- | --- | --- | --- |
| 1 | 400-point breadboard | body | any |
| 1 | 9 V rechargeable + clip | V_TOP | pack |
| 2 | 2N7000 or BS170 TO-92 | Q1 Q2 pair | jellybean N-FET |
| 2 | 10 kΩ 1/4 W | drain loads | |
| 2 | 100 kΩ 1/4 W | gates to PACK- | |
| 1 | 100 nF ceramic | pack clip | |
| 1 | DMM | DB, DC, D | |
| 1–2 | **square-loop / magamp toroid** not EMI bead | figure-8 windows / CENTER | Magnetics magamp, VAC tape, or Proterial MEGAMP. Fair-Rite 61/43 is EMI — last resort only |
| 1 m | magnet wire 28–32 AWG | through the 8 | |
| 1 | 1N5819 Schottky | steer to BUS after Br seen | |
| 1 | 10 nF C0G | C_steer | |
| 1 | 1 µF film or X7R | C_BUS | |

Two toroids touching = figure-8. One toroid = Cell-0 baby window.

## Add for PERMIT (same board later)

| Qty | What |
| --- | --- |
| 1 | LM339 quad comparator | windows + sign + trip |
| 1 | CD4066 or TS5A analog switch | ±Iss into SUM |
| 1 handful | 10 k / 100 k for SUM and 1.5 / 1.2 dividers |
| 2 | more 2N7000 | half-bridge when you drive a winding |

## Lattice / stack (after D exists)

| What | Role |
| --- | --- |
| Copper wire or pour | V_BUS |
| Permalloy foil or square-ferrite sheet under the pour | hysteresis skin |
| Copper as the “heavy strip” | Oersted write now |
| Ta/Pt later | SOT write |

## Pin / hook (2N7000 TO-92, flat toward you)

Left to right: **S G D** (confirm the bag — some clones swap).

Q1 source and Q2 source = CENTER row only.

## Wind

10–20 turns on the toroid for Cell-0. Enough to see flyback on the Schottky. Not a transformer design yet.
