# Two-of-three

Not a CPU vote. Analog coherence on D_A D_B D_C.

Each axis already has a trit: DOWN / HOLD / UP (outside wobble or in it).

---

## Per axis, two bits of meaning

- IN: |D| left the wobble
- SIGN: D positive or negative

HOLD = not IN.

## Flower commit

Commit UP when at least two IN and those signs match and the third is not IN with the opposite sign.
Commit DOWN same with minus.
Else HOLD.

If the third is walking (IN rising toward opposite): wait. That is a window on dD/dt or simply “third still in the gap bands.”

## Circuit family (proposal)

Three window comparators on |D| vs wobble edge → IN_A IN_B IN_C.
Three sign comparators on D → S_A S_B S_C.

Coherence:

- majority of IN in the same S, and no IN with ~S → fire that way
- analog way: current-sum the signed INs (each IN sources +Iss or −Iss). If the sum current exceeds a threshold (~1.5 units) and no opposing IN is present (inhibit from XOR of signs among IN axes), commit.

That current-sum *is* the two-of-three. Threshold ~ one-and-a-half axes. Third opposed shunts the sum back under threshold.

Output of that block only *permits* PUSH/FLIP on the heading pair. It does not replace the pairs. PASS if no permit.
