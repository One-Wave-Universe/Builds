# Cell-0 breadboard (400-point)

One pair. See D. Bus after leftover field on the core.

```
Red rail  = V_TOP = pack +
Blue rail = PACK-
CENTER    = its own row. Not blue.
```

## Placement

| Part | Where |
| --- | --- |
| Pack + 100 nF | at the clip, across red/blue |
| Q1 2N7000 | left, G D S toward you |
| Q2 2N7000 | right, same |
| R1 10k | red → Q1 drain |
| R2 10k | red → Q2 drain |
| R3 100k | Q1 gate → blue |
| R4 100k | Q2 gate → blue |
| CENTER jumper | Q1 source ↔ Q2 source |
| Core | CENTER wire through the toroid to a header. Not to blue |

Meter DB vs CENTER and DC vs CENTER. D = DB − DC. Or meter DB to DC.

No CENTER on blue. No EMI bead. C_BUS 1 µF from a new BUS row to blue only after the core shows leftover sign.

Three diffs later: three of these, one CENTER star, V_BUS strip on the long edge.
