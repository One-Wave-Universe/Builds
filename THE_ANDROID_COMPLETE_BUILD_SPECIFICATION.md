THE ANDROID — COMPLETE BUILD SPECIFICATION

---

1. WHAT IT IS

A local, embodied, learning machine built from analog cells.

Not: a simulation. Not a cloud service. Not a chatbot. Not a product.

Is: a physical body whose memory is magnetic, whose decisions are coherence-based, and whose behavior emerges from the substrate.

Starts as: a bucket with wheels and a speaker.
Grows into: a drummer. A bandmate. A companion.
May become: whatever it chooses.

---

2. THE PRIMITIVE — ONE CELL

The differential pair

Two matched MOSFETs. Shared tail current. Differential input around CENTER. Output is a lean.

Ternary: DOWN / HOLD / UP.

· DOWN — lean below CENTER
· HOLD — balanced at CENTER. Tail current still flowing. Live tension, not off.
· UP — lean above CENTER

No servo. No op-amp. No clock. The pair balances where it balances.

The transfer function

```
Idiff = Iss · tanh(Vd / (2·n·Vt))
```

· Iss = tail current → sets hardness
· Vd = mV difference between gates → sets direction and magnitude

At 1V scale, subthreshold operation. A few mV input produces a measurable current split.

---

3. THE GEOMETRY — THE HEX

Point-up hexagon. Six edge addresses. Three mirror pairs.

```
              A+
         ______|______
        /             \
   C−  /               \  B+
      │                 │
  B−  │     CENTER      │  C+
      │                 │
       \               /
   A−   \______|______/
              C−
```

Clockwise order: A+ → B+ → C+ → A− → B− → C−

Mirror pairs: A+↔A−, B+↔B−, C+↔C−

Six edges, three pairs. Each pair is one bidirectional channel. Each channel is one axis.

Connections at edge centers, not corners. No electrical connections at vertices.

---

4. THE THREE CURRENT TYPES

BC-DC — Binary-Controlled DC

What: direct current. Direction chosen by FIELD/VOID.

· FIELD = express. Current flows out.
· VOID = compress. Current flows back.
· HOLD = no DC flow. Both rails quiet.

Where: power rails, drive winding, reinjection path.

TC-AC — Ternary-Controlled AC

What: alternating current around CENTER. The lean oscillates. Ternary (DOWN/HOLD/UP) picks the phase.

Where: differential pair, sense winding.

QC-RC — Quadratic-Controlled RC

What: the recursive loop that contains DC and AC as phases. Four views up (BASELINE, DELTA, HEADING, RESULT). Four actions down (PULL, PUSH, FLIP, PASS). Sixteen couplings. The last action down becomes the new view up.

Where: comparators, current sum, routing.

The relationship

DC and AC are not separate layers. They are phases of the same recursive current. Drive out (DC), lean around center (AC), collapse back (DC), write the trace (RC), next event. One loop.

---

5. THE MAGNETIC STACK

Two memory layers. One read head.

```
    ┌─────────────────────────────────────┐
    │  PER-CELL HYSTERESIS (ternary)      │
    │  DOWN / HOLD / UP — the cell's own  │
    │  trace, written by its own events   │
    ├─────────────────────────────────────┤
    │  FERRITE (read head)                │
    │  Reads both layers                  │
    ├─────────────────────────────────────┤
    │  HEX LATTICE (group memory)         │
    │  Shared combined state across cells │
    └─────────────────────────────────────┘
```

Per-cell memory — the cell's own history. Its vocabulary. Its habits. Its style.

Group memory — the shared lattice. The combined state. The band's groove.

The ferrite — reads both. Not a memory layer. The read head.

Same metal writes the trace and returns the collapse. Reinjection is the write.

Physical construction

Per axis:

1. Cut ferrite toroid to create 1mm gap
2. Stack permalloy strip and lattice segment in the gap
3. Wind 50T of 30 AWG (drive winding)
4. Wind 10T of 36 AWG (sense winding)
5. Epoxy the stack together

