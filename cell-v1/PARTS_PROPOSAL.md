# Parts and cousins (proposed architecture)

Not a shopping list you must buy tonight. Named families so the architecture is specific.

## Magnetic hold (CENTER)

Do not spec an EMI suppression bead. That is a loss lump.

Family: **tape-wound square-loop** nickel-iron, the mag-amp / flux-counter class.

- Square Orthonol (Magnetics code A) — 50% Ni-Fe, very square B-H, saturable / bistable class. High remanence. Deep write lives here.
- Square Permalloy 80 (code D) — 80% Ni-Fe, square but softer. Shallower write / modulator class.
- Supermalloy (code F) — high µ, low loss. Too round for a hard lean; useful as a contrast part in the text (“if we had used this, hold would fade”).

Catalog: Magnetics Inc tape-wound cores. Bobbin cores if the cell must stay small.

Proposal line: *memory element is a square-loop tape core on CENTER, chosen for remanence and a usable coercivity window so write depth can be shallow or deep on the same part.*

IC endgame (same job, later): exchange-bias MTJ / domain-wall MTJ multi-state. Keep as “scale path,” not the Cell-0 noun.

## Bidirectional port (1 V layer)

Not a 2N7000 asked to be analog at 10 mV.

Family:

- CMOS transmission gate (N+P, complementary drive) — both-ways analog, rail-to-rail inside VDD.
- Low-voltage analog mux specified from ~1.08 V (example class: PSMUX1247 and kin). Bidirectional S/D, GND to VDD.
- Back-to-back discrete N-FETs only as the 9 V Cell-0 explanation of polarity, not the 1 V port.

Proposal line: *each axis is a bidirectional analog port; polarity is the lean, not a pin label.*

## Pair (1 V lean)

Subthreshold matched MOSFET pair. Iss = tail = hardness. Vd = millivolt difference.

Foundry / MPW later (TinyTapeout, university analog CMOS). Proposal does not need a die in hand. It needs the bias region named.

## Bus

Half-bridge per winding, steering into C_BUS, shared rail. Energy identity in ARCHITECTURE.md. Recovery family in the literature is resonant / adiabatic drive — cite as cousin, not as a 99% promise.

## Who already lives nearby (collaborators, not merges)

- Analog event-driven CMOS: DYNAP-SE2, Blumind AMPL, Mead-line labs.
- Magnetic multi-state: EB-MTJ / DW-MTJ papers (2024–26).
- Charge return: adiabatic LIF / resonant arrays.

They store weights beside the neuron. We do not. That sentence is the differentiator.

## NSF-shaped risk (architecture, not a prototype boast)

Phase I language they want: high-risk technical question that is *unproven*. Ours:

*Can a square-loop element on the same path as a subthreshold pair hold a lean that changes the next crossing, while collapse returns to a shared DC bus and not to the floating center?*

That is the innovation paragraph. Existing chips do pieces. None of them do that sentence.
