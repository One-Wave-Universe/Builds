# DC bus-bar — where loss and waste go

CENTER / floating ground is the lean. It is not the dump.

Loss, flyback, unused split, heat-bound current that can still be steered — those feed a **DC bus-bar lattice**, then a reservoir, then a later permitted event.

```
9V pack +
    |
    +---- R1 ---- DB ---- Q1 ----+
    |                             \
    |                              CENTER ---- square-loop core ---- lean header
    |                             /
    +---- R2 ---- DC ---- Q2 ----+
    |
    +---- C_BUS (reservoir) ---- BUS BAR ---- waste/return nodes
    |
    pack -
```

## Law

- `D = DB − DC` is the lean. Measure it. That is weight / memory.
- `BUS` is a separate metal. Waste lands here.
- `C_BUS` holds what can be used again.
- Do not tie waste to CENTER. That would shove the lean and call it recovery.
- Do not call the pack minus the reservoir. The pack is supply. The bus is return-of-event.

## What feeds the bus

- unmatched current from the pair after the event
- inductive kick from the core when drive drops
- path that was opened and not taken
- anything the cell spent that is still charge, not heat-only

Heat-only is gone. Do not invent gain. If it does not show up as a voltage rise on `C_BUS`, it did not reinject.

## First bench add-on to Cell-0

Keep the T1–T5 pair as written in `CELL0.md`.
Then add:

- one capacitor `C_BUS` across a dedicated bus rail (not CENTER)
- one header on that rail
- one path from each drain node through a steering diode or MOSFET body toward `C_BUS` so leftover drain energy can sit on the bus

Measure:

```
V_pack
V_BUS before event
V_BUS after event
D = DB - DC
CENTER vs pack minus (must not be the same node)
```

Pass: `V_BUS` rises when an event ends and that charge is still there for a later event.
Fail: CENTER moves and you called it reinjection.

## Lattice later

One cell = one bus spur.
Flower = bus bars tied edge-to-edge, each cell still has its own CENTER.
Shared bus is allowed. Shared CENTER is not.
