import numpy as np
from _common import section
section("A. ORIGINAL: servers")
A=np.array([[4.,2],[8,12]]); b=np.array([20.,72]); x=np.linalg.solve(A,b)
print("Type A, Type B:",x,"| residual norm",np.linalg.norm(b-A@x))
section("C. CHANGED INPUT: totals 30 CPU and 100 GB")
x2=np.linalg.solve(A,np.array([30.,100])); print("Solution:",x2)
print("Note: non-integer -> measurement inconsistent with whole servers")
section("C2. CHANGED INPUT: nearly singular matrix (Type B ~ 2x Type A)")
A3=np.array([[4.,2],[8.,4.0001]]); print("cond(A) =",np.linalg.cond(A),"-> cond(A3) =",np.linalg.cond(A3))
print("Solution with b=[20,40]:",np.linalg.solve(A3,[20,40]),"| with b=[20,40.01]:",np.linalg.solve(A3,[20,40.01]))
section("E. RELATED CASE: 3-loop circuit mesh currents (Kirchhoff voltage law)")
R=np.array([[10,-4,0],[-4,12,-5],[0,-5,9.]]); V=np.array([12,0,-6.])
I=np.linalg.solve(R,V); print("Mesh currents (A):",np.round(I,4),"| residual",np.linalg.norm(V-R@I))
