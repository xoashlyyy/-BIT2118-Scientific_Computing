"""Task 03 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np, timeit
from common import section
def run(N, label):
    rng = np.random.default_rng(42)
    lat = rng.uniform(5, 250, N)
    def loop():
        out = []
        for v in lat:
            out.append((v/1000.0)**2)
        return out
    def vec():
        return (lat/1000.0)**2
    lt = timeit.timeit(loop, number=1); vt = timeit.timeit(vec, number=3)/3
    print(f"{label}: N={N:,} loop={lt:.4f}s vectorized={vt:.5f}s speed-up={lt/vt:.0f}x")
    return vec()
section("A. ORIGINAL (N = 1,000,000)")
r = run(1_000_000, "original"); print("First five:", r[:5])
section("C. CHANGED INPUT: N = 10,000 and 5,000,000")
run(10_000, "small"); run(5_000_000, "large")
