# Algorythm-Zer0 — Implementation Status

**Current status: architecture defined; implementation unresolved.**

## What exists

- Four-branch X/Y/Z/T model.
- Six cumulative levels per branch.
- Field/Void mirror structure.
- 1,296 level-coordinate address space.
- Threshold / hysteresis bands.
- T6 resolve / rebase closure concept.
- A rule that software descriptions are not physical CELL_V1 memory.

## What does not yet exist

There is no verified implementation that takes a real input, traverses all four branches, resolves Field/Void conflicts, performs T6 closure, and demonstrates that the resulting next reference is useful in a real control task.

That is the implementation gap.

## Smallest useful implementation target

Do not begin with the whole 168-term vocabulary.

A first demonstrator should prove only this:

1. Accept one measurable starting state.
2. Establish its current reference.
3. Produce one binary / opposed choice.
4. Permit HOLD as a real third outcome.
5. Produce one move.
6. Generate four views and four candidate actions.
7. classify current state / scale.
8. perform one Level-6 resolve.
9. produce a new reference.
10. repeat and show that the new cycle actually depends on the previous resolved cycle.

Run the same test through X, Y, Z, and T so the four branches describe one shared event rather than four unrelated calculations.

## Pass condition

The demonstrator passes only if:

- every higher level retains traceable lower-level context;
- the final choice can be traced back through the branch state;
- T6 creates a reproducible next reference;
- HOLD is distinguishable from failure / missing data;
- no hidden arbitrary rule chooses the answer when branches disagree.

## Physical implementation question

The eventual CELL_V1 mapping is still open.

Possible quantities to investigate include:

- differential lean;
- direction;
- magnitude;
- hysteresis / retained bias;
- body / bus state;
- structural orientation;
- rate of change;
- consequences returned from the previous action.

Those are **candidate interfaces**, not established Zer0 hardware encodings.

## Presentation rule

Say:

> “We know the recursive information structure we want. We are still determining the correct physical or computational mechanism that realizes it.”

Do not say:

> “Algorythm-Zer0 is already running the android.”

It is not yet demonstrated.


## Physical precedents worth testing — not canon replacements

Independent review identified several useful precedent classes:

- **multi-aperture hysteretic cores / transfluxors** for history-dependent shared magnetic paths;
- **magnetic majority / current-summing elements** for physical two-of-three coherence;
- **coupled oscillators / asynchronous threshold systems** for non-clocked consensus;
- **adaptive-reference / moving-equilibrium systems** for comparison with Zer0's rebase idea;
- **non-dissipative inductive recovery** for V_BUS return.

These are not one-to-one matches and must not rename Zer0 by analogy.

## Smallest physical Zer0 experiment

The first physical implementation attempt should test only one recursive cycle:

```text
REFERENCE
-> opposed CHOICE with HOLD
-> one MOVE
-> returned consequence
-> STATE / SCALE classification
-> RESOLVE
-> bounded NEW REFERENCE
```

Required observations:

1. the next reference depends on the prior physical cycle;
2. the next reference remains bounded rather than drifting blindly to saturation;
3. HOLD is a stable physical outcome, not missing data;
4. lower-level state remains inferable after higher-level resolution;
5. no software variable, comparator bank, or op-amp state machine performs the hidden decision.

### Failure tests

- **Runaway rebase:** repeated same-sign events push reference monotonically into saturation.
- **Context loss:** final resolved state cannot be traced back to lower-level state.
- **False HOLD:** HOLD appears only because drive disappears.
- **Hidden arbiter:** result requires an external digital or IC decision element.
- **Mismatch domination:** component tolerance determines the state more strongly than the intended input.

## RC terminology warning

Do not assume project **RC** means a resistor-capacitor relaxation path. The current project use is a broader remainder / returned-consequence role and still requires reconciliation with standard engineering terminology. No resistor-based relaxation path is part of the locked CELL architecture.
