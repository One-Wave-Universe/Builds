# Windings and ternary actuator drive

The same three axes that lean also drive metal. A / B / C are windings. Ternary is the drive alphabet. No extra motor CPU is required in the proposal.

---

## One axis is already a motor leg

Half-bridge + winding + steering to C_BUS is a standard inverter *leg*. Three of them is a three-phase bridge.

Ternary on one leg:

| Trit | Bridge | Winding |
| --- | --- | --- |
| +1 UP | high-side on | current out A+ (or into A−) |
| 0 HOLD | both off **or** both low (choose) | float (coast) **or** short (brake) |
| −1 DOWN | low-side on | current the other way |

HOLD must pick **one** meaning per mode:

- **Coast HOLD** — both FETs off. Field collapses into C_BUS. This is the cell’s normal return.
- **Brake HOLD** — both lows on. Winding shorted. Fast stop. Energy stays in the copper until it dumps as heat unless you still steer.

Proposal default: **coast HOLD** so return stays on the bus. Brake is an override trit pattern, not the home state.

Never high and low on the same leg at once. Dead zone in the lean map is also dead time on the silicon.

---

## Three windings = six-step body

A three-phase BLDC / PMSM already lives on six states. Those six states *are* the hex seats.

Classic six-step (two legs on, one float):

```
1  A+ B−  C hold
2  A+ C−  B hold
3  B+ C−  A hold
4  B+ A−  C hold
5  C+ A−  B hold
6  C+ B−  A hold
```

Clockwise around the hex. Reverse the signs, reverse the shaft. That is FLIP on the rotation, not a second controller.

Each step: two trits committed (±1 or ±2), one trit HOLD. The floating phase is the cell in 0.45–0.55 on that axis.

Hardness / tail / duty on the two live legs is how hard the torque is — magnitude of the lean, not a PWM chip with a different religion. If you later PWM the high side to set torque, that is still the same leg. Call it magnitude. Do not call it a second brain.

---

## What each body part hangs on

| Actuator | Windings | Trit pattern |
| --- | --- | --- |
| 3-phase BLDC / PMSM | A B C wye or delta | six-step above |
| Brushed DC / voice coil / solenoid | one axis (A only) | + go, 0 coast/brake, − reverse |
| H-bridge limb (one joint) | two axes as a full bridge | A vs B differential |
| Drum / speaker | one winding, AC lean | rate of crossings is the pitch-ish; HOLD is silence |
| Haptic tick | short +1 or −1 pulse, then HOLD | one event |
| Linear voice coil 3-axis | A B C as XYZ coils | three independent trits |

A flower can drive six outer actuators plus a center (grip / posture) off one bus. Outers are limbs. Center is stance. That is hypothesized scale, not a required first drawing.

---

## Ternary vs FOC

Field-oriented control is a digital estimator plus sine PWM. It is allowed later as an *option* on the same three half-bridges. It is **not** the architecture.

The architecture is: the cell’s trit *is* the gate command. Position can come from the same magnetic core (reluctance / back-EMF on the floating leg — six-step already does that) or from a lean on a sense winding. No Hall required in the proposal. Hall is a cheap add-on, not the law.

Old ternary servo work (COS/MOS + complementary bipolars) already did: error trit 0 → motor off; +1 → CW; −1 → CCW. Same alphabet.

Multilevel inverters that use +1 / 0 / −1 per leg (NPC / ANPC) are the high-voltage cousin. Same trit, fancier silicon. Cite as family, not as the cell.

---

## Collapse while you drive

When a step ends, the outgoing winding’s field is steered to C_BUS *before* the next step seizes that axis. That is the same return law as the cell. Commutation is an event. The path is busy until CENTER is home and the kick has settled. Firing the next six-step state into a winding that is still collapsing is chatter — same as a second crossing in the refractory window.

Torque readiness follows V_BUS. Spent bus → weaker current → the limb *is* sluggish. Same readiness page. Not a feeling.

---

## What not to put in this drawing

- A separate MCU “ESC” as the intelligence. The cell issues trits. An ESC is a stand-in while the pair does not exist.
- FOC as the definition of the architecture.
- Sharing CENTER with the motor return.
- Cosmology, speech, hemispheres.

---

## Proposal sentence

Three half-bridges on A, B, C drive both the cell field and the body. Balanced ternary per leg is go / hold / reverse. Six hex seats are six commutation states. Hold defaults to coast so collapse returns to the shared DC bus. Brake is an override. Magnitude of the lean is torque. Rate of completed steps is speed.
