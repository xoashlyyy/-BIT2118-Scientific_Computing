import numpy as np
from _common import section, plt, save
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
section("E. RELATED CASE: logistic population growth dP/dt=r P (1-P/K), r=0.4, K=1000, P0=50")
def logi(h,r=0.4,K=1000,P0=50,end=30):
    t=np.arange(0,end+h,h); P=np.zeros_like(t); P[0]=P0
    for i in range(len(t)-1): P[i+1]=P[i]+h*r*P[i]*(1-P[i]/K)
    return t,P
t,P=logi(0.5); print("Population at t=10,20,30:",[round(float(P[int(x/0.5)]),1) for x in (10,20,30)]); 
plt.plot(t,P); plt.xlabel("Time"); plt.ylabel("Population"); plt.grid(True); plt.title("Logistic growth (Euler)"); save("Task_17_logistic.png")
