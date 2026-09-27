# CELL_V1 — prior-art candidates and test targets

**Status:** comparison map, not canon. Nothing in this file proves CELL_V1 works.

The purpose of this file is to connect current CELL functions to established mechanism classes, then identify the exact mismatch that still requires testing.

## 1. Multi-aperture hysteretic cores / transfluxors

### Why this matters

The motor-control nucleus is currently a **one-piece square two-aperture figure-8 hysteretic core**. Historical multi-aperture magnetic cores and transfluxor-like devices are relevant because they use multiple flux paths in one magnetic body and allow prior magnetic state to alter later response.

### What this may support

- retained-history dependence;
- multiple coupled flux paths in one core;
- write / probe separation;
- a physical old-state / new-excitation interaction.

### What it does NOT prove

- Zer0 semantics;
- Field/Void mapping;
- four views / four actions;
- three-mirror recursion;
- useful motor control;
- stable moving reference.

### Bench quantities

- coercive force Hc;
- remanence Br;
- write current;
- probe response;
- aperture-to-aperture coupling;
- retention / decay;
- thermal sensitivity.

### Falsification test

Apply equal-magnitude opposite prior writes, then the same probe. If the response is not repeatably distinguishable beyond noise and drift, retained-history use in that core fails.

---

## 2. Magnetic majority / physical current-summing logic

### Why this matters

CELL currently uses:

```text
two agree -> push
one voice -> wait
opposition -> HOLD
gap -> wait
```

Magnetic majority gates, current-summing threshold elements, and coupled-oscillator consensus systems are relevant precedent classes because multiple physical contributions can sum to a threshold without a digital arbiter.

### What this may support

- 2-vs-1 physical coherence;
- cancellation near HOLD;
- asynchronous threshold crossing;
- no central software vote.

### What it does NOT prove

- that CELL's A/B/C geometry performs majority logic automatically;
- that HOLD is stable;
- that coercivity is the right threshold mechanism;
- that the three axes should share one core.

### Bench quantities

- summed current / flux;
- threshold current;
- dead-band width;
- CENTER motion;
- chatter;
- switching latency;
- history dependence.

### Falsification test

Test all principal A/B/C sign combinations and confirm that nominally equivalent cases resolve the same way. If the result depends more on device mismatch than intended state, the physical consensus mechanism is not ready.

---

## 3. Non-dissipative inductive recovery / DC-link return

### Why this matters

CELL routes recoverable inductive collapse toward **V_BUS**, while CENTER remains the local differential reference.

Relevant precedent classes include non-dissipative flyback recovery, regenerative clamp networks, and DC-link energy recovery.

### What this may support

- returning inductive energy to a shared rail;
- avoiding intentional resistor dumps;
- measuring recovered energy separately from retained magnetic state.

### What it does NOT prove

- useful cross-cell sharing;
- that reinjection improves the next action;
- that return will not disturb CENTER;
- that memory and energy recovery are the same physical variable.

### Bench quantities

- E_in;
- E_rec;
- peak flyback voltage;
- bus ripple;
- CENTER disturbance;
- return timing;
- nucleus-state change before / after return.

### Falsification test

Load V_BUS strongly during return. If CENTER shifts or the nucleus state is corrupted beyond repeatable limits, the current isolation topology fails.

---

## 4. Six-sector magnetic geometry

CELL currently defines six tapered magnetic sectors:

```text
A+ B+ C+ A- B- C-
```

with opposed mirrors:

```text
A+ <-> A-
B+ <-> B-
C+ <-> C-
```

Closest precedent classes to investigate include multiphase stator geometries, switched / synchronous reluctance structures, saturable magnetic assemblies, and multiwinding flux-summing cores.

### Required comparison questions

- Does tapering improve field concentration or only complicate construction?
- Does tip-to-tip geometry improve differential isolation or worsen cross-coupling?
- Can the same field relation be produced with simpler cores?
- Does base-to-base tiling create a useful intercell path?
- Is the central region magnetically stable across temperature and tolerance?

### Bench quantities

- sector inductance;
- mutual coupling matrix kij;
- leakage flux;
- saturation onset;
- thermal drift;
- center-field magnitude;
- axis isolation.

### Falsification test

Perturb one sector and quantify how much the error spreads into its opposed partner, neighboring axes, CENTER, and the next cycle.

---

## 5. Moving reference / bounded physical rebase

Zer0 requires:

```text
(0)t -> event -> consequence -> resolve -> (0)t+1
```

Relevant precedent classes include adaptive reference systems, moving-equilibrium control, hysteretic systems, attractor dynamics, and phase/history-biased oscillators.

These are comparisons, not exact matches.

### Required physical question

Can a purely physical retained state create a **bounded, useful next reference** instead of merely drifting toward saturation?

### Bench quantities

- cycle-to-cycle reference offset;
- saturation margin;
- relaxation / decay;
- hysteresis loop position;
- repeatability;
- effect of reversed input.

### Falsification test

Drive repeated same-sign events. If reference shift grows monotonically to saturation with no physical release / rebasing behavior, that implementation candidate fails.

---

## 6. What to research next

High-priority historical and modern mechanism classes:

- transfluxors;
- multi-aperture magnetic cores;
- magnetic core memory;
- magnetic amplifiers;
- saturable reactors;
- magnetic majority logic;
- parametrons;
- fluxgates;
- current-mode threshold logic;
- discrete asynchronous analog logic;
- coupled-oscillator consensus;
- non-dissipative snubbers;
- regenerative DC-link recovery;
- switched / synchronous reluctance machines;
- continuous-time recurrent analog systems.

For every claimed match, record:

1. established mechanism;
2. exact CELL function being compared;
3. exact overlap;
4. exact mismatch;
5. chip-free implementation relevance;
6. measurable quantities;
7. falsification test.

Do not rename a CELL concept until a one-to-one equivalence is demonstrated.
