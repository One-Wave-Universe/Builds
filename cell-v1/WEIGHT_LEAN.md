# WEIGHT = LEAN

A weight is a physical lean off a moving reference. Same path as the signal.

## 1 V threshold map (locked)

Full scale 1.00 V. Home 0.50 V. Seven bands, 100 mV each. Gaps stay empty.

| Band | Voltage | Meaning |
| --- | --- | --- |
| Terminal UP | 1.00–0.90 | crisis / collapse |
| *gap* | 0.90–0.85 | dead |
| Strong UP | 0.85–0.75 | committed plus |
| *gap* | 0.75–0.70 | dead |
| Moderate UP | 0.70–0.60 | leaning plus |
| *gap* | 0.60–0.55 | dead |
| **HOLD** | **0.55–0.45** | home |
| *gap* | 0.45–0.40 | dead |
| Moderate DOWN | 0.40–0.30 | leaning minus |
| *gap* | 0.30–0.25 | dead |
| Strong DOWN | 0.25–0.15 | committed minus |
| *gap* | 0.15–0.10 | dead |
| Terminal DOWN | 0.10–0.00 | crisis / collapse |

Do not fill the gaps. A value in a gap is in transit, not a named state.

This is the analog-brain layer. Cell-0 stays 9 V jellybean parts. Millivolt pair later.

## Lean

Direction / magnitude / hardness. HOLD is live tail current, not off.

```
Idiff = Iss · tanh(Vd / (2 · n · Vt))
```

Iss = hardness. Vd = direction + magnitude.

Use deepens. Disuse fades. Identical probe, different prior lean, different answer — or it is not a lean.
