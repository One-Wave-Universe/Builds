# Differentials

The cell is a difference. Not a single-ended pin. Not a drum.

## CENTER first

**CENTER is the virtual-ground center reference.** It is the midpoint against which the differential structure is interpreted.

**V_BUS is separate.** V_BUS is the live shared analog / reinjection state and must not be substituted for CENTER.

---

## One pair

A first bench implementation may use two matched MOSFET paths with a shared bias / tail arrangement:

```
        bias / tail
           |
        ---+---
       /       \
     M+         M-
      |          |
     D+         D-
```

One useful read is:

```
D = D+ − D−
```

Sign of D is direction. |D| is magnitude. Bias / tail sets sensitivity or hardness.

HOLD is D inside the wobble while the pair remains alive. It is not simply off.

The exact transistor topology is a bench implementation choice, not a locked claim that one specific small-signal differential-pair equation must describe every final CELL_V1 stage.

---

## One axis is a mirrored differential

A+ and A− are not two unrelated inputs. They are two opposed ends of one bidirectional channel around CENTER.

Conceptually:

```
A+ drive / sense path ↔ CENTER ↔ A− drive / sense path
B+ drive / sense path ↔ CENTER ↔ B− drive / sense path
C+ drive / sense path ↔ CENTER ↔ C− drive / sense path
```

The same physical channel may sense and act. Direction is determined by the differential lean and the threshold / hysteresis state, not by permanently labeling one side input and the other output.

Three differentials. Six seats. Three signed local leans.

---

## Relation to V_BUS

A/B/C are resolved around virtual-ground CENTER.

Their actions are coupled through the larger cell and lattice, and returned energy / consequences can feed V_BUS. The resulting V_BUS state is then available to both mirrored sides on the next interaction.

Therefore:

- CENTER supplies the center reference.
- A/B/C supply the three local ± differential leans.
- V_BUS supplies the live shared lattice condition.
- Do not collapse these into one node.

---

## Flower is differentials meeting

Center A+ meets neighbor A−. That joint is one differential surface: plus of one cell against minus of the other.

Stack inverted: A+ of the upper flower meets A− of the lower. Another differential surface. That is a hypothesized coupled lean boundary, not automatically a digital data bus.

---

## Drive is still a difference

A power stage does not create meaning from ground alone. It produces a voltage / current difference across the associated winding or coupled path relative to its opposed end and CENTER.

Ternary on an axis:

- UP: D positive enough to leave the wobble — net current one way
- HOLD: D remains inside the home / hysteresis band — no committed net direction
- DOWN: D negative enough — net current the other way

For the motor-field layer, three such axes can form the A/B/C rotating-field structure without a global clock; commutation is intended to be threshold / state driven.

---

## What still needs bench work

- exact MOSFET / switch topology for each bidirectional ± path,
- gate drive when polarity reverses,
- body-diode / back-to-back-FET handling,
- current-direction sensing,
- threshold and hysteresis bands,
- winding gauge / turns / spacing / geometry,
- coupling strength between A/B/C and the outer 3+3 windings,
- V_BUS isolation so one branch does not swamp another.

## What a differential is not

- Not D+ or D− alone as the answer. The answer is the difference.
- Not a single-ended ADC of one drain.
- Not PWM duty as a replacement for physical differential state.
- Not a fixed input/output pin assignment.

## Proposal sentence

CELL_V1 uses three mirrored bidirectional differential axes, A+/A−, B+/B−, and C+/C−, interpreted around virtual-ground CENTER. Their threshold / hysteresis state drives local action, while the coupled result and recovered energy can update the separate live V_BUS state.
