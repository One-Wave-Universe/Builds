#!/usr/bin/env python3
"""One millivolt ternary gate. Input [0,100] plus signed drive. Output {-1,0,+1}."""
from __future__ import annotations
from dataclasses import dataclass

BANDS = [(lo, lo + 10) for lo in range(0, 100, 10)]
DEAD = 5.0

def band_index(x: float) -> int:
    x = max(0.0, min(100.0, x))
    return min(9, int(x // 10))

@dataclass
class Gate:
    name: str = "G0"
    hold: float = 50.0

    def decide(self, x: float, drive: float) -> int:
        if abs(drive) < DEAD:
            return 0
        target = x + drive
        delta = target - self.hold
        if abs(delta) < DEAD:
            return 0
        bit = 1 if delta > 0 else -1
        self.hold = max(0.0, min(100.0, target))
        return bit

def demo() -> None:
    g = Gate("action")
    print("GCAC single gate — dead zone", DEAD)
    samples = [(50, 1), (50, 6), (56, 2), (56, -20), (30, -3), (30, -8), (5, 40), (90, 20)]
    for x, d in samples:
        out = g.decide(x, d)
        print(x, d, out, g.hold, band_index(g.hold))

if __name__ == "__main__":
    demo()
