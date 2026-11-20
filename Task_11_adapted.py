"""Task 11 - real-world adaptation (E)."""
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
section("E. RELATED CASE: loan rate. Borrow 5000, repay 450/month for 12 months")
npv=lambda r:5000-sum(450/(1+r)**t for t in range(1,13))
s=root_scalar(npv,x0=0.01,x1=0.03,method="secant",xtol=1e-12)
print(f"Monthly rate {s.root:.4%}  -> nominal annual {12*s.root:.2%}, effective annual {(1+s.root)**12-1:.2%}")
print("Total repaid:",450*12,"| interest paid:",450*12-5000)
