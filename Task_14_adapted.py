"""Task 14 - real-world adaptation (E)."""
import numpy as np
from scipy.optimize import curve_fit
from common import section, plt, save
u=np.array([50,100,150,200,250,300,350.]); y=np.array([82,95,115,145,185,238,305.])
quad=lambda x,a,b,c:a*x**2+b*x+c; lin=lambda x,a,b:a*x+b; cub=lambda x,a,b,c,d:a*x**3+b*x**2+c*x+d
rm=lambda f,p:np.sqrt(np.mean((y-f(u,*p))**2))
section("E. RELATED CASE: bacterial/user growth y=A*exp(r*t)")
t=np.arange(0,8.); N=np.array([100,135,178,240,320,430,580,770.])
ex=lambda t,A,r:A*np.exp(r*t); pe,_=curve_fit(ex,t,N,p0=[100,0.3])
print(f"A={pe[0]:.1f}, growth rate r={pe[1]:.4f}/hr, doubling time={np.log(2)/pe[1]:.2f} h, forecast t=10: {ex(10,*pe):.0f}")
