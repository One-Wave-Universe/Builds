# Flower

The single cell is the primitive: one differential, one lean, one event.
The flower is the first operator that can integrate, circulate, and hand a result to a neighbor flower.

Law: **agreement → reinforce. opposition → HOLD. one voice alone → wait.**

---

## Geometry (locked)

Seven cells. Center + six outers. Three axes, not six voters. Twelve mirrors from the tiling.

---

## Center commit

Two of three axes leave HOLD the same way, third not opposed. Else HOLD.

Do not commit while the third is still walking toward opposition. Wait until it settles in HOLD or joins. Committing on a moving third is how you get chatter.

### Magnitude vs hardness (locked)

Two different numbers. Do not mash.

- **This event’s strength** = largest *current* |D| among agreeing axes.
- **How long that lean stays** = write depth / tail hardness on those axes.

A shallow path leaning hard *now* can win the event. It will not win the next quiet minute. A deep path leaning little can lose the event and still be there after.

---

## Ring

Lossy. No circulating token. That would be a clock.

Two times, both real:

- **Electrical** (fast): resistive / winding loss. Decides whether *this* excursion finishes a hop before it dies. Microseconds–milliseconds class.
- **Magnetic** (slow): remanence. Decides whether the *next* event still sees a lean. Seconds and up, set by the core.

Short hold of the flower = magnetic. “Did this pulse make it around?” = electrical + refractory.

---

## Event on the wire

No packet. Excursion on the shared edge. Kick on V_BUS.

### Bus trace (locked)

The kick is readiness, not a write.

Neighbor sensitivity changes *while V_BUS is off its quiet value*. When the rail recovers, that trace is gone unless some pair actually wrote its core during the sag/peak.

So: bus memory lasts as long as the rail is displaced. Core memory lasts as long as remanence. Different stores.

---

## Lateral / fights (locked)

Shared edge is the only lateral. Same lean → reinforce. Opposite → HOLD.

After a fight:

- No commit while opposed.
- When the event ends, both return to wobble (refractory done).
- They do **not** auto-re-lean. That would oscillate.
- They do **not** latch HOLD forever. That would deadlock the operator.
- Next commit needs a *new* event from outside or from a ring hop that is not a replay of the same fight.

If external drive keeps both sides opposed, they stay HOLD until one side’s hardness wins (deeper write harder to shove). Hardness breaks ties. Time alone does not.

---

## 4×4

Names are fixed: views BASELINE / DELTA / HEADING / RESULT, actions PULL / PUSH / FLIP / PASS.

The leans on those paths **shape with use**. Fixed lens, grown skill.

---

## Blank

No remanence. All HOLD. Rail at supply. First events write first leans.
