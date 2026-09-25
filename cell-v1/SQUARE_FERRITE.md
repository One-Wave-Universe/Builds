# Square figure-8 nucleus

**The square figure-8 toroidal structure is the CELL_V1 nucleus.**

It is the central retained-state / magnetic core structure of the cell. It is not the outer motor-field shell and it is not interchangeable with CENTER or V_BUS.

## Relationship to the rest of the cell

- **Nucleus:** one square figure-8 toroidal structure at the center.
- **Gate structure:** three mirrored differential gate pairs resolve the local ternary lean around − / (0) / +.
- **Outer shell:** two round figure-8 toroidal structures surround the nucleus and form the larger coupled electrical / magnetic field structure.
- **Motor windings:** the two outer round figure-8 structures carry six windings total, organized as two mirrored groups of three.
- **Bus / reinjection:** recovered inductive energy returns through the cell's reinjection path to V_BUS. CENTER remains the local lean reference and is not the recovery bus.

The nucleus participates in retained-state bias and the next threshold decision. The outer two figure-8 structures turn the resolved ternary lean into the larger 3+3 differential motor-field response.

```
            outer round figure-8
            3 windings / side
                  ╲
        mirrored gates + ternary lean
                  │
        square figure-8 nucleus
                  │
        retained state / hysteresis
                  │
        reinjection → V_BUS
                  ╱
            outer round figure-8
            3 windings / side
```

This file defines the **proposed CELL_V1 architecture**. Magnetic coupling, winding geometry, field strength, efficiency, and retention depth remain bench quantities until measured.

## Do not drift

- Do not call the square figure-8 the bus.
- Do not put the square figure-8 on CENTER and collapse CENTER into V_BUS.
- Do not describe the six outer windings as six independent motors.
- Do not split the nucleus, gates, motor windings, memory, and reinjection into unrelated controllers.
- Do not claim measured performance until the bench log contains it.
