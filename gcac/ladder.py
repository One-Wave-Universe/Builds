#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, field
from gate import Gate

@dataclass
class Cell:
    gate: Gate = field(default_factory=Gate)
    def step(self, x: float, drive: float) -> int:
        return self.gate.decide(x, drive)

@dataclass
class Rubik:
    cells: list = field(default_factory=lambda: [Cell() for _ in range(27)])
    def step(self, xs, drives):
        return [c.step(x, d) for c, x, d in zip(self.cells, xs, drives)]
    def vote(self, word):
        s = sum(word)
        if s > 3: return 1
        if s < -3: return -1
        return 0

@dataclass
class TwoRubiks:
    left: Rubik = field(default_factory=Rubik)
    right: Rubik = field(default_factory=Rubik)
    midline_phase: int = 0
    def tick(self, left_x, left_d, right_x, right_d):
        self.midline_phase = (self.midline_phase + 1) % 12
        lw = self.left.step(left_x, left_d)
        rw = self.right.step(right_x, right_d)
        lv, rv = self.left.vote(lw), self.right.vote(rw)
        if lv == -rv and lv != 0:
            return {"clock": self.midline_phase, "action": 0, "note": "reject"}
        action = lv if abs(lv) >= abs(rv) else rv
        return {"clock": self.midline_phase, "action": action, "note": "accept"}

if __name__ == "__main__":
    brain = TwoRubiks()
    for t in range(8):
        print(brain.tick([50+4*t]*27, [8 if t%2==0 else -2]*27, [50-3*t]*27, [-8 if t%3==0 else 3]*27))
