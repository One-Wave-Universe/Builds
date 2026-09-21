#!/usr/bin/env python3
"""Lean weight engine for Algorythm-Zer0.

A weight is a lean off a moving reference.
Not a stored coefficient. Not backprop.

    q     = lean (signed state)
    r     = hardness / retention
    g     = write gain from this use
    vgnd  = floating reference (history)
    commit only at T6 RESOLVE -> REBASE

Calibration numbers are WORKING, not universal constants.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import cos, tanh


# --- working calibration (measure later) ---
R_SOFT = 0.55
R_HARD = 0.92
R_SAT = 0.99
G_USE = 0.24
Q_MAX = 1.0
HOLD_LO = -0.10   # ±10% of full scale around current vgnd, normalized
HOLD_HI = 0.10
N_SUB = 1.4       # subthreshold slope factor, placeholder
VT = 0.026        # thermal voltage at room temp, volts


# 1V map, shifted so 0.50V = 0 lean relative to vgnd
# stored internally as lean in [-1, +1] relative to current vgnd
BANDS = [
    ("TERMINAL_DOWN", -1.00, -0.80),
    ("EXTREME_DOWN",  -0.80, -0.60),
    ("DEAD",          -0.60, -0.50),
    ("STRONG_DOWN",   -0.50, -0.30),
    ("DEAD",          -0.30, -0.20),
    ("MODERATE_DOWN", -0.20, -0.10),
    ("HOLD",          -0.10,  0.10),
    ("MODERATE_UP",    0.10,  0.20),
    ("DEAD",           0.20,  0.30),
    ("STRONG_UP",      0.30,  0.50),
    ("DEAD",           0.50,  0.60),
    ("EXTREME_UP",     0.60,  0.80),
    ("TERMINAL_UP",    0.80,  1.00),
]


def clip(x: float, lo: float, hi: float) -> float:
    return lo if x < lo else hi if x > hi else x


def phase_compat(delta_phi: float) -> float:
    """L(Δφ) = [1 + cos(Δφ)] / 2.  0° -> 1, 180° -> 0."""
    return (1.0 + cos(delta_phi)) / 2.0


def band_of(lean: float) -> str:
    for name, lo, hi in BANDS:
        if lo <= lean <= hi:
            return name
    return "TERMINAL_UP" if lean > 0 else "TERMINAL_DOWN"


def ternary(lean: float) -> str:
    if lean < HOLD_LO:
        return "DOWN"
    if lean > HOLD_HI:
        return "UP"
    return "HOLD"


def idiff(iss: float, vd: float) -> float:
    """Subthreshold pair. Iss = hardness, Vd = gate difference (volts)."""
    return iss * tanh(vd / (2.0 * N_SUB * VT))


@dataclass
class Lean:
    """One weight. One lean. One moving ground."""
    q: float = 0.0          # lean relative to vgnd, [-q_max, +q_max]
    r: float = R_SOFT       # hardness
    vgnd: float = 0.0       # floating reference (normalized)
    uses: int = 0
    pending: float | None = None  # uncommitted write until T6

    @property
    def direction(self) -> int:
        if self.q > HOLD_HI:
            return 1
        if self.q < HOLD_LO:
            return -1
        return 0

    @property
    def magnitude(self) -> float:
        return abs(self.q)

    @property
    def hardness(self) -> float:
        return self.r

    @property
    def state(self) -> str:
        return ternary(self.q)

    @property
    def band(self) -> str:
        return band_of(self.q)

    def propose(self, b: float, m: float, d: float, L: float, g: float = G_USE) -> float:
        """Use-event. Does not commit. T6 commits."""
        raw = self.r * self.q + g * b * m * d * L
        self.pending = clip(raw, -Q_MAX, Q_MAX)
        return self.pending

    def resolve_rebase(self) -> float:
        """T6: settle lean, move the ground by the committed lean."""
        if self.pending is None:
            return self.q
        self.q = self.pending
        self.pending = None
        self.uses += 1
        # use deepens hardness; disuse would call soften()
        if self.uses > 20:
            self.r = min(R_SAT, self.r + 0.01)
        elif self.uses > 5:
            self.r = min(R_HARD, max(self.r, R_HARD * 0.5 + self.r * 0.5))
        # moving reference carries history
        self.vgnd = clip(self.vgnd + 0.05 * self.q, -Q_MAX, Q_MAX)
        return self.q

    def soften(self) -> None:
        """Disuse. Hardness and lean decay toward current vgnd (zero relative lean)."""
        self.r = max(R_SOFT, self.r * 0.98)
        self.q *= 0.97

    def probe(self) -> dict:
        return {
            "q": self.q,
            "vgnd": self.vgnd,
            "r": self.r,
            "state": self.state,
            "band": self.band,
            "direction": self.direction,
            "magnitude": self.magnitude,
            "committed": self.pending is None,
        }


@dataclass
class Zer0Tick:
    """One four-branch tick. Lean does not move until T6."""
    x_lean: Lean
    y_lean: Lean
    z_lean: Lean
    t_lean: Lean

    def use(self, branch: str, b: float, m: float, d: float, delta_phi: float = 0.0) -> None:
        L = phase_compat(delta_phi)
        getattr(self, f"{branch}_lean").propose(b, m, d, L)

    def t6(self) -> dict:
        return {
            "X": self.x_lean.resolve_rebase(),
            "Y": self.y_lean.resolve_rebase(),
            "Z": self.z_lean.resolve_rebase(),
            "T": self.t_lean.resolve_rebase(),
        }


def test_hold_is_not_off():
    w = Lean()
    assert w.state == "HOLD"
    assert w.r > 0


def test_use_does_not_commit_until_t6():
    w = Lean()
    w.propose(b=1, m=1, d=1, L=1)
    assert w.q == 0.0
    assert w.pending is not None
    w.resolve_rebase()
    assert w.q != 0.0
    assert w.pending is None


def test_identical_probe_different_prior():
    a, b = Lean(), Lean()
    for _ in range(8):
        a.propose(1, 1, 1, 1)
        a.resolve_rebase()
    assert a.probe()["q"] != b.probe()["q"]
    assert a.state != "HOLD" or a.magnitude > 0


def test_disuse_softens():
    w = Lean(q=0.4, r=R_HARD)
    for _ in range(30):
        w.soften()
    assert w.r < R_HARD
    assert abs(w.q) < 0.4


def test_bands_have_dead_zones():
    names = [n for n, _, _ in BANDS]
    assert names.count("DEAD") == 4
    assert "HOLD" in names


def test_four_branch_lock():
    tick = Zer0Tick(Lean(), Lean(), Lean(), Lean())
    tick.use("x", 1, 1, 1)
    assert tick.x_lean.q == 0.0
    out = tick.t6()
    assert out["X"] != 0.0


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"PASS  {name}")
    print("lean_weight ok")
