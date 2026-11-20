"""Task 16 - real-world adaptation (E)."""
import numpy as np
from scipy.integrate import simpson
from common import section
trap=getattr(np,"trapezoid",None) or np.trapz
tt=np.array([0,2,4,6,8,10,12.]); P=np.array([.8,1,1.4,1.8,1.6,1.2,.9])
section("E. RELATED CASE: total water volume from a flow meter (L/s every 10 s)")
ts=np.arange(0,70,10.); q=np.array([0,2.5,4.0,4.8,4.2,2.0,0.5])
print(f"Volume trapezoid {trap(q,ts):.1f} L | Simpson {simpson(q,x=ts):.1f} L")
