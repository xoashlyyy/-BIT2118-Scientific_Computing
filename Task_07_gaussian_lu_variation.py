"""Task 07 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np, timeit
from scipy.linalg import lu_factor, lu_solve
from common import section
A=np.array([[4.,-1,0],[-1,4,-1],[0,-1,3]])
sets=[np.array([15.,10,10]),np.array([16.,11,9]),np.array([14.,12,11])]
section("A. ORIGINAL")
lu,piv=lu_factor(A)
for i,b in enumerate(sets,1):
    x=lu_solve((lu,piv),b); print(i,np.round(x,4),"residual",np.linalg.norm(b-A@x))
print("Direct:",np.linalg.solve(A,sets[0]))
section("C. CHANGED INPUT: 300x300 system with 500 right-hand sides (speed)")
rng=np.random.default_rng(0); n=300; B=rng.random((n,n))+n*np.eye(n); bs=rng.random((500,n))
t1=timeit.timeit(lambda:[np.linalg.solve(B,b) for b in bs],number=1)
def lu_way():
    f=lu_factor(B); return [lu_solve(f,b) for b in bs]
t2=timeit.timeit(lu_way,number=1)
print(f"Repeated solve: {t1:.3f}s | LU once + reuse: {t2:.3f}s | speed-up {t1/t2:.1f}x")
