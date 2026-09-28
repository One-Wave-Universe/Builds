# CELL_V1 electrical/state references — 2026-09-27 lock

This file supersedes older fixed-CENTER wording where it conflicts.

## CENTER / (0): live full-body-state balance reference

CENTER is the **current combined full-body-state balance relation** presented locally to the three A/B/C differentials.

- DOWN / HOLD / UP resolve relative to this live balance.
- 50 / 0.50 is the normalized coordinate for balance, not a requirement for an independently generated fixed 0.50 V source.
- A/B/C remain three distinct differential axes; sharing the body-state reference must not electrically collapse them.
- CENTER is not V_BUS.
- Recoverable energy is not intentionally dumped onto CENTER.
- Exact physical coupling/distribution that presents the moving body-state reference to all three axes remains OPEN / BENCH.

## V_BUS: energy / readiness / reinjection reservoir

V_BUS is the shared energy rail/reservoir.

- cells may draw energy from it;
- recoverable inductive energy may return to it after passing through the intended steering/reinjection process;
- bus condition may affect readiness;
- V_BUS voltage alone is not long-term muscle memory;
- V_BUS is not the ternary balance reference.

## Hysteretic memory roles

CELL_V1 now explicitly has more than one physical hysteresis scale:

1. **gate-local hysteresis** — local/fast transition memory at mirror/loss gates; prevents chatter and preserves enter/leave history;
2. **local nucleus retention** — role-specific retained cell state/history;
3. **shared under-cell hysteretic layer** — distributed body/path/muscle memory across connected cells.

The active loss-threshold / reinjection structures sit above and couple into the shared body-memory layer. Reinjection revisits/writes/biases the retained path while V_BUS handles conservative energy supply/return.

## Nucleus relationship

The role-specific nucleus is a magnetic/state element, not another electrical rail.

Current role map remains governed by CELL.md. Geometry names do not replace physical components.

## Hard rule

```
live body-state CENTER != V_BUS != role-specific nucleus
gate-local hysteresis != shared body hysteresis
```

A/B/C compare around the live body-state CENTER relation. Reinjection must re-enter the same physical state loop. Any claimed memory, lower-loss settling, coupling, or recovery must be measured.
