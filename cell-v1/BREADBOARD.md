# Cell-0 breadboard (400-point)

One pair. See D. Bus after T5.

Power rail = V_TOP = 9 V pack. CENTER is a *row*, not the blue line.

```
400-point
+  [red line]   V_TOP  = pack +
-  [blue line]  PACK-  = pack -

LEFT half = Q1 (B / A+)
RIGHT half = Q2 (C / A-)
MIDDLE trench = CENTER jumpers only. No pack- there.
```

## Placement

| Part | Where |
| --- | --- |
| Pack clip | top rails, 100 nF right at the clip |
| Q1 2N7000 | left, pins facing you: G D S |
| Q2 2N7000 | right, same |
| R1 10k | V_TOP red → Q1 drain row |
| R2 10k | V_TOP red → Q2 drain row |
| R3 100k | Q1 gate row → PACK- blue |
| R4 100k | Q2 gate row → PACK- blue |
| CENTER wire | Q1 source row ↔ Q2 source row (one dedicated row) |
| Core | CENTER wire *through* the toroid, then to a header pin. Not to blue. |
| Meter + | Q1 drain (DB) |
| Meter - | Q2 drain (DC) |   wait that's D if floating; better two readings to CENTER |

Measure: DB vs CENTER, DC vs CENTER, then D = DB−DC. Or meter between DB and DC.

## Do not

- Do not put CENTER on the blue rail.
- Do not put the core on an EMI-bead junk loop to PACK-.
- Do not add C_BUS until T5 leftover field is seen.

## After T5 — bus tap

One extra row: BUS. Steering diode from leftover/kick node to that row. C_BUS 1 µF from BUS to PACK-. That row is V_BUS, still not CENTER.

## Hook for three diffs later

Repeat this triple on a bigger board. Three CENTER *stars* to one CENTER row. Three cores. Bottom rail = V_BUS strip along the long edge.
