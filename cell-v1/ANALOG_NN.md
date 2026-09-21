# Analog nets vs this cell

Four families out there. Steal physics. Do not steal the table.

## 1. Crossbar CIM (memristor / flash / Mythic-class)

Kirchhoff does the MAC. G is the weight. Beautiful current-sum — same *idea* as two-of-three Iss add.
Difference: G is programmed, copied, inferred as a matrix. History is a file in disguise.
Steal: summing currents on a node. Keep: H in the core, not G in a crossbar.

## 2. Analog CMOS / FPAA / OTA / switched-cap

Mead descendants, Hasler-style FPAA, capacitor memory near the compute.
Steal: subthreshold pair, no ADC in the loop, local C.
Cap-as-weight fades. Your square-loop is the longer RC.

## 3. Event-driven mixed analog (DYNAP, Blumind AMPL, BrainScaleS analog core)

No big clock in the neuron. Blumind: one transistor stores a coefficient *and* multiplies. Event-driven. Strong cousin on “no ADC, no master clock.”
Difference: they still load a network from software (PyTorch → coefficients). You grow leans.
Steal: event, subthreshold, skip converters.

## 4. Coupled analog learners (CLLN / nonlinear resistor nets)

Physical network that learns with local rules, no processor in the loop. XOR on a bench. That is the closest *philosophy*: the net *is* the learner.
Difference: they freeze a resistive mesh. You keep a living bus + per-axis cores + coherence vote.

---

## What we already are

Current-sum coherence (family 1 physics).
Subthreshold pair + local C (family 2–3).
No clock, no packet (family 3).
State in the hardware (family 4).
Plus what they skip: hex mirror, two references, bus fed-by/feeds-all, three cores so axes can oppose.

Do not “become an ANN.” Do not put a crossbar on CENTER.
