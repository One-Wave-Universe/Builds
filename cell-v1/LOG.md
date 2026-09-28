# Hardware log

Copy a block per session. Empty log = hardware score 0%.

## Session ____ / date ____

VCC = ______ V

T1 floating gates: pass / fail
T2 drains high at rest: DB ______  DC ______
T3 B driven: DB ______  DC ______  D ______   pass / fail
T4 C driven: DB ______  DC ______  D ______   sign reversed: yes / no
T5 rails-off remanence matches last D sign: yes / no
  core part: ________________  loop type: square / unknown / EMI (illegal)
  sense method: ________________

T window if used: T = ______ mV

Notes:

## Ring (only after T5)

R2 A holds while B moves: yes / no
R3 C isolated: yes / no
Hex names written on board: yes / no
Field/void per pair: A ____  B ____  C ____

## Memory / meta (only after T5 / Test A)

processor in write path: no / FAIL

A two-lean separable: pass / fail    D+ ______  D- ______
F HOLD dwell writes: no / yes-FAIL   dwell_s ______  D_after ______
G fence walk: pass / fail            V_cross_rest ______  V_cross_busy ______
H palimpsest: one-beaker / frozen / depth
  A1 ______  B1 ______  A2_idle ______
I fade τ: ______ s / fail            method: opposite / wait / heat
D return: E_in ______  E_rec ______  CENTER_ok: yes / no
J tag same-body: pass / fail / skip
  window_how_measured: field / FAIL-clock

## Validation map

A retained-history: ____
B bounded reference: ____
C triad: ____
D V_BUS isolation: ____
E six-sector: ____
F HOLD stop-learn: ____
G fence: ____
H palimpsest: ____
I fade: ____
J tag: ____
