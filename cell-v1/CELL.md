# CELL

## Canonical CELL_V1 lock

**1 volt normalized axis.** CENTER **0.50 / 50.** HOLD band **0.45–0.55 / 45–55.** Seven-band scale locked below.

The basic cell is a **hexagon containing six tapered triangular / pyramidal magnetic sectors**, clockwise **A+ B+ C+ A− B− C−**. Each sector carries one round winding. The six narrow sector tips converge on the local center region; the six broad sector bases are the six hex faces. Opposed sectors form the three mirrors **A+↔A−, B+↔B−, C+↔C−**. Within a cell the geometry is tip-to-tip through the center relation; neighboring cells tile **base-to-base** at matching hex faces.

Three leans. Ternary is **DOWN / HOLD / UP** around **− / (0) / +**. **CENTER / (0) is the shared active virtual-ground reference used to construct the physical ternary state; it is balanced/confirmed, not OFF.** The − and + states are signed differential leans away from that shared reference. **All analog. No global clock.**

## Cell-role geometry map

CELL_V1 uses one **common outer/body differential interface** across cell types, while the **nucleus geometry changes by role**.

### Common body differential interface — all cells
- **Outer/body pair:** two **plain round toroids**.
- This pair is shared across sensor, motor-control, five-mind, and six-mind cells.
- Purpose: preserve one common physical differential / body-state / lattice connection language so mixed cell types can connect directly without adapter geometries.
- The common round toroids are **not figure-8 toroids**.
- Nucleus geometry is the specialization layer inside that common body interface.

### Sensor cell
- **Nucleus:** one planar **one-piece round two-aperture figure-8 hysteretic magnetic core**.
- Purpose: local sensor-state/history element using the same shared-flux-path / two-aperture mechanism class as the motor nucleus, with round geometry for the sensor role.
- In the first flower, six of these sensor cells surround one motor/control cell.

### Motor-control cell
- **Nucleus:** one planar **one-piece square two-aperture figure-8 hysteretic magnetic core**.
- Purpose: motor-control brain with clean grid / lattice alignment and connection.
- Do not generalize this square nucleus to the sensor cell or M4 cell.

### M4 routing layer
M4 is **not a separate nucleus or cell role**.

M4 is the six-pyramid routing/connection geometry:
- the six tapered wedge sectors route A+/B+/C+/A-/B-/C-;
- opposed wedges meet **tip-to-tip inside the same cell**;
- wedge bases meet **base-to-base between neighboring cells**;
- this routing layer carries the physical consequence/state coupling from one cell into the next while local differential resolution remains referenced around CENTER.

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
- CENTER / (0) is the shared active virtual-ground reference for the physical ternary − / (0) / +; (0) means balanced/confirmed rather than OFF.
- No global clock.
- No second controller bypasses the local physical decision path.
- Geometry does not by itself prove retention, computation, torque, or coupling performance.

## Connected-cell hysteretic body-state layer

Connected cells sit over a dedicated hysteretic magnetic layer that carries **body state / muscle memory** across the lattice.

- local nucleus = local retained state;
- hysteretic under-cell layer = connected-body / path / muscle memory;
- V_BUS = returned energy / readiness;
- CENTER = local differential reference.

The hysteretic layer follows shared cell edges / lattice routes and is physically separate from V_BUS and CENTER.

Repeated use may bias the shared path so the next action encounters a changed physical substrate rather than starting from zero.

For the first flower, the target is one continuous or magnetically coupled hysteretic layer beneath the center motor cell and six sensor cells.

Exact material, thickness, patterning, coercivity, and coupling are open until measured.

### Phase-I body-memory scale

For the first wheel / propeller-style motor work, the connected cells use **one shared domain-wall hysteretic body-state layer**.

Nested hysteretic layers are not part of Phase I.

They are reserved for later articulated movement where separate local and larger-scale motor habits must coexist, such as finger -> hand -> limb -> body.

Add another layer only when:
- the movement requires a separate physical memory scale; or
- measured cross-coupling shows one layer cannot preserve independent motor habits.

## Unified role-aware loop

```text
sensor / neighbor consequence
        ↓
role-specific nucleus
(one-piece round two-aperture figure-8 sensor
 one-piece square two-aperture figure-8 motor-control
 M4 pyramid routing through the six wedges
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

## Six-sector / three-mirror physical build — current prototype lock

The hex differential is a magnetic/electrical structure, not a flat six-trace diagram.

- **6 tapered triangular/pyramidal magnetic sectors:** A+, B+, C+, A−, B−, C−.
- **6 round windings:** one winding on/around each magnetic sector; bring both leads of every winding out for polarity and coupling tests.
- **3 opposed mirrors:** A+↔A−, B+↔B−, C+↔C−.
- **Tip-to-tip local relation:** opposed tapered cores point toward the center region.
- **Base-to-base lattice relation:** broad magnetic/structural faces align with neighboring hex-cell faces when cells tile into a flower.
- **Shared virtual-ground bus:** all three differential center branches reference the same active CENTER/(0) virtual-ground bus. This is the electrical ternary reference; it does not require the six magnetic tips to be electrically shorted together.
- **Bidirectional center gate per differential:** A, B and C each get an independently gated bidirectional branch at the differential center. The discrete implementation target is a back-to-back MOSFET pair (or measured equivalent) per differential so the branch can control current in both directions without relying on a single MOSFET body diode.
- **Keep A/B/C distinct:** the three gated differential branches share the CENTER reference but are not hard-shorted into one signal path.

Prototype topology shorthand:

```text
A+ core/winding <-> [A bidirectional center gate] <-> A- core/winding
                                  |
B+ core/winding <-> [B bidirectional center gate] <-> B- core/winding
                                  |
