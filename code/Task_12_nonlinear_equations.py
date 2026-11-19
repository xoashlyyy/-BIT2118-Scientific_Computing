import numpy as np
from scipy.optimize import root
from _common import section
def inter(R,guesses):
    eq=lambda z:[z[0]**2+z[1]**2-R**2, z[1]-(z[0]**2-1)]
    for g in guesses:
        s=root(eq,g); print(f"  guess {g} -> {np.round(s.x,5)} residual {np.round(eq(s.x),10)} converged={s.success}")
section("A. ORIGINAL (R=2)"); inter(2,([1.,1.],[-1.,1.]))
section("C. CHANGED INPUT: radius 2 -> 1 (circle may only touch/miss)"); inter(1,([1.,1.],[-1.,1.],[0.5,-0.5]))
section("C2. CHANGED INPUT: radius 0.5 (no real intersection)"); inter(0.5,([1.,1.],))
section("E. RELATED CASE: kinematics. Ball: h(t)=2+20t-4.9t^2. When is h = 10 m?")
r=np.roots([-4.9,20,2-10]); print("Times (s):",np.round(r,4),"-> goes up at",round(min(r),3),"s and comes down at",round(max(r),3),"s")
print("Time to hit ground (h=0):",np.round(np.roots([-4.9,20,2]),4))
section("E2. polynomial x^2-5x+6"); print("roots:",np.roots([1,-5,6]))
