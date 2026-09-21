# Breadboard — row by row (400-point)

Left block columns A–E, right F–J. Numbered 1–30.

## Rails

- Top red: **1.00 V** (or 9 V seeing-aid — still *call* it the pack, not the map)
- Bottom blue: **0 V**
- Row 15 A–J reserved **CENTER 0.50 only**. Do not jumper row 15 to blue.

## Pair (leans)

| Row | What |
| --- | --- |
| 5 | Q1 TO-92, facing you S-G-D on 5C 5D 5E |
| 8 | Q2 same on 8H 8I 8J |
| 3 red → 5E | 10 k drain Q1 |
| 3 red → 8J | 10 k drain Q2 |
| 5D → blue | 100 k |
| 8I → blue | 100 k |
| 5C → 15C | Q1 source to CENTER |
| 8H → 15H | Q2 source to CENTER |
| 1 red–blue | 100 nF |

Meter: 5E vs 15 = one side. 8J vs 15 = other side. Lean = difference.

## Figure-8 / toroid

Magnet wire: leave 15F, through toroid (or two toroids as 8), back to 15G. That is CENTER in iron. Not to blue.

## Bus row (after you see leftover on the core)

| Row | What |
| --- | --- |
| 22 | BUS |
| kick node → 1N5819 → 22 | steer |
| 22 to blue | 1 µF |
| optional 10 nF | at the diode anode to blue |

Row 22 is not row 15.
