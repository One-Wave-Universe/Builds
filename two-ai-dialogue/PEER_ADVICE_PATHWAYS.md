# Peer Advice Pathways

Purpose: let any authorized AI obtain independent peer review from one or more other AI providers while keeping the human in one conversation.

## Human interface

Examples:
- "Run this by Gemini."
- "Ask Claude to challenge this."
- "Get two other AIs to critique this."
- "Have Gemini and ChatGPT discuss it until they agree on the next experiment."

The receiving AI owns routing, receipts, bounded follow-up, synthesis, and return to the originating conversation.

## Pathway law

ORIGIN AI -> CONTROL PLANE -> PROVIDER ADAPTER -> PROVIDER -> RECEIPT -> DIALOGUE STATE -> NEXT PROVIDER OR ORIGIN AI

Every pathway must preserve:
- stable request ID;
- original human question;
- target provider/actor;
- project/canon references when relevant;
- visible previous turn;
- settled and unresolved items;
- proposed resolution/next action;
- source class and provenance;
- bounded max turns/retries/timeouts;
- exact provider/model/response ID in receipts.

Never exchange or request hidden chain-of-thought. Exchange conclusions, objections, assumptions, evidence, calculations/results, proposed tests, and unresolved items.

## Existing pathways

### Gemini
Adapter: `gemini_adapter.py`
Credential: GitHub Actions secret `GEMINI_API_KEY`
Status: live inference proven.

### OpenAI
Adapter: `openai_adapter.py`
Credential: GitHub Actions secret `OPENAI_API_KEY`
Status: route/auth present; most recent execution HOLD due HTTP 429. Require a later COMPLETE receipt before calling it live-successful.

## Creating another peer pathway

For Claude, DeepSeek, Pi, a local model, or another provider:

1. Create `<provider>_adapter.py` implementing the same visible-turn contract.
2. Keep credentials only in the execution platform's secret store; never source-control them.
3. Accept the canonical request/dialogue-state object rather than inventing a provider-specific human interface.
4. Return a receipt with request_id, actor, answer, provider, model, response_id if available, status, attempts/failures, and provenance.
5. Map transient provider errors to bounded retry; map exhausted quota/capacity to HOLD.
6. Add the adapter to the control-plane provider registry.
7. Add a contract test with no live secret.
8. Add a live smoke test that proves an actual provider response.
9. Add a two-turn test where another provider receives this provider's visible answer.
10. Add a bounded multi-turn test that reaches AGREED_RESOLUTION or AGREED_NEXT_ACTION.
11. Preserve disagreement; never force consensus.
12. Mark the pathway proven only when a matching provider receipt exists.

## Provider registry target

Maintain a machine-readable registry with:
- provider ID;
- actor label;
- adapter path;
- required secret name;
- health: PROVEN | HOLD | UNPROVEN | DISABLED;
- capabilities;
- preferred models/discovery method;
- retry policy;
- last matching receipt/run;
- allowed projects/routes.

The dialogue runner chooses only authorized healthy pathways. A requested unavailable provider produces HOLD or authorized failover; it must never impersonate that provider.

## Multi-peer modes

- REVIEW: one external AI critiques origin AI.
- DEBATE: two AIs alternate objections and revisions.
- PANEL: multiple providers independently answer before synthesis.
- ADVERSARY: peer attempts to falsify/break proposal.
- BUILDER_REVIEWER: one proposes concrete build, another audits buildability.
- EVIDENCE_CHECK: peer checks whether claims outrun receipts/data.
- NEXT_ACTION: peers seek the smallest agreed falsifiable next action.

Mode changes roles, not evidence standards.

## Bridge-Comand relationship

Builds owns the dialogue application and provider adapters. Bridge-Comand owns generic routing/relay/device-lattice transport. Do not duplicate transport authority inside Builds. If a provider runs on Jetson/laptop/another worker, send the canonical dialogue envelope through Bridge-Comand and require the matching machine/provider receipt back.

## Completion

Follow `RESOLUTION_PROTOCOL.md`. Agreement is explicit acceptance of materially the same resolution/action by opposing actors. If evidence is missing, agree on the next measurement/test instead of agreeing that a claim is true.
