# DC / AC / RC

They did not get thrown out. They got unnamed while we locked D, HOLD, and the two references. Here they are on those parts.

Not three power supplies. Three *kinds of current in the same path*.

| Kind | What it is on the cell |
| --- | --- |
| **DC** | Committed flow. Axis left the wobble. HOLD is over. Net current one way. The lean *as a stand*. |
| **AC** | Drive across the dead zone. The excursion that tries to leave HOME. Event in motion. |
| **RC** | What remains after the event. The lean still in the path. Core remanence + the pair’s leftover offset. Not a third rail. |

---

## Where they sit vs the two references

- DC and AC live as current *across* an axis, measured as D against **CENTER**.
- Collapse / waste still goes to **V_BUS**. That is not RC. That is return.
- RC is CENTER-side memory (core + pair). If you call V_BUS “RC” you mashed dump and hold again.

---

## Nested names (same path, different grain)

- **BC-DC** — binary choice of DC direction (UP vs DOWN once committed).
- **TC-AC** — ternary move: DOWN / HOLD / UP while AC is trying the fence.
- **QC-RC** — 4×4 views/actions reading and writing the leftover RC (the grown leans).

---

## One event

1. HOLD (no net DC, tail on).
2. AC drive. D walks.
3. Two-of-three: DC commits or you fall back to HOLD.
4. Collapse to V_BUS.
5. RC left on that axis core.

Next event sees RC as the new home offset. That is use-deepens.
