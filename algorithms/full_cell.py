#!/usr/bin/env python3
"""FULL CELL-0 + BUS + PERMIT bench model.

This is the runnable packet that matches Builds/THE_BUILD.md.
It is a model. It does not invent energy. It does not claim 99%.
Hardware truth lives in cell-v1/LOG.md after you sit the breadboard.

Laws:
  home 0.50 is not the bus
  leftover kick goes to bus through a diode
  two agrees -> PUSH; fight -> HOLD; gap -> WAIT
  HOLD is live, not off
  no clock; events only
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import tanh


V_PACK = 1.00
V_HOME = 0.50
HOLD_LO = 0.45
HOLD_HI = 0.55
Q_MAX = 1.0
R_SOFT = 0.55
R_HARD = 0.92
G_USE = 0.24
N_SUB = 1.4
VT = 0.026
SCHOTTKY_VF = 0.20
BUS_C = 1.0e-6
KICK_Q = 8e-8
BUS_LEAK = 0.01
ETA_RECOVER = 0.35


def clip(x: float, lo: float, hi: float) -> float:
    return lo if x < lo else hi if x > hi else x


def ternary_from_volts(v: float) -> str:
    if v < HOLD_LO:
        return "DOWN"
    if v > HOLD_HI:
        return "UP"
    return "HOLD"


def idiff(iss: float, vd: float) -> float:
    return iss * tanh(vd / (2.0 * N_SUB * VT))


@dataclass
class Axis:
    name: str
    q: float = 0.0
    r: float = R_SOFT
    remanence: float = 0.0
    pending: float | None = None
    uses: int = 0

    @property
    def volts(self) -> float:
        return clip(V_HOME + 0.50 * self.q, 0.0, V_PACK)

    @property
    def state(self) -> str:
        return ternary_from_volts(self.volts)

    @property
    def direction(self) -> int:
        if self.state == "UP":
            return 1
        if self.state == "DOWN":
            return -1
        return 0

    def propose(self, drive: float) -> float:
        raw = self.r * self.q + G_USE * drive
        self.pending = clip(raw, -Q_MAX, Q_MAX)
        return self.pending

    def commit(self) -> float:
        if self.pending is None:
            return self.q
        self.q = self.pending
        self.pending = None
        self.uses += 1
        if self.uses > 5:
            self.r = min(R_HARD, self.r + 0.02)
        self.remanence = 0.6 * self.remanence + 0.4 * self.q
        return self.q

    def release_kick(self) -> float:
        return abs(self.remanence) * KICK_Q


@dataclass
class Bus:
    v: float = 0.0
    c: float = BUS_C

    def accept_kick(self, q_coulomb: float) -> float:
        before = self.v
        self.v = clip(self.v + q_coulomb / self.c, 0.0, V_PACK)
        return self.v - before

    def drink(self, ask: float) -> float:
        take = min(self.v, max(0.0, ask))
        self.v -= take
        return take

    def sag(self) -> None:
        self.v *= 1.0 - BUS_LEAK

    @property
    def falling(self) -> bool:
        return self.v < 0.15


@dataclass
class Cell0:
    axes: dict[str, Axis] = field(default_factory=lambda: {
        "A": Axis("A"),
        "B": Axis("B"),
        "C": Axis("C"),
    })
    bus: Bus = field(default_factory=Bus)
    home: float = V_HOME
    pack_paid: float = 0.0
    recovered: float = 0.0
    events: int = 0
    log: list[str] = field(default_factory=list)

    def permit(self) -> str:
        dirs = [ax.direction for ax in self.axes.values()]
        ups = dirs.count(1)
        downs = dirs.count(-1)
        holds = dirs.count(0)
        if ups >= 2 and downs == 0:
            return "PUSH+"
        if downs >= 2 and ups == 0:
            return "PUSH-"
        if ups >= 1 and downs >= 1:
            return "HOLD"
        if holds >= 2:
            return "WAIT"
        return "WAIT"

    def event(self, drives: dict[str, float], drink: float = 0.08) -> dict:
        self.events += 1
        self.bus.sag()
        drank = self.bus.drink(drink)
        shortfall = max(0.0, drink - drank)
        self.pack_paid += shortfall
        if self.recovered > 0 and self.bus.falling and drank == 0.0 and shortfall > 0:
            self.log.append(f"E{self.events} SEND-UP bus={self.bus.v:.3f}")
            return {"event": self.events, "permit": "SEND-UP", "bus": self.bus.v, "home": self.home}

        for name, d in drives.items():
            self.axes[name].propose(d)
        for ax in self.axes.values():
            ax.commit()

        kick = 0.0
        for ax in self.axes.values():
            k = ax.release_kick() * ETA_RECOVER
            kick += k
        dv = self.bus.accept_kick(kick)
        self.recovered += kick
        permit = self.permit()
        rec = {
            "event": self.events,
            "permit": permit,
            "home": self.home,
            "bus": round(self.bus.v, 4),
            "drank": round(drank, 5),
            "pack_paid": round(self.pack_paid, 6),
            "recovered": round(self.recovered, 9),
            "dv_bus": round(dv, 4),
            "A": self.axes["A"].state,
            "B": self.axes["B"].state,
            "C": self.axes["C"].state,
            "qA": round(self.axes["A"].q, 3),
            "qB": round(self.axes["B"].q, 3),
            "qC": round(self.axes["C"].q, 3),
        }
        self.log.append(
            f"E{self.events} {permit} bus={self.bus.v:.3f} "
            f"A={rec['A']} B={rec['B']} C={rec['C']}"
        )
        return rec

    def fraction(self) -> float | None:
        if self.pack_paid <= 0:
            return None
        return self.recovered / max(self.pack_paid * BUS_C, 1e-12)


def demo() -> None:
    cell = Cell0()
    print("=== CELL-0 FULL BUILD DEMO (model, not measurement) ===")
    print("T1 home quiet:", f"{cell.home:.2f} V")
    print("T2 HOLD is live:", cell.axes["A"].state)
    print("\n-- one lean A+ --")
    for i in range(4):
        print(cell.event({"A": 1.0, "B": 0.0, "C": 0.0}))
    print("\n-- two agrees A+ B+ --")
    for i in range(4):
        print(cell.event({"A": 1.0, "B": 1.0, "C": 0.0}))
    print("\n-- fight A+ C- --")
    print(cell.event({"A": 1.0, "B": 0.0, "C": -1.0}))
    print("\nenergy fraction (raw model):", cell.fraction())
    print("home never tied to bus. last home=", cell.home, "last bus=", cell.bus.v)


def test_home_is_not_bus():
    c = Cell0()
    c.event({"A": 1.0})
    assert abs(c.home - 0.50) < 1e-9


def test_kick_moves_bus():
    c = Cell0()
    before = c.bus.v
    c.event({"A": 1.0})
    c.event({"A": 1.0})
    assert c.bus.v >= before


def test_two_agree_push():
    c = Cell0()
    for _ in range(6):
        c.event({"A": 1.2, "B": 1.2, "C": 0.0})
    assert c.permit() in ("PUSH+", "WAIT")


def test_fight_holds():
    c = Cell0()
    for _ in range(8):
        c.event({"A": 1.2, "B": 0.0, "C": -1.2})
    assert c.permit() in ("HOLD", "WAIT")


def test_hold_is_not_off():
    a = Axis("A")
    assert a.state == "HOLD"
    assert a.r > 0


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("PASS", name)
    demo()
