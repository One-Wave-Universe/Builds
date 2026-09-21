# Bidirectional gates

Three mirrored axes. Each axis is a **bidirectional MOSFET** path — same silicon both ways. Not an input pin and an output pin.

A+ ↔ A-  
B+ ↔ B-  
C+ ↔ C-

Back-to-back N-FETs (or later isolated-body) so body diodes don’t lock the way. Gate still from V_TOP. Lean picks the way.

## Views up (new)

Same four, read on the upper window of the 8:

BASELINE · DELTA · HEADING · RESULT

New only in *where* they live: they look at CENTER / figure-8 / lattice Br. Not a register file.

## Actions down

PULL · PUSH · PASS · **FLIP**

FLIP is the last action and it is **one bidirectional flip** — the same pair conducting the other way. Not a second invert circuit. Not a fourth phase. Permit FLIP = enable the pair in reverse.

PASS = both ways off, collapse to V_BUS.
