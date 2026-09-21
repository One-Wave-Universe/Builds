# PERMIT to metal

Live flag. Hysteresis. GAP kills it at the trip, not after a glitch on the gates.

## Trip

SUM vs CENTER, units of Iss through R_SUM.

- Rise: |SUM| > 1.5 → PERMIT_UP or PERMIT_DOWN
- Fall: |SUM| < 1.2 → release
- Mutually exclusive. Both low = no permit.

GAP_A OR GAP_B OR GAP_C clamps both comparators off **at the trip**. No PERMIT pulse to route.

Not latched for the whole write. Live + 0.3 unit hysteresis so a dip does not chatter the FETs.

## Heading

PERMIT_UP enables PUSH/FLIP only on axes that are IN and S=+.  
PERMIT_DOWN same for S=−.

The lone opposite axis (if any) does not get PUSH/FLIP. It may PULL or PASS.

## What each action does to a half-bridge

| Action | High-side | Low-side | When |
| --- | --- | --- | --- |
| PASS | off | off | always allowed (coast, collapse → bus) |
| PULL | off | on (toward CENTER / reduce \|D\|) | always allowed |
| PUSH | on | off | needs PERMIT on that heading |
| FLIP | swap which device was on | needs PERMIT on that heading |

Never high and low together. Dead time = the wobble / GAP idea on the same axis.

## Parts (proposal)

- Window + sign: LM339 quad comparators on V_TOP, or three window chips.
- ±Iss: analog switch (TS5A / 4066-class) from V_TOP and from a current sink to SUM. Later: matched pair current sources.
- SUM: R to V0_TOP mid.
- Trip: two comparators with resistors for 1.5 / 1.2.
- GAP OR: diodes or one extra comparator input tied.
- Route: AND PERMIT_UP with IN&S+ per axis → that axis high-side enable. Same DOWN / low-side.
- Half-bridge: same 2N7000-class as Cell-0 for the 9 V face; logic-level pair when V_BUS is 1 V class. Gate drive from V_TOP, not from SUM.

Buffer PERMIT before the FETs. Do not let gate charge pull on SUM.
