# One-Wave Foreman Workstation

A repo-backed project-control workstation for the One-Wave program.

The Foreman does **not** decide scientific truth and does not mark work complete from prose. It keeps project state coherent across Builds, One-Wave-Science, Bridge-Comand and later project repos.

## First runnable version

Open `index.html` directly in a browser. It reads its embedded default registry and can also import/export the same JSON registry used by workers.

Headless validation:

```bash
python3 foreman.py validate registry.json
python3 foreman.py summary registry.json
```

## Lifecycle

`IDLE → PRIMED → EXECUTING → VECTORING → RESOLVING → DONE`

DONE requires acceptance criteria plus at least one receipt. A BLOCKED job must name a blocker.

## Authority

Each lane declares canonical references. Workers should load those before modifying the lane. Receipts point to commits, test outputs, measurements or artifacts. A worker claim is not itself a receipt.

## Next adapters

1. GitHub issue/commit synchronizer.
2. Science 24→1 sandbox registry adapter.
3. Bridge-Comand/Jetson receipt adapter.
4. Worker handoff queue.
5. stale/canon-drift detection.
