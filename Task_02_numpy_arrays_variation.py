"""Task 02 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from common import section
section("A. ORIGINAL: weather station")
t = np.array([18.5,18.0,17.8,17.5,17.9,19.0,21.5,23.8,25.6,27.1,28.3,29.0,
              29.4,29.1,28.5,27.6,26.2,24.8,23.4,22.1,21.0,20.2,19.6,19.0])
print(f"Mean {t.mean():.2f} C, min {t.min():.2f} C, max {t.max():.2f} C")
print("First six F:", 1.8*t[:6]+32)
section("C. CHANGED INPUT: heat wave (+5 C to every reading)")
h = t + 5
print(f"Mean {h.mean():.2f} C, min {h.min():.2f}, max {h.max():.2f}")
print("Range (max-min) original vs heat wave:", np.ptp(t), np.ptp(h))
