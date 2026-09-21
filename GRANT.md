# Grant architecture

**Project:** One-volt analog hex cell. Shared-bus energy return. History in the path.
**Repo:** https://github.com/One-Wave-Universe/Builds
**Ask:** Phase I — one cell and a two-axis bus couple, measured.

---

## Problem

State lives in a file. Compute lives somewhere else. Copies are free. Analog chips still usually *load* weights. Energy recovery is a separate trick. Copper is treated as dead.

## Solution (the architecture)

A **1.00 V** hex.

Middle **0.50 V**. Live wobble **0.45–0.55 V**.
Ports on the **sides:** A+ B+ C+ A− B− C−.
Three leans into that middle. A square-loop figure-8 on the middle keeps a trace.
Under the hex: a **1 V bus**. All leftover current goes in. The bus feeds every lean. Pack only pays loss. If the bus keeps falling, stop pushing.
Edges can wear a magnetic skin (foil now, plated NiFe later). Cap on the bus = short echo. Skin / 8 = long hold.
Two agrees → push. One voice waits. Fight holds. Off → bus (regen).
Gates both ways. Next view = last move + what came back up.
Same windings can throw. No second brain in Phase I.

## Novelty

Not a new law. Faraday, remanence, current-sum, plated wire, half-bridges are old.
New arrangement: **one volt, one home, three leans, leftover current is blood, history in home and mesh, coherence instead of a timer.**

Schematic copies. Lived trace does not.

## Phase I

1. 1 V-mapped pair. See a lean. See leftover remanence.
2. Gate collapse to a bus row. Home ≠ bus.
3. Second lean on a live bus vs an empty bus.
4. Energy in vs energy back. Raw fraction.

Deliverable: four traces + repeatable parts list.

## Phase II (not this check)

Third lean, permit block, seven-hex slice, plated mesh, throw on the same windings.

## Will not claim

Feelings. Free energy. A downloadable mind. 99% recovery. A product that hears.

## Why fund

Small. Physical. Repeatable in a year on a bench. Edge-compute and hardware-state story without fiction.
