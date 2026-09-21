# Builds

The grant and engineering home of One Wave.

Proposed designs until a file records a measured result. Empty `cell-v1/LOG.md` means hardware score is 0%.

## Read this first

The weight is a physical lean off a moving virtual ground.
Memory is that lean remaining in the same path. Not a receipt. Not a log that remembers for the cell. Not a float in `/algorithms`.

- Law: `cell-v1/WEIGHT_LEAN.md`
- Boundary: `cell-v1/NOT_SOFTWARE.md`
- First solder: `cell-v1/CELL0.md`
- Zer0 lock (talk only): `algorithms/LEAN_INTO_ZER0.md`

`algorithms/lean_weight.py` tests the *commit rule*. It does not hold memory.

## Two workstreams

1. **Cell** — `/cell-v1/` — body, lean, hardness, log.
2. **Algorithm** — `/algorithms/` — addressing + when a lean may be called committed.

Science stays in `One-Wave-Science`. Fiction stays in `Mythos-and-Stories`. Neither is this package.

See `STATUS.md` and `GRANT.md`.
