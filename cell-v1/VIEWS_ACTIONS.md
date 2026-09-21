# Views and actions on three differentials

The 4×4 is not a fourth axis. It is how you *read and drive* A, B, C.

---

## Three numbers you actually have

At any quiet instant the flower only owns:

- D_A, D_B, D_C (current leans)
- H_A, H_B, H_C (hardness / write depth / tail)
- V_BUS (readiness)
- whether each axis is in HOLD wobble or committed

Everything below is those, named.

---

## Four views (sense)

| View | What you read |
| --- | --- |
| BASELINE | Which axes are in HOLD. Home. |
| DELTA | Sign and size of D on axes that left HOLD. Change. |
| HEADING | Which way the two-of-three points (the agreeing pair). Direction. |
| RESULT | After the event settles: new D and H vs what they were. What stuck. |

BASELINE is not “zero volts.” It is “in the wobble.”
DELTA is not a derivative chip. It is D while the event is live.
HEADING is the coherence bit: the way two axes agree.
RESULT is remanence after refractory — memory of that event, not a log file.

You cannot have a fifth view without a fourth axis or a bus-as-memory cheat. V_BUS is readiness, not RESULT.

---

## Four actions (drive)

| Action | What the half-bridges do |
| --- | --- |
| PULL | Drive agreeing axes *toward* CENTER (reduce \|D\|). |
| PUSH | Drive agreeing axes *farther* from CENTER (increase \|D\|). |
| FLIP | Swap sign on the heading pair (A+/A− role reverse). |
| PASS | No drive. Coast HOLD. Collapse to bus. Let neighbors / ring act. |

PASS is the default. PUSH/PULL/FLIP only after two-of-three has committed a heading.

One voice alone never PUSH/FLIP. That would be winner-take-all.

---

## Sixteen couplings

Each view×action is a *permission*, not a wire:

- You may PUSH on a DELTA (deepen the live lean).
- You may PULL on a RESULT that is too far (home a stuck axis).
- You may FLIP on a HEADING (turn).
- You may PASS on BASELINE (stay).

The path that carries that permission is still A, B, or C plus a center–outer mirror. Use hardens that path. Disuse fades it. That is how the 4×4 becomes a skill instead of a lookup table.

Forbidden: PASS that is actually a hidden clock. If nothing is crossing, nothing steps.

---

## Hardness breaks a fight

Two flowers (or two axes) opposed:

1. Both HOLD. No commit.
2. Drive continues from outside.
3. The axis whose H is larger moves less for the same Vd (tail / remanence).
4. The softer axis gets shoved into the harder one’s wobble or into agreement.
5. When opposition ends, two-of-three may commit.

If H is equal and external drive stays symmetric, they stay HOLD. That is a stalemate, not a crash. PASS. Wait for a third event (ring hop, bus sag changing Iss, neighbor).

No oscillator. No referee chip.

---

## Axis gates (still three seats on one winding)

Along one axis the proposed chain remains CHOICE → PIVOT → FLIP → PIVOT → CHOICE.

- CHOICE: enter or refuse the lean (wobble gate).
- PIVOT: hand the difference to the other end / the neighbor.
- FLIP: sign change (same as action FLIP).

Transistor map open. Meaning locked to the differential, not to six extra FETs per adjective.
