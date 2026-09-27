# CELL_V1 — Phase-I validation plan

This file is the executable research plan corresponding to `MASTER_CURRENT_STATE.md`.

## Rule

A successful test validates only the premise that test was designed to measure.

Do not promote a local pass into proof of the whole CELL_V1 architecture.

## Order

1. Test A — retained-history nucleus.
2. Test B — bounded moving reference.
3. Test C — physical triadic coherence.
4. Test D — V_BUS / CENTER isolation and reinjection.
5. Test E — six-sector mismatch and cross-coupling.

Do not scale to the next stage until the previous premise is measurable and repeatable.

## Test A — retained-history nucleus

Goal: identical probe, different prior physical write, repeatably different response.

Measure:
- write current / voltage;
- probe response;
- remanence / retained bias proxy;
- drift;
- decay;
- temperature;
- repeatability.

Pass: prior-state-dependent response remains separable from noise and drift across repeated trials.

Fail: no repeatable state-dependent difference.

Fallback sequence:
1. material;
2. write conditions;
3. turns;
4. aperture / flux-path geometry.

## Test B — bounded moving reference

Goal: history influences next reference without runaway saturation.

Measure:
- cycle-to-cycle reference;
- saturation margin;
- reversal;
- relaxation;
- hysteresis-loop movement.

Pass: bounded, repeatable history-dependent next reference.

Fail: monotonic drift into saturation or irrecoverable state.

## Test C — physical triadic coherence

Goal: A/B/C relation resolves physically without a digital arbiter.

Cases:
- 2 aligned / 1 opposed;
- polarity reverse;
- one active / two near HOLD;
- balanced opposition;
- all near HOLD.

Measure:
- summed current / flux;
- CENTER;
- chatter;
- latency;
- mismatch sensitivity;
- history dependence.

Pass: equivalent relations resolve reproducibly and HOLD is distinguishable from OFF.

Fail: mismatch / uncontrolled coupling dominates.

## Test D — V_BUS / CENTER isolation

Goal: return recoverable inductive energy without corrupting CENTER or retained state.

Measure:
- E_in;
- E_rec;
- flyback peak;
- V_BUS ripple;
- CENTER disturbance;
- retained-state before / after;
- return timing.

Pass: measurable return, CENTER stays within allowed operating region, retained-state test remains repeatable.

Fail: return corrupts CENTER or dominates / erases retained state.

No resistor dump / bleed / damping return is part of the intended solution.

## Test E — six-sector mismatch

Goal: verify usable opposed-axis behavior in the real six-sector geometry.

Perturb one sector in a controlled way.

Measure:
- opposed partner;
- neighboring axes;
- coupling matrix;
- leakage;
- CENTER;
- next lean;
- temperature.

Pass: intended axis relation remains distinguishable and repeatable.

Fail: geometry collapses into uncontrolled common coupling.

## Phase-I conclusion

If A-E pass:

> The five Phase-I CELL_V1 premises survived bench validation in the tested configuration.

That does not yet validate the flower, M4, five-mind, six-mind, full motor performance, or full Algorythm-Zer0 runtime.

## First build target

Start with one hysteretic multi-aperture / figure-8 nucleus.

Do not lock arbitrary current, pulse width, turn count, or acceptance percentage before measuring the actual core.

Use externally current-limited test equipment for characterization rather than inserting a resistor-based architectural path.

First question:

> Does opposite prior write history produce a repeatably different response to the same probe?
