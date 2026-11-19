import numpy as np
from _common import section, plt, save
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
section("A. ORIGINAL (5 nodes, 100 C and 20 C boundaries)")
A,b=build(5,100,20); xj,ej=jacobi(A,b); xg,eg=gs(A,b)
print("Jacobi:",np.round(xj,4),"iters",len(ej)); print("Gauss-Seidel:",np.round(xg,4),"iters",len(eg)); print("Direct:",np.round(np.linalg.solve(A,b),4))
plt.semilogy(ej,label="Jacobi"); plt.semilogy(eg,label="Gauss-Seidel"); plt.xlabel("Iteration"); plt.ylabel("Max change"); plt.legend(); plt.grid(True); plt.title("Convergence"); save("Task_08_convergence.png")
section("C. CHANGED INPUT: tolerance 1e-3 vs 1e-12, and grid size 5 vs 20 nodes")
for tol in (1e-3,1e-12): print(f"tol={tol:.0e}: Jacobi {len(jacobi(A,b,tol)[1])} iters, GS {len(gs(A,b,tol)[1])} iters")
A20,b20=build(20,100,20); print("20 nodes: Jacobi",len(jacobi(A20,b20)[1]),"iters, GS",len(gs(A20,b20)[1]),"iters")
section("E. RELATED CASE: metal rod, 10 interior points, ends at 0 C and 80 C")
A,b=build(10,0,80); x,e=gs(A,b); print("Temperatures along rod:",np.round(x,2)); print("Iterations:",len(e))
print("Linear profile expected (steady state): ",np.round(np.linspace(80/11,80*10/11,10),2))
