"""Task 17 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from common import section, plt, save
def cool(h,k=0.12,Ta=25.,T0=90.,end=30.):
    t=np.arange(0,end+h,h); T=np.zeros_like(t); T[0]=T0
    for i in range(len(t)-1): T[i+1]=T[i]+h*(-k*(T[i]-Ta))
    return t,T,Ta+(T0-Ta)*np.exp(-k*t)
section("A. ORIGINAL (h=1)")
t,T,ex=cool(1.0); print(f"Euler {T[-1]:.3f} | exact {ex[-1]:.3f} | error {abs(T[-1]-ex[-1]):.4f} C")
plt.plot(t,T,"o-",label="Euler"); plt.plot(t,ex,label="Exact"); plt.xlabel("Minutes"); plt.ylabel("Temp (C)"); plt.legend(); plt.grid(True); plt.title("Cooling"); save("Task_17_cooling.png")
section("C. CHANGED INPUT: step size")
for h in (5.0,2.0,1.0,0.5,0.1,0.01):
    t,T,ex=cool(h); print(f"h={h:<5}: Euler {T[-1]:.4f}  error {abs(T[-1]-ex[-1]):.5f}")
section("C2. CHANGED INPUT: h=20 with k=0.12 (k*h=2.4 > 2 -> unstable)")
t,T,ex=cool(20.0); print("Euler values:",np.round(T,1))
