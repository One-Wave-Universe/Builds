# Builds Work Board

This board organizes executable work. Detailed scientific simulation work remains in One-Wave-Science.

## P0 — interfaces and maps
- [ ] W-001 Animator project/state schema — see `maps/ANIMATOR_PRODUCT_MAP.md`
- [ ] W-002 CELL authoritative interface/state map — see `maps/CELL_V1_CONCEPT_MAP.md`
- [ ] W-003 Android scale/interface schema — see `maps/ANDROID_CELL_TO_CORTEX_MAP.md`
- [ ] W-004 Universal Sensory State schema
- [ ] W-005 DCACRC-IR v0 grammar/schema

## P0B — digital CELL / state-machine brain ladder
See `maps/DIGITAL_CELL_TWO_STATE_BRAIN_LADDER.md`.
- [ ] W-010 L0 Digital Cell reference + fixtures
- [ ] W-011 L1 Parser Cell
- [ ] W-012 L2 Validator Cell
- [ ] W-013 L3 Chooser Cell
- [ ] W-014 L4 bounded Controller Cell
- [ ] W-015 common Field/Void state + receipt schema

## P1B — workers and reconstruction
- [ ] W-110 L5 Worker Cell
- [ ] W-111 L6 Recursive Worker
- [ ] W-112 L8 Recall/Rebuild Worker
- [ ] W-113 L9 crucial permanent-reference store + versioning
- [ ] W-114 corruption/missing-source/rebuild test suite

## P2B — internal Field/Void cognition
- [ ] W-210 L7 structured Field/Void dialogue worker
- [ ] W-211 disagreement/resolution fixtures
- [ ] W-212 memory promotion validator
- [ ] W-213 DCACRC-IR mapping for parser/validator/chooser/controller

## P3B — brain integration
- [ ] W-310 L10 Multi-Worker Brain
- [ ] W-311 worker permission/arbitration layer
- [ ] W-312 L11 embodied brain + sensory interfaces
- [ ] W-313 L12 full digital reference brain
- [ ] W-314 waking/dream source-switch and replay validation

## P1 — runnable reference work
- [ ] W-101 DCACRC-IR Python interpreter
- [ ] W-102 DCACRC trace/visual debugger
- [ ] W-103 Jetson audio capture + deterministic replay
- [ ] W-104 Jetson camera capture + deterministic replay
- [ ] W-105 Animator acceptance fixture

## P2 — sensory baselines
- [ ] W-201 audio calibration/filterbank/onset pipeline
- [ ] W-202 binaural time/level difference benchmark
- [ ] W-203 camera calibration/local-contrast/edge pipeline
- [ ] W-204 motion/optical-flow benchmark
- [ ] W-205 sensory combined-state projection

## P3 — cortex + sandbox
- [ ] W-301 hearing cortex processing graph
- [ ] W-302 vision cortex processing graph
- [ ] W-303 simulated audio source adapter
- [ ] W-304 simulated visual source adapter
- [ ] W-305 dreamscape environment interface
- [ ] W-306 real-vs-sim comparison/replay harness

## P4 — physical backend
Blocked until relevant CELL primitives have bench receipts.
- [ ] W-401 map validated DCACRC-IR primitives to analog backend
- [ ] W-402 sensor-cell hardware interface
- [ ] W-403 motor/action hardware interface
- [ ] W-404 flower/body-state integration

## Definition of done
Every job has an owner or worker, inputs, outputs, acceptance tests, dependencies, result receipt and claim/status boundary. Work is promoted by evidence, not by completion text.
