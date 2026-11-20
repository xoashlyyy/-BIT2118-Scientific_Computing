"""Task 10 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from scipy.optimize import root_scalar
from common import section, plt, save
def solve(amb,amp,tau,bracket):
    f=lambda T:T-amb-amp*np.exp(-T/tau); g=lambda T:amb+amp*np.exp(-T/tau)
    r=root_scalar(f,bracket=bracket,method="bisect",xtol=1e-10)
    T=30.0;n=0
    for n in range(1,200):
        Tn=g(T)
        if abs(Tn-T)<1e-10: T=Tn;break
        T=Tn
    return f,r,T,n
section("A. ORIGINAL")
f,r,T,n=solve(25,10,20,[20,40]); print(f"Bisection {r.root:.6f} C ({r.iterations} iters) | Fixed-point {T:.6f} C ({n} iters)")
ts=np.linspace(20,40,300); plt.plot(ts,f(ts)); plt.axhline(0,lw=.8); plt.axvline(r.root,ls="--"); plt.xlabel("Temperature (C)"); plt.ylabel("f(T)"); plt.grid(True); plt.title("Equilibrium temperature"); save("Task_10_root.png")
section("C. CHANGED INPUT: ambient 25->35 C, amplitude 10->20")
f,r,T,n=solve(35,20,20,[20,60]); print(f"Bisection {r.root:.6f} C | Fixed-point {T:.6f} C ({n} iters)")
section("C2. CHANGED INPUT: bracket [30,40] has no sign change")
try: root_scalar(lambda T:T-25-10*np.exp(-T/20),bracket=[30,40],method="bisect")
except ValueError as e: print("Error:",e)
