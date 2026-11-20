"""Task 06 - real-world adaptation (E)."""
import numpy as np
from common import section
section("E. RELATED CASE: 3-loop circuit mesh currents (Kirchhoff voltage law)")
R=np.array([[10,-4,0],[-4,12,-5],[0,-5,9.]]); V=np.array([12,0,-6.])
I=np.linalg.solve(R,V); print("Mesh currents (A):",np.round(I,4),"| residual",np.linalg.norm(V-R@I))
