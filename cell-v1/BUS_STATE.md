# V_BUS state

The bus is a reference. It is the lattice-wide number that talks to the pack and to the operator field.

---

## Quiet

V_BUS in band. Loop feeds from return. Pack idle or trickle.

---

## Ask (refill)

Rail sags → ask the pack to refill the loop. Comparator. Pack is makeup for loss, not the default source.

---

## Up / redline (strain)

Ask is already on and the rail still falls, or event rate outruns return: **send up**.

That flag is what a body calls burn / exhaustion / redline. In this architecture it is not a feeling. It is the rail telling the operator field:

- prefer PASS
- no new PUSH / FLIP
- shed load

Same role as muscle burn: the tissue is already spending faster than refill. The “brain” here is the flower field that issues actions, not a soul.

| Bus | Meaning |
| --- | --- |
| high / rising | ready |
| in band | quiet |
| sagging | ask pack |
| low + falling while asking | redline → send up |

Levels, not ticks. Not CENTER. Sag may change tail current (sensitivity). A write still needs an axis event.
