"""Task 17 - real-world adaptation (E)."""
import numpy as np
from common import section, plt, save
def cool(h,k=0.12,Ta=25.,T0=90.,end=30.):
    t=np.arange(0,end+h,h); T=np.zeros_like(t); T[0]=T0
    for i in range(len(t)-1): T[i+1]=T[i]+h*(-k*(T[i]-Ta))
    return t,T,Ta+(T0-Ta)*np.exp(-k*t)
section("E. RELATED CASE: logistic population growth dP/dt=r P (1-P/K), r=0.4, K=1000, P0=50")
def logi(h,r=0.4,K=1000,P0=50,end=30):
    t=np.arange(0,end+h,h); P=np.zeros_like(t); P[0]=P0
    for i in range(len(t)-1): P[i+1]=P[i]+h*r*P[i]*(1-P[i]/K)
    return t,P
t,P=logi(0.5); print("Population at t=10,20,30:",[round(float(P[int(x/0.5)]),1) for x in (10,20,30)]); 
plt.plot(t,P); plt.xlabel("Time"); plt.ylabel("Population"); plt.grid(True); plt.title("Logistic growth (Euler)"); save("Task_17_logistic.png")
