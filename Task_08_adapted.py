"""Task 08 - real-world adaptation (E)."""
import numpy as np
from common import section, plt, save
def build(n,left,right):
    A=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1); b=np.zeros(n); b[0]=left; b[-1]=right; return A,b
def jacobi(A,b,tol=1e-8,mx=5000):
    D=np.diag(A); R=A-np.diagflat(D); x=np.zeros_like(b); errs=[]
    for _ in range(mx):
        xn=(b-R@x)/D; e=np.linalg.norm(xn-x,np.inf); errs.append(e); x=xn
        if e<tol: break
    return x,errs
def gs(A,b,tol=1e-8,mx=5000):
    x=np.zeros_like(b); errs=[]
    for _ in range(mx):
        old=x.copy()
        for i in range(len(b)): x[i]=(b[i]-A[i,:i]@x[:i]-A[i,i+1:]@old[i+1:])/A[i,i]
        e=np.linalg.norm(x-old,np.inf); errs.append(e)
        if e<tol: break
    return x,errs
section("E. RELATED CASE: metal rod, 10 interior points, ends at 0 C and 80 C")
A,b=build(10,0,80); x,e=gs(A,b); print("Temperatures along rod:",np.round(x,2)); print("Iterations:",len(e))
print("Linear profile expected (steady state): ",np.round(np.linspace(80/11,80*10/11,10),2))
