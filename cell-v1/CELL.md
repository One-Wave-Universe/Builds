# CELL

## Canonical CELL_V1 lock

**1 volt normalized axis.** CENTER **0.50 / 50.** HOLD band **0.45–0.55 / 45–55.** Seven-band scale locked below.

The basic cell is a **hexagon containing six tapered triangular / pyramidal magnetic sectors**, clockwise **A+ B+ C+ A− B− C−**. Each sector carries one round winding. The six narrow sector tips converge on the local center region; the six broad sector bases are the six hex faces. Opposed sectors form the three mirrors **A+↔A−, B+↔B−, C+↔C−**. Within a cell the geometry is tip-to-tip through the center relation; neighboring cells tile **base-to-base** at matching hex faces.

Three leans. Ternary is **DOWN / HOLD / UP** around **− / (0) / +**. **CENTER / (0) is the shared active virtual-ground reference used to construct the physical ternary state; it is balanced/confirmed, not OFF.** The − and + states are signed differential leans away from that shared reference. **All analog. No global clock.**

## 2026-10-03 explicit analog magnetic architecture lock

This section makes the intended CELL_V1 physical architecture explicit and supersedes looser wording where it conflicts.

### Analog-only decision path
- CELL_V1's decision/control path is **physical analog hardware**. Digital logic, software, ADC interpretation, PWM computation, or a clocked controller must not become the mechanism that decides the cell state.
- Digital equipment may be used to **measure, log, simulate, or characterize** the bench system; it is not the decision element.

### Hysteretic transfluxor-class nucleus
- The local retained-state nucleus is a **one-piece two-aperture / figure-8 hysteretic magnetic core**, in the historical **transfluxor / multi-aperture magnetic-core mechanism class**.
- The two apertures share magnetic material/flux paths so prior magnetization can alter the response to later excitation.
- For the first flower: sensor nucleus = round two-aperture figure-8; motor/control nucleus = square two-aperture figure-8.
- This identifies the intended physical mechanism class; exact material, coercivity, dimensions, winding count and transfer function remain bench quantities.

### Two-toroid body-field pair: six windings on each toroid
Each cell has exactly **two plain round outer/body toroids total**, mirrored as FIELD and VOID body sides.

**Each outer toroid carries six independently exposed windings**, organized as three opposed differential channels:

```text
FIELD TOROID                         VOID TOROID
A+_F winding   A-_F winding          A+_V winding   A-_V winding
B+_F winding   B-_F winding          B+_V winding   B-_V winding
C+_F winding   C-_F winding          C+_V winding   C-_V winding

          three leans / three differentials on each mirrored body side
                 A+ <-> A-    B+ <-> B-    C+ <-> C-
```

Thus the paired body-field structure is **2 toroids x 6 windings = 12 independently exposed body-toroid windings** before any experimentally justified series/parallel interconnection.

The term **Helmholtz / opposed-field relation** in CELL documentation refers to this paired toroidal FIELD/VOID body-field arrangement. It must not be silently replaced by a conventional laboratory two-coil Helmholtz pair. Exact field uniformity, winding polarity, phase, coupling and whether the resulting field meets a formal Helmholtz condition remain measurement questions.

### Three leans are the three differentials
There is no separate computed lean:

```text
DA = A+ - A-
DB = B+ - B-
DC = C+ - C-
LEAN = {DA, DB, DC}
```

A/B/C operate concurrently as three mirrored analog differential axes. Their continuous magnitude may occupy the seven strength bands, but their primitive ternary sign is negative / balanced / positive.

### Balanced virtual ground is the ternary center
The physical ternary is constructed around the **shared active CENTER virtual-ground relation**:

```text
negative lean  <->  CENTER / BALANCED  <->  positive lean
      -                    (0)                    +
```

