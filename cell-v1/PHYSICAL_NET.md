# Physical analog network

Reinjection is a current that has to land somewhere. A vector in a simulator is a description. The architecture is copper, silicon, C, L, D.

Not a routing algorithm. Not BASIS as the thing.

---

## Per axis

```
V_BUS -- steering (diode first, sync later) -- local C_steer -- winding -- half-bridge -- return
```

Local cap sees the winding collapse. Not the FET Vds as a substitute.

Start values (proposal, not a measured result):

- C_steer ~ 10 nF, C0G/X7R, at the winding
- C_BUS ~ 1 µF at the flower, ~100× the local cap so the rail is a reservoir not a pulse shaper

Fast RC (local) = does this hop finish. Slow RC (bus) = readiness window. Magnetic H is still the core, not these caps.

---

## Bus is a reservoir

Shared. Whoever draws next, draws. No address. No “route pulse to neighbor 4.”

Two-of-three still lives at CENTER on the three D’s. The bus does not vote. A pulse on V_BUS may bias everyone’s tail. That is readiness, not a commit.

Hex does not magically split one flyback into a 2-of-3 decision. Three half-bridges on one rail is just one reservoir and three drinkers.

---

## Steering

Proposal sequence:

1. Schottky — simple flyback, drop is large on a 1 V rail. Loss is part of the story.
2. Synchronous MOSFET — after the diode path is the law, not before. Gate drive is a *separate* rail (1.8 / 3.3 V). Not the 1 V signal band.

---

## Two references still

C_BUS sits on V_BUS. It does not sit on CENTER. Filter or separate pour. A kick on the reservoir must not be a kick on V0.

---

## What “reinjection” means

One axis collapsing into C_BUS is **recovery**.

Reinjection is only real when a *second* axis then draws that charge instead of the pack. Same rail, later event, different axis.

Three axes is the triad. Still one law: agreement at CENTER, energy on V_BUS.

---

## Energy identity (proposal law, not a filled log)

```
E_in   = ∫ V I dt during drive
E_rec  = ½ C (V_after² − V_before²) on C_BUS
E_loss = E_in − E_rec − E_useful
```

Say the fraction. Never invent 100%. Pack refill is makeup for E_loss only.

---

## Not in this page

A function-generator shopping list. A claim that the network has been run. A simulated memory that stands in for H.
