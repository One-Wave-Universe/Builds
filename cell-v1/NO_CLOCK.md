# No clock

The cell is event-driven. Nothing says sample now. It moves when a lean crosses a band. Timing is what the lattice *does*, not a wire that tells it when.

No global clock. No shared phase reference. Different seats can run at different rates. Rhythm is a consequence of thresholds.

## Bidirectional ports

A+ is not an input or an output. It is a port. Same path, either way.

Sending vs receiving is which way the lean is pointing, not a pin label.

A+ out and A− back are one channel with opposite polarity at a given moment. That is the mirror.

Needs:

- Symmetric devices both ways
- Gate drive that still works when polarity flips
- Sense of *direction*, not only size
- Back-to-back FETs or an honest body-diode plan

## Locked threshold bands

The event bands are fixed in normalized 0–100 form:

- +3: 90–100
- +2: 75–85
- +1: 60–70
- HOLD: 45–55
- −1: 30–40
- −2: 15–25
- −3: 0–10

The six 5-point spaces between those bands are hysteresis / transition gaps. No timer resolves them. Prior settled state plus the direction of the analog lean determines which band owns the crossing.

## Thresholds are the events

HOLD is the wait between crossings. Lean gathers. Cross a band → fire (drive, write the core, bus sees the return). Then HOLD again.

Bands are not labels on a chart. They are the crossings.

- Center → moderate → one commit
- Moderate → strong → deeper commit
- Strong → extreme → crisis

Hysteresis is not optional. No clock means chatter at the fence unless enter ≠ exit.

Dead zones are the forgive.

## HOLD revised

HOLD is readiness. Tail current on. Pair sensitive. Not committing.

After fire, return to HOLD is not a clock edge. It is the analog falling back inside the home band.

## Choice is flow direction

- Lean to A+ → current A+ → A−
- Lean to A− → current A− → A+
- HOLD → no net way

DOWN / HOLD / UP is the flow. Same wire senses and acts.

## What gets easier / harder

Easier: no clock tree, no lattice-wide phase lock.

Harder: threshold drift, chatter, noise that looks like an event, catching events instead of probing a clock.

Tempo is produced. Pocket is the *rate of crossings*. Two cells couple when their crossings line up. That is the loop.

## Open (bench, not theory)

1. Threshold stay-put vs heat and time
2. Chatter / refractory without a clock chip
3. What a fire looks like on the wire
4. Bidirectional gate drive
5. Sensing which way current is going
6. How HOLD comes back after fire
7. Power-up: factory fence or leftover core

Work next: refractory (2 and 6). That is whether a pocket can exist. Gate drive after that, or the mirror is a drawing.
