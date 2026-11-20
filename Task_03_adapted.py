"""Task 03 - real-world adaptation (E)."""
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
section("E. RELATED CASE: gamma correction of a 1000x1000 grey image")
rng = np.random.default_rng(1)
img = rng.integers(0, 256, (1000, 1000)).astype(float)/255
import time
t0=time.perf_counter(); out=np.empty_like(img)
for i in range(200):                      # loop on 200 rows only (to save time)
    for j in range(1000): out[i,j]=img[i,j]**(1/2.2)
loop_est=(time.perf_counter()-t0)*5
t0=time.perf_counter(); g = img**(1/2.2); vt=time.perf_counter()-t0
print(f"Mean brightness before {img.mean():.3f}, after gamma {g.mean():.3f}")
print(f"Estimated full loop {loop_est:.2f}s vs vectorized {vt:.4f}s (~{loop_est/vt:.0f}x faster)")
