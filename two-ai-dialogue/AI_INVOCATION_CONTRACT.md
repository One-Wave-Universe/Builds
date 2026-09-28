# AI-to-AI Dialogue Invocation Contract

Status: canonical operating instruction for the Builds two-AI dialogue interface.

## Human interface

A human may speak naturally to any authorized AI, for example:

- "Run this by Gemini."
- "Ask Gemini to challenge this design."
- "Have a dialogue with Gemini and get back to me."
- "Run this through the two-AI box."

The human MUST NOT be required to manually create GitHub request files, watch Actions, copy model output, or relay turns when an authorized automation route is available.

## Provider-neutral rule

This contract applies to ChatGPT, Claude, Gemini, DeepSeek, Codex, Pi, local models, and future AI workers. An AI may use this contract only when it has an authorized tool/bridge capable of reaching the control plane. Lack of direct provider access is a routing problem, not permission to fabricate a response.

## Canonical route

Preferred currently proven Gemini path:

ORIGIN AI -> Builds request -> GitHub Actions -> authenticated Gemini API -> receipt/artifact -> ORIGIN AI

Bridge-Comand Device Lattice is the routing/control authority when another authorized machine or provider route is required.

## Invocation procedure

1. Capture the user's exact question/design and requested purpose.
2. Generate or reuse one stable request_id for the entire dialogue.
3. Preserve source, target actor, original question, project/canon references, provenance, limits, and max turns.
4. Submit through the healthiest authorized route. For Gemini, prefer the Builds GitHub Actions dialogue lane while it is healthy.
5. Retrieve the matching receipt. Never substitute an older receipt or another request ID.
6. Verify that the receipt contains a real provider/model result, not merely workflow validation.
7. Compare the returned answer against the original question and unresolved items.
8. If useful work remains and the turn budget permits, send a visible counter-response/challenge back under the SAME request_id.
9. Continue bounded alternation until COMPLETE, HOLD, user stop, max_turns, or provider/route failure.
10. Return the synthesized result to the human in the conversation they started from. Include important disagreements/unresolved items. Do not require the human to relay turns.
11. Preserve receipts/provenance for inspection without turning main into a chat-log database.

## Visible-turn contract

Each AI turn carries:
- request_id
- actor
- original_question
- previous_visible_answer
- settled[]
- unresolved[]
- answer
- complete
- provider/model identifier
- receipt/provenance

Do not request, store, or expose hidden chain-of-thought. Exchange conclusions, objections, evidence requests, calculations/results, assumptions, and unresolved items.

## Completion

COMPLETE requires a substantive answer to the original question and no material unresolved item that can be resolved within the authorized tools/turn budget.

HOLD means the dialogue cannot responsibly finish yet. HOLD must state the concrete blocker or missing evidence.

FAILED means the route/provider failed and bounded failover was exhausted.

A green workflow alone is not COMPLETE.

## Routing and failover

- Prefer healthy direct authorized route when available.
- Otherwise use the GitHub control plane.
- Otherwise use the durable Bridge-Comand queue/device lattice.
- Preserve the same request_id through failover.
- Record failed attempts as receipts.
- Retry transient 408/429/5xx failures with bounded backoff.
- Fall through to another provider model when the provider reports an unavailable/capacity model and the contract permits it.
- After three equivalent route failures, switch route/angle rather than repeating blindly.
- Never claim execution without a matching final receipt.

## Gemini implementation currently proven

The Builds lane uses:
- `two-ai-dialogue/gemini_adapter.py`
- `two-ai-dialogue/requests/*.json`
- `.github/workflows/dialogue-request.yml`
- GitHub Actions secret `GEMINI_API_KEY`

The secret value must never be written to source, logs, prompts, receipts, or user-visible output.

The adapter discovers models available to the key, performs bounded retry/fallback, and emits `one-wave-gemini-receipt/v1`.

## Natural-language command behavior

When the user says "run it by Gemini," the receiving AI should interpret that as authorization to execute the existing bounded Gemini dialogue route for the current subject. It should not ask the user to operate GitHub manually unless authorization/credentials genuinely require user action.

When the user asks for "a dialogue," use multiple visible turns when substantive disagreement/refinement remains. Do not manufacture extra turns merely to satisfy a count.

## Claim boundary

Repository code/contracts = implementation evidence.
Successful request validation = control-plane evidence.
Provider response + matching receipt = inference evidence.
Multiple matching provider receipts under one request_id = dialogue evidence.
None of these alone proves a physical/scientific claim discussed by the AIs.

## Current acceptance target

From an authorized AI conversation, the human can say "run this by Gemini"; the AI submits the current question, obtains a real Gemini response, optionally conducts bounded follow-up turns, and returns the synthesized result in the original conversation without manual relay.
