import numpy as np
from _common import section, plt, save
def speeds(t,x):
    v=np.zeros_like(x); v[0]=(x[1]-x[0])/(t[1]-t[0])
    for i in range(1,len(t)-1): v[i]=(x[i+1]-x[i-1])/(t[i+1]-t[i-1])
    v[-1]=(x[-1]-x[-2])/(t[-1]-t[-2]); return v
t=np.arange(7.); x=np.array([0,4.8,10.2,16.1,22.7,30.,38.])
section("A. ORIGINAL"); v=speeds(t,x)
for a,b,c in zip(t,x,v): print(f"t={a:.0f}s pos={b:.1f}m speed={c:.2f}m/s")
plt.plot(t,v,marker="o"); plt.xlabel("Time (s)"); plt.ylabel("Speed (m/s)"); plt.grid(True); plt.title("Speed from GPS"); save("Task_15_speed.png")
section("C. CHANGED INPUT: step size h for f=sin(x) at x=1 (exact cos(1)=%.8f)"%np.cos(1))
for h in (0.1,0.01,0.001,1e-6,1e-10,1e-14):
    f=(np.sin(1+h)-np.sin(1))/h; c=(np.sin(1+h)-np.sin(1-h))/(2*h)
    print(f"h={h:.0e}: forward err {abs(f-np.cos(1)):.2e} | central err {abs(c-np.cos(1)):.2e}")
section("E. RELATED CASE: acceleration of a car from velocity readings (np.gradient)")
tv=np.arange(0,6.); vv=np.array([0,3.1,6.5,10.4,14.0,17.2]); a=np.gradient(vv,tv)
print("Acceleration (m/s^2):",np.round(a,2),"| mean %.2f"%a.mean())
