# CELL

## Canonical CELL_V1 lock

**1 volt normalized axis.** CENTER **0.50 / 50.** HOLD band **0.45–0.55 / 45–55.** Seven-band scale locked below.

Letters **are the six edges:** A+ B+ C+ A− B− C−. Flowers share sides. Opposed edges form three mirrored axes.

Three leans. Ternary is **DOWN / HOLD / UP** around **− / (0) / +**. **All analog. No global clock.**

## One cell, four coupled layers

1. **Square figure-8 toroidal nucleus — brain side**
   - The square figure-8 toroidal structure is the cell nucleus.
   - It is the brain-side retained-state structure coupled to the lattice-bus / vagus-nerve side.
   - It is not CENTER and it is not V_BUS.
   - Its magnetic history biases the next physical state.

2. **Three mirrored differential axes around the nucleus**
   - A+↔A−, B+↔B−, C+↔C− are three spatial axes / edge-seat pairs, not three voltage levels.
   - Each axis is one opposed differential bias loop across the two sides of the cell around the nucleus.
   - Each axis can be live on both sides while its net lean resolves DOWN / HOLD / UP around CENTER.
   - The cell-level action is formed from the coupled A/B/C leans; A, B, and C are not a promotion ladder.
   - CHOICE → PIVOT → FLIP is the voltage-gated depth ladder inside the differential behavior, not A → B → C.
   - Threshold crossings, hysteresis, retained state, bus condition, and neighbor state drive transitions.

3. **Two outer round figure-8 toroidal structures — motor-field shell**
   - The two outer round figure-8 toroidal structures form one combined outer electrical / magnetic field.
   - They carry **six windings total**, organized as **two mirrored groups of three**.
   - The 3+3 winding system amplifies the cell's resolved − / (0) / + lean into a larger differential bias for motor control.
   - The six windings are not six independent motors or six independent gates.

4. **Lattice bus / vagus-nerve side**
   - V_BUS is the shared energy / readiness / reinjection rail across the lattice.
   - CENTER is the local lean reference and stays distinct from V_BUS.
   - Collapse energy returns to V_BUS; it is never dumped onto CENTER.
   - Neighbor coupling and returned consequences feed the next cell decision.

## Unified loop

```
neighbor / sensor consequence
        ↓
square figure-8 nucleus
(retained-state bias)
        ↓
three mirrored gate pairs
(A, B, C differential)
        ↓
− / (0) / + ternary lean
        ↓
two outer round figure-8s
6 windings = mirrored 3 + 3
        ↓
combined motor / field action
        ↓
collapse / inductive return
        ↓
V_BUS reinjection + lattice consequence
        ↓
next nucleus / gate decision
```

No subsystem bypasses the ternary decision. Nucleus, gates, outer windings, reinjection, bus, and neighbor coupling are one coupled physical state machine.

## Locked seven-band differential scale

Normalize each axis to a 0–100 differential magnitude scale around CENTER = 50.

| Band | State | Gate depth |
| --- | --- | --- |
| 100–90 | +3 | FLIP |
| 85–75 | +2 | PIVOT |
| 70–60 | +1 | CHOICE |
| 55–45 | 0 | HOLD |
| 40–30 | −1 | CHOICE |
| 25–15 | −2 | PIVOT |
| 10–0 | −3 | FLIP |

The unassigned 5-point windows are hysteresis / transition gaps:

- 90–85
- 75–70
- 60–55
- 45–40
- 30–25
- 15–10

These gaps are intentional anti-chatter regions. They are not extra logical states. Entry and exit direction through a gap depend on the prior settled state / hysteresis history.

Locked mapping:

```
±1 = CHOICE
±2 = PIVOT
±3 = FLIP
0  = HOLD
```

A/B/C each use this same seven-band scale. A/B/C remain three spatial differential axes around the nucleus; the seven bands are the voltage / magnitude states on each axis.

## Axis / gate / scale law

Keep three different things separate:

1. **Axis:** A, B, C = three mirrored spatial differentials around the nucleus.
2. **Gate depth:** CHOICE → PIVOT → FLIP = voltage-gated progression as differential magnitude crosses calibrated hysteretic bands. It must also be able to fall back through the bands as the lean relaxes.
3. **Scale:** POINT → PATH → FIELD = larger coupled organization. Scale promotion is not the same thing as moving from A to B to C.

A live differential may oscillate / circulate around CENTER while carrying a net lean. HOLD means the opposed sides remain active but balanced closely enough that no directional commit is permitted. Crossing a voltage band changes gate depth; it does not rename the active axis.

Next view = last move + what came back up.

Two agrees → push.  
One voice → wait.  
Opposition → HOLD.  
Drive off → return energy to V_BUS.

HOLD is live readiness around center, not a clocked idle.

## Hard anti-drift rules

- Square figure-8 = **nucleus / brain side**, not the bus itself.
- Two outer round figure-8s = **combined outer field shell**.
- Six outer windings = **mirrored 3+3**.
- A/B/C are axes, **not voltage levels**.
- CHOICE/PIVOT/FLIP are the voltage-gated depth ladder.
- POINT/PATH/FIELD are scale states and must not be collapsed into A/B/C.
- CENTER ≠ V_BUS.
- No global clock or timing-based commutation.
- No second controller that bypasses the cell's ternary decision.
- Reinjection must re-enter the same state loop.
- Do not claim measured retention, coupling, recovery, torque, or efficiency until bench data exists.

This file is the CELL_V1 authority. Detail files must agree with it.
