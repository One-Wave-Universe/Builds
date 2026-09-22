# Grant Proposal — Build Plan: Option A (Native Magnetic Substrate Gating)

## Executive Summary
Option A replaces active operational/comparator stages with intrinsic material properties: the coercivity ($H_c$) of square-loop ferrite toroids defines the decision band edges directly.

---

## 1. Elimination of Active Threshold Stages
Conventional analog and neuromorphic systems rely on multi-stage comparator ladders and reference voltage dividers that force artificial symmetry and consume quiescent power. Option A utilizes the non-linear B-H magnetization curve:
- Threshold trip is an instantaneous physical domain flip ($d\Phi/dt$).
- Eliminates 4 LM339 comparators, 18 ladder resistors, and 15 decoupling capacitors per cell.
- Reduces component count, board real estate, and traces on the analog layer.

---

## 2. Substrate Physics as Logic
1. **Coercivity as Band Edge:** The threshold voltage is parameterized strictly by turns ratio and magnetic path length:
   $$V_{\text{threshold}} = \frac{H_c \cdot l_{\text{path}}}{N \cdot G_{\text{sense}}}$$
2. **Current-Pulse SUM Node:** Flipping cores directly source current into a passive summing junction.
3. **Diode-Gated PERMIT:** A single forward diode drop validates the two-of-three consensus condition before unlocking the output drive bridge.

---

## 3. The Tri-Functional Lattice (Memory, Distributed Intelligence, Strain)
The lattice provides three functions simultaneously within one continuous magnetic medium:
1. **Muscle Memory:** The accumulated remanent magnetization pattern ($B_r$).
2. **Distributed Intelligence:** Multi-cell non-local coordination via inductive figure-8 read heads without central polling.
3. **Intrinsic Strain Sensing:** Load and fatigue reporting through saturation proximity, bus sag, and differential permeability flattening. Enables emergent load shedding (send-up) rather than programmed software throttling.

---

## 4. Milestone Phasing
- **Phase I (Bench Calibration):** Validate $H_c$ flip reproducibility, pulse amplitude/duration, and energy recovery on a single axis using passive diode gating.
- **Phase II (Two-Toroid Multi-Band):** Introduce dual-coercivity or bias-wound cores to reintroduce fine-grained `GAP` / walking-third hardware inhibition without restoring semiconductor comparators.