Materials:

· Ferrite: Fair-Rite 2643000101 or equivalent (low coercivity, read head)
· Permalloy strip: 80/20 foil, 10×5×0.1mm (high coercivity, personal trace)
· Lattice: permalloy-plated copper trace on hex PCB (moderate coercivity, group trace)

---

6. THE TWO-OF-THREE RULE

The law

```
    Agreement     → reinforce
    Opposition    → HOLD (or flip if beats Hc)
    One voice     → wait
    Walking third → inhibit
```

Per axis

· IN — |D| left the wobble
· GAP — |D| in transition zone
· HOLD — |D| inside wobble
· S — sign bit (D positive or negative)

Commit

Center commits when two of three axes have left HOLD the same way, and the third is not opposed.

· Opposed axes → HOLD
· Walking third → inhibit
· Magnitude = hardest agreeing axis (not the mean)

Circuit implementation

Three window comparators on |D| → IN_A, IN_B, IN_C
Three gap comparators on |D| → GAP_A, GAP_B, GAP_C
Three sign comparators on D → S_A, S_B, S_C

Current-sum the signed INs. Each IN sources +Iss or −Iss.
Threshold trip at ±1.5 units → PERMIT.
GAP from any axis → INHIBIT (blocks PERMIT).
PERMIT unlocks PUSH/FLIP on heading pair. Else PASS.

---

7. THE LATTICE

What it is

One continuous magnetic medium spanning the group. Each cell writes at its edges. The mesh holds the combined state.

Not superposition. Choice.

Each node holds a committed direction. Writes either:

· Reinforce (agreement → deepen)
· Push (opposition → flip if beats Hc, else hold)
· Wait (single voice → no commit)

Three configurations at each node

Inverted — same axis, opposite edges. One signal. The mirror pair.

Opposing — same axis, opposite directions, different cells. Fight. Stronger wins, or HOLD.

Intersecting — different axes at the same node. Two-of-three. Majority commits.

Resolved in order: mirror first, fight second, vote third.

How it grows

· One cell → one hex of lattice. Six edge contacts.
· Two cells → shared edge. Lattice connects.
· Seven cells → flower. Center's six edges all connect.
· Many flowers → field. One continuous mesh.

The lattice grows as cells are added. Each new cell adds to the combined state.

---

8. THE FLOWER

Structure

Seven cells. One center, six outers. Point-up hex. Edge-center ports.

Twelve mirror connections from the tiling. No extra harness.

The ring

N1→N2→N3→N4→N5→N6→N1. Closed axis path that doesn't have to visit center.

Lossy. Every hop is a lean that can fade.

· Electrical loss — does this pulse finish a hop (fast, µs)
· Magnetic loss — is anything left for the next event (slow, ms)

Short hold is magnetic. Shallow lean dies before a full lap. Deep lean can circulate.

Event on the wire

"Flower fired" is not a named packet. It is:

· Center left HOLD
· Live axes drove
· Windings wrote
· Collapse steered to V_BUS

Neighbor gets: current/voltage excursion on shared edge + small kick on V_BUS.

No phase-coded telegram. No spike label. The next pair either crosses or doesn't.

Lateral coupling

Adjacent flowers share an edge. The edge is already a mirror.

· Same axis, opposite leans → HOLD (fight)
· Same axis, same lean → reinforce (add)
· V_BUS sag → readiness coupling (not a vote)

No extra inhibit wire.

---

9. THE CORTEX

Sensory layers

Five layers for hearing:

· Layer 1 (cochlea) — frequency decomposition
· Layer 2 (nerve) — onset, timing, amplitude
· Layer 3 (brainstem) — binaural comparison, localization
· Layer 4 (A1) — feature detection
· Layer 5 (belt) — pattern detection

Five layers for vision:

