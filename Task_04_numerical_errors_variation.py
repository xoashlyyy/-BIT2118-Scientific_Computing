"""Task 04 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np, math
from common import section
section("A. ORIGINAL")
c = 0.1+0.2
print("0.1+0.2 =", c, "| exact ==:", c==0.3, "| isclose:", np.isclose(c,0.3))
ae = abs(np.sqrt(2)-1.414); print(f"Abs err {ae:.8f}, rel err {ae/np.sqrt(2):.8%}")
for x in [1e-4,1e-8,1e-12]:
    d=(np.sqrt(1+x)-1)/x; s=1/(np.sqrt(1+x)+1)
    print(f"x={x:.0e}: direct={d:.12f}, stable={s:.12f}")
section("C. CHANGED INPUT: approximation 1.41421 instead of 1.414; smaller x")
ae = abs(np.sqrt(2)-1.41421); print(f"Abs err {ae:.3e}, rel err {ae/np.sqrt(2):.6%}")
for x in [1e-14,1e-16]:
    d=(np.sqrt(1+x)-1)/x; s=1/(np.sqrt(1+x)+1)
    print(f"x={x:.0e}: direct={d:.12f}, stable={s:.12f}")
