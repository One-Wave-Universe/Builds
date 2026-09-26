# Differentials

The cell is a difference. Not a single-ended pin. Not a drum.

---

## One pair

Two matched MOSFETs, shared tail.

```
        Iss (hardness)
           |
        ---+---
       /       \
     M_B       M_C
      |         |
     DB        DC
```

Lean:

```
D = DB − DC
Idiff = Iss · tanh(Vd / (2 · n · Vt))
```

Vd is the gate difference. Sign of D is direction. |D| is magnitude. Iss is hardness.

HOLD is D inside the wobble and Iss still on. The pair is alive. It is not off.

---

## One axis is a mirrored differential

A+ and A− are not two inputs. They are two ends of one channel.

- Current out A+ is current in A− (and the reverse).
- The lean is which end is high relative to CENTER.
- The winding sits across that difference, or the next cell’s opposite seat eats it.

Same for B and C. Three differentials. Six seats. Three numbers.

A/B/C are geometric axes, not sequential voltage levels. The two sides of each axis form one opposed bias loop around the nucleus. Both sides may remain electrically active; the state is the signed imbalance between them.

Cell-0 is exactly this: one pair, read D, CENTER in the middle. That is the whole first drawing.

---

## Flower is differentials meeting

Center A+ meets neighbor A−. That joint is one differential surface: plus of one cell against minus of the other.

Stack inverted: A+ of the upper flower meets A− of the lower. Another differential surface. That is the hypothesized split — a difference between two lean fields, not a data bus.

---

## Live orbit / lean

The differential does not need an OFF neutral. Around CENTER the opposed sides can remain live and exchange / circulate current while the net difference stays near zero. A bias shifts that live orbit toward + or −.

What changes with voltage is **commit depth**, not axis identity:

- inside the home wobble: HOLD / live balance
- first calibrated crossing: CHOICE depth
- next crossing: PIVOT depth
- next crossing: FLIP depth

Exact enter/exit voltages remain bench calibration and must include hysteresis. When magnitude falls, the axis can descend the same depth ladder rather than being forced to continue upward.

A/B/C therefore run in parallel as three spatial differentials. CHOICE/PIVOT/FLIP is the threshold ladder within their coupled behavior. POINT/PATH/FIELD belongs to larger scale organization and is not an alias for A/B/C.

## Drive is still a difference

A half-bridge does not create a voltage from ground as the meaning. It creates a voltage *across the winding* relative to the other end and to CENTER.

Ternary on an axis:

- UP: D positive enough to leave the wobble — net current one way
- HOLD: D inside 0.45–0.55 — no net way, tail on
- DOWN: D negative enough — net current the other way

A three-phase motor is three of these differences timed around the hex. The body is optional. The cell is the differences.

---

## What a differential is not

- Not DB or DC alone as the answer. The answer is D.
- Not a single-ended ADC of one drain.
- Not PWM duty as a replacement for Vd.
- Not a speaker coil story.

---

## Proposal sentence

The primitive is a subthreshold differential pair whose output is D = DB − DC. Three mirrored pairs are three axes. Memory is the lean of that difference. The next cell sees the opposite seat of the same difference.
