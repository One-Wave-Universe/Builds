#!/usr/bin/env python3
"""Rabbit Hopping — reversible packet addressing. Arithmetic only. No physical claims."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Optional

ALPHABET_26 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MUSICAL_12 = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def label_to_rank(label: str, domain: str = "alphabet-26", orientation: str = "normal") -> int:
    seq = ALPHABET_26 if domain == "alphabet-26" else MUSICAL_12
    if domain == "alphabet-26":
        n = seq.index(label.upper()) + 1
    else:
        n = seq.index(label) + 1
    if orientation == "reversed":
        n = len(seq) + 1 - n
    return n

def rank_to_label(n: int, domain: str = "alphabet-26", orientation: str = "normal") -> str:
    seq = ALPHABET_26 if domain == "alphabet-26" else MUSICAL_12
    if orientation == "reversed":
        n = len(seq) + 1 - n
    return seq[n - 1]

FAMILIES = {
    "A": lambda N, K: 2 * N + K,
    "B": lambda N, K: 2 * (N + K),
    "C": lambda N, K: Fraction(N, 2) + K,
    "D": lambda N, K: Fraction(N + K, 2),
}

@dataclass
class Packet:
    source_id: str
    label: str
    domain: str
    orientation: str
    source_rank: int
    polarity: int
    route_family: str
    K: int
    center: Fraction
    wrapper_side: str
    wrapper: Fraction
    traversal_direction: str = "forward"
    hierarchy_level: int = 0
    branch_choice: Optional[str] = None
    def as_tuple(self):
        return (self.source_rank * self.polarity, self.center * self.polarity, self.wrapper * self.polarity)

def make_packets(source_id, label, domain, orientation, route_family, K, polarity=1, hierarchy_level=0):
    N = label_to_rank(label, domain, orientation)
    T = FAMILIES[route_family](N, K)
    out = []
    for side, w in (("lower", T - 1), ("upper", T + 1)):
        out.append(Packet(source_id, label, domain, orientation, N, polarity, route_family, K, T, side, w, hierarchy_level=hierarchy_level))
    return out

def mirror_packet(p: Packet) -> Packet:
    m = Packet(**{**p.__dict__})
    m.polarity = -p.polarity
    return m

def shared_wrapper_connects(a: Packet, b: Packet) -> bool:
    return (a.source_id == b.source_id and a.route_family == b.route_family
            and a.orientation == b.orientation and a.hierarchy_level == b.hierarchy_level
            and a.wrapper == b.center and b.wrapper == a.center
            and abs(a.center - b.center) == 2)

def test_source_fixed_center_moves():
    p2 = make_packets("A1", "A", "alphabet-26", "normal", "A", 0)[0]
    p4 = make_packets("A1", "A", "alphabet-26", "normal", "A", 2)[0]
    assert p2.source_rank == p4.source_rank == 1
    assert p2.center != p4.center

def test_wrappers_opposite_parity():
    ps = make_packets("A1", "A", "alphabet-26", "normal", "A", 2)
    T = ps[0].center
    assert ps[0].wrapper % 2 != T % 2
    assert ps[1].wrapper % 2 != T % 2

def test_mirror_sign():
    p = make_packets("A1", "A", "alphabet-26", "normal", "A", 2)[0]
    m = mirror_packet(p)
    assert m.polarity == -1
    assert m.route_family == p.route_family

if __name__ == "__main__":
    test_source_fixed_center_moves()
    test_wrappers_opposite_parity()
    test_mirror_sign()
    print("Rabbit Hopping tests passed.")
