import numpy as np
from scipy.integrate import solve_ivp
from _common import section, plt, save
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
section("E. RELATED CASE: SIR epidemic, N=10000, beta=0.4, gamma=0.1")
b,g,N=0.4,0.1,10000
def sir(t,y): S,I,R=y; return [-b*S*I/N, b*S*I/N-g*I, g*I]
s=solve_ivp(sir,(0,160),[N-10,10,0],t_eval=np.linspace(0,160,400),rtol=1e-8)
pk=np.argmax(s.y[1]); print(f"R0={b/g:.1f} | peak infected {s.y[1,pk]:.0f} at day {s.t[pk]:.0f} | total ever infected {s.y[2,-1]+s.y[1,-1]:.0f}")
for i,n in enumerate(["Susceptible","Infected","Recovered"]): plt.plot(s.t,s.y[i],label=n)
plt.xlabel("Day"); plt.ylabel("People"); plt.legend(); plt.grid(True); plt.title("SIR model"); save("Task_18_sir.png")
