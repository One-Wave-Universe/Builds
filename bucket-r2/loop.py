#!/usr/bin/env python3
from __future__ import annotations
import argparse
from clock import slot_at
from senses import Drum, Ear, Eye, Mouth
DEAD = 0.08

def gate(motion: float, guitar: bool) -> int:
    drive = motion + (0.2 if guitar else 0.0)
    if abs(drive) < DEAD:
        return 0
    return 1 if drive > 0 else -1

def bar(t, eye, ear, drum, mouth):
    slot = slot_at(t)
    frame = eye.grab(t)
    guitar = slot["polarity"] == "express"
    decision = gate(frame.motion, guitar)
    hit = drum.hit(frame.motion + 0.25 * decision) if decision >= 0 else False
    word = slot["gray"] if hit else ""
    return {"t": t, "gate": decision, "hit": hit, "said": mouth.say(word), "slot": slot["tag"]}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--beats", type=int, default=12)
    args = p.parse_args()
    eye, ear, drum, mouth = Eye(), Ear(), Drum(), Mouth()
    for t in range(args.beats):
        print(bar(t, eye, ear, drum, mouth))

if __name__ == "__main__":
    main()
