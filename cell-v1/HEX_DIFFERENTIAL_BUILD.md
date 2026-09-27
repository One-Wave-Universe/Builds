# HEX_DIFFERENTIAL_BUILD — wiring-level prototype

## Purpose

This file defines an actual first hardware build for the CELL hex differential. It is not a geometry-only description.

The prototype separates four things so each can be measured:
1. six wound magnetic sectors;
2. three opposed differential branches;
3. three bidirectional center switches;
4. one shared active midpoint reference.

## H0 — build one differential before duplicating three times

Build A first. Once A passes, rotate/copy it twice for B and C.

### A differential electrical path

```text
A+ OUTER TERMINAL
      |
   L_A+  wound tapered magnetic sector
      |
   A+ INNER
      |
 D -- Q_A1 -- S
             |
             S -- Q_A2 -- D
      |      back-to-back N-MOSFET pair
      |
   A-CENTER node
      |
      +---- R_A0 ---- CENTER_BUS
      |
 D -- Q_A3 -- S
             |
             S -- Q_A4 -- D
      |      back-to-back N-MOSFET pair
      |
   A- INNER
      |
   L_A-  wound opposed tapered magnetic sector
      |
A- OUTER TERMINAL
```

This gives A two independently measurable half-differentials around the same CENTER reference instead of shorting the two coils together.

Duplicate exactly for B and C:
- B+ / B− -> B-CENTER -> CENTER_BUS
- C+ / C− -> C-CENTER -> CENTER_BUS

The six outer terminals are the six hex faces.

## H1 — six magnetic sectors

Fabricate six identical tapered magnetic pieces arranged at 60-degree intervals in a true hexagonal carrier.

For the first prototype the carrier is nonmagnetic and nonconductive. Each magnetic sector has:
- broad outer base at one hex face;
- narrow inner tip facing the center gap;
- one removable round coil wound around the sector;
- two coil leads brought to screw/header terminals;
- no permanent electrical bond between magnetic core and CENTER_BUS.

Clockwise identity:
A+, B+, C+, A−, B−, C−.

Opposed magnetic axes:
A+ <-> A−
B+ <-> B−
C+ <-> C−.

Start with an intentional center air gap. Do not physically fuse all six magnetic tips into one core in H0; the gap makes cross-axis coupling measurable and adjustable.

## H2 — winding construction

All six coils must initially be identical:
- same wire gauge;
- same turn count;
- same winding length;
- same winding direction relative to marked outer-base -> inner-tip core direction.

Mark every winding START with a dot. Bring START and FINISH out separately. Do not series-connect coils permanently.

Before installing gates, measure and record for each coil:
- DC resistance;
- inductance if meter/LCR is available;
- induced-voltage polarity using a low-energy pulse in an opposed coil.

Acceptance: no winding is accepted as "identical" until its resistance and induced polarity are recorded.

## H3 — CENTER_BUS

CENTER_BUS is the shared active midpoint reference for A, B and C.

For a 5 V bench supply, begin characterization at 2.5 V. A 10 kOhm / 10 kOhm divider may establish the unloaded reference for signal-only tests, with a capacitor from midpoint to supply return. It is NOT the final current-carrying center because a passive divider has substantial output impedance.

Do not send coil current through a weak divider. During coil/gate power tests use a midpoint source/sink stage or a true split supply capable of the measured center current.

CELL normalized reporting can map the physical midpoint to CENTER=0.50 after measurement; do not confuse the normalized 0-1 representation with MOSFET gate-drive voltage.

## H4 — bidirectional differential gates

Use back-to-back MOSFETs when an OFF branch must block both current polarities. A single ordinary MOSFET does not do that because of its body diode.

For H0, use common-source back-to-back N-MOSFET pairs and expose:
- both drains;
- common-source node;
- common gate node;
- gate-source test points.

Do not select a MOSFET merely because VGS(th) is low. Select only after deciding the available discrete gate-drive amplitude and required coil current.

The no-IC CELL decision constraint remains: any final threshold/gate control must be discrete analog/magnetic. Bench supplies and instruments may be used to characterize the power path.

## H5 — true hex wiring

```text
                    [ A+ OUT ]
                       L_A+
                         |
                   gate A+ half
                         |
                       A0
                         |
                       R_A0
                         |
[C- OUT]-L_C-...C0--R_C0-+--R_B0--B0...L_B+--[B+ OUT]
                         |
                    CENTER_BUS
                         |
[B- OUT]-L_B-...B0--R_B0-+--R_C0--C0...L_C+--[C+ OUT]
                         |
                       R_A0
                         |
                       A0
                         |
                   gate A- half
                         |
                       L_A-
                    [ A- OUT ]
```

Physical placement is 60 degrees around the carrier even though the ASCII wiring is flattened.

The three branch center nodes A0/B0/C0 remain separate. They meet only through their defined CENTER coupling elements; they are not one copper blob.

## H6 — base-to-base flower connector

Each OUTER terminal is paired with its broad magnetic face. Neighboring cells attach at the matching hex face with a removable electrical jumper and a controlled magnetic/mechanical spacing fixture.

This makes base-to-base coupling an experiment:
- electrical only;
- magnetic only;
- electrical + magnetic;
- disconnected control.

## H7 — first measurements

### Test 1: one coil
Drive A+ with a current-limited low-energy source. Record I, V, field/induced response and temperature.

### Test 2: A opposed pair
Drive A+ and measure A− induced response with gates open, then closed. Reverse polarity. Repeat from A− to A+.

### Test 3: center loading
Measure CENTER_BUS movement while A transfers current in both directions. If CENTER moves outside the intended hold band under expected current, strengthen the midpoint source/sink stage before adding B/C.

### Test 4: cross-axis matrix
Excite each of six windings one at a time and record induced voltage on the other five. This produces a 6x6 coupling matrix. It tells us what the physical hex actually does.

### Test 5: three mirrors
Install B and C. Repeat the matrix and then excite A/B/C with controlled phase relations. Scope all three center nodes and CENTER_BUS.

### Test 6: base-to-base
Add one neighboring passive hex or one matching sector fixture. Compare disconnected, electrical-only, magnetic-only and combined coupling.

## H8 — pass/fail for HEX_V1

HEX_V1 passes its first stage when:
- all six windings have known polarity and comparable electrical properties;
- each opposed pair transfers a reversible measurable response;
- each back-to-back gate conducts both polarities ON and blocks both polarities OFF over the tested range;
- A0/B0/C0 remain distinguishable while sharing CENTER_BUS;
- CENTER_BUS can source/sink the measured imbalance without collapsing;
- the 6x6 coupling matrix is repeatable;
- base-to-base coupling produces a repeatable change relative to the disconnected control.

Only after these pass do we map the measured three-mirror behavior onto the full one-loop/one-FLIP CELL semantics.

## Existing engineering precedents used

- Three windings at 120 degrees and differential terminal relationships: synchro/stator precedent.
- Back-to-back MOSFETs: standard bidirectional/four-quadrant switch topology.
- Midrail reference: standard split-supply / rail-splitter practice; passive divider only for light signal loading.

The novel part is the integration of six tapered wound sectors, three opposed mirrors, shared active CENTER, lattice face coupling and the CELL state semantics. That integration is what HEX_V1 is designed to measure.