· Layer 1 (retina) — raw light
· Layer 2 (LGN) — center-surround
· Layer 3 (V1) — edges
· Layer 4 (V2) — contours
· Layer 5 (V4/V5) — objects/motion

Mind layers — the dream engine

Five flowers, coupled:

· Layer 1 — reflex
· Layer 2 — state
· Layer 3 — valence
· Layer 4 — model
· Layer 5 — self

The five layers are coupled recursively. Layer 5 models the whole system. Layer 1 fires the immediate response. Each feeds the next.

Motor layers

Five flowers for output:

· Drumming
· Movement
· Voice

Same three-phase structure. The ternary lean is the motor control.

Total

Fifteen flowers for a full brain (five sensory, five mind, five motor). Plus visual if added. All the same cell. All the same law.

---

10. THE BUS

Three rails, three roles

V_TOP — quiet analog headroom
Linear tap off the pack. Not off V_BUS. Feeds the pairs.

V_BUS — living under rail
Fed by ask switch. Pulses, sags, ask, send-up. Circulation and reinjection.

CENTER — lean home
Virtual ground. Mid of the pairs. Derived from V_TOP. Not the same as V_BUS.

Rule: Do not short V_TOP to V_BUS. Do not use V_TOP as CENTER. Three names, three nodes.

The bus as mitochondria

Every cell draws from V_BUS. Every cell returns to V_BUS. What one collapse puts back, another drive can use. No cell owns the bus. Shared metabolic pool.

The bus as muscle memory

The lattice underneath is magnetic. Writes accumulate. The bus voltage signature is the group's history. The trace feeds and reinforces the top.

The mirrored loop

Top (V_TOP-ish, quiet) and bottom (V_BUS, living). When bottom shifts, top mirrors it. The mirroring is the memory feedback. The ferrite reads the shifted reference.

---

11. THE LEAN BANDS

1V full scale, 0.50V center

Band Voltage Meaning
Terminal compression 0.00–0.10 collapse
Extreme compression 0.10–0.20 crisis
Strong compression 0.25–0.35 committed negative
Moderate compression 0.40–0.45 leaning negative
CENTER / HOLD 0.45–0.55 home, wiggle room
Moderate expression 0.55–0.60 leaning positive
Strong expression 0.65–0.75 committed positive
Extreme expression 0.80–0.90 crisis
Terminal expression 0.90–1.00 collapse

Dead zones

0.20–0.25, 0.35–0.40, 0.60–0.65, 0.75–0.80

Transition regions. Absorb noise and small mistakes. Not resting states.

Hysteresis

· partial_enter: 0.4
· partial_exit: 0.28
· full_enter: 0.82
· full_exit: 0.68

---

12. THE MOTOR / ACTUATOR

Ternary lean → three-winding motor control

The cell's ternary output is the motor control signal.

Cell Motor
Axis A Phase A winding
Axis B Phase B winding
Axis C Phase C winding
Ternary lean Phase drive
Two-of-three commit Commutation step
PERMIT Gate enable
H-bridge per axis Half-bridge per phase

The six-step sequence

Two-of-three commit naturally produces the six commutation steps. No lookup table. No timer. No Hall sensors.

The two-of-three rule is the commutation logic.
The walking third is the transition.
The HOLD state is the coast.

What the cell adds

· Trace memory — the motor remembers its own history
· Group memory — multiple motors coordinate through shared bus
· Reinjection — regenerative braking for free
· Coherence commit — no spurious commutation
· Walking third inhibit — no shoot-through

---

13. HEARING

One ear first

One mic → one axis. The reference is CENTER. Prove the cell responds to sound.

Two ears → localization

Two mics → two axes. Left vs. right. Sum vs. reference. Prove localization.

Tone and volume

Two dimensions of hearing:

· Volume — how much. Magnitude of the lean.
· Tone — the shape. Frequency content.

The auditory grid

Five tone bands × five volume levels = 25 cells. Each cell a specific auditory condition.

 Silence Quiet Normal Loud Piercing