- **(0) means balanced differential, not OFF.**
- CENTER is the live/common balance reference seen by A/B/C; it is not V_BUS.
- Both opposed sides may remain electrically/magnetically active at (0).
- The signed state is the imbalance about that reference.
- The normalized 0.50/50 notation is a coordinate for balance, not proof that a fixed 0.50 V source must exist.

### Hysteresis is part of the state machine
Hysteresis is not an optional storage add-on. The intended analog loop uses retained magnetic history at the nucleus and local gates so the response to a present field depends on prior state. The connected under-cell hysteretic layer remains the slower body/muscle-memory path.

Canonical physical shorthand:

```text
three A/B/C differential leans
        <-> balanced CENTER ternary
        <-> paired FIELD/VOID six-winding toroids
        <-> hysteretic transfluxor-class nucleus
        <-> local analog threshold/gating/action
        <-> consequence + reinjection/body hysteresis
        <-> next analog state
```

### Anti-drift
- Do not reduce the body toroids to three windings each: **current lock is six independently exposed windings per toroid**.
- Do not call A/B/C three voltage levels: they are **three differential lean axes**.
- Do not call CENTER OFF: **CENTER/(0) is active balanced virtual ground and the ternary middle**.
- Do not replace the transfluxor-class nucleus with software memory or a digital state register.
- Do not use digital computation to close the cell's decision loop.
- Do not claim the paired toroids have demonstrated Helmholtz field quality, nucleus retention, coupling, torque, or useful computation until measured.


## Complete seven-cell / two-halves-per-cell target — opposing polarity / RC rotation

The **complete CELL_V1 flower target contains seven physical cells total**: **one center motor/control cell plus six surrounding sensor cells**.

**Every one of those seven cells is itself divided into two opposing polarity halves: FIELD and VOID.** Do not duplicate the flower into fourteen or thirteen cells. The two opposed halves belong **inside each cell**.

### Nucleus geometry
- **One center motor/control cell:** one planar one-piece **square two-aperture figure-8 transfluxor-class hysteretic nucleus**.
- **Six surrounding sensor cells:** each has one planar one-piece **round two-aperture figure-8 transfluxor-class hysteretic nucleus**.
- Total physical nuclei in the seven-cell flower: **7** — one square center nucleus + six round sensor nuclei.

### Two opposed halves per cell
Each physical cell carries its mirrored FIELD/VOID body structure:

```text
                    ONE PHYSICAL CELL
              hysteretic transfluxor nucleus
                         /       \
                        /         \
              FIELD HALF         VOID HALF
              polarity +         polarity -
              round toroid       round toroid
              6 windings         6 windings
                 \                 /
                  \-- A/B/C -----/
                    differentials
                         |
                 balanced CENTER
```

The FIELD and VOID halves use opposing polarity. Each half's toroidal structure targets six independently exposed windings arranged as the three mirrored differential relationships A+<->A-, B+<->B-, C+<->C-.

Thus **each cell** contains the paired/opposed toroidal field structure; the seven-cell flower is built from seven such two-sided cells.

### QC / RC opposed-rotation target
The target physical basis for **QC/RC** is the opposed rotational relationship generated by the **FIELD and VOID halves of each cell**, with those local opposed relationships coupled across the seven-cell flower.

This is not a second seven-cell flower. The counter-rotational target begins locally inside each two-sided cell and participates in the coupled flower-wide state.

### DC / AC / RC target mapping
- **DC / BC:** reinjection, body consequence, strain/loss return, refill/readiness.
- **TC / AC:** the live three-axis A/B/C differential ternary around balanced CENTER.
- **QC / RC:** the targeted opposed/counter-rotational FIELD/VOID relationship across the two halves of each cell and their coupled flower state.

### Reinjection bus + connected-cell muscle memory
All seven cells participate in the connected physical consequence loop:

```text
local two-half analog interaction
        -> action / physical consequence
        -> thresholded reinjection
        -> V_BUS energy return / readiness
        -> connected hysteretic lattice
        -> retained flower/body muscle-memory bias
        -> changed condition for the next analog interaction
```

