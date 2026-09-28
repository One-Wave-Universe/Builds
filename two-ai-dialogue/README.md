# Two-AI Dialogue Box v0

Small visual proof before the Hyperbolic Evolution Chamber.

One user question drives a bounded back-and-forth between two adapters:
- CHATGPT
- GEMINI

The UI shows both streams, current turn, unresolved items, settled items and the final synthesis.

## Loop

QUESTION → CHATGPT → GEMINI → CHATGPT → … → RESOLVE → FINAL

Each turn receives the original question, the previous response, settled points and unresolved points. The adapter must return structured JSON:
`answer, settled, unresolved, complete`.

Stop on:
- both sides report complete and no unresolved items;
- max turns;
- user Stop;
- adapter failure/HOLD.

No hidden chain-of-thought is requested or stored. The visible exchange contains conclusions, objections, evidence requests and proposed answers.

## Run

Open `index.html` for the visual shell.

The browser shell intentionally uses adapter URLs rather than embedding API secrets. Real ChatGPT/Gemini adapters belong behind the authenticated Bridge-Comand/device lattice.

For deterministic development:
`python3 two-ai-dialogue/loop.py two-ai-dialogue/fixtures/question.json`

This v0 proves orchestration/state/replay. Live model transport is the next adapter job.


## AI invocation

Any authorized AI that receives a natural-language request such as **"run it by Gemini"** must follow [AI_INVOCATION_CONTRACT.md](AI_INVOCATION_CONTRACT.md). The human-facing contract is that routing, request creation, receipt retrieval, bounded follow-up, and return of the result are handled by the AI/control plane rather than manually relayed by the human.
