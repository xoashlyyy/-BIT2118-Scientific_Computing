"""Task 05 - baseline (A) and parameter-variation experiments (C)."""
import numpy as np
from common import section, plt, save
def transform(points, angle_deg, sx, sy):
    a=np.deg2rad(angle_deg)
    R=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]]); S=np.diag([sx,sy])
    T=R@S
    return points@T.T, T
sq=np.array([[0,0],[1,0],[1,1],[0,1.]])
section("A. ORIGINAL: rotate 45 deg, scale (2,1.5)")
p,T=transform(sq,45,2,1.5); print(np.round(p,3)); print("T=\n",np.round(T,3)); print("det =",np.linalg.det(T))
section("C. CHANGED INPUT: rotate 90 deg, scale (1,1) and scale (3,3)")
p2,T2=transform(sq,90,1,1); print(np.round(p2,3),"\ndet =",np.linalg.det(T2))
p3,T3=transform(sq,45,3,3); print("det with scale 3x3 =",np.linalg.det(T3),"(area factor 9)")