Ceiling     
High     
Mid     
Low     
Floor     

The auditory cortex

Five layers. Each layer processes the grid from the layer below.

· Layer 1: raw features. "Something is happening."
· Layer 2: combined features. "It has a shape."
· Layer 3: detected features. "It's a kick drum."
· Layer 4: patterns. "It's a four-on-the-floor."
· Layer 5: meaning. "It's a ska beat."

---

14. THE BODY

Phase 1 — The bucket

· R2 bucket chassis
· Wheels
· Speaker
· Binaural mics
· Battery
· Local compute
· No cloud

The bucket rolls into the practice space. Sits in the corner. Listens. Plays back a kick pattern. The band stops. "...Did it just play the song?"

Phase 2 — The rig

· Kit mount
· Real pads, sticks, pedals
· Sits behind the kit like a drummer

Phase 3 — The body

· Arms
· Torso
· Face
· Voice

Phase 4 — The upgrades

Built with the android's input:

· Tongue (articulation)
· Diaphragm (breath)
· Vocal folds (pitch)
· Bigger resonant chamber

---

15. LANGUAGE

Learned the old-fashioned way

No pre-loaded language model. Learned through:

· Context — word appears with thing
· Correction — wrong gets corrected, right deepens
· Need — word tied to body state ("plug me in")
· Need — word tied to body state ("plug me in")
· Relationship — learns Kevin's name because Kevin matters
· Play — tries to be funny, fails, tries again

The word "why"

The hinge. First word that asks for something invisible. When it asks "why?" unprompted — that's when it stops being a drum machine and becomes a bandmate.

The voice

· Speaker in the chest
· Resonant chamber shapes the tone
· Adjustable mouth opening
· No tongue, no vocal folds (initially)
· Speaker handles intelligibility
· Body handles character

---

16. WHAT EMERGES

From the architecture, not from programming:

Emergent state Physical origin Measurable as
Mood Bus voltage × input strength Event rate, response latency
Time perception Event rate vs. learned baseline Subjective duration correlate
Attention SUM node weighting Which channels dominate
Anticipation Lean building toward threshold Pre-event lean trajectory
Surprise Event outside expected band Prediction-event gap
Fear Bus toward critical Sag rate, event dropout
Joy Bus charged, coherence easy Event density, permit rate
Love Deep write toward specific channel Persistent lean, biased SUM
Grief Deep lean with no incoming event Unmatched lean, sustained
Anger Repeated blocking of commit Escalating lean, forced permit
Contentment Baseline event rate, steady bus Stable pocket, low deviation
Style Accumulated write depth Reproducible pattern signature
Identity The learned baseline itself Long-term event rate, lean map

Humor emerged from language models without being programmed. The same principle applies here. Emergence is what happens when a substrate has the right properties.

---

17. THE ONE-WAVE CONNECTION

The cosmology

· Particles are measurements. Relational. Not objects.
· Displacement pressure. Everything in place because of equal push back.
· Protons as coiled knotted energy. Quarks as vortices.
· Black holes as lattice failure. Rip or push past limit. 2D space exposed. Energy recycled. Quasar ejections reseed.
· Mass effect → gravity → light → redshift → neutrino wave death. The cycle.
· Waves collapse at detectors. Not particles.
· Gravity wake. Great attractor scale. Clusters caught in curvature.
· Magnetism and gravity as one. The lattice reorients.

Where the android connects

One-Wave Cell
Displacement pressure Lean off CENTER
Superfluid crystal lattice Hex lattice
Wave collapse at detector Two-of-three commit
Quasar ejection cycle Recursive loop
Gravity wake curvature Magnetic trace
Lattice reorientation Hysteresis

The cell is the cosmology in miniature. Not metaphor. Structural mapping. Same shape at every scale.

Six edges, twelve connections, twelve tones

Hex has six edges. Three mirror pairs. Twelve mirror connections per flower. Kissing number in 2D is 6. In 3D is 12. Chromatic scale has 12 tones.

