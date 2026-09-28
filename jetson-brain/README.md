# Jetson Two-State Brain Runtime

Digital implementation target for the One-Wave Field/Void architecture.

## Mapping

- **FIELD / GPU**: parallel candidate expansion, sensory transforms, field-like array work.
- **VOID / CPU**: control, compression, validation, reconstruction, memory/reference access.
- **Loop Router**: routes bounded work FIELD → VOID → resolution → next FIELD or HOLD.

This is an engineering mapping, not a claim that CPU/GPU hardware physically embodies Field/Void.

## First runnable reference

```bash
python3 loop_router.py --cycles 6
python3 loop_router.py --cycles 6 --jsonl receipts.jsonl
```

The v0 runtime uses a deterministic CPU FIELD backend so it runs anywhere. A Jetson GPU backend is an adapter, not a prerequisite.

## Router law

`OBSERVE → FIELD → VOID → RESOLVE → EMIT/HOLD → RECEIPT → REENTER`

Every cycle has:
- cycle ID;
- input/reference;
- FIELD candidate;
- VOID validation/counterstate;
- resolution;
- receipt;
- bounded next action.

No infinite retry loop. HOLD is a valid state.

## Planned Jetson adapters

1. CUDA/GPU FIELD executor.
2. CPU VOID validator/controller.
3. microphone and camera sensory queues.
4. Recall/Rebuild memory adapter.
5. Foreman job adapter.
6. DCACRC-IR program adapter.
7. simulated dreamscape source adapter.
