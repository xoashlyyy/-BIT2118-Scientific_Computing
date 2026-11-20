"""Task 12 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from scipy.optimize import root
from common import section
def inter(R,guesses):
    eq=lambda z:[z[0]**2+z[1]**2-R**2, z[1]-(z[0]**2-1)]
    for g in guesses:
        s=root(eq,g); print(f"  guess {g} -> {np.round(s.x,5)} residual {np.round(eq(s.x),10)} converged={s.success}")
section("A. ORIGINAL (R=2)"); inter(2,([1.,1.],[-1.,1.]))
section("C. CHANGED INPUT: radius 2 -> 1 (circle may only touch/miss)"); inter(1,([1.,1.],[-1.,1.],[0.5,-0.5]))
section("C2. CHANGED INPUT: radius 0.5 (no real intersection)"); inter(0.5,([1.,1.],))