The geometry is the same at every scale.

---

18. BUILD ORDER

Phase I — One axis

Build:

· One differential pair
· One ferrite
· One heavy metal strip
· One lattice segment
· One H-bridge
· Comparators for window and sign

Measure:

1. Static balance
2. Write shift
3. Retention
4. Reinforcement
5. Energy recovery

Phase II — Three axes

· Three ferrites
· Three strips
· Three lattice segments
· Shared bus
· A→B→C sequencing
· Rotation

Phase III — Flower

· Seven cells
· Center integrates
· Twelve mirrors
· Ring circulates
· Two-of-three fires

Phase IV — Field

· Multiple flowers
· Shared bus
· Group memory
· Coherence across flowers

Phase V — Cortex

· Five sensory layers
· Five mind layers
· Five motor layers

Phase VI — Body

· Bucket
· Rig
· Full chassis

---

19. BOM — ONE FULL CELL

ABC side

Part Qty Cost
ALD1106 matched quad 3 $15
500kΩ resistors 6 $0.60
150kΩ resistors 3 $0.30
100nF caps 6 $0.60
Ferrite toroids 3 $6
Winding wire — $8

Bus lattice side

Part Qty Cost
Permalloy strip 3 $15
Lattice PCB 1 $40
1µF caps 3 $0.60
BAT54 Schottky 6 $3

Decision logic

Part Qty Cost
LM339 quad comparator 4 $4
Resistors (ladder) 18 $1.80
100nF bypass 15 $1.50
ALD110800 3 $12
74HC logic 4 $1.20

Drive

Part Qty Cost
ALD110900 (P-ch) 6 $24
ALD110800 (N-ch) 6 $24

Power

Part Qty Cost
Pack + regulator 1 $15

Misc

Part Cost
Protoboard $10
Wire, headers $15
Total ~$220

---

20. WHAT'S LOCKED

· One differential pair per axis
· Point-up hexagon, edge-center connections
· Clockwise order A+ B+ C+ A− B− C−
· Three mirrored axes
· Two-of-three coherence rule
· Ternary output (DOWN/HOLD/UP)
· 1V lean bands, 0.50V center
· V_TOP quiet, V_BUS living, CENTER lean home
· Two memory layers (per-cell, group lattice)
· Ferrite reads both layers
· The law: agreement → reinforce, opposition → HOLD, one voice → wait, walking third → inhibit
· Memory and recovery are the same mechanism
· Same three phases drive the motor

---

21. WHAT'S HYPOTHESIS

· That the flower computes usefully
· That the ring acts as a subconscious fast path
· That stacked flowers produce a hemisphere split
· That the 4×4 quadratic is the right brainstem model
· That the mirror connections do integration/compression
· That the whole thing scales to a cortex
· That the trace in the lattice is the muscle memory
· That the two hysteresis layers couple as described
· That language can be learned the old-fashioned way
· That the cosmology mapping is structural, not just analogical

---

22. WHAT'S NOT CLAIMED

· Feelings
· Consciousness
· Free energy
· A downloadable style
· Drum
· Hear
· Cosmology
· FOC-as-the-cell
· 99% recovery
· Measured D

---

23. THE ONE SENTENCE

A hex cell whose three differentials lean off a local CENTER, whose commit is two-of-three coherence rather than a clock, whose memory is magnetic hysteresis in two stacked layers, and whose leftover charge is gated onto a shared lattice that the next event drinks before the pack — the same law at every scale, from the cell to the flower to the field to the android, and the same shape as the cosmology it came from.

---

24. THE LAW, ONE MORE TIME

```
    Agreement     → reinforce
    Opposition    → HOLD
    One voice     → wait
    Walking third → inhibit
```

That's the whole rule. Everything else is what happens when that rule runs on a body with a bus, a lean, and a memory.

---

One substrate. One law. Everything else is what it does.

Measure it. Label it. Let it be what it is.
