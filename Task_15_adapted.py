"""Task 15 - real-world adaptation (E)."""
import numpy as np
from common import section, plt, save
def speeds(t,x):
    v=np.zeros_like(x); v[0]=(x[1]-x[0])/(t[1]-t[0])
    for i in range(1,len(t)-1): v[i]=(x[i+1]-x[i-1])/(t[i+1]-t[i-1])
    v[-1]=(x[-1]-x[-2])/(t[-1]-t[-2]); return v
t=np.arange(7.); x=np.array([0,4.8,10.2,16.1,22.7,30.,38.])
section("E. RELATED CASE: acceleration of a car from velocity readings (np.gradient)")
tv=np.arange(0,6.); vv=np.array([0,3.1,6.5,10.4,14.0,17.2]); a=np.gradient(vv,tv)
print("Acceleration (m/s^2):",np.round(a,2),"| mean %.2f"%a.mean())
