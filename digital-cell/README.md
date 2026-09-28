# L0 Digital Cell

Deterministic executable reference for W-010.

FIELD and VOID are explicit signed candidate values. Resolution uses their relation:

`difference = FIELD - VOID`

With threshold `t > 0`:
- difference > t → POSITIVE
- difference < -t → NEGATIVE
- otherwise → HOLD

This is a software reference contract, not proof of analog CELL physics.

Run:
`python3 digital-cell/l0_cell.py digital-cell/fixtures/positive.json`

Tests:
`python3 -m unittest digital-cell/test_l0_cell.py -v`

Output is JSON state followed by a JSONL-compatible receipt. The adapter block names DCACRC-IR-compatible REFERENCE, DIFF and LEAN semantics without claiming a completed IR compiler.
