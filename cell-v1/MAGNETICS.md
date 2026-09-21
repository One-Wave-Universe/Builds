# Magnetics

The part you buy is a **toroid** (or two toroids making the figure-8). Square-loop ferrite / magamp tape. Not an EMI bead.

## Field on a toroid

Mean magnetic path ℓ_e around the ring.

```
H = N I / ℓ_e
B = μ(H, history)     ← μ is not a constant. That is hysteresis.
Φ = B · A_e
λ = N Φ
v = dλ/dt = N dΦ/dt
```

Ampère: current in the winding *is* H. Faraday: when Φ changes, the same winding *is* the voltage that the gate sends to V_BUS.

Energy in the field ~ ∫ H·dB · volume. Loop area is loss-per-cycle. Minor loop → small area. Major loop → large area.

Remanence: I → 0, H → 0, B → Br ≠ 0. That Br is old state in iron.

## Toroid per window

Figure-8 = **two toroids** (or one binoc / two-hole core) with a shared or tightly coupled center. Each toroid is one window (+ or −).

```
   (toroid +)     (toroid −)
      A+             A-
        \           /
         shared sense of one axis
```

Wind the same N on each ring, opposite sense if you want D to be the difference of two λ's. Or one winding through both holes like a common-mode choke — then the figure-8 *is* the differential.

Cell-0: **one toroid** on CENTER / on the pair so Br leftover is visible.
Full cell: two toroids per axis × three axes = six rings, or three binoc cores. Still one settled cell state on V_BUS + CENTER.

## Why toroid not a rod

Closed path. Flux stays in the ferrite. Little stray H to write the neighbor axis. 120° and closed rings are the isolation. A bar through the hex center would yoke all three — illegal.

## Numbers (order, not a bench log)

Square ferrite: Br/Bm high, Hc set by mix (NiZn / MnZn square, or tape 80 permalloy). Turns N: enough λ that dλ/dt at your event speed is a clean pulse into C_steer, not a spark and not invisible. Cell-0: whatever fits the 9 V flyback the diode can eat.
