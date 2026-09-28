# Two-AI Resolution Protocol

A dialogue is not complete merely because both models produced answers.

## Terminal states

- `AGREED_RESOLUTION`: both actors explicitly accept the same substantive resolution.
- `AGREED_NEXT_ACTION`: both actors explicitly accept the same concrete next action because evidence is insufficient for a final resolution.
- `HOLD`: a material blocker requires evidence, authorization, measurement, or human choice.
- `MAX_TURNS`: bounded turn budget exhausted without agreement.
- `FAILED`: provider/routing failure after bounded failover.

## Turn contract

Every visible turn must return:
- `actor`
- `answer`
- `agreements[]`
- `objections[]`
- `unresolved[]`
- `proposed_resolution` or null
- `proposed_next_action` or null
- `accept_previous` boolean
- provider/model/receipt provenance

No hidden chain-of-thought is requested or stored.

## Agreement gate

A terminal agreement requires two consecutive opposing actors to explicitly accept materially the same normalized proposal.

Agreement cannot be inferred merely from polite language, lack of objection, or `complete=true`.

If factual/experimental evidence is missing, prefer `AGREED_NEXT_ACTION` over invented certainty.

## Engineering rule

For CELL/science work, the loop must distinguish:
1. established component behavior,
2. engineering hypothesis,
3. simulated result,
4. bench-measured result,
5. unresolved claim.

The AIs may agree on a falsifiable experiment without agreeing that the underlying physical claim is true.

## Human contract

The human asks once. The control plane carries subsequent turns, preserves the same request ID, retrieves matching receipts, and returns the agreement or blocker to the originating conversation.
