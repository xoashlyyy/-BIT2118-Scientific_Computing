"""Task 20 - real-world adaptation (E)."""
import numpy as np
from common import section, plt, save
def overload(cap,mu,sd,N,seed=42):
    d=np.random.default_rng(seed).normal(mu,sd,N); return (d>cap).mean()
from math import erfc, sqrt
exact=lambda cap,mu,sd:0.5*erfc((cap-mu)/(sd*sqrt(2)))
section("E. RELATED CASE: estimate pi by random points in a unit square")
for N in (100,10_000,1_000_000):
    pts=np.random.default_rng(7).random((N,2)); est=4*np.mean((pts**2).sum(1)<=1); print(f"N={N:>9,}: pi ~ {est:.5f}  error {abs(est-np.pi):.5f}")
