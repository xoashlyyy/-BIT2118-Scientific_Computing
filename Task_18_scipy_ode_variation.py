"""Task 18 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from scipy.integrate import solve_ivp
from common import section, plt, save
def rc(Vs,R,C,tend,V0=0.):
    te=np.linspace(0,tend,200)
    s=solve_ivp(lambda t,V:[(Vs-V[0])/(R*C)],(0,tend),[V0],t_eval=te,rtol=1e-9,atol=1e-11)
    return s,Vs+(V0-Vs)*np.exp(-s.t/(R*C))
section("A. ORIGINAL (R=1k, C=1mF, tau=1 s)")
s,ex=rc(5,1000,0.001,5); print("success",s.success,f"| V(5s)={s.y[0,-1]:.4f} V | max error {np.max(abs(s.y[0]-ex)):.2e}")
plt.plot(s.t,s.y[0],label="solve_ivp"); plt.plot(s.t,ex,"--",label="Exact"); plt.xlabel("Time (s)"); plt.ylabel("V"); plt.legend(); plt.grid(True); plt.title("RC charging"); save("Task_18_rc.png")
section("C. CHANGED INPUT: R=4.7k (tau=4.7 s) -> V at 1 s and 5 s")
s,_=rc(5,4700,0.001,5); print(f"V(1s)~{np.interp(1,s.t,s.y[0]):.3f} V, V(5s)={s.y[0,-1]:.3f} V (original reached {5*(1-np.exp(-5)):.3f} V)")
section("C2. CHANGED INPUT: discharge from V0=5 V with Vs=0")
s,_=rc(0,1000,0.001,5,V0=5); print(f"V(1s)~{np.interp(1,s.t,s.y[0]):.3f} V (expected 5/e = {5/np.e:.3f}), V(5s)={s.y[0,-1]:.4f}")
