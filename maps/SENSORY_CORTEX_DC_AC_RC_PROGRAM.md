# Sensory Cortex + DC/AC/RC Computing Program

## Purpose
Develop hearing and vision first as measurable Jetson experiments, then define a hardware-neutral DC/AC/RC intermediate representation (IR) that can later compile to analog CELL hardware if the physical primitives validate.

## Do not invent an analog language too early
The first programming language is a **declarative state/flow IR**, not Python disguised as analog hardware and not raw transistor instructions.

### Proposed DCACRC-IR primitives
`REFERENCE` — declared center/home
`DIFF A B -> D` — signed differential
`LEAN D bands -> state` — − / HOLD / + with hysteresis
`COUPLE x y` — declared bidirectional relation
`INTEGRATE x tau -> h` — retained/history state
`GATE condition -> path` — threshold/state-controlled route
`FIELD group -> combined` — combined-state projection
`EMIT observable unit` — measurable output
`SOURCE real|simulated` — provenance boundary

Every primitive needs units, continuous-time meaning, digital reference implementation, analog target semantics, and tests. Python is the reference/runtime language initially; DCACRC-IR is the domain language; later hardware backends can map validated primitives to CELL circuits.

## Jetson hearing program
H0 microphone capture + timestamp/provenance
H1 calibrated waveform/spectrum
H2 filterbank/frequency decomposition
H3 onset/amplitude/temporal-envelope features
H4 binaural interaural time/level differences with two microphones
H5 localization benchmark against known source positions
H6 learned/pattern layer only after H0-H5 have receipts

Gold metrics: latency, sample loss, SNR/noise floor, frequency response, onset error, localization angular error, CPU/GPU load, deterministic replay from recorded audio.

## Jetson vision program
V0 camera capture + timestamp/provenance
V1 calibration/exposure/noise characterization
V2 local contrast/center-surround reference transform
V3 edges/orientations
V4 motion/optical-flow reference
V5 contour/object/state representation
V6 learned representation only after deterministic V0-V5 baselines

Gold metrics: frame loss, end-to-end latency, calibration error, edge/motion benchmark error, robustness to lighting, compute load, deterministic replay from recorded frames.

## Cortex interface
Both senses emit Universal Sensory State packets:
- source: real or simulated;
- timestamp;
- reference/baseline;
- local features;
- uncertainty/confidence;
- spatial/temporal relations;
- retained history;
- combined-state projection;
- provenance.

## Dreamscape
A dreamscape simulator must produce the same *interface shape* as the real sensor adapters but remain tagged `SOURCE simulated`. Visual cortex and audio cortex can therefore be exercised in two modes:
- waking: camera/microphone adapters;
- dream: sandbox visual/audio scene adapters.

No dream output may be relabeled as measured real-world evidence.

## Work packages
S1 DCACRC-IR grammar/schema
S2 Python reference interpreter
S3 trace/visual debugger
S4 Jetson audio capture/replay
S5 Jetson binaural benchmark
S6 Jetson camera capture/replay
S7 deterministic vision baselines
S8 Universal Sensory State schema
S9 simulated audio/visual source adapters
S10 cortex processing graph
S11 analog backend specification after CELL primitives pass
S12 dreamscape cortex integration
