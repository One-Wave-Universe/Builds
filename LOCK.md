# Lock list

If it is here, stop re-litigating it in the packet.

## Object
- Sandwich cell: top ternary, figure-8 iron, bottom V_BUS lattice
- Hex seats clockwise A+ B+ C+ A- B- C-
- Three diffs, one CENTER
- Figure-8 square ferrite **per axis** (two squares, +/− windows)
- Hysteresis = **settled whole loop**, not three widgets
- Bus fed by everything, feeds everything
- Leftover **current** from all three diffs gated to V_BUS
- Pack only on ask; redline send-up → PASS
- No clock. Event = band crossing
- No weight file. No created energy. No drum. No hear yet

## Nodes
- V_TOP = pair headroom from pack (Cell-0: 9 V)
- CENTER = lean home (not pack, not bus)
- V_BUS = energy home
- 1 V map = D bands, not pack volts

## Coherence
- Two-of-three current-sum, unit = Iss, trip 1.5 / release 1.2
- GAP inhibit at the trip
- PERMIT_UP/DOWN → PUSH/FLIP on heading only
- PULL and PASS always allowed

## Actuator
- Same three windings. HOLD = coast/regen to bus
- Heading rotate A→B→C = ternary step

## Sequence of boards
1. Cell-0 one pair + one figure-8, see D and leftover Br
2. Gate that pair onto a BUS row
3. Second axis drinks a live rail vs a dead rail
4. Three axes + sum block + PERMIT
5. Flower tile

## Still pick-at-build, not pick-at-philosophy
- Schottky then sync
- LDO vs divider for V_TOP
- How much three figure-8s bleed in-plane (120° first)
- Heat fade rate
- Exact FET kit beyond 2N7000 / LM339-class
