"""Task 11 - baseline (A) and parameter-variation experiments (C)."""
from scipy.optimize import root_scalar
from common import section
def make(cf):
    npv=lambda r:sum(c/(1+r)**t for t,c in enumerate(cf))
    d=lambda r:sum(-t*c/(1+r)**(t+1) for t,c in enumerate(cf) if t>0)
    return npv,d
def irr(cf,x0=0.10):
    npv,d=make(cf)
    n=root_scalar(npv,fprime=d,x0=x0,method="newton",xtol=1e-12)
    s=root_scalar(npv,x0=0.05,x1=0.20,method="secant",xtol=1e-12)
    return n,s
section("A. ORIGINAL")
cf=[-10000,3000,3500,4000,2500]; n,s=irr(cf)
print(f"Newton IRR {n.root:.6%} ({n.iterations} iters) | Secant IRR {s.root:.6%} ({s.iterations} iters)")
section("C. CHANGED INPUT: investment 12000 instead of 10000")
n,s=irr([-12000,3000,3500,4000,2500]); print(f"Newton IRR {n.root:.6%} | Secant IRR {s.root:.6%}")
section("C2. CHANGED INPUT: starting guess x0 = 0.90 for Newton")
npv,d=make(cf); n=root_scalar(npv,fprime=d,x0=0.9,method="newton"); print(f"IRR {n.root:.6%} in {n.iterations} iters")