Keep the physical roles separate:
- **V_BUS / reinjection:** recoverable energy and consequence.
- **CENTER:** active balanced virtual-ground ternary reference; CENTER != V_BUS.
- **transfluxor-class nucleus:** retained local cell history/state.
- **FIELD/VOID halves:** opposed-polarity local body-field / rotational target.
- **connected hysteretic lattice:** slower shared path/body/muscle memory across the seven cells.

### Target/evidence boundary
This is the **build target**. The opposed toroidal geometry, Helmholtz-style field behavior, counter-rotation, nucleus retention, inter-cell coupling, reinjection behavior and lattice muscle memory remain bench/falsification measurements until demonstrated.


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

### First-flower role-specific hardware build lock

The seven-cell flower requires **two distinct physical cell builds**, not one generic cell copied seven times.

#### Six surrounding sensor cells
- Each sensor cell receives its local physical sensor input(s) and resolves them through its A/B/C mirrored differential structure.
- **Nucleus:** one planar one-piece **round two-aperture figure-8 hysteretic core** for local retained sensor state/history.
- **Broad wedge/base faces:** the intercell interfaces. Each shared face uses a **bidirectional threshold-driven nerve gate/coupling path** so neighboring cells can influence and compare against one another without hard-shorting their local states together.
- **Narrow wedge tips:** remain intra-cell. The A/B/C tip relations **cross-reference one another bidirectionally** as part of the local three-differential resolution. They are **not dedicated wires to the main brain**.
- **Body reference/write:** the cell is biased/written by the shared connected-body state through the common body/lattice interface and hysteretic body-state layer. Higher layers therefore receive compressed consequence rather than individually commanding each triangle/wedge.
- The exact sensor technologies assigned to A/B/C are role/application dependent and remain open until selected and measured.

#### Center motor/control cell
- The center cell consumes the distributed state/consequence arriving from the six surrounding sensor cells through the same nerve-gated base-to-base interfaces.
- **Nucleus:** one planar one-piece **square two-aperture figure-8 hysteretic core** for retained motor/control state.
- Its A/B/C wedges are **control differentials**, not copies of the surrounding environmental sensor front ends.
- Its narrow tips use the same **bidirectional intra-cell cross-reference** rule as the sensor cells.
- Its broad bases use the same **bidirectional nerve-gated neighbor** rule so the center participates in distributed local comparison with the ring.
- The resolved local control lean drives a **separate actuator power stage**. Signal/comparison nerve gates are not assumed to carry actuator current.
- Actuator consequence returns into the same physical state/body/reinjection loop; no software or second controller bypasses this path.

Canonical first-flower information/power split:

```text
six SENSOR CELLS
physical sensing -> A/B/C local differential
                -> round figure-8 retained local state
                -> bidirectional nerve-gated shared faces
                              <->
                    CENTER MOTOR/CONTROL CELL
                    A/B/C control differential
                    <-> square figure-8 retained state
                    -> separate actuator power stage
                    -> actuator consequence
                    -> V_BUS/body-state return

within EACH cell:
A/B/C narrow tips <-> cross-reference bidirectionally
between CELLS:
broad bases <-> bidirectional nerve gates <-> broad bases
whole connected body:
shared body-state/hysteretic layer writes/biases local cells
```

**Anti-drift:** base-to-base is distributed peer-cell intelligence; tip-to-tip/cross-tip behavior is local intra-cell comparison. Do not reinterpret the tips as direct main-brain command/reference wires.


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

## 2026-09-27 architecture lock — differential flow, gate memory, loss correction, reinjection

This section supersedes older wording where it conflicts.

### Dynamic balance reference
- CENTER/(0) is the **current combined full-body-state balance reference** presented locally to A/B/C.
- It is not a separately meaningful fixed midpoint source and it is not V_BUS.
- The normalized 50 / 0.50 notation remains a **relative balanced coordinate** around the live body-state reference, not a requirement for an independently generated fixed 0.50 V rail.
- A/B/C remain electrically distinct while all compare against the same live body-state relation.
- Exact physical distribution/coupling that presents the shared body-state reference without collapsing A/B/C remains OPEN / BENCH.

