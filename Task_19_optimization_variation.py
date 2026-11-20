"""Task 19 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from scipy.optimize import minimize
from common import section
def opt(cA,cB,kA,kB,req):
    r=minimize(lambda z:cA*z[0]+cB*z[1],[5,3],method="SLSQP",bounds=[(0,None)]*2,constraints={"type":"ineq","fun":lambda z:kA*z[0]+kB*z[1]-req})
    best=min(((cA*a+cB*b,a,b,kA*a+kB*b) for a in range(0,40) for b in range(0,40) if kA*a+kB*b>=req))
    return r,best
section("A. ORIGINAL"); r,b=opt(12,18,100,170,1000); print("A=%.3f B=%.3f cost=%.2f | integer best (cost,A,B,cap)=%s"%(r.x[0],r.x[1],r.fun,b))
section("C. CHANGED INPUT: Type B price rises 18 -> 25"); r,b=opt(12,25,100,170,1000); print("A=%.3f B=%.3f cost=%.2f | integer best=%s"%(r.x[0],r.x[1],r.fun,b))
section("C2. CHANGED INPUT: capacity requirement 1000 -> 2500"); r,b=opt(12,18,100,170,2500); print("A=%.3f B=%.3f cost=%.2f | integer best=%s"%(r.x[0],r.x[1],r.fun,b))
