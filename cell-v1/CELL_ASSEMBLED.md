# Cell — assembled

Geometry, lean, flower, gates, bus, machines, build order. One page.

Hypothesis stays tagged. Empty LOG.md still means 0% hardware.

## Geometry

- Point-up hexagon. Six edges. Connections at edge centers, not corners.
- Clockwise: A+ → B+ → C+ → A− → B− → C−
- Three mirrored axes: A+↔A−, B+↔B−, C+↔C−
- Six edge seats are not six independent gates. Three physical mirrored axes.
- Each plus edge is three seats clockwise from its minus. On a hex that is the opposite side. The mirror is the shape.

## Flower self-wiring

- Seven cells: one center, six around.
- Center-to-outer is automatic mirror. Center A+ meets neighbor A− by tiling.
- Outer-to-outer is automatic mirror. Neighbors share an edge so one C+ meets the other C−.
- Twelve mirror connections per flower. Zero custom wiring. Six center-outer, six outer-outer.
- Outer ring is a closed loop N1→N2→N3→N4→N5→N6→N1. Signal can go around without the center. Hypothesized fast under-path. Not measured.
- Twelve mirror pairs ↔ twelve tones is model mapping, not a proven mechanism.

## Stacking

- Same orientation stacked: A+ meets A+. Reinforces.
- Inverted stacked: A+ meets A−. Differential surface. Hypothesized split / crossing. Not measured.
- Point → flower → stacked flower → volume → next-scale point. Same connection rule.

## Three physical gate functions

CHOICE, PIVOT, FLIP. Three mirrored functions, not six unrelated gates.

Traversal: CHOICE → PIVOT → FLIP → PIVOT → CHOICE

Exact transistor map is open.

## Lean

Weight is the lean off a moving virtual ground. Same path as the signal. Not a table.

Subthreshold pair. Shared tail current.

- Tail current = hardness. 1 µA soft, 10 µA hard (working numbers).
- Gate difference = direction + magnitude.
- Idiff = Iss · tanh(Vd / (2·n·Vt))
- DOWN / HOLD / UP. HOLD is live tail current, gm on. Not off.
- Use deepens. Disuse fades. No separate training season.

See `WEIGHT_LEAN.md`, `NOT_SOFTWARE.md`, `ANTI_DRIFT.md`.

## Voltage scale (1 V layer)

1 V full scale. 0.50 V center. Named bands with dead zones. Center 0.45–0.55 V is home.

Commitment on that map:

- 0.10–0.20 FULL DISAGREE (−3)
- 0.25–0.35 PARTIAL DISAGREE (−2)
- 0.40–0.50 lean minus
- 0.50 UNITY (0)
- 0.50–0.60 lean plus
- 0.65–0.75 PARTIAL AGREE (+2)
- 0.80–0.90 FULL AGREE (+3)

Extremes 0.00–0.10 and 0.90–1.00 are terminal / crisis.

Working hysteresis: partial_enter 0.4, partial_exit 0.28, full_enter 0.82, full_exit 0.68.

Millivolt layer later. Same band shape, finer scale. Do not design Cell-0 around millivolts. Cell-0 is 9 V parts.

## q-update (talk about the lean, not the lean)

q(n+1) = clip(r·q(n) + g·b·m·d·L, −q_max, +q_max)

Working: r = 0.92, g = 0.24, q_max = 1.
L(Δφ) = [1 + cos(Δφ)] / 2

This equation *describes* a leaky hold-and-add. It does not make the cell a software neuron and it does not store memory. Memory is the lean in the path. See `ANTI_DRIFT.md`.

## Compression and authority

- 3:1 nerve compression. Six edge seats → three axes → one nerve channel.
- 6:1 oversight / override. Six cheap continuous oversight channels. One rare expensive override.
- Oversight is normal. Override is the exception.

## Two machines and the under-loop

- Brain machine: intent, language, sequence, plan.
- Body machine: motor, balance, hearing, battery.
- Under-loop: reflex, muscle memory, pocket. Does not wait on deliberation.

Not a stack. Two peers coupled by a mirror. Fast loop from the coupling. Flower ring is the hypothesized seat of that loop.

## Current kinds

- DC — base flow, one way
- AC — oscillation around center
- RC — not a third supply. The lean itself. Asymmetric departure from the moving ground. That *is* the move and the choice.
- BC-DC — binary relation picks direction of DC
- TC-AC — ternary move picks phase of AC
- QC-RC — 4×4 operator picks path through the recursive lean

## Moving ground

Virtual ground is not a bolted zero. The system leans off it. HOLD is a lean that cancels. The ground moves with the lean. Next choice starts from that ground. That is how history sits in the body.

## Brainstem as quadratic

4 views up × 4 actions down = 16 couplings. Classical bilinear. Not a bit. Not a trit. Not a qubit.

Cells ternary. Brainstem quadratic. Hemispheres above. Hypothesis until built.

## Views up / actions down (locked lexicon)

- X: BASELINE / DELTA / HEADING / RESULT × PULL / PUSH / FLIP / PASS
- Y: ROOT / TRAJECTORY / EXTENT / CONFIGURATION × DRAW / DRIVE / INVERT / TRANSMIT
- Z: PROJECT / COUPLE / TRANSFORM / INTEGRATE × SELECT / ARRANGE / PERMUTE / COLLAPSE
- T: STILL / SLOW_MOTION / ACCELERATED / EXHAUSTED × COINCIDENCE / HOPE / TARGET / STRATEGY

T5 rate (not T4): REST / SLOW / NORMAL / FAST / GLARE
Lifetime unit (not rate): LIFE / GEOLOGIC / PLANET / GALACTIC / UNIVERSAL

## Magnetic hold

Identical probe, different prior lean, different response. That test is the gate.

Shallow / deep / saturated write energy on the same core.
Paths saturate — need fade or the lattice freezes its first habit.
Deep paths need protection (coercivity, region, or active lock).

## Reinjection

See `REINJECT_BUS.md`.
Return through the same element that wrote. Bus is lattice blood. CENTER stays off that metal. No created energy.

## Build order

1. 0.50 V reference quiet under switching (1 V layer) / Cell-0 9 V pair first on the bench
2. Pair responds to a small gate difference
3. Hardness via tail current
4. HOLD measurable
5. Magnetic element shows state-dependent response ← stop here if this fails
6. Write depth control
7. Inductive recovery measured
8. One axis full loop
9. Three axes, rotation
10. Flower
11. Nerve compression and override
12. Brainstem
13. Hemispheres
14. Bucket

Nothing above 5 matters until 5 works.

## Locked vs hypothesis

Locked: hex geometry, three axes, twelve flower mirrors from tiling, voltage band *shape*, ternary, hysteresis *structure*, memory in the processing path, no free energy.

Hypothesis: flower computes, outer ring is the under-loop, inverted stack is the split, 4×4 is the brainstem, 3:1 and 6:1 do what we want, the whole thing plays.

## Open

HOLD circuit. Magnetic material. Write-depth method. Fade. CHOICE / PIVOT / FLIP transistors. Views/actions topology. One shared core vs A/B/C cores. Winding count. Flower flip rules.
