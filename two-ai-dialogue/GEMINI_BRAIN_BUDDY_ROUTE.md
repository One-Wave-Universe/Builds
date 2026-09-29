# Gemini Brain Buddy Route Authority

Status: canonical route authority for One-Wave Gemini collaboration.

## Route

`ORIGIN AI -> Builds request -> checkout One-Wave-Science -> bounded repo evidence pack -> define claim/test -> metadata -> CERN/GWOSC/other external wave data -> Gemini API -> validate against repo -> matching receipt -> ORIGIN AI`

The order is mandatory: **repo lens first, metadata second, external measured wave data third**.

This is the default Gemini Brain Buddy route.

## Non-dependencies

The canonical route does **not** depend on:
- Desktop Commander;
- Jetson availability;
- local Gemini CLI OAuth;
- browser extensions;
- human copy/paste relay.

Those may exist as independent fallbacks, but they are not prerequisites and must not silently become the control plane.

## Required proof of success

A Gemini interaction is complete only when all of the following exist:
1. one stable request ID;
2. a successful `Grounded Peer Dialogue` run;
3. a non-empty `repo-evidence.json` from the Science checkout;
4. a matching `one-wave-gemini-receipt/v1`;
5. `status=COMPLETE`;
6. a real provider/model identifier;
7. returned answer text.

A workflow start, checkout, evidence pack, or artifact upload alone is not a Gemini response.

## Latest verified receipt

Verified 2026-09-29:
- Builds commit `a29b36c7b15a655e53bd4793138b7cb591556342`
- run `36585092067`
- request `gemini-brain-buddy-proof-test-20260929-02`
- Gemini model `gemini-3.1-flash-lite`
- artifact `grounded-peer-review`
- conclusion `success`

## Back-and-forth law

For a dialogue request, do not create unrelated new request IDs for every turn. Preserve one dialogue ID, alternate visible turns, carry forward only visible conclusions/objections/evidence needs, and apply `RESOLUTION_PROTOCOL.md`. Hidden chain-of-thought is neither requested nor stored.
