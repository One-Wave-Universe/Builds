# Two-of-three — current-sum block

Identity of the flower. Analog. No MCU.

One **unit** = Iss from one IN. Threshold = 1.5 units.

| INs | Sum | Result |
| --- | --- | --- |
| 0 | 0 | HOLD |
| 1 | ±1 | HOLD |
| 2 same | ±2 | permit |
| 2 opposite | 0 | HOLD |
| 3 same | ±3 | permit |
| 3 mixed 2v1 | ±1 | HOLD |

Walking third is **not** inside the sum. Separate inhibit. If any axis is in a gap band (leaving wobble, not yet a commit band), INHIBIT. Sum may already be ±2; we still wait.

---

## Parts family (Cell-0 headroom, 1 V D)

Per axis:

- Diff already exists (the pair). D is a voltage.
- Window: two comparators (or one window chip e.g. window detector) vs 0.45 / 0.55 and vs commit edges. Outputs: HOLD, GAP (in the unnamed bands), IN (in ±1/±2/±3).
- Sign: one comparator on D vs CENTER → S.

Shared:

- Three gated current sources. When IN and S=+: source +Iss into SUM. When IN and S=−: sink Iss from SUM. HOLD or GAP: source off.
- Iss from a shared bias (can track tail / V_BUS later so redline softens the vote — optional).
- SUM node: resistor to CENTER (or a virtual ground at V_TOP mid). Voltage = k × (N_plus − N_minus).
- Two comparators on SUM vs +1.5 and −1.5 units → PERMIT+ / PERMIT−.
- INHIBIT = GAP_A OR GAP_B OR GAP_C. Gates both PERMITs off.

Permit only enables PUSH/FLIP on the heading pair. No permit → PASS.

Comparators: jellybean op-amp or LM339-class on V_TOP. Current sources: matched PFET/NFET or Howland if you want tidy. First build can be resistors + analog switches from V_TOP / PACK− into SUM (ugly Iss, legal for the proposal).

---

## Why inhibit is outside the sum

The sum only sees committed INs. GAP is a fourth state per axis: not HOLD, not IN. Putting dD/dt in the summer is a differentiator on a noisy D. OR of three GAP flags is a level. Cleaner. Same law: wait on a walking third.
