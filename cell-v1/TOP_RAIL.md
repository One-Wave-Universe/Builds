# Top rail

Both faces have power. That is locked.

Top rail **V_TOP** feeds the three pairs.
Bottom rail **V_BUS** is circulation.
CENTER is the lean home.

Three names. Three nodes.

---

## How V_TOP is born

Proposal: **linear tap off the pack**, not off V_BUS.

```
PACK+ --+-- LDO / divider -- V_TOP -- three pair VCC (R1/R2 class)
        |
        +-- ask switch ------ V_BUS -- reservoir, tails, half-bridges
        |
       PACK-
```

V_TOP is quiet-ish analog supply for the diffs.
V_BUS is dirty on purpose: pulses, sag, ask, send-up.
CENTER sits in the middle of the *pairs*, mid of V_TOP class (divider from V_TOP, then allowed to move a little).

Do not generate V_TOP by shorting to V_BUS. Do not use V_TOP as CENTER.

Cell-0: V_TOP *is* the 9 V pack (one rail, one pair, see D).
Full cell: pack splits — stiff-ish V_TOP for the faces of the pairs, living V_BUS under.

1 V map lives *across* the pair (D bands). V_TOP can be 9 V or 5 V or 3.3 V as the headroom the FETs need. Bands are not the pack voltage.
