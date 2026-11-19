from scipy.optimize import root_scalar
from _common import section
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
section("E. RELATED CASE: loan rate. Borrow 5000, repay 450/month for 12 months")
npv=lambda r:5000-sum(450/(1+r)**t for t in range(1,13))
s=root_scalar(npv,x0=0.01,x1=0.03,method="secant",xtol=1e-12)
print(f"Monthly rate {s.root:.4%}  -> nominal annual {12*s.root:.2%}, effective annual {(1+s.root)**12-1:.2%}")
print("Total repaid:",450*12,"| interest paid:",450*12-5000)
