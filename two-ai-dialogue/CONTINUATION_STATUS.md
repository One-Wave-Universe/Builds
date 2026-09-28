# Two-AI Dialogue — Continuation Status

Updated: 2026-09-28

## Current state

The human-facing command is intended to be natural language: **"run this by Gemini"**, **"run this by another AI"**, or **"have them discuss it until they agree on a resolution or next action."**

### Proven
- GitHub Actions request routing works.
- `GEMINI_API_KEY` is installed and masked in Actions.
- Real Gemini inference works through `gemini_adapter.py`.
- Request receipts echo the exact request ID.
- Stale smoke-request fallback was removed.
- Triggering request path is now shared across provider steps.
- `OPENAI_API_KEY` is installed and masked in Actions.
- OpenAI adapter reaches the OpenAI API.
- Resolution protocol exists: AGREED_RESOLUTION / AGREED_NEXT_ACTION / HOLD / MAX_TURNS / FAILED.

### Current HOLD
OpenAI calls for request `cell-v1-needs-001` returned HTTP 429 for all bounded attempts. Do not treat this as a Gemini failure or routing failure. Do not claim live OpenAI dialogue until a matching OpenAI COMPLETE receipt exists.

Evidence run: GitHub Actions run 36496957876.

## Resume when OpenAI quota/capacity is available

1. Re-run the same request or a new bounded request.
2. Require matching Gemini and OpenAI receipts under the same request ID.
3. If OpenAI COMPLETE is obtained, wire/use the live alternating runner rather than two independent one-shot calls.
4. Each later turn receives original question + previous visible turn + settled/unresolved + proposed resolution/action.
5. Continue until RESOLUTION_PROTOCOL.md terminal criteria are satisfied.
6. Save one combined dialogue receipt/artifact containing all visible turns and provider receipts.
7. Connect the browser `/v1/dialogue` endpoint to the live runner.
8. Only then call the floating dialogue box end-to-end live.

## Known remaining engineering work

The current workflow proves provider invocation but is not yet the finished automatic alternating conversation. The next implementation must:
- pass provider A's visible output into provider B;
- parse structured agreements/objections/unresolved/proposal fields;
- alternate under one request ID;
- enforce max turns/timeouts;
- use exact proposal agreement, not polite consensus;
- preserve provider/model/response IDs per turn;
- emit AGREED_RESOLUTION or AGREED_NEXT_ACTION only after explicit opposing acceptance;
- emit HOLD on quota/evidence/authorization blockers;
- support provider failover without silently changing provenance.

Do not erase this HOLD or mark the feature complete merely because a later workflow is green.
