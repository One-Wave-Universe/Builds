# Bus-side lattice

The under hex is not bare copper. It is the **hysteresis lattice**.

Every edge that returns charge to V_BUS runs through that axis core first.

```
        A+ seat (top)
            |
         wind A
            |
      [ HYSTERESIS A ]     remanence / write depth / trace
            |
         gate A
            |
         V_BUS  <--- same node for B and C
```

Three edges, three cores, one rail.
Neighbor hex shares V_BUS and a shared edge. That shared edge also hits a core before the rail — no memory-free return.

Hysteresis is not a software flag drawn on the top face. It is the iron on the bus-side lattice.
