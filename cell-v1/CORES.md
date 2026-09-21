# Three cores

One magnetic core per axis. Not one shared core. Not six cores.

A single shared core makes H global. Then two-of-three and fights are fake: opposition washes in one lump.

---

## Where they sit

**One core on each axis path. Physically parked at A+, B+, C+ outers.**

A− / B− / C− are the other *end of that same core*, not a second memory and not dead copper. Current still runs A+↔A−. Remanence lives once per axis.

Center has **no** core of its own. Center is the electrical read / two-of-three. If you put three cores in the center puck they magnetically become one core again.

120° apart at the + outers is the isolation. Orient the three easy-axes as close to mutually orthogonal as a flat flower allows (in-plane 120° is the honest 2D answer; a later stack can tilt).

---

## How center sees three states

Electrical, not a shared flux lump.

Each axis: drive winding on its core + a sense of D (the pair already is the sense: DB−DC, or a dedicated pickup on that core only).

Center node reads three D voltages (or three pair outputs). No Hall required in the proposal. Hall is an instrument add-on.

---

## Drive

Three half-bridges. One per axis. Shared V_BUS. Not a multiplexed single driver — that would serialize the flower into a clock.

Minimum windings per axis: one drive (the port winding). Sense can be the same winding (bridge voltage / current) or a second pickup if the drive is too dirty. Proposal starts at **one winding per core**. Second winding only if drive and sense fight.

Flower count: 3 cores, 3 windings (start), 3 half-bridges, 1 V_BUS, 1 local CENTER per cell, no center core.

Ring uses the same six seats. It does not get a fourth core.

---

## Cross-talk

Will happen. Treat it as a leak, not as coupling-by-design.

Mitigations in the proposal: distance at + outers, 120°, no ferrous bar through the center, CENTER copper not a magnetic short.

If two cores write each other as hard as they write themselves, the layout failed. Then shield or stand the cores off-plane. Do not “use the bleed as the 4×4.”

---

## Blank

Three cores, remanence near zero. Blank is “no intended write yet,” not laboratory zero.

Assembly current will leave some junk. First events overwrite it. Do not invent a factory reset file. A degauss / AC fade is allowed as a bench ritual, not as runtime memory erase.

---

## Why this matches the law

- Flash vs habit can differ on A vs B.
- Two-of-three can oppose for real.
- Fight is two cores, not one cancelled loop.
- 4×4 permissions stay per-axis leans.
