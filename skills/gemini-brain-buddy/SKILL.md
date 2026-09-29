---
name: gemini-brain-buddy
description: Use the proven GitHub-hosted Grounded Peer Dialogue route to ask Gemini questions against a bounded checkout of One-Wave-Science, retrieve the matching receipt, and optionally continue a bounded visible back-and-forth under one request ID.
---

# Gemini Brain Buddy

## Baseline-zero route

Mandatory evidence order:

`ONE-WAVE REPO LENS -> CLAIM/TEST DEFINITION -> METADATA -> CERN/GWOSC/OTHER EXTERNAL WAVE DATA -> GEMINI INTERPRETATION -> VALIDATE BACK AGAINST REPO`

The repo lens always comes first. Metadata is second. External measured data is third. No external source may silently redefine the One-Wave claim under test.

For any request equivalent to "ask Gemini", "run it by Gemini", "have Gemini review this", or "have a dialogue with Gemini":

1. Use the Builds repository as the invocation/control plane.
2. Create one request under `two-ai-dialogue/requests/`.
3. Set `repo_read.repository` to `One-Wave-Universe/One-Wave-Science`, `root` to `peer-repo`, and provide a bounded query.
4. Let `.github/workflows/grounded-peer-dialogue.yml` checkout Science and build `repo-evidence.json` first.
5. Before any bulk/external data, identify the exact One-Wave claim/test from the repo evidence pack.
6. Query bounded metadata next.
7. Only then consult CERN Open Data, GWOSC, LIGO, spectroscopy, or other external wave-domain data needed for the test.
8. Gemini performs external research/grounding with provider material kept separate from repo claims.
9. Gemini answers the originating AI's bounded question and the receipt records repo evidence, metadata used, external data/research sources, and unresolved gaps.
10. Retrieve the exact workflow run and require `one-wave-gemini-receipt/v1` with the same request ID and `status=COMPLETE`.
11. Treat only paths in the evidence pack as repository files actually read by Gemini.
12. Return Gemini's answer, repository paths used, metadata consulted, external data/research sources, and unresolved items to the originating conversation.

## Proven route

Canonical route:

`ORIGIN AI -> Builds request -> Grounded Peer Dialogue -> checkout One-Wave-Science -> repo evidence pack -> Gemini API -> matching receipt/artifact -> ORIGIN AI`

This route is intentionally independent of Desktop Commander, Jetson, local Gemini CLI, browser extensions, and manual human relaying.

Latest matching proof at time of this update:
- Builds workflow: `Grounded Peer Dialogue`
- run: `36585092067`
- request: `gemini-brain-buddy-proof-test-20260929-02`
- result: `COMPLETE`
- artifact: `grounded-peer-review`
- provider/model: Google Gemini / `gemini-3.1-flash-lite`

## Evidence law

Repository lens is context, not proof. Preserve established mathematics, repository-derived claims, hypotheses, assumptions, simulations, and measurements as distinct classes. Never upgrade a scientific claim merely because Gemini agrees with it.

## Failure law

If the Grounded Peer Dialogue route fails:
1. read the matching job/receipt;
2. change route or model only after identifying the failing boundary;
3. preserve the same request ID through bounded failover where possible;
4. never fall back to Desktop Commander merely because it exists;
5. never claim a queued workflow is a Gemini answer.

## Default interaction

The default is **not** a debate. It is:

`ORIGIN AI QUESTION -> REFERENCE ONE-WAVE-SCIENCE -> EXTERNAL RESEARCH -> GEMINI ANSWER -> RECEIPT -> ORIGIN AI`

Use back-and-forth only when the user explicitly asks for dialogue, debate, iteration, or follow-up.

## Back-and-forth

Use `two-ai-dialogue/grounded_dialogue_runner.py` for bounded alternation. One stable request ID survives all turns. Each visible turn must carry the original question, previous visible answer, settled/unresolved items, proposal/next action, provider/model/response ID, and receipt provenance. Stop only under `RESOLUTION_PROTOCOL.md`.
