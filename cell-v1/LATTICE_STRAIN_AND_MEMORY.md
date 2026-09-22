# The Lattice: Muscle Memory, Distributed Intelligence, and Strain Signal

The lattice is the full body state. It is not an abstract communication bus or a memory buffer. It is a single continuous magnetic medium (permalloy on hex PCB) that carries three functions simultaneously without dedicated supervisory hardware.

---

## 1. The Cross-Mirror Mapping: Toroid (FIELD) ↔ Lattice (VOID)

The architecture maps directly to the primary cross-mirror axis:

$$\text{Toroid (FIELD)} \iff \text{Lattice (VOID)}$$

| Dimension | Toroid (FIELD) | Lattice (VOID) |
|:---|:---|:---|
| **Scope** | Per-cell, local | Body-level, shared collective |
| **State Nature** | Active, discrete flips ($B_r^+$ or $B_r^-$) | Continuous, graded potential across the mesh |
| **Role** | Expressed state (what the cell is doing now) | Potential band (the space of what can be expressed) |
| **Trace** | The cell's personal vocabulary & habits | The body's accumulated history & groove |
| **Coupling** | **FIELD $\rightarrow$ VOID:** Flip writes into the lattice | **VOID $\rightarrow$ FIELD:** Pattern biases next cell flip |

---

## 2. The Three Functions in One Metal

```
                  ┌─────────────────────────────────────┐
                  │          THE HEX LATTICE            │
                  │     (Single Continuous Metal)       │
                  └──────────────────┬──────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
  1. MUSCLE MEMORY         2. DISTRIBUTED INTEL           3. STRAIN SIGNAL
  Physical remanence       Non-local collective           Load & saturation
  pattern in permalloy;    read/write coordination;       reporting; emergent
  deepens with usage       no central polling or clock    load-shedding (send-up)
```

### 1. Muscle Memory
- Remanent magnetic domain orientation in the metal.
- Deepens with repeated consensus writes; fades with disuse or thermal relaxation.
- Encodes physical habits, motor timing, and coordination grooves.

### 2. Distributed Intelligence
- All cells write to and read from the exact same shared physical sheet.
- Local decisions at cell 1 perturb the magnetic boundary condition at cell 7.
- Coordination emerges organically without a CPU, arbitration bus, or global clock.

### 3. Strain Signal
Strain is the physical limit of the substrate:
- **Flux Saturation:** As a node approaches maximum saturation ($B_{\text{sat}}$), differential permeability ($d\Phi/dB$) flattens. Subsequent writes cannot deepen the trace.
- **Bus Sag ($V_{\text{BUS}}$):** Heavy drive loads drop the under-rail, reducing inductive collapse efficiency.
- **Thermal Shift:** Sustained high-frequency cycling lowers effective $H_c$, shifting the threshold band.

---

## 3. Emergent Load-Shedding (Send-Up)

Strain is not an arbitrary rule evaluated by software; it is a physical condition that attenuates the cell's drive capability:

- **Low Strain:** Wide permeability, high $V_{\text{BUS}} \rightarrow$ Free to `PUSH` / `FLIP`.
- **Medium Strain:** Moderate permeability, slight sag $\rightarrow$ `PULL` only (consolidate inward).
- **High Strain:** Approaching saturation $\rightarrow$ `PASS` (coast, zero injection).
- **Critical Strain:** Saturation limit / extreme sag $\rightarrow$ **Send-up** (quiescent hold, allow lattice relaxation).

---

## 4. The Unified View Matrix (Memory + Strain)

Each view up through the figure-8 read head extracts both memory pattern and physical strain simultaneously:

| View | Memory Read | Strain Read |
|:---|:---|:---|
| **BASELINE** | Resting pattern at local node | Quiescent baseline magnetic load |
| **DELTA** | Change since last event | Excursion rate of strain / load spike |
| **HEADING** | Trajectory of pattern development | Trend toward or away from saturation |
| **RESULT** | Committed remanence state | Residual locked load on the mesh |

One substrate. One law. Three jobs in the same metal.
