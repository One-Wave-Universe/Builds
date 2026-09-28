# CELL_V1 — Phase-I validation plan

This file is the executable research plan corresponding to `MASTER_CURRENT_STATE.md`.

Recipes for the memory extensions: `USABLE_MEMORY_BENCH.md`.
Catalog of other plasticities (not Phase-I): `OTHER_PLASTICITIES.md`.
Chip ban: `METAPLASTICITY_ANALOGUE.md`, `NOT_SOFTWARE.md`.

## Rule

A successful test validates only the premise that test was designed to measure.

Do not promote a local pass into proof of the whole CELL_V1 architecture.

No processor in the write path. No digital synapse. No resistor dump on the intended return.

## Order

Phase-I core (do not skip):

1. Test A — retained-history nucleus.
2. Test B — bounded moving reference.
3. Test C — physical triadic coherence.
4. Test D — V_BUS / CENTER isolation and reinjection.
5. Test E — six-sector mismatch and cross-coupling.

Phase-I memory extensions (require A; do not replace A–E):

6. Test F — stop-learn in HOLD wobble.
7. Test G — fence walk (θ_M analogue).
8. Test H — palimpsest / cascade depth.
9. Test I — fade / erase τ.
10. Test J — tag-and-capture on one body.

Do not scale to the next stage until the previous premise is measurable and repeatable.
Do not run J before A and H.
Do not run flower / I-cell / lactate-as-modulator before A–E.

## Test A — retained-history nucleus

Goal: identical probe, different prior physical write, repeatably different response.

Measure: write current / voltage; probe response; remanence / retained bias proxy; drift; decay; temperature; repeatability.

Pass: prior-state-dependent response remains separable from noise and drift across repeated trials.

Fail: no repeatable state-dependent difference.

Fallback: material → write conditions → turns → aperture / flux-path geometry.

## Test B — bounded moving reference

Goal: history influences next reference without runaway saturation.

Measure: cycle-to-cycle reference; saturation margin; reversal; relaxation; hysteresis-loop movement.

Pass: bounded, repeatable history-dependent next reference.

Fail: monotonic drift into saturation or irrecoverable state.

## Test C — physical triadic coherence

Goal: A/B/C relation resolves physically without a digital arbiter.

Cases: 2 aligned / 1 opposed; polarity reverse; one active / two near HOLD; balanced opposition; all near HOLD.

Measure: summed current / flux; CENTER; chatter; latency; mismatch sensitivity; history dependence.

Pass: equivalent relations resolve reproducibly and HOLD is distinguishable from OFF.

Fail: mismatch / uncontrolled coupling dominates.

## Test D — V_BUS / CENTER isolation

Goal: return recoverable inductive energy without corrupting CENTER or retained state.

Measure: E_in; E_rec; flyback peak; V_BUS ripple; CENTER disturbance; retained-state before / after; return timing.

Pass: measurable return, CENTER stays within allowed operating region, retained-state test remains repeatable.

Fail: return corrupts CENTER or dominates / erases retained state.

No resistor dump / bleed / damping return is part of the intended solution.

## Test E — six-sector mismatch

Goal: verify usable opposed-axis behavior in the real six-sector geometry.

Perturb one sector. Measure opposed partner, neighboring axes, coupling matrix, leakage, CENTER, next lean, temperature.

Pass: intended axis relation remains distinguishable and repeatable.

Fail: geometry collapses into uncontrolled common coupling.

## Test F — stop-learn in HOLD wobble

Goal: 0.45–0.55 V dwell does not deepen remanence.

Pass: same probe as A, after long HOLD dwell, is indistinguishable from pre-dwell within drift.

Fail: wobble writes.

## Test G — fence walk

Goal: dense same-direction burst (off terminal bands) moves the next crossing voltage after return to HOLD.

Pass: rested vs busy crossing voltages separable.

Fail: fence fixed; no analogue θ_M on this core.

## Test H — palimpsest / cascade depth

Goal: A once, conflicting B many, probe soon (B dominates), idle / low bus, probe again.

Pass: B visible soon; A residue or bias remains vs virgin after idle. Hidden depth.

Fail-one-beaker: A gone with no residue.
Fail-frozen: A never yields to B.

## Test I — fade / erase

Goal: deep write is reversible by opposite excursion or measured wait/heat.

Pass: probe walks toward virgin; τ quoted.

Fail: no fade; first habit locks.

## Test J — tag-and-capture analogue

Goal: weak seat persists only when a strong seat on the *same* square figure-8 body wrote inside the measured leftover-field window.

Pass: W lives iff S happened on that body in that window.

Fail: W lives with S off-body, or W never lives, or the window is a phone timer not a field measurement.

No protein. No chip. Flux + remanence + shared core only.

## Phase-I conclusion

If A–E pass:

> The five Phase-I CELL_V1 premises survived bench validation in the tested configuration.

If F–J also pass:

> Retained-history on this nucleus also supports HOLD-stop, fence walk, palimpsest depth, fade, and same-body tag in the tested configuration.

That does not yet validate the flower, M4, five-mind, six-mind, full motor performance, inhibitory second species, lactate-as-modulator, or full Algorythm-Zer0 runtime.

## First build target

Start with one hysteretic multi-aperture / figure-8 nucleus.

Do not lock arbitrary current, pulse width, turn count, or acceptance percentage before measuring the actual core.

Use externally current-limited test equipment for characterization rather than inserting a resistor-based architectural path.

First question:

> Does opposite prior write history produce a repeatably different response to the same probe?
