# V_BUS state

## Two different references — do not merge them

**CENTER** is the virtual-ground center reference.

**V_BUS** is the live shared lattice state / energy / reinjection rail.

V_BUS is **not** zero, neutral, CENTER, or a preset midpoint. At the instant it is read, its value is whatever physical value the coupled lattice has actually reached.

Both mirrored sides may:

- read the present V_BUS condition,
- act relative to CENTER and their local differential state,
- return consequences / recovered inductive energy to V_BUS,
- thereby help create the next bus condition.

So the loop is:

```
present V_BUS
   ↓
both mirrored sides read it
   ↓
A/B/C threshold + hysteresis decision around CENTER
   ↓
local magnetic / motor action
   ↓
gated return / reinjection
   ↓
new physical V_BUS
```

The bus therefore carries an evolving analog state and can carry history indirectly through the coupled hysteretic system. It is reference-by-measurement for the next interaction, not a fixed electrical zero.

---

## Quiet

V_BUS inside its currently acceptable operating band. Loop can feed from return. Pack idle or trickle.

---

## Ask (refill)

Rail sags relative to the required operating band → ask the pack to refill the loop. Comparator / threshold behavior. Pack is makeup for loss, not assumed to be the default source.

---

## Up / redline (strain)

Ask is already on and the rail still falls, or event rate outruns return: **send up**.

That flag is a physical load / readiness condition. It may bias the operator field toward:

- prefer PASS
- no new PUSH / FLIP
- shed load

This is an engineering state label, not a claim of subjective feeling.

| Bus tendency | Engineering interpretation |
| --- | --- |
| adequately charged / rising | more drive margin |
| inside operating band | quiet / ready |
| sagging | ask pack |
| low + falling while asking | redline → send up |

Levels, not ticks. No clock. Sag may change tail current / sensitivity. A write still needs an axis event.

## Bench status

Exact acceptable bands, bus impedance, refill threshold, cross-cell coupling, and whether V_BUS is a useful coordination variable remain measured quantities. Do not freeze numeric claims before bench data.