C+ core/winding <-> [C bidirectional center gate] <-> C- core/winding
                                  |
                         shared CENTER/(0)
                       active virtual-ground bus
```

This is the current physical candidate for mapping the **three A/B/C mirrors** into the three-mirror loop. The first bench build must expose every winding and gate node so winding sense, cross-coupling, CENTER stability and the one-loop/one-FLIP mapping can be measured rather than hidden in the assembly.

### First-flower geometry

The first seven-cell flower is:
- **center:** one motor/control cell with the one-piece square two-aperture figure-8 hysteretic nucleus;
- **ring:** six local sensor cells, each with a one-piece round two-aperture figure-8 hysteretic nucleus;
- **intercell connection:** matching hex faces meet base-to-base while each cell retains its own six-sector / three-mirror local differential geometry;
- **M4 routing:** the pyramid connection network is already part of the first flower because it is how the cells route into one another.


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

- **Sensor nucleus = one-piece round two-aperture figure-8 hysteretic magnetic core.**
- **Motor-control nucleus = one-piece square two-aperture figure-8 hysteretic magnetic core for grid/lattice connection.**
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


## Three-mirror-gate oscillating loop — locked

A complete local state transition is **three mirrored gates = one complete loop = one FLIP**.

At **every gate**, the physical signal remains a **bidirectional oscillation around CENTER/(0)**. CENTER is the reference at each step; it is not visited only at the beginning or end.

During the same loop:

- the **old state expresses ACTIONS DOWN**;
- the **new state returns VIEWS UP**;
- both directions coexist as opposed wave information around CENTER;
- each mirror gate compares/couples the two directions physically;
- completion of the third mirror gate permits one FLIP;
- the settled new state becomes the old/action side of the next loop while the next views are already propagating upward.

This is not a sequential read-old / erase / calculate / write-new machine.

Canonical shorthand:

```text
NEW VIEWS UP  ↑
              │
       MIRROR GATE 3
              ↕  CENTER/(0)
       MIRROR GATE 2
              ↕  CENTER/(0)
       MIRROR GATE 1
              │
OLD ACTIONS DOWN ↓

3 mirror gates = 1 loop = 1 flip
```

The nerve/interconnect implementation target is a **bidirectional wave gate** built from discrete MOSFET/passive/magnetic elements. The normalized CELL electrical span remains **1 V or less** around its CENTER reference. Exact MOSFET technology, gate topology, usable VGS, on-resistance and threshold margin are **not locked** until a real device is selected and measured; MOSFET datasheet threshold voltage alone must not be treated as a guaranteed low-resistance ON voltage.


## Motor nucleus retained-history interaction — reference-anchored

The motor nucleus is a **single continuous magnetic piece with two square apertures**, not two joined square cores. Its nearest established mechanism class is the historical **transfluxor / multi-aperture hysteretic magnetic core**: multiple apertures form distinct flux paths that share portions of the same magnetic body, and a prior magnetic setting changes the response to later excitation.

CELL uses that established history dependence as the physical candidate for:

```text
OLD retained state + NEW incoming excitation -> shared magnetic transition -> NEXT retained state
```

This supports the *mechanism class* for simultaneous old-history/new-drive interaction. It does not establish CELL's semantic mapping. The four views, four actions, ternary CENTER, three mirror gates and one-FLIP recursion remain CELL-specific hypotheses requiring bench validation.


## Literal wedge-to-toroid wiring target

This is the current bench wiring target.

### Geometry lock

Inside one cell:

```text
A+ tip <-> tip A-
B+ tip <-> tip B-
C+ tip <-> tip C-
```

Between neighboring cells:

```text
cell N wedge BASE <-> BASE neighboring-cell wedge
```

Hard rule:
- tip-to-tip = intra-cell differential geometry;
- base-to-base = inter-cell lattice connection.

### FIELD / VOID body sides

FIELD and VOID are the two mirrored sides of the body architecture.

Each cell couples into both sides through **exactly two plain round toroids total**:

```text
FIELD BODY SIDE                 VOID BODY SIDE
      |                              |
 FIELD round toroid             VOID round toroid
  TA_F TB_F TC_F                TA_V TB_V TC_V
      \   |   /                    \   |   /
       local A/B/C differential cell
```

Each toroid carries three separate coupling windings, one for A, one for B, and one for C.

Do not electrically short A/B/C together on either toroid.

### Wedge winding exposure

Each of the six wedge windings is brought out independently:

```text
WA+_1 WA+_2
WB+_1 WB+_2
WC+_1 WC+_2
WA-_1 WA-_2
WB-_1 WB-_2
WC-_1 WC-_2
```

The two body toroids are also fully exposed:

```text
FIELD toroid:
TA_F1 TA_F2
TB_F1 TB_F2
TC_F1 TC_F2

VOID toroid:
TA_V1 TA_V2
TB_V1 TB_V2
TC_V1 TC_V2
```

No permanent series/parallel connection is locked until winding sense, coupling, phase, and CENTER behavior are measured.

### CENTER rule

A/B/C remain three separate mirrored differentials, but all three must reference the same active CENTER relation at every mirror step.

```text
A differential <-> CENTER
B differential <-> CENTER
C differential <-> CENTER
```

CENTER is not V_BUS and is not the main winding-current return.

The exact winding/coupling geometry that makes the two body toroids participate in one balanced CENTER relation remains a bench question.

### Mirrored body-side power

Both FIELD and VOID receive energy and return consequence:

```text
V_BUS -> FIELD side -> local event -> FIELD return -> V_BUS
V_BUS -> VOID side  -> local event -> VOID return  -> V_BUS
```

Neither side is permanently input-only or return-only.
