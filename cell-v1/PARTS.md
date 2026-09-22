# Cell V1 — Parts List (BOM)

Bill of materials for one complete analog hex cell with two-of-three coherence commit, magnetic dual-layer memory stack, and ternary actuator/bus interface. Derived directly from `THE_ANDROID_COMPLETE_BUILD_SPECIFICATION.md`.

---

## 1. ABC Side (Differential Pairs & Magnetic Drive)

| Part | Description | Qty | Est. Cost |
|:---|:---|:---:|:---:|
| **ALD1106** | Matched quad MOSFET (EPAD, subthreshold pair) | 3 | $15.00 |
| **500kΩ Resistors** | Tail current & bias setting | 6 | $0.60 |
| **150kΩ Resistors** | Load & reference pull | 3 | $0.30 |
| **100nF Capacitors** | Analog rail bypass / stabilization | 6 | $0.60 |
| **Ferrite Toroids** | Fair-Rite 2643000101 (or equiv), 1mm cut gap read head | 3 | $6.00 |
| **Winding Wire** | 30 AWG (50T drive) & 36 AWG (10T sense) | — | $8.00 |

---

## 2. Bus & Lattice Side (Shared Metabolic & Memory Layer)

| Part | Description | Qty | Est. Cost |
|:---|:---|:---:|:---:|
| **Permalloy Strip** | 80/20 foil, 10×5×0.1mm (high Hc personal trace) | 3 | $15.00 |
| **Lattice PCB** | Permalloy-plated copper trace on hex PCB (group trace) | 1 | $40.00 |
| **1µF Capacitors** | Bus reservoir & energy recovery | 3 | $0.60 |
| **BAT54 Schottky** | Low-drop steer & reinjection diodes | 6 | $3.00 |

---

## 3. Decision Logic (Two-of-Three Window, Gap, Sign)

### Option Standard (Active Window Comparators)
| Part | Description | Qty | Est. Cost |
|:---|:---|:---:|:---:|
| **LM339** | Quad comparator (window, gap, sign detection) | 4 | $4.00 |
| **Resistors (Ladder)** | Precision divider ladder for 1V lean bands & dead zones | 18 | $1.80 |
| **100nF Bypass** | Logic decoupling capacitors | 15 | $1.50 |
| **ALD110800** | Zero-threshold MOSFET switches | 3 | $12.00 |
| **74HC Logic** | Quad gates for PERMIT and INHIBIT gating | 4 | $1.20 |

### Option A (Toroid $H_c$ Substrate Threshold — No Comparators)
*Replaces active comparators and resistor ladder with intrinsic magnetic switching.*
- **Toroid Coercivity ($H_c$):** Acts as the hardware band-edge detector.
- **Pulse Injection:** $\mathrm{d}\Phi/\mathrm{d}t$ flip pulse sources directly into the passive diode-gated SUM node.
- **BOM Reduction:** Removes LM339 quad comparators, 18 ladder resistors, and 15 ladder bypass caps. Adds calibration winding turns.

---

## 4. Drive & Actuation (Phase Bridge & Motor Interface)

| Part | Description | Qty | Est. Cost |
|:---|:---|:---:|:---:|
| **ALD110900** | P-channel precision matched drive MOSFETs | 6 | $24.00 |
| **ALD110800** | N-channel precision matched drive MOSFETs | 6 | $24.00 |

---

## 5. Power & Reference

| Part | Description | Qty | Est. Cost |
|:---|:---|:---:|:---:|
| **Battery Pack + Reg** | Clean analog rail (V_TOP), live living bus (V_BUS) | 1 | $15.00 |

---

## 6. Prototyping & Interconnect

| Part | Description | Qty | Est. Cost |
|:---|:---|:---:|:---:|
| **Protoboard / Breadboard** | High-density prototype fixture | — | $10.00 |
| **Interconnect Headers & Wire** | 0.1" gold pin headers, Teflon hookup wire | — | $15.00 |

---

### Total Estimated BOM (One Cell): ~$220.00 (Standard) / ~$213.00 (Option A)
