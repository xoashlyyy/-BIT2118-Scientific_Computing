"""Task 16 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from scipy.integrate import simpson
from common import section
trap=getattr(np,"trapezoid",None) or np.trapz
tt=np.array([0,2,4,6,8,10,12.]); P=np.array([.8,1,1.4,1.8,1.6,1.2,.9])
section("A. ORIGINAL"); e1=trap(P,tt); e2=simpson(P,x=tt); print(f"Trapezoid {e1:.3f} kWh | Simpson {e2:.3f} kWh | diff {abs(e1-e2):.3f}")
section("C. CHANGED INPUT: peak reading 1.8 -> 3.0 kW; and hourly sampling of smooth model")
P2=P.copy(); P2[3]=3.0; print(f"Trapezoid {trap(P2,tt):.3f} | Simpson {simpson(P2,x=tt):.3f}")
f=lambda t:np.sin(t); ex=1-np.cos(np.pi)*-1 if False else 2.0
for n in (5,9,33):
    x=np.linspace(0,np.pi,n); print(f"n={n:2d} points on sin(x), exact 2: trap err {abs(trap(f(x),x)-2):.2e} | Simpson err {abs(simpson(f(x),x=x)-2):.2e}")
