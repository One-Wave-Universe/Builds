# Animator — Product / Work Map

## Outcome
A reflex-fast frame-by-frame desktop animation tool that lets a creator pick actual character/background art, compose frames, play full-screen, save/reopen, and export a usable reel/video. It is not a physics simulator.

## Canonical flow
INSTALL → OPEN PROJECT → PICK BACKGROUND → PICK CHARACTER ART → PLACE FRAME → NEXT FRAME → PLAY → SAVE → REOPEN → EXPORT

## Gold acceptance
- one-click install and desktop launch;
- actual image assets, not placeholder boxes;
- fixed-layer frame editor;
- placement grid visible while editing and hidden in playback/export;
- frame-by-frame editing: do not move one frame continuously across the screen as a substitute for animation;
- full-screen playback;
- project save/reopen without drift;
- deterministic export;
- asset library with provenance/license fields;
- crash-safe project file;
- keyboard + pointer workflow;
- test scenes: walk toward/away, look around, kick can, pick flower/sniff.

## Work packages
A1 project/state schema
A2 asset library + character/background picker
A3 frame/layer editor
A4 onion/reference/grid tools
A5 playback
A6 save/reopen migration tests
A7 reel/video export
A8 installer/desktop shortcut
A9 performance/reflex-latency pass
A10 acceptance fixture project

## Boundary
Anime-like is an art direction, not permission to copy protected characters or artwork. Use owned/licensed/generated assets.
