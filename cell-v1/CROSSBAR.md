# Memristor crossbars

## What they are

Rows × columns. A two-terminal resistor at every crossing. Conductance G is the weight. Input voltages on rows, currents sum on columns. Ohm × Kirchhoff = analog multiply-add.

Write = a pulse that moves G. Read = a smaller voltage. Copy = read all G into a file.

## What bites them

**Sneak paths.** Current skips the cell you meant and walks three other devices. Read lies. Write disturbs neighbors. Gets worse as the array grows. Selectors (1T1R, diodes, timing switches) fight that — and fight the linear G you wanted for the multiply.

Drift, forming, limited analog levels, device-to-device mess.

## Steal

Current on a shared line adds. That is already two-agrees on our sum node and leftover current on our bus.

## Refuse

G as a programmable number. A row-column grid. Selectors that exist to isolate cells we *want* to share.

## Us instead of a crossbar

We do not have (i,j) synapses. We have **edges**. The letter *is* the side. Two hexes own that side. Lattice hysteresis on that side is *supposed* to be common. That is group memory, not a sneak error.

Figure-eight shape on the middle is the one-hex diary. Not a cross-point G.

If a current walks the flower, that is the bus doing its job — blood — unless it floods the 0.50 middle. The keep-out on the middle island is our selector. Not a transistor per synapse.
