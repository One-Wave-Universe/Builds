# Builds Work Board

This board organizes executable work. Detailed scientific simulation work remains in One-Wave-Science.

## P0 — interfaces and maps
- [ ] W-001 Animator project/state schema — see `maps/ANIMATOR_PRODUCT_MAP.md`
- [ ] W-002 CELL authoritative interface/state map — see `maps/CELL_V1_CONCEPT_MAP.md`
- [ ] W-003 Android scale/interface schema — see `maps/ANDROID_CELL_TO_CORTEX_MAP.md`
- [ ] W-004 Universal Sensory State schema
- [ ] W-005 DCACRC-IR v0 grammar/schema

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
