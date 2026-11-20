"""Task 09 - real-world adaptation (E)."""
import numpy as np
from common import section
def centrality(A,names):
    w,v=np.linalg.eig(A); i=np.argmax(w.real); vec=np.abs(v[:,i].real); c=vec/vec.sum()
    return w[i].real,{n:round(s,4) for n,s in zip(names,c)},np.linalg.norm(A@v[:,i].real-w[i].real*v[:,i].real)
section("E. RELATED CASE: PCA on exam scores (Maths vs Physics) via covariance eigenvectors")
rng=np.random.default_rng(3); maths=rng.normal(60,12,50); phys=0.8*maths+rng.normal(0,5,50)
X=np.c_[maths,phys]; C=np.cov(X.T); w,v=np.linalg.eigh(C)
print("Covariance:\n",np.round(C,2)); print("Eigenvalues:",np.round(w,2))
print("Variance explained by PC1: %.1f %%"%(100*w[-1]/w.sum())); print("PC1 direction:",np.round(v[:,-1],3))
