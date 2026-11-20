"""Task 18 - real-world adaptation (E)."""
import numpy as np
from scipy.integrate import solve_ivp
from common import section, plt, save
def rc(Vs,R,C,tend,V0=0.):
    te=np.linspace(0,tend,200)
    s=solve_ivp(lambda t,V:[(Vs-V[0])/(R*C)],(0,tend),[V0],t_eval=te,rtol=1e-9,atol=1e-11)
    return s,Vs+(V0-Vs)*np.exp(-s.t/(R*C))
section("E. RELATED CASE: SIR epidemic, N=10000, beta=0.4, gamma=0.1")
b,g,N=0.4,0.1,10000
def sir(t,y): S,I,R=y; return [-b*S*I/N, b*S*I/N-g*I, g*I]
s=solve_ivp(sir,(0,160),[N-10,10,0],t_eval=np.linspace(0,160,400),rtol=1e-8)
pk=np.argmax(s.y[1]); print(f"R0={b/g:.1f} | peak infected {s.y[1,pk]:.0f} at day {s.t[pk]:.0f} | total ever infected {s.y[2,-1]+s.y[1,-1]:.0f}")
for i,n in enumerate(["Susceptible","Infected","Recovered"]): plt.plot(s.t,s.y[i],label=n)
plt.xlabel("Day"); plt.ylabel("People"); plt.legend(); plt.grid(True); plt.title("SIR model"); save("Task_18_sir.png")
