# Minor hysteresis and flux linkage

The winding does not see a spreadsheet. It sees **flux linkage** λ = NΦ.

Voltage on the axis is v = dλ/dt. Energy shoved in is related to ∫ i dλ. What stays after the event is leftover λ — remanent flux times turns — sitting in the figure-8.

---

## Major vs minor

**Major loop** — H big enough to run Br → opposite Br. Full flip. Fat ∮ H·dB. Fat Δλ. Fat collapse onto V_BUS.

**Minor loop** — H only jiggles around the Br you already have. Small Δλ. Small v·dt. Small leftover to gate. That is habit on the same heading.

HOLD / wobble lives on a tiny minor loop or just sits on Br (almost no Δλ).
±1 is a small minor loop.
±2 ±3 walk out. FLIP is the major loop on purpose.

---

## Linkage on the figure-8

Two windows, one Φ path around the 8. Turns on + and − seats share that Φ with opposite sense. That is why D and the iron are the same axis: current on A+ increases λ one way, A- the other.

When drive drops, λ tries to stay. The winding then produces the flyback v = dλ/dt as λ relaxes a little. That pulse is what the gate sends to V_BUS. The part of λ that does **not** relax is remanence — the old state still linked.

So:

- linked and kept → trace (hysteresis of the settled cell)
- linked and released → charge on the bus

Same λ. Two fates.

---

## Why energy gets better

A heading you keep using starts each event with λ already near the useful value. dλ/dt you must buy is small. Pack ask shrinks because Δλ shrinks. That is flux linkage talking, not a planner.
