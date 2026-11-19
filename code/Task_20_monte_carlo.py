import numpy as np
from _common import section, plt, save
def overload(cap,mu,sd,N,seed=42):
    d=np.random.default_rng(seed).normal(mu,sd,N); return (d>cap).mean()
from math import erfc, sqrt
exact=lambda cap,mu,sd:0.5*erfc((cap-mu)/(sd*sqrt(2)))
section("A. ORIGINAL"); p=overload(1000,850,120,100_000); print(f"Estimated {p:.4%} | theoretical {exact(1000,850,120):.4%}")
rng=np.random.default_rng(42); d=rng.normal(850,120,100_000); o=d>1000; run=np.cumsum(o)/np.arange(1,len(o)+1)
idx=np.unique(np.logspace(1,5,200).astype(int))-1; plt.semilogx(idx+1,run[idx]); plt.axhline(exact(1000,850,120),ls="--"); plt.xlabel("Simulations"); plt.ylabel("Estimated probability"); plt.grid(True); plt.title("Monte Carlo convergence"); save("Task_20_convergence.png")
section("C. CHANGED INPUT: N and standard deviation")
for N in (100,1000,100_000): print(f"N={N:>7,}: {overload(1000,850,120,N):.4%}")
for sd in (60,120,200): print(f"std={sd}: {overload(1000,850,sd,100_000):.4%} (theory {exact(1000,850,sd):.4%})")
section("E. RELATED CASE: estimate pi by random points in a unit square")
for N in (100,10_000,1_000_000):
    pts=np.random.default_rng(7).random((N,2)); est=4*np.mean((pts**2).sum(1)<=1); print(f"N={N:>9,}: pi ~ {est:.5f}  error {abs(est-np.pi):.5f}")
