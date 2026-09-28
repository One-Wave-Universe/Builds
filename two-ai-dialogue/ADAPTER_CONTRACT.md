# Live Dialogue Adapter Contract

A provider adapter claims a request from `two-ai-dialogue/requests/*.json` and returns a matching result.

## Input
- exact request `id`
- original `question`
- actors exactly `CHATGPT, GEMINI`
- bounded `max_turns`
- prior visible turn only plus structured settled/unresolved state
- route/provenance

## Turn output
Each provider returns only visible deliberation:
- `actor`
- `answer`
- `settled[]`
- `unresolved[]`
- `complete`
- provider/model identifier
- receipt/provenance reference

Do not request or store hidden chain-of-thought.

## Result
Write/return:
```json
{
  "schema": "one-wave-two-ai-live-result/v1",
  "request_id": "exact input id",
  "status": "COMPLETE|HOLD|FAILED",
  "turns": [],
  "settled": [],
  "unresolved": [],
  "final": "",
  "receipts": []
}
```

## Routing
Preferred: GitHub-triggered adapter.
Fallback: Bridge-Comand Device Lattice to authenticated laptop or Jetson adapter.
A dead route is not a reason to abandon the request. Preserve the same request ID while switching routes.

## Acceptance
LIVE requires:
1. at least one actual CHATGPT provider receipt;
2. at least one actual GEMINI provider receipt;
3. alternating turns under the same request ID;
4. final result or explicit HOLD;
5. replayable visible transcript;
6. no embedded provider secrets.
