# CELL (canonical)

**One volt.** The cell is a 1.00 V analog map. CENTER home is 0.50 V. HOLD wobble is 0.45–0.55 V.

9 V is only a junk-box FET trick if you have no low-Vt parts. It is not V_TOP of the architecture. It is not the bus. It is not CENTER.

## Rails at 1 V

| Name | Volts |
| --- | --- |
| Pack / high | 1.00 |
| CENTER / V0 | 0.50 |
| HOLD | 0.45–0.55 |
| +1 / −1 | just outside HOLD |
| +2 / −2 | 0.65–0.75 / 0.25–0.35 |
| +3 / −3 | 0.80–0.90 / 0.10–0.20 |
| V_BUS | same 1 V class, living, sag allowed |

Do not scale the bands to 9 V. Do not call 9 V the cell.

## Object

**Top:** hex, edge-center ports clockwise A+ B+ C+ A- B- C-. Three pairs star to CENTER. Figure-8 on CENTER.

**Bottom:** 1 V V_BUS lattice. Leftover current in. Feeds everyone. Pack ask / send-up. Magnetic skin = Br. Cap = short echo. Reinject = refresh. Three jobs, not one word.

## Loop

New views up → last action down → new state → repeat.
New views = last actions + sent-up.

## D ladder (same 0.50 home)

D1 stand · D2 out-and-back · D3 rotate on the slice.

## Gates

Bidirectional on A B C and on CHOICE→PIVOT→FLIP. PERMIT 1.5 / 1.2 Iss units. PASS → bus.

## Sequence

See D at **1 V** (or a divider that *maps* to 1 V — the numbers you write down are 1 V numbers). Then bus, then D2, then third seat. Flower last.

Low-Vt / analog-switch silicon for real 1 V ports. 2N7000 at 9 V is a seeing-aid only. Do not publish 9 V as the cell.