### Wedge meaning
Each tapered sector is bidirectional hardware:
```
TIP <-> WEDGE <-> BASE
```
- **compression** = lean/transfer toward the narrow point;
- **expression** = lean/transfer toward the broad base;
- these words describe opposed differential tendency, not permanent current direction;
- both tip and base interfaces remain capable of bidirectional consequence transfer.

### Tip and base interfaces
- Inside the cell, opposed wedge tips converge tip-to-tip through the local center/mirror-gate region.
- Between cells, matching hex faces meet **flat base-to-flat base**.
- A base-to-base boundary is a shared inter-cell differential/coupling interface, not a one-way output/input.
- **Do not lock an extra MOSFET gate at every base-to-base boundary yet.** Whether the shared base interface itself supplies the required isolation/threshold behavior or requires a dedicated bidirectional gate is OPEN / BENCH.
- Local mirror/crossing connection points require bidirectional controlled conduction; back-to-back MOSFETs remain a candidate, not a selected part/topology.

### Gate-local hysteresis
Every active local mirror/loss gate requires its **own local hysteresis / retained transition history**.
- Purpose: prevent chatter, preserve prior lean/entry direction, and provide distinct enter/leave behavior around thresholds.
- This fast/local gate memory is distinct from the slower distributed body/muscle-memory hysteresis layer.
- Exact magnetic/electronic implementation, coercivity, retention time and coupling are OPEN / BENCH.

### Loss-threshold correction
The architecture does not intentionally drive harder into a loss excursion.
- When a live A/B/C differential crosses the selected loss threshold, the loss gate steers the recoverable excess/consequence into the local reinjection path.
- The return acts oppositely to the excursion and pushes the live ternary oscillation back toward the **current body-state balance**, not toward an unrelated fixed zero.
- Hysteresis determines enter/release behavior so the correction does not chatter.
- The physical target is:
```
difference -> useful action + remainder
remainder above threshold -> gated return
gated return -> oppose excursion -> settle toward live balance
```

### Reinjection / muscle-memory stack
Reinjection is part of the distributed physical learning loop, while energy accounting remains conservative.
The active loss-gate / reinjection structures sit **above and couple into** the shared hysteretic body-state layer:
```
TOP:      A/B/C wedges + local mirror gates
          gate-local hysteresis
          loss-threshold / ternary reinjection structures
                         <-> vertical magnetic/state coupling
UNDER:    shared hysteretic body-state / muscle-memory layer
POWER:    V_BUS / feed / recoverable-energy reservoir
```
The shared hysteretic layer retains path consequence. Reinjection revisits and can write/bias that physical substrate. V_BUS supplies/receives energy but is not itself the long-term memory.

Proposed recursive physical law:
```
current difference
 -> action
 -> thresholded remainder / loss consequence
 -> reinjection correction toward balance
 -> changed retained hysteretic path
 -> bias on next difference
```

### Artery / vein functional naming
These are functional names, not claims about a finalized schematic:
- **artery/feed** = energy made available from the local/shared reservoir into the active cell loop;
- **vein/return** = threshold-steered recoverable remainder/consequence returning through the local reinjection path;
- the return must interact with the retained hysteretic path before/while rejoining the continuing energy loop so prior use can influence later traversal.

### Required falsification measurements
Measure rather than assume:
1. gate-local hysteresis and separate enter/release thresholds;
2. thresholded return opposing both + and - excursions;
3. settling relative to a moving body-state reference;
4. retained body-layer state before/after repeated reinjection;
5. whether repeated traversal changes required input/loss for the same physical action;
6. V_BUS energy in/returned and actual dissipative loss;
7. base-to-base transfer with and without an additional dedicated boundary gate.
