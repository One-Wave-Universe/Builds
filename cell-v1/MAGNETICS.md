# Magnetics — CELL_V1 rebuilt layout

This file must agree with `CELL.md`. References R1–R8 are defined in `PROVEN_PARTS_REFERENCES.md`.

## 1. Motor-control nucleus — square figure-8 core with twisted bifilar winding

One planar **square figure-8 magnetic nucleus with a twisted bifilar winding pair** is the motor-control nucleus. The figure-8 geometry is retained; bifilar describes the two conductors wound together, not a replacement core geometry.

Proposed CELL role:
- receive coupled continuous analog differential/alternating bias from BC–DC and TC–AC;
- support the QC–RC rotating/vector magnetic relation;
- expose physical proxies for Direction / Phase / Strength / Reference;
- retain local magnetic history through material hysteresis where measurements support it.

Established basis:
- orthogonal magnetic information channels / sine-cosine coupling: resolver precedent **R1**;
- rotating field from phase-related windings: **R3**;
- ferrite hysteresis/material characterization: **R4**.

**Not established:** that this square figure-8 geometry automatically behaves as a resolver, performs the CELL QC–RC operation, or gives useful memory. Those are simulation/bench claims.

Ordinary magnetic relationships:

```text
H = N I / l_e
B = B(H, history)
Phi = B A_e
lambda = N Phi
v = d(lambda)/dt
```

For a two-component view field:

```text
B_view = Bx x_hat + By y_hat
|B_view|^2 = Bx^2 + By^2
theta = atan2(By, Bx)
```

These equations describe vector geometry; the actual Bx/By winding placement and coupling must be measured.

## 2. Common outer/body interface — two PLAIN round toroids

Every current CELL role uses **two plain round toroids** as its common outer/body differential interface.

They are:
- plain round toroids;
- **not figure-8 toroids**;
- not automatically a Helmholtz pair;
- not independent memories;
- a common physical coupling/body-state interface whose exact winding map remains a validation item.

This replaces the obsolete description of “two outer round figure-8 toroidal structures.”

Where A/B/C electromagnetic projection is used, the established comparison is the 120-degree stator geometry of a synchro (**R2**) and rotating-field machinery (**R3**). Those references establish electromagnetic projection/rotation, not the exact toroid geometry.

## 3. A/B/C and four actions are different layers

- **Four actions down:** Inward / Outward / Across / Over.
- **A/B/C:** three mirrored spatial differential axes / edge-seat pairs.

Do not rename the four actions A/B/C.

A/B/C may use a three-half-bridge power topology as a proven power-stage precedent (**R7**), but CELL's analog threshold/hysteresis path must determine action; an MCU/PWM/FOC controller is not substituted for the cell.

## 4. Etched hysteretic lattice

The distributed muscle-memory candidate is the **etched/patterned hysteretic path layer**.

Patterned Permalloy nanowires and geometrical pinning structures demonstrate that magnetic domain state can be stored/manipulated and domain walls can be pinned by geometry (**R5, R6**).

That establishes a candidate mechanism class only. CELL must determine:
- material and thickness;
- path width/geometry;
- write field/current;
- coercive/depinning thresholds;
- retention and decay;
- crosstalk;
- thermal sensitivity;
- whether return/reinjection preserves, reverses, erases or leaves path state unchanged.

## 5. Reinjection / V_BUS

Inductive field energy and motor back-EMF can return current toward a DC link through a suitable switching/diode path (**R8**). Standard three-phase stages also use DC-link capacitors (**R7**).

CELL mapping:

```text
magnetic/load action
    -> field collapse / return current
    -> protected steering
    -> DC-link reservoir
    -> V_BUS
    -> next physical event
```

CENTER/(0) is separate and must not become the recovery rail.

## 6. Coupled-system measurements

