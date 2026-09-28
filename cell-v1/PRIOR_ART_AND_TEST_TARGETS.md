# CELL_V1 — prior-art candidates and test targets

**Status:** comparison map, not canon. Nothing in this file proves CELL_V1 works.

The purpose of this file is to connect current CELL functions to established mechanism classes, then identify the exact mismatch that still requires testing.

Chip-free only for implementation. Digital / ASIC / memristor-crossbar cousins may be read as Gray. They are not the body.

## 1. Multi-aperture hysteretic cores / transfluxors

The motor-control nucleus is currently a **one-piece square two-aperture figure-8 hysteretic core**. Historical multi-aperture magnetic cores and transfluxor-like devices are relevant because they use multiple flux paths in one magnetic body and allow prior magnetic state to alter later response.

May support: retained-history; coupled flux paths; write / probe separation.

Does not prove: Zer0 semantics; Field/Void; motor control; stable moving reference.

Bench: Hc, Br, write current, probe, aperture coupling, decay, thermal.

Falsify: equal-magnitude opposite prior writes, same probe. No separable response → fail. (Validation Test A.)

---

## 2. Magnetic majority / physical current-summing logic

CELL: two agree → push; one voice → wait; opposition → HOLD; gap → wait.

Precedent: magnetic majority, current-summing thresholds, coupled-oscillator consensus. No digital arbiter.

Does not prove CELL A/B/C is majority, or that three axes should share one core.

Falsify: all A/B/C sign combinations; if mismatch beats intended state, fail. (Test C.)

---

## 3. Non-dissipative inductive recovery / DC-link return

Return to V_BUS. CENTER stays local. Precedent: flyback recovery, regen clamp, DC-link energy recovery.

Does not prove sharing, that return improves the next action, or that memory = recovered energy.

Falsify: load V_BUS during return; CENTER shift or nucleus corruption → fail. (Test D.)

---

## 4. Six-sector magnetic geometry

A+ B+ C+ A- B- C- with opposed mirrors. Precedent: multiphase stator, reluctance, saturable assemblies, multiwinding flux-sum.

Falsify: perturb one sector; measure spread. (Test E.)

---

## 5. Moving reference / bounded physical rebase

Zer0: (0)t → event → consequence → resolve → (0)t+1.

Precedent: adaptive reference, hysteretic attractors, history-biased oscillators. Comparison only.

Falsify: repeated same-sign events walk to hard sat with no physical release → fail. (Test B.)

---

## 6. Metaplasticity / BCM sliding threshold (Gray biology)

Abraham-Bear: prior activity changes the *rule*, not only present efficacy. BCM θ_M slides with history. Mechanisms: NR2A/NR2B, CaMKII vs CaN, AHP / I_h, neuromodulator pull-push.

CELL overlap: fence voltage after a burst (Test G); HOLD must not write (Test F).

Mismatch: no NMDA, no kinase. Fence must move in *this* core's volts / Br.

Falsify: busy vs rested crossing identical → no analogue θ_M.

---

## 7. Cascade / palimpsest / Benna-Fusi (Gray theory)

Hidden states delink fast write from slow keep. Power-law-ish fade from many τ. New on top, old underneath until the stack saturates.

CELL overlap: local nucleus vs square-figure-8 body diary; cap = last kick not diary (MEMORY.md). Test H.

Mismatch: Fusi states are occupancy probabilities. CELL hidden state is Br / threshold bias.

Falsify: A-then-B-then-idle leaves either nothing of A (one beaker) or A that never yields (frozen habit).

---

## 8. Tag-and-capture / spacing (Frey-Morris)

Weak local tag; strong neighbor supplies diffusible products; tag captures; weak trace lives. Tag ≠ LTP expression.

CELL overlap: two seats on one square figure-8; leftover field is the only legal PRP. Test J.

Mismatch: no protein synthesis, no dopamine novelty pulse.

Falsify: weak seat lives with strong write off-body, or window is a wall clock.

---

## 9. Other classes (explored, later)

See `OTHER_PLASTICITIES.md`.

- Intrinsic excitability (LTP-IE, I_h, AHP) — pair threshold vs Br split.
- Synaptic scaling — all seats after long rail high/low.
- Heterosynaptic LTP/LTD — write A, probe untouched B.
- Inhibitory plasticity — opposed flux only; no second digital species.
- Neuromodulator pull-push — same write, rail high vs low.
- E/I co-dependence — physical 2-on-1 / 1-on-2 sum.

Do not promote these into Phase-I.

---

## 10. What to research next (chip-free)

Transfluxors; multi-aperture cores; magnetic core memory; magnetic amplifiers; saturable reactors; magnetic majority; parametrons; fluxgates; current-mode threshold; discrete asynchronous analog; coupled-oscillator consensus; non-dissipative snubbers; regen DC-link; switched / synchronous reluctance; continuous-time recurrent analog.

For every claimed match record: established mechanism; CELL function; overlap; mismatch; chip-free relevance; quantities; falsification test.

Do not rename a CELL concept until a one-to-one equivalence is demonstrated.
