# Builds

The grant and engineering home of One Wave.

Proposed designs until a file records a measured result. Empty `cell-v1/LOG.md` means hardware score is 0%.

## Read this first

The weight system is **physical**. A lean off a moving virtual ground. Voltage, current split, magnetic hold. It lives in the same path that processes the signal.

Not a float in a table. Not backprop. Not a download.

- Law: `cell-v1/WEIGHT_LEAN.md`
- Boundary: `cell-v1/NOT_SOFTWARE.md`
- First solder: `cell-v1/CELL0.md`
- How Zer0 is allowed to *talk* about a lean: `algorithms/LEAN_INTO_ZER0.md`

`algorithms/lean_weight.py` is a receipt so the four-branch lock can be tested in a sandbox. It is not the weight. Do not ship it as parameters.

## Two workstreams

1. **Cell** — `/cell-v1/` — the body. Pair, lean, hardness, log.
2. **Algorithm** — `/algorithms/` — addressing (Rabbit Hopping) and the Zer0 lock that may only *commit* a lean at T6.

Science thought-experiments stay in `One-Wave-Science`. Fiction stays in `Mythos-and-Stories`. Neither is this package.

## Status

See `STATUS.md` and `GRANT.md`.
