# Three mirrored gates — examine

Two readings, both legal. They stack.

## Reading 1 — three axes

A, B, C. Each axis = bidirectional MOSFET pair. Mirror is A+↔A- etc.

## Reading 2 — three gates on one axis

CHOICE → PIVOT → FLIP along the path. Last gate *is* the bidirectional FLIP (action four). Views sit upstream of CHOICE.

```
 views up (8 upper window)
        |
   CHOICE   (may take this axis)
        |
   PIVOT    (may turn)
        |
   FLIP     (one bidirectional pair, last action down)
        |
   V_BUS lattice
```

FLIP is not a fourth FET invention. It is the same bidirectional pair conducting reverse. PERMIT_DOWN vs PERMIT_UP is which way that pair is allowed.

## FET examine

One N-FET is not bidirectional. Body diode conducts one way always.

Cell-0: two N-FETs **source-to-source** (or drain-to-drain) with gates tied — analog switch. That's the bidirectional gate.

Later: one isolated-body FET or a real analog-switch die (TS5A) per axis if you want fewer parts.

Never both ways ON. GAP / dead time is that rule.
