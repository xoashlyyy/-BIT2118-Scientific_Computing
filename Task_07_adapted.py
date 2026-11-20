"""Task 07 - real-world adaptation (E)."""
import numpy as np, timeit
from scipy.linalg import lu_factor, lu_solve
from common import section
A=np.array([[4.,-1,0],[-1,4,-1],[0,-1,3]])
sets=[np.array([15.,10,10]),np.array([16.,11,9]),np.array([14.,12,11])]
section("E. RELATED CASE: Leontief input-output economy (3 sectors, 3 demand scenarios)")
T=np.array([[0.2,0.3,0.1],[0.1,0.1,0.3],[0.2,0.2,0.1]])   # input needed per unit output
M=np.eye(3)-T; f=lu_factor(M)
for name,d in [("Base",[100,80,60]),("Demand +20% agri",[120,80,60]),("Recession",[80,60,40])]:
    out=lu_solve(f,np.array(d,float)); print(f"{name:18s} total output required:",np.round(out,2))
