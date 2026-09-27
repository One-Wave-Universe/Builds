# CELL

## Canonical CELL_V1 lock

**1 volt normalized axis.** CENTER **0.50 / 50.** HOLD band **0.45–0.55 / 45–55.** Seven-band scale locked below.

Letters **are the six edges:** A+ B+ C+ A− B− C−. Flowers share sides. Opposed edges form three mirrored axes.

Three leans. Ternary is **DOWN / HOLD / UP** around **− / (0) / +**. **All analog. No global clock.**

## Cell-role geometry map

CELL_V1 uses one **common outer/body differential interface** across cell types, while the **nucleus geometry changes by role**.

### Common body differential interface — all cells
- **Outer/body pair:** two **plain round toroids**.
- This pair is shared across sensor, motor-control, M4, five-mind, and six-mind cells.
- Purpose: preserve one common physical differential / body-state / lattice connection language so mixed cell types can connect directly without adapter geometries.
- The common round toroids are **not figure-8 toroids**.
- Nucleus geometry is the specialization layer inside that common body interface.

### Sensor cell
- **Nucleus:** one planar **round figure-8 toroid**.
- Purpose: simplest local binary / differential sensing brain.
- This is the figure-8 role currently retained for the sensor cell.

### Motor-control cell
- **Nucleus:** one planar **square figure-8 toroid**.
- Purpose: motor-control brain with clean grid / lattice alignment and connection.
- Do not generalize this square nucleus to the sensor cell or M4 cell.

### M4 cell
- **Nucleus:** **two triangular toroidal loops base-to-base** — the planar double-triangle / pyramid nucleus.
- **Outer/body pair:** the same two **plain round toroids** used by every other cell type.
- The existing mirrored 3+3 winding / motor-field concept may be mapped onto the common round-toroid pair, subject to bench validation.

### Five-mind cell
- **Nucleus:** **double pentagon** toroidal geometry.

### Six-mind cell
- **Nucleus:** **double hexagon** toroidal geometry.

### Dimensional rule
The present core / winding hardware is **2D / planar**. The resulting magnetic field is inherently **3D** and must be simulated and measured as such.

## Shared electrical / state-machine rules

Across these cell roles:
- the **two plain round outer/body toroids remain common** so every cell type speaks the same body differential / interconnect geometry;
- A+↔A−, B+↔B−, C+↔C− remain three mirrored spatial axes / edge-seat pairs where that interface is used.
- DOWN / HOLD / UP remain the local ternary around CENTER.
- Threshold crossings, hysteresis, retained state, bus condition, and neighbor state drive transitions.
- V_BUS remains the shared energy / readiness / reinjection rail.
- CENTER remains the local lean reference and is not V_BUS.
- No global clock.
- No second controller bypasses the local physical decision path.
- Geometry does not by itself prove retention, computation, torque, or coupling performance.

## Unified role-aware loop

```text
sensor / neighbor consequence
        ↓
role-specific nucleus
(round figure-8 sensor
 square figure-8 motor-control
 double-triangle M4
 double-pentagon five-mind
 double-hexagon six-mind)
        ↓
local differential / threshold resolution
        ↓
DOWN / HOLD / UP where applicable
        ↓
role-specific field / actuator coupling
        ↓
collapse / inductive return
        ↓
V_BUS reinjection + lattice consequence
        ↓
next physical decision
```

## Locked seven-band differential scale

Normalize each axis to a 0–100 differential magnitude scale around CENTER = 50.

| Band | State | Gate depth |
| --- | --- | --- |
| 100–90 | +3 | EXTREME EXPRESSION / DANGER |
| 85–75 | +2 | STRONG EXPRESSION |
| 70–60 | +1 | MODERATE EXPRESSION |
| 55–45 | 0 | ACTIVE MIDDLE / STABLE OSCILLATING REGION |
| 40–30 | −1 | MODERATE COMPRESSION |
| 25–15 | −2 | STRONG COMPRESSION |
| 10–0 | −3 | EXTREME COMPRESSION / DANGER |

The unassigned 5-point windows are hysteresis / transition gaps:

- 90–85
- 75–70
- 60–55
- 45–40
- 30–25
- 15–10

These gaps are intentional anti-chatter regions. They are not extra logical states. Entry and exit direction through a gap depend on the prior settled state / hysteresis history.

Locked band meaning:

```
+3 = EXTREME EXPRESSION / DANGER
+2 = STRONG EXPRESSION
+1 = MODERATE EXPRESSION
 0 = ACTIVE MIDDLE / STABLE OSCILLATING REGION
-1 = MODERATE COMPRESSION
-2 = STRONG COMPRESSION
-3 = EXTREME COMPRESSION / DANGER
```

The ±3 edge bands are terminal / protection boundaries for a domain-specific reset, release, clamp, or failure response. They are not ordinary CHOICE/PIVOT/FLIP operating steps.

A/B/C each use this same seven-band scale. A/B/C remain three spatial differential axes around the nucleus; the seven bands are the voltage / magnitude states on each axis.

## Axis / gate / scale law

Keep three different things separate:

1. **Axis:** A, B, C = three mirrored spatial differentials around the nucleus.
2. **Expression/compression strength:** the seven voltage bands say how far the live differential has leaned from CENTER, from moderate through strong to extreme. CHOICE/PIVOT/FLIP remain separate control functions and are not aliases for ±1/±2/±3.
3. **Scale:** POINT → PATH → FIELD = larger coupled organization. Scale promotion is not the same thing as moving from A to B to C.

A live differential may oscillate / circulate around CENTER while carrying a net lean. HOLD means the opposed sides remain active but balanced closely enough that no directional commit is permitted. Crossing a voltage band changes gate depth; it does not rename the active axis.

Next view = last move + what came back up.

Two agrees → push.  
One voice → wait.  
Opposition → HOLD.  
Drive off → return energy to V_BUS.

HOLD is live readiness around center, not a clocked idle.

## Hard anti-drift rules

- **Sensor nucleus = round figure-8 toroid.**
- **Motor-control nucleus = square figure-8 toroid for grid/lattice connection.**
- **M4 nucleus = two triangular toroidal loops base-to-base.**
- **Every cell type uses the same two plain round outer/body toroids.**
- **The common outer/body pair is not figure-8.**
- Nucleus geometry changes by cell role; outer/body differential geometry does not.
- **Five-mind nucleus = double pentagon.**
- **Six-mind nucleus = double hexagon.**
- Current core hardware geometry is planar / 2D; magnetic fields are 3D.
- Any mirrored 3+3 winding mapping on the M4 outer pair remains a bench-tested implementation detail.
- A/B/C are axes, **not voltage levels**.
- The seven voltage bands are EXPRESS ↔ COMPRESS strength bands, not CHOICE/PIVOT/FLIP.
- POINT/PATH/FIELD are scale states and must not be collapsed into A/B/C.
- CENTER ≠ V_BUS.
- No global clock or timing-based commutation.
- No second controller that bypasses the cell's ternary decision.
- Reinjection must re-enter the same state loop.
- Do not claim measured retention, coupling, recovery, torque, or efficiency until bench data exists.

This file is the CELL_V1 authority. Detail files must agree with it.