Characterize:
- B-field map of the square figure-8;
- Bx/By magnitude and relative phase;
- rotation/ellipticity/handedness;
- mutual inductance nucleus ↔ outer/body pair;
- remanence and coercivity;
- minor/major loops;
- saturation;
- turns and winding resistance;
- thermal loss;
- field symmetry and stray field;
- A/B/C projection;
- path write/depinning threshold;
- V_BUS excursion and recovered energy;
- CENTER disturbance during action and return.

## Anti-drift

- motor nucleus = **one planar square figure-8 toroid**;
- outer/body interface = **two plain round toroids**;
- no outer figure-8 pair;
- BC–DC → TC–AC → QC–RC is the nested view stack;
- QC–RC rotating field is a CELL mapping built from established electromagnetic precedents, not yet a demonstrated CELL function;
- four actions down ≠ A/B/C;
- etched hysteretic paths = distributed muscle-memory candidate;
- V_BUS = energy/readiness/reinjection rail, not stored memory;
- CENTER/(0) = active balanced ternary reference, not V_BUS;
- no IC/chip, MCU, PWM/FOC, MTJ, or software state controller is used as the CELL decision mechanism.


### Twisted-bifilar Field / Void winding — locked build hypothesis

Use one closely coupled insulated wire pair, twisted together before winding, as the **Field (F)** and **Void (V)** conductors on the square figure-8 nucleus. Bifilar construction is selected because the two conductors follow nearly the same magnetic path and therefore have high mutual coupling / low leakage relative to separated windings.

Mark the starts **F·** and **V·** (dot convention) before winding. Keep equal turn count and the same physical twist/winding path. Do not infer polarity from wire color after construction; verify it with a low-energy induced-voltage polarity test.

The two useful excitation modes are:

```text
COMMON / REINFORCING TEST
F and V ampere-turns same magnetic sense
H_net ~ (N_F I_F + N_V I_V) / l_e
-> strong net core excitation / write candidate

DIFFERENTIAL / OPPOSING TEST
F and V ampere-turns opposite magnetic sense
H_net ~ (N_F I_F - N_V I_V) / l_e
-> cancellation/balance candidate near equal currents
-> imbalance leaves a signed residual field
```

This is the physical basis for testing Field/Void as an opposed read/write pair. **Do not lock which mode means WRITE, READ, EXPRESS, COMPRESS, Field or Void until measured.** Bifilar winding guarantees close coupling; it does not guarantee the CELL semantics.

### Figure-8 lobe relation

The square figure-8 has two lobes joined by a crossover/shared central region. Wind/route the pair so the lobe magnetic senses are deliberately known. The first prototype must expose four test leads (F start/finish, V start/finish) so series-aiding and series-opposing configurations can be swapped without rewinding.

Test both lobe configurations:
1. **counter-lobe:** flux sense in lobe 1 opposes lobe 2 at the shared/crossover relation;
2. **co-lobe:** flux sense is reinforcing through the intended shared magnetic path.

The correct CELL configuration is whichever produces the required measurable combination of: stable CENTER balance, signed residual for imbalance, reversible hysteretic write, readable induced return, and no destructive saturation. Do not choose it by diagram alone.

### Read / write measurement

WRITE candidate: apply a controlled low-energy F/V current relation and record current plus B/H proxy.

READ candidate: remove/reduce drive and observe induced voltage in the paired conductor / sense winding while probing the same nucleus after controlled opposite histories.

A memory claim passes only if the **same read probe after different controlled histories produces reproducibly different responses beyond noise/drift**. The process/history is the memory; the bifilar pair is the tightly coupled interface to that process.

### Three-mirror integration

The bifilar nucleus does not create three mirror gates by itself. It supplies a bidirectional magnetic Field/Void interface that each gate may use. The architecture remains:

```text
NEW views UP
    ^
Field/Void induced return
    ^
3 mirrored CENTER-referenced gates = one loop / one FLIP
    v
Field/Void controlled excitation
    v
OLD actions DOWN
```

Every gate remains an oscillating differential around CENTER/(0); old-down and new-up coexist.
