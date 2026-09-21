# Flower

The single cell is the primitive: one differential, one lean, one event.
The flower is the first operator that can integrate, circulate, and hand a result to a neighbor flower.
Do not call the primitive a brain cell. Do not call the flower a software neuron.

---

## Geometry (locked)

Seven cells. Center + six outers. Point-up hex. Edge-center ports.

Twelve mirrors from the tiling. No extra harness.

Three axes, not six independent voters:

- A+ ↔ A−
- B+ ↔ B−
- C+ ↔ C−

Center A+ meets an outer A−. That is one difference, not two ballots.

Nerve compression 6→3→1 is *seats → axes → one nerve*, not “add six floats.”

---

## 1. Center threshold (proposal)

Center does **not** linearly sum six scalars.

It holds three leans: D_A, D_B, D_C. Each is a pair against CENTER.

**Transfer (best guess):**

- Each axis is already ternary: DOWN / HOLD / UP after its own wobble.
- Center commits as a *unit* when **two of three axes** have left HOLD the same way, and the third is not opposed.
- Opposed axes (one UP, one DOWN) → center HOLD. That is consensus, same as GCAC admin reject.
- Magnitude of the commit is the **hardest** of the agreeing axes (deepest write / largest |D|), not the mean. Mean would wash a deep path with two shallow ones.

Winner-take-all is too sharp for a first guess. Two-of-three + no opponent is the HOLD-respecting rule.

Hysteresis: enter commit outside wobble; leave only after all three axes are back in 0.45–0.55 *and* the bus kick from that event has settled. That is the flower refractory. Not a timer chip.

---

## 2. Outer ring (proposal)

N1→N2→N3→N4→N5→N6→N1 is a closed axis path that does not have to visit center.

It is lossy. Every hop is a lean that can fade. There is no lossless circulating token.

**Decay:** a ring event that is not refreshed by a neighbor crossing or by center coupling dies in a small number of hops (proposal: fewer than one full lap unless hardness is already deep). That duration *is* the flower’s short hold. Deep cores keep a lap. Shallow cores don’t.

Center sees the ring only through the six mirrors. It does not own a separate wire around the loop.

Call the ring an under-path, not a subconscious soul.

---

## 3. Event on the wire (proposal)

“Flower fired” is not a named packet.

It is: center left HOLD, three half-bridges (or the live axes) drove, windings wrote, collapse steered to V_BUS.

What a neighbor flower gets:

- a current / voltage excursion on the shared *edge* (axis metal)
- a small kick on V_BUS (readiness, not memory)

Not a phase-coded telegram. Not a spike label. The next flower’s pair either crosses or it doesn’t.

Shape: whatever that pair + winding already produce. No third waveform type.

---

## 4. Lateral coupling (proposal)

Adjacent flowers share an edge. That edge is already a mirror (one C+ to the other C−).

So lateral “inhibition” is not a new circuit. If two flowers lean the same axis opposite ways, the shared edge is a fight. Consensus HOLD. If they lean the same way, the edge reinforces.

V_BUS is the other coupling: a firing flower sags or kicks the rail. Neighbors get sluggish or sharp together. That is readiness coupling, not a vote.

No extra inhibit wire in the proposal.

---

## 4×4 at flower scale (proposal)

Views (sense the ring / the three D’s): BASELINE, DELTA, HEADING, RESULT  
Actions (drive the axes): PULL, PUSH, FLIP, PASS

Sixteen couplings are sixteen *leans*, each a magnetic hold on a path that already exists (axis or center–outer mirror). Not a 4×4 SRAM.

Implementation is still open as transistors. Meaning is not: it is those views and actions on the same three differentials.

---

## Blank flower

No prior write. All cores near zero remanence. All pairs in HOLD wobble. V_BUS at whatever the supply sits. That is blank. You do not load a file. First events write the first leans.

---

## Scale one sentence

Primitive = one differential.  
Operator = flower (three differentials + ring + twelve mirrors).  
Tissue = field of flowers on hex + shared V_BUS.  
Inverted stack = opposed field (hypothesis).

Missing silicon: exact two-of-three gate, winding count, one core vs three. Not missing the idea.
