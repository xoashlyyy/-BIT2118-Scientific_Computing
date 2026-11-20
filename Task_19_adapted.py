"""Task 19 - real-world adaptation (E)."""
import numpy as np
from scipy.optimize import minimize
from common import section
def opt(cA,cB,kA,kB,req):
    r=minimize(lambda z:cA*z[0]+cB*z[1],[5,3],method="SLSQP",bounds=[(0,None)]*2,constraints={"type":"ineq","fun":lambda z:kA*z[0]+kB*z[1]-req})
    best=min(((cA*a+cB*b,a,b,kA*a+kB*b) for a in range(0,40) for b in range(0,40) if kA*a+kB*b>=req))
    return r,best
section("E. RELATED CASE: diet problem. Food X (3 per unit, 20 g protein, 300 kcal), Food Y (2, 10 g, 500 kcal). Need >=60 g protein and >=1500 kcal")
r=minimize(lambda z:3*z[0]+2*z[1],[3,3],method="SLSQP",bounds=[(0,None)]*2,constraints=[{"type":"ineq","fun":lambda z:20*z[0]+10*z[1]-60},{"type":"ineq","fun":lambda z:300*z[0]+500*z[1]-1500}])
print("Food X %.3f, Food Y %.3f, cost %.3f"%(r.x[0],r.x[1],r.fun),"| protein %.1f g, energy %.0f kcal"%(20*r.x[0]+10*r.x[1],300*r.x[0]+500*r.x[1]))
