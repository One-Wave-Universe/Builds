# The cell

**Top:** three differentials. Ternary. CENTER.
**Bottom:** reinjection bus. Mirror loop. Pack ask. Send-up.

Every leftover from all three top diffs is **gated down to V_BUS**. Not CENTER. Not only the winding flyback. Pair waste and heat-that-can-be-steered too.

---

## Seats

```
                    A+
                 ________
                /        \
           C-  /          \  B+
              |   CENTER   |
           B-  \          /  C+
                \________/
                    A-
```

A+ top ↔ A- bottom + core A between. Same B, C.

---

## Three gates, one bus

```
 TOP A dump --gate A--\
 TOP B dump --gate B---+-- V_BUS (bottom) -- C_BUS -- pack ask
 TOP C dump --gate C--/
```

Each axis has its own gate (steer diode first, sync later). All three land on the **same** V_BUS.

What gets gated:
- winding collapse (inductive)
- pair leftover / tail dump that would otherwise be heat
- anything that is still current, not already I²R in silicon

What does not get gated: CENTER. Heat that already became temperature (that’s the later thermal redline, not this path).

---

## Law

If it can still be charge, it goes to the bus.
If three diffs all dump, the reservoir takes three pulses. Next event drinks the rail first.
Pack only makes up what the gates could not save.
