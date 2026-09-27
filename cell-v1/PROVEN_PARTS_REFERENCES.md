# CELL_V1 — evidence / reference map

This file references **established mechanisms**, not proof of the integrated CELL_V1 architecture. CELL-specific geometry, coupling, thresholds, memory behavior, and the complete recursive loop remain experimental until measured.

## R1 — Resolver: orthogonal magnetic information channels
Analog Devices, *Precision Resolver-to-Digital Converter Measures Angular Position and Velocity*.
https://www.analog.com/en/analog-dialogue/articles/precision-rtdc-measures-angular-position-and-velocity.html

Established mechanism used here: a resolver is a variable-coupling transformer; two differential secondary signals carry sine/cosine information about magnetic/mechanical angle. CELL_V1 uses this only as precedent for continuous analog magnetic direction/phase representation. The downstream digital converter described by ADI is **not** part of CELL_V1.

## R2 — Synchro: three 120-degree electromagnetic axes
Analog Devices, *Synchro/Resolver Conversion Handbook, Chapter 1*.
https://www.analog.com/media/en/training-seminars/design-handbooks/synchro-resolver-conversion/Chapter1.pdf

Established mechanism used here: three stator windings arranged 120 degrees apart provide a proven three-axis electromagnetic projection geometry. This is precedent for the A/B/C physical interface; it does not prove the CELL four-action or ternary logic.

## R3 — Rotating magnetic field from phase-related windings
Analog Devices, *AC Synchronous Motors — ADALM1000*.
https://wiki.analog.com/university/courses/alm1k/circuits1/alm-ac-sync-motors

Established mechanism used here: phase-related stator fields vector-sum into a continuously rotating magnetic field. This supports the physical feasibility of a QC–RC rotating-field layer. CELL's square figure-8 realization is unproven.

## R4 — Ferrite hysteresis is measurable material behavior
TDK Electronics, *Magnetic Design Tool*.
https://tools.tdk-electronics.tdk.com/mdt/index.php

Established mechanism used here: ferrite material data include hysteresis loops, power loss, permeability, flux-density/field-strength behavior, temperature dependence and DC-bias behavior. The final CELL nucleus material remains open and must be selected from measured requirements.

## R5 — Patterned Permalloy can store/path magnetic-domain history
A. et al., *Information storage in permalloy modulated magnetic nanowires*, Scientific Reports (2021).
https://www.nature.com/articles/s41598-021-00165-1

Established mechanism used here: magnetic domains/domain walls can encode information and geometrical inhomogeneities can provide pinning/control locations. This is precedent for a patterned hysteretic path layer, **not proof** that the proposed CELL etched lattice is writable, durable, scalable, or suitable.

## R6 — Geometric notches produce domain-wall pinning and hysteresis
*Depinning of domain walls in permalloy nanowires with asymmetric notches*, Scientific Reports (2016).
https://www.nature.com/articles/srep32617

Established mechanism used here: patterned geometry can nucleate, pin and depin domain walls at measurable applied fields. This strengthens the physical basis for testing path-dependent etched magnetic tracks.

## R7 — Three MOSFET half-bridges are a standard three-phase power stage
Infineon, TLE994x/995x daughterboard user guide.
https://www.infineon.com/assets/row/public/documents/10/44/infineon-infineon-tle994x-995x-daughterboard-ug-en-usermanual-en.pdf

Established mechanism used here: three half-bridges form a motor power stage and use DC-link buffering. CELL_V1 borrows the **power topology only**; its ordinary IC/PWM controller is not the CELL decision mechanism.

## R8 — Inductive energy can return to the DC link
Infineon Developer Community accepted technical explanation, *6EDL7141 Braking* (2026).
https://community.infineon.com/t5/Gate-Driver-ICs/6EDL7141-Braking/td-p/1173852

Established mechanism used here: winding current cannot change instantaneously; collapsing magnetic field/back-EMF can forward-bias body diodes and return energy to the DC link. CELL must measure how much energy is actually recovered and whether return disturbs CENTER or memory.

## Evidence classification

| CELL block | Established precedent | CELL-specific claim |
|---|---|---|
| opposed differential signals | transformer/differential electromagnetic coupling | BC–DC semantic role and thresholds |
| two-component magnetic view | resolver sine/cosine channels (R1) | square figure-8 realization |
| rotating field | phase-related winding vector sum (R3) | QC–RC role and useful state representation |
| A/B/C physical axes | synchro 120° stator geometry (R2) | mapping from four actions to cell axes |
| nucleus hysteresis | ferrite B-H behavior (R4) | useful retained CELL state |
| etched magnetic paths | patterned Permalloy/domain-wall pinning (R5,R6) | muscle-memory behavior in CELL lattice |
| A/B/C power stage | three half-bridges (R7) | analog threshold-driven commutation |
| V_BUS return | inductive DC-link return (R8) | useful shared reinjection without state corruption |
| CENTER/(0) | ordinary midpoint/differential-reference physics | active ternary interpretation and exact bands |
| complete recursive cell | none — integration is novel/experimental | must be demonstrated interface by interface |

