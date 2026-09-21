# V_BUS state

The bus is a reference. It is also the only lattice-wide number that may talk to the pack.

---

## Quiet

V_BUS in its working band. Reinjection loop is feeding cells from C_BUS / rail. Battery is idle or trickle. No strain flag.

---

## Ask (refill)

When V_BUS sags below the working band, the rail **asks the battery** to push charge into the loop.

Ask is a comparator on the bus, not a processor.

- Below band → close the refill path (supply FET / ideal diode / charger into the rail).
- Back in band → open it. Loop lives on recovered energy again.

The battery is not the default source. It is the makeup for E_loss. Reinjection is first. Pack is second.

---

## Up (strain)

When ask is already on and the rail still falls, or event rate vs tail says the loop cannot keep up, the bus **sends up**.

Up = strain flag to the next scale (flower → field, field → pack manager). Meaning: stop issuing new PUSH / FLIP, prefer PASS, or shed load. Not a mood. Not speech.

Proposal thresholds (named, not measured):

| Bus | Meaning |
| --- | --- |
| high / rising | ready |
| in band | quiet |
| sagging | ask battery |
| low and still falling while asking | strain → send up |

---

## What the bus must not do

- Must not be CENTER.
- Must not write cores by itself. A sag may change Iss (hardness / sensitivity). That is readiness. A write still needs an axis event.
- Must not clock the lattice. Ask and up are levels, not ticks.
