# Ternary windings — motors and actuators

The actuator is not a second invention. It is the **same three windings** on the three figure-8s.

A B C hex seats already are a three-phase set. Two-of-three + PERMIT already is commutation permission. HOLD already is coast. Collapse already returns to V_BUS (regen).

No FOC chip required for the proposal. Field-oriented control is a later overlay if someone wants sine. The cell speaks UP / HOLD / DOWN.

---

## Map

| Cell | Winding / machine |
| --- | --- |
| PUSH on heading axes | torque / force that way |
| PULL | reduce |D|, current toward CENTER |
| FLIP | reverse that axis |
| PASS / HOLD | coast — switches open, current steers to V_BUS |
| PERMIT off | no PUSH/FLIP |
| send-up (bus redline) | PASS, ask pack |

Three half-bridges on V_BUS = the ordinary three-phase inverter *topology*. The *brain* of it is two-of-three, not a PWM timer.

---

## What HOLD is on a motor

Coast / regen. Current has to go somewhere; it goes to the bus lattice. That is the same reinjection. A parked actuator is HOLD + leftover Br in the figure-8, not a shorted winding unless you choose a brake (that's a different action, not default).

---

## Sequence (proposal)

Rotate heading A→B→C by which two axes are IN the same way. That *is* six-step / ternary step on a three-phase machine. Smoothness later. First: the same PERMIT that fires the flower can turn a shaft or a linear coil if those windings *are* the figure-8 windings or are coupled to them.

Do not add a second ABC that ignores the cell. If you need more force, scale current on V_BUS or stack flowers. Don't invent a fourth phase.

---

## Linear actuators

Same map. One figure-8 can be a voice-coil / solenoid pair (+ window / − window). HOLD = rest. PUSH/PULL = throw. FLIP = other direction. Three of those at 120° on the hex is a planar stepper if you want it. Still one bus.