## Hard rule

A reference proves only the mechanism stated beside it. Do not cite a resolver as proof of CELL cognition, a domain-wall paper as proof of muscle memory, or a motor inverter as proof of CELL control. The complete architecture remains a testable integration hypothesis.


## R9 — Six discrete MOSFETs / three half-bridges for A/B/C
Texas Instruments, *Power Block MOSFETs in Different Motor-drive Topologies* and *Three-Phase vs Three-Single Half-Bridge Gate Drivers*.
https://www.ti.com/document-viewer/lit/html/SSZT955/GUID-064DDA53-B0F0-4EDC-909D-7D601DA643B2
https://www.ti.com/lit/an/slvafz0/slvafz0.pdf

Established mechanism used here: a three-phase motor power stage uses three half-bridges, six MOSFETs total, with one high-side and one low-side MOSFET per A/B/C phase. CELL_V1 adopts this as the **A/B/C power projection skeleton only**. Conventional PWM, MCU, gate-driver IC and FOC control are not adopted as the CELL decision mechanism.

## R10 — MOSFET threshold is not the fully-ON gate voltage
onsemi, *Shielded Gate PowerTrench MOSFET Datasheet Explanation* (AN-4163) and *Power MOSFET Basics* (AN-9010).
https://www.onsemi.com/download/application-notes/pdf/an-4163.pdf
https://www.onsemi.com/pub/Collateral/AN-9010.pdf

Established mechanism used here: MOSFET drain current begins around threshold, while useful on-resistance depends on actual VGS, drain current and temperature. Therefore CELL's <=1 V analog nerve/wave signal must not be assumed to drive an arbitrary A/B/C power MOSFET directly. The nerve stage may require a discrete translation/amplification mechanism while preserving the analog CELL decision; exact topology is a bench target.


## R11 — Transfluxor: one-piece multi-aperture hysteretic core with shared flux paths
J. A. Rajchman and A. W. Lo, *The Transfluxor*, Proceedings of the IRE, 1956, pp. 321–332. Historical scan:
https://www.bitsavers.org/pdf/afips/1956-02_%2309.pdf

Established mechanism used here: a core made from magnetic material with a nearly rectangular hysteresis loop can contain two or more apertures, creating multiple distinct flux paths through the legs of one magnetic body. Controlled transfer of flux from leg to leg provides switching/storage behavior. The authors report that the prior setting can determine subsequent AC transmission and that intermediate settings can produce a continuous range of output levels.

CELL use: closest identified precedent for the **one-piece square two-aperture figure-8 nucleus** and for a retained OLD magnetic condition physically affecting response to NEW excitation. Historical transfluxors do not establish CELL semantics or geometry dimensions.

## R12 — Transfluxor shared-path magnetic switch
W. J. Mahoney, *Transfluxor Magnetic Switch*, US3376427A.
https://patents.google.com/patent/US3376427A/en

Established mechanism used here: a hysteretic core with a central aperture and coupling aperture defines at least two closed magnetic paths with portions in common; saturation state in the common portions controls coupling between windings. This is direct precedent for shared magnetic legs coupling the two apertures of one body.

## R13 — Double-aperture transfluxor common read/write circuitry
IBM, *Transfluxor Memory Employing Common Read-Write Circuits*, US3328785A.
https://patents.google.com/patent/US3328785A/en

Established mechanism used here: a double-apertured magnetic core supports retained magnetic state, threshold-dependent switching and common read/write circuitry. Coincident sub-threshold currents can jointly produce a switching condition. CELL cites this as precedent for physical combination of retained magnetic condition and applied excitation, not as proof of CELL's three-mirror gate or ternary interpretation.

## R14 — Multi-aperture / square-loop magnetic storage and continuous setting context
Historical technical literature describes transfluxors as square-loop hysteretic magnetic cores with multiple apertures and flux-transfer paths; related implementations used the storage property to retain adjusted transmission characteristics. These references establish a magnetic history-dependent mechanism without software state.

### Evidence-map addition

| CELL block | Established precedent | CELL-specific claim |
|---|---|---|
| one-piece two-aperture nucleus | transfluxor multi-aperture hysteretic core (R11-R13) | square-window dimensions and CELL winding layout |
| shared magnetic legs | closed flux paths with common portions (R11,R12) | Field/Void semantic assignment |
| OLD + NEW physical interaction | retained setting/history changes later transmission/switching; coincident excitation can cross threshold (R11,R13) | old ACTIONS DOWN + new VIEWS UP and three-mirror recursion |
| analog/intermediate retained setting | continuous intermediate transfluxor transmission setting reported by Rajchman/Lo (R11) | CELL ternary CENTER and seven-band scale |
