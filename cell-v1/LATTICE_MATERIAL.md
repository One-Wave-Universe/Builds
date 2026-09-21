# Lattice material

Copper carries current. It does not keep Br.
The under lattice that *remembers* is a **magnetic layer on that current path**.

Old cousin: plated-wire memory — BeCu or Cu wire with ~1 µm Permalloy (Ni80Fe20). Current in the wire writes the film. Film holds remanence. We use that class, hex-shaped, shared, analog depth not a bit cell.

---

## Stack (proposal)

```
[ current ]  copper / BeCu  (V_BUS metal)
[ memory ]   Permalloy / NiFe film or square-ferrite sheet under/around it
[ read ]     figure-8 on CENTER sees that field as a shift of home
```

Cap on V_BUS = short hold (electrostatic).
Magnetic lattice = long hold (Br).
Figure-8 = how CENTER reads the home including that Br.

---

## What to make it out of

**First board (exists):** copper pour or wire for V_BUS + a **square-ferrite sheet or tape under the pour**, or Permalloy foil along the hex edges. No fab line.

**Next (plated):** electrodeposited **NiFe (Permalloy ~80/20 or 45/55)** on copper. Done on PCB in literature. Hc is low–medium — easy minor loops, shallow-to-mid traces. Zero-magnetostriction mix if the board flexes.

**Deeper traces:** thicker film, a little Co in the NiFe, or a second higher-Hc layer (NiCo on Permalloy — plated-wire already did dual layer). That is graded write depth in the stack, not in software.

**Avoid as the only metal:** bare copper, bare Al. Mu-metal sheet is high-μ shielding; Hc is low and it is miserable to etch. Fine as a foil experiment, bad as the only plan.

---

## Grant sentence (honest)

Plated magnetic interconnect is old. Using it as the *shared hex blood* that every flower writes and every figure-8 reads — analog depth, regen on the same path — is the arrangement.
