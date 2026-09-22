# Option A — Toroid Coercivity ($H_c$) as the Threshold

Fixed physical thresholds. No external comparators. No reference ladder. The magnetic core's coercivity ($H_c$) is the band edge.

---

## 1. What Goes Away

Per axis:
- **LM339 Quad Comparator (or equiv):** Removed.
- **Reference Ladder Resistors (18):** Removed.
- **Bypass Capacitors for Ladder (15):** Removed.
- **74HC Logic Gates for Window/Sign:** Simplified or replaced with passive diode-gated current summing.

**Net Result:** Complete removal of active semiconductor comparator stages in favor of native substrate physics.

---

## 2. Operating Principle

The toroid has intrinsic coercivity $H_c$. When the accumulated magneto-motive force (MMF) from the sense winding crosses $H_c$, the magnetic domain flips. The flip causes a rapid flux excursion ($d\Phi/dt$) that induces a voltage pulse in the winding:

$$\mathrm{MMF} = N \times I$$
$$I = \frac{V_d}{R_{\text{sense}}}$$
$$H_c \cdot l_{\text{path}} = N \cdot I_{\text{threshold}}$$

- **No pulse:** Below threshold $\rightarrow$ `HOLD` or `GAP`.
- **Positive pulse:** `IN`, positive polarity.
- **Negative pulse:** `IN`, negative polarity.

The core is inherently self-detecting.

---

## 3. Threshold Calibration & Walking Third

1. **Winding Count Calibration:**
   $$V_{\text{threshold}} = \frac{H_c \cdot l_{\text{path}}}{N \cdot G_{\text{sense}}}$$
   $N$ is the calibration knob. Setting turns sets the voltage threshold without trim pots.

2. **Phase I Implementation (Option A2):**
   - Single toroid per direction flips at the $0.10\,\text{V}$ band edge (`IN`).
   - Below $0.10\,\text{V}$ is treated as uncommitted.
   - Walking third conflicts resolve iteratively on the subsequent event.
   - Optional bias winding can dynamically shift effective $H_c$ if tunability is required.

---

## 4. Two-of-Three Passive Current Sum

1. Each toroid flip injects a current pulse into the passive `SUM` node.
2. The three axes contribute up to 6 directional pulses.
3. A single forward diode drop on the `SUM` node gates the `PERMIT` condition.
4. One diode serves as the entire threshold decision gate.
