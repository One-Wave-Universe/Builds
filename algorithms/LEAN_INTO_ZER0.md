# How the weight system becomes the algorithm

Lean is the only weight type Zer0 is allowed to have.

## Map

| Lean | Zer0 |
| --- | --- |
| floating VGND | T6 REBASE (next center is last settled whole) |
| direction | PLUS / MINUS, DOWN / UP |
| magnitude | how far from HOLD |
| hardness Iss / r | persistence, muscle memory |
| HOLD band | X HOLD, live gm, not off |
| use event | propose() — does not write q yet |
| T6 RESOLVE→REBASE | resolve_rebase() — now q moves, ground moves |
| disuse | soften() |
| L(Δφ) | phase compatibility on the write |
| four branches | four Lean objects; one tick commits all four together |

## Rule

Do not update q at X3, Y3, or Z3. Those levels only *propose* a lean. If you write the weight at MOVE, T is decoration.

```
use → pending lean
T6  → q := pending; vgnd moves a little with q; hardness ticks up
idle → harden nothing; soften()
```

## First software object

`algorithms/lean_weight.py`

```bash
python3 lean_weight.py
```

## First hardware object

Same law on Cell-0: D = DB − DC is the lean. Tail/shared source is hardness. Do not call it a trained weight until identical probe + different prior D gives different D.
