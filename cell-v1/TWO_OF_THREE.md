# Two-of-three — current-sum block

Identity of the flower. Analog. No MCU.

Axis state is first quantized by the locked seven-band differential scale: 0, ±1, ±2, ±3. The two-of-three summer acts only on committed signed axis states; hysteresis gaps inhibit commitment.

One **unit** = Iss from one committed IN contribution. Threshold = 1.5 units.

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
- Windowing must implement the locked bands: 45–55 HOLD; 60–70 / 30–40 CHOICE; 75–85 / 15–25 PIVOT; 90–100 / 0–10 FLIP, with the six 5-point gaps treated as hysteresis / transition bands. Outputs: HOLD, GAP (in the unnamed bands), IN (in ±1/±2/±3).
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
