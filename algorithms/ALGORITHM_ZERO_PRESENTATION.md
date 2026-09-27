# Algorythm-Zer0 — Presentation Authority

**Status:** Presentation-ready conceptual architecture. **Implementation path remains open.**

Algorythm-Zer0 is not presented as a finished executable algorithm or as a replacement for the physical CELL_V1 control loop. It is a proposed **nested recursive grammar for describing, comparing, routing, and rebasing state**.

The key presentation claim is structural:

> A useful recursive algorithm should not discard the context that produced the current state. Each higher level retains the lower levels, and each completed cycle establishes the reference for the next cycle.

## 1. The four orthogonal branches

Algorythm-Zer0 describes a state through four simultaneous branches:

| Branch | Question | Role |
| --- | --- | --- |
| **X — CONTROL** | What is the system doing? | choice, action, routing, control state |
| **Y — STRUCTURE / ROTATION** | How is it arranged? | axis, orientation, topology, structural relation |
| **Z — DEPTH** | At what mathematical / relational depth is it represented? | scalar through harmonic / layered relation |
| **T — TIME / CHANGE** | How does the combined state persist or change? | temporal position, lifecycle, closure, rebase |

The branches are not intended as four independent programs. They are four views of the **same state**.

## 2. Six cumulative levels

Every branch passes through six cumulative levels:

| Level | Universal function |
| --- | --- |
| **1** | REFERENCE |
| **2** | POLARITY / CHOICE |
| **3** | MOVE |
| **4** | VIEWS UP / ACTIONS DOWN |
| **5** | STATE / SCALE |
| **6** | RECURSE / RESOLVE / RETURN |

The structural rule is:

```text
L1 ⊂ L2 ⊂ L3 ⊂ L4 ⊂ L5 ⊂ L6
```

A higher level does not replace the previous level. It **contains and references it**.

That is the central distinction Zer0 is meant to explore.

## 3. Field and Void

Each level has two opposed but cooperating sides:

- **FIELD** — the currently expressed / active interaction.
- **VOID** — the unexpressed possibility and validating counter-side.

Void is not simply “nothing.” In the current canon it acts as the counter-reference that can confirm, reject, defer, reserve, or redirect what Field is expressing.

The universal relation is:

```text
+  <->  (0)  <->  -
EXPRESS <-> COMPRESS
```

The center is a **reference / pivot**, not a value judgment.

## 4. Cross-mirror rule

Across the six levels:

```text
F1 <-> V6
F2 <-> V5
F3 <-> V4
F4 <-> V3
F5 <-> V2
F6 <-> V1
```

The low-level expressed state is checked against the high-level potential context, and vice versa.

For presentation purposes, this is one of the strongest visual ideas in Zer0: the system does not only climb upward; it continually checks the opposite side of the hierarchy.

## 5. The recursive cycle

The universal cycle is:

```text
REFERENCE
   ↓
CHOICE / POLARITY
   ↓
MOVE
   ↓
VIEWS UP / ACTIONS DOWN
   ↓
STATE / SCALE
   ↓
RESOLVE / RECURSE
   ↓
NEW REFERENCE
```

The important rule is that the **baseline moves**.

The next zero is not necessarily the original zero:

```text
(0)t -> interaction -> consequence -> resolve -> (0)t+1
```

This is why it is called Zer0: zero is the current reference from which difference is evaluated, not a permanently fixed origin.

## 6. Four-branch closure

A complete state is treated as the combination:

```text
X · Y · Z · T
```

The current canon states that the combined state is not fully committed until the temporal branch reaches its Level-6 resolution / rebase step.

Conceptually:

```text
X1..6
Y1..6
Z1..6
T1..5
   ↓
T6 RESOLVE
   ↓
REBASE
   ↓
new X·Y·Z·T reference
```

## 7. 6 × 6 × 6 × 6 address space

The four branches each expose six hierarchical levels.

That gives:

```text
6 × 6 × 6 × 6 = 1,296
```

possible **level-coordinate addresses** across X/Y/Z/T.

This does **not** mean there are 1,296 primitive words. The current term vocabulary is organized separately as 21 Field + 21 Void terms per branch.

The 1,296 number describes the four-dimensional level-address space.

## 8. Thresholds are separate from meaning

Zer0 intentionally separates:

**WHAT a state means**  
from  
**WHEN / HOW STRONGLY it commits.**

The current normalized relation bands are:

| Range | Interpretation |
| --- | --- |
| 90–100 | extreme expression / danger |
| 75–85 | strong expression |
| 60–70 | moderate expression |
| 45–55 | active middle / stable oscillating region |
| 30–40 | moderate compression |
| 15–25 | strong compression |
| 0–10 | extreme compression / danger |

The gaps are intentional transition / hysteresis regions. They are not silently filled.

This lets the same logical grammar potentially be calibrated differently in different physical domains.

## 9. Relationship to CELL_V1

Zer0 must not be presented as software memory for CELL_V1.

CELL_V1 memory, if the hardware works as proposed, is retained in the **physical path / hysteretic state**.

Zer0 may describe or route a physical state, but it must not claim that a stored number replaces the body's retained state.

Presentation distinction:

```text
CELL_V1 = physical state / body
Zer0    = recursive description and routing grammar
```

A future implementation may bind Zer0 coordinates to measured physical states, but that interface is **not yet demonstrated**.

## 10. What is locked for presentation

The following ideas are mature enough to present as the proposed architecture:

- four branches: X / Y / Z / T;
- six cumulative levels;
- Field / Void dual description;
- cross-mirror pairing;
- updated reference after each completed cycle;
- views-up / actions-down at Level 4;
- state / scale at Level 5;
- recursive closure at Level 6;
- thresholds separated from primitive identity;
- 6^4 = 1,296 level-coordinate address space;
- no software value may be presented as physical CELL_V1 memory.

## 11. What is still open

Do **not** present these as solved:

- exact executable semantics for every primitive;
- exact mapping from a real-world input into one X/Y/Z/T coordinate;
- conflict resolution when branches request incompatible moves;
- how physical CELL_V1 signals bind to Zer0 terms;
- whether Zer0 should ever run as conventional software in the body architecture;
- hardware realization of the full six-level recursion;
- timing / convergence guarantees;
- formal proof that the grammar is complete or minimal;
- performance advantage over conventional state machines / control systems.

## 12. Implementation position

For the presentation, the correct statement is:

> **We have a defined recursive architecture and vocabulary, but we do not yet claim a finished implementation. The next engineering task is to define the smallest falsifiable interpreter or physical mapping that can execute one complete X·Y·Z·T cycle without changing the canon to fit the implementation.**

Possible implementation experiments are allowed to be temporary test harnesses. They must not be confused with the intended final physical architecture.

## 13. Current canon-source warning

There is currently a repository conflict:

- `FOUR_BRANCHES_AND_UNIVERSAL_RULES.md` contains the newer presentation vocabulary.
- `algorithm_zero_locked_canon.json` contains an older vocabulary for several X and Y levels.

Until reconciled, **the JSON must not be presented as the authoritative term list**.

For presentation, use this document together with:

- `FOUR_BRANCHES_AND_UNIVERSAL_RULES.md`
- `thresholds.md`
- `LEAN_INTO_ZER0.md`

The machine-readable canon should be rebuilt only after the human-readable canon is rechecked term by term.
