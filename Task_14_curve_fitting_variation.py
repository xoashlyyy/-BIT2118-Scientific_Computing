"""Task 14 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from scipy.optimize import curve_fit
from common import section, plt, save
u=np.array([50,100,150,200,250,300,350.]); y=np.array([82,95,115,145,185,238,305.])
quad=lambda x,a,b,c:a*x**2+b*x+c; lin=lambda x,a,b:a*x+b; cub=lambda x,a,b,c,d:a*x**3+b*x**2+c*x+d
rm=lambda f,p:np.sqrt(np.mean((y-f(u,*p))**2))
section("A. ORIGINAL")
p,_=curve_fit(quad,u,y); print("a,b,c =",np.round(p,6),"| RMSE %.2f ms"%rm(quad,p),"| at 400 users %.1f ms"%quad(400,*p))
xp=np.linspace(50,400,300); plt.scatter(u,y,label="Data"); plt.plot(xp,quad(xp,*p),label="Quadratic fit"); plt.xlabel("Users"); plt.ylabel("Response (ms)"); plt.legend(); plt.grid(True); plt.title("Curve fitting"); save("Task_14_fit.png")
section("C. CHANGED INPUT: try linear and cubic models")
pl,_=curve_fit(lin,u,y); pc,_=curve_fit(cub,u,y)
print("Linear RMSE %.2f | prediction 400 users %.1f ms"%(rm(lin,pl),lin(400,*pl)))
print("Cubic  RMSE %.2f | prediction 400 users %.1f ms"%(rm(cub,pc),cub(400,*pc)))
section("C2. CHANGED INPUT: one outlier (response at 250 users = 400 ms)")
y2=y.copy(); y2[4]=400; p2,_=curve_fit(quad,u,y2); print("Quadratic params with outlier:",np.round(p2,5),"prediction 400:",round(quad(400,*p2),1))
