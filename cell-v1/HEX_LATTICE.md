# Hex lattice — hysteretic body-state / muscle-memory layer

The connected CELL lattice needs a **dedicated hysteretic layer laid beneath the cells**.

This layer is the physical body-state / muscle-memory substrate.

It is **not V_BUS** and it is **not CENTER**.

## Layer stack

```text
TOP
  local cell:
  A/B/C differentials
  CENTER/(0)
  role-specific nucleus
  common body toroids

MID
  actuator / write coupling
  local field / gate structures

UNDER-CELL HYSTERESIS LAYER
  continuous or segmented hysteretic magnetic sheet / traces
  follows shared cell edges and flower paths
  carries Br / path bias / body-state history

POWER LAYER
  V_BUS + return
  energy / readiness / reinjection only

REFERENCE
  CENTER remains local
```

## What the hysteresis layer does

Each connected cell sits over / couples into the shared hysteretic layer.

Repeated physical use may alter the local magnetic history of the path beneath and between cells.

That gives two related memories:

1. **local retained state** — nucleus / local hysteretic path;
2. **group muscle memory / body state** — shared hysteretic layer spanning connected cells.

Neighboring cells can therefore share history through the physical path that connects them rather than by copying software state.

## Shared edges

Clockwise cell edges remain:

```text
A+ B+ C+ A- B- C-
```

The hysteretic layer should follow these edge / lattice relationships so repeated use can bias a **path through the body**, not only a single private core.

Candidate physical implementation:

- patterned hysteretic magnetic film / sheet under the copper lattice;
- magnetic strip or laminated path following the shared edges;
- segmented hysteretic tiles whose shared boundaries couple magnetically.

Exact material and fabrication are open.

## Body-state role

The layer is intended to hold distributed physical history such as:

- repeatedly used movement paths;
- preferred / practiced motor routes;
- persistent load / posture bias;
- local cluster condition;
- recent repeated action history that should influence the next traversal.

This is the architecture's **muscle-memory / body-state layer**.

The state must remain physical and measurable.

## Relation to reinjection

```text
ACTION
  -> motor / field event
  -> consequence
  -> inductive collapse / V_BUS reinjection
  -> next traversal through the same connected body
  -> hysteretic layer already carries prior path bias
  -> changed next action
```

V_BUS carries returned energy.

The hysteretic layer carries the longer-lived path bias.

They participate in the same cycle but are different physical layers.

## Relation to the nucleus

The nucleus and hysteretic body-state layer are not duplicates.

- **nucleus** = local cell state / local retained history;
- **hysteresis layer** = connected-body / path / muscle memory;
- **V_BUS** = energy return / readiness / short echo.

The nucleus can read / be biased by the local field produced by the body-state layer, subject to bench validation.

## First flower

For the seven-cell flower:

- one continuous hysteretic sheet / patterned lattice should underlie all seven connected cells;
- shared edges should align to one continuous or magnetically coupled path;
- the center motor cell and six sensor cells should all be able to influence and sense the same body-state substrate through their local coupling;
- the layer should not electrically short A/B/C, CENTER, or V_BUS.

## What must be measured

- remanence Br after repeated route use;
- spatial localization of the written path;
- cross-talk into neighboring paths;
- retention / decay;
- whether repeated use reduces required drive for the same route;
- whether opposite practice can rewrite / reverse the path;
- whether the layer biases the next motor decision without corrupting CENTER;
- whether the effect survives when V_BUS condition changes.

## Failure condition

If the hysteretic layer cannot hold a localized, repeatable path bias without collapsing into global cross-coupling, it cannot serve as the body-state / muscle-memory layer in its current form.

## Anti-drift rule

Do not merge this layer back into V_BUS.

Do not call bus voltage muscle memory.

Do not move this memory into software.

The hysteretic body-state layer is a dedicated physical substrate under the connected cells.


## Phase-I scope

The first connected-body build uses **one domain-wall hysteretic layer**.

That one layer is the target for simple repeated motor behaviors such as:
- wheel motion;
- propeller / rotor motion;
- other single-scale motor habits.

Do not stack multiple hysteretic body-state layers in the first build.

Nested muscle-memory layers are a later extension for articulated movement, where memory must exist at multiple physical scales, for example:

```text
finger-local trace
-> hand coordination trace
-> limb trace
-> body trace
```

The rule is **one layer until complexity or measured interference proves another layer is needed**.

## 2026-09-27 stack lock — active reinjection above retained body memory
The Phase-I vertical relationship is:
```
A/B/C wedge differential hardware
local bidirectional mirror/loss gates
LOCAL GATE HYSTERESIS
LOSS-THRESHOLD / TERNARY REINJECTION LAYER
          <-> coupling / write / read consequence
SHARED HYSTERETIC BODY-STATE / MUSCLE-MEMORY LAYER
V_BUS / FEED / RECOVERABLE-ENERGY LAYER
```
Do not merge the two hysteresis scales:
- local gate hysteresis remembers transition/lean history and suppresses chatter;
- the under-cell shared hysteresis layer retains distributed path/body history.

Reinjection is coupled to and revisits the shared hysteretic path; V_BUS performs energy accounting and reservoir duty but is not itself the retained muscle memory.
