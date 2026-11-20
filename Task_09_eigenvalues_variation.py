"""Task 09 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from common import section
def centrality(A,names):
    w,v=np.linalg.eig(A); i=np.argmax(w.real); vec=np.abs(v[:,i].real); c=vec/vec.sum()
    return w[i].real,{n:round(s,4) for n,s in zip(names,c)},np.linalg.norm(A@v[:,i].real-w[i].real*v[:,i].real)
section("A. ORIGINAL")
A=np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0.]]); print(centrality(A,"ABCD"))
section("C. CHANGED INPUT: add link A-D")
A2=A.copy(); A2[0,3]=A2[3,0]=1; print(centrality(A2,"ABCD"))
section("C2. CHANGED INPUT: remove node B's links to A and D (B becomes weak)")
A3=A.copy(); A3[0,1]=A3[1,0]=0; A3[1,3]=A3[3,1]=0; print(centrality(A3,"ABCD"))
