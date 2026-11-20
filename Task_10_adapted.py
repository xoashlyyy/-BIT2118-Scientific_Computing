"""Task 10 - real-world adaptation (E)."""
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
section("E. RELATED CASE: break-even quantity, profit(q)=50q-(2000+20q+0.01q^2)")
p=lambda q:50*q-(2000+20*q+0.01*q**2)
for br in ([1,200],[200,3000]):
    r=root_scalar(p,bracket=br,method="bisect",xtol=1e-9); print(f"Break-even at q = {r.root:.2f} units")
q=np.linspace(0,3000,400); plt.plot(q,p(q)); plt.axhline(0,lw=.8); plt.xlabel("Units sold"); plt.ylabel("Profit"); plt.grid(True); plt.title("Break-even"); save("Task_10_breakeven.png")
