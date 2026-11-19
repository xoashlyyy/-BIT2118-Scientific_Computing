import numpy as np
from scipy.interpolate import interp1d, CubicSpline
from _common import section, plt, save
h=np.array([8,9,10,11,12,13,14.]); T=np.array([18,20,22.5,24,25,25.5,25.])
lin=interp1d(h,T); cub=CubicSpline(h,T)
section("A. ORIGINAL")
print(f"10:30 linear {float(lin(10.5)):.2f} C | cubic {float(cub(10.5)):.2f} C")
tt=np.arange(8,14+1/6,1/6); plt.scatter(h,T,label="Hourly"); plt.plot(tt,lin(tt),label="Linear"); plt.plot(tt,cub(tt),label="Cubic spline")
plt.xlabel("Hour"); plt.ylabel("Temp (C)"); plt.legend(); plt.grid(True); plt.title("Interpolation"); save("Task_13_interp.png")
section("C. CHANGED INPUT: estimate at 13:30 and compare with extrapolation at 15:00")
print(f"13:30 linear {float(lin(13.5)):.2f} | cubic {float(cub(13.5)):.2f}")
print("15:00 cubic extrapolation:",round(float(cub(15)),2),"(unreliable: outside data range)")
try: lin(15)
except ValueError as e: print("Linear at 15:00 ->","ValueError (out of bounds)")
section("E. RELATED CASE: air-quality sensor lost readings at 11:00 and 12:00")
pm=np.array([35,38,42,np.nan,np.nan,55,52,48.]); hrs=np.arange(8,16.)
ok=~np.isnan(pm); l=interp1d(hrs[ok],pm[ok]); c=CubicSpline(hrs[ok],pm[ok])
for t in (11,12): print(f"{t}:00 PM2.5 estimate: linear {float(l(t)):.1f}, cubic {float(c(t)):.1f} ug/m3")
