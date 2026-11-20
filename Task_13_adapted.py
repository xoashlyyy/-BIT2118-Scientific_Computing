"""Task 13 - real-world adaptation (E)."""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
from common import section, plt, save
h=np.array([8,9,10,11,12,13,14.]); T=np.array([18,20,22.5,24,25,25.5,25.])
lin=interp1d(h,T); cub=CubicSpline(h,T)
section("E. RELATED CASE: air-quality sensor lost readings at 11:00 and 12:00")
pm=np.array([35,38,42,np.nan,np.nan,55,52,48.]); hrs=np.arange(8,16.)
ok=~np.isnan(pm); l=interp1d(hrs[ok],pm[ok]); c=CubicSpline(hrs[ok],pm[ok])
for t in (11,12): print(f"{t}:00 PM2.5 estimate: linear {float(l(t)):.1f}, cubic {float(c(t)):.1f} ug/m3")
