# CELL-0 — primitive mirror + magnetic hold

Body state first. One pair. One square-loop core.

**Voltage: whatever the parts already take.** Right now that is a rechargeable 9 V and 2N7000 / BS170.

## Law

- Asymmetry past the fence → move
- Balance inside the fence → hold
- `D = DB − DC` is the lean in the path
- CENTER holds that lean (core on CENTER)
- Loss and waste do **not** go to CENTER. They go to the DC bus. See `REINJECT_BUS.md`

## Netlist (lean first)

```
VCC = one rechargeable 9 V battery +
PACK- = that battery −

R1 10k : VCC — DB (Q1 drain)
R2 10k : VCC — DC (Q2 drain)
Q1, Q2 : 2N7000 or BS170
Q1 source + Q2 source = CENTER
Square-loop ferrite on CENTER (memory/magamp, NOT EMI bead)
Do NOT tie CENTER to PACK- until T3 is written.
Do NOT tie CENTER to the bus.

R3 100k : Q1 gate (B) — PACK-
R4 100k : Q2 gate (C) — PACK-
C1 100nF : VCC — PACK- at the battery clip
```

```
        9V+
       /   \
     R1     R2
      |     |
     DB     DC     lean meter here (D = DB-DC)
      |     |
     Q1     Q2
      |     |
      +--+--+  CENTER ----[ square-loop core ]---- header
                         (not PACK-, not BUS)

        leftover drain / kick --+--> BUS bar --> C_BUS reservoir
```

Add `C_BUS` and the bus bar after T5. Not before. Lean first.

## BOM

| Ref | Part | Qty |
|-----|------|-----|
| Q1 Q2 | 2N7000 or BS170 | 2 |
| R1 R2 | 10 kΩ | 2 |
| R3 R4 | 100 kΩ | 2 |
| C1 | 100 nF | 1 |
| Core | square-loop memory/magamp toroid | 1 |
| Power | one rechargeable 9 V | 1 |
| Board | 400-point breadboard | 1 |
| Meter | DMM | 1 |
| C_BUS | reservoir cap on the bus (after T5) | 1 |

## Tests — LOG.md

T1 gates not floating.
T2 both gates low: DB and DC near 9 V.
T3 gate B to 9 V, C low: DB falls. Write DB, DC, D.
T4 swap gates: D reverses sign.
T5 rails off: leftover field on the core matches last D sign.
T6 (after bus is on): V_BUS rises when an event ends. CENTER did not take that charge.

No extra chips. No millivolt hunt. Parts that exist.
