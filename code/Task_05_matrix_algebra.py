import numpy as np
from _common import section, plt, save
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
section("E. RELATED CASE: robot-arm triangle, rotate 30 deg + mirror in x + translate (homogeneous)")
tri=np.array([[0,0],[2,0],[1,1.5]])
a=np.deg2rad(30)
H=np.array([[np.cos(a),-np.sin(a),4],[np.sin(a),np.cos(a),1],[0,0,1]])   # rotate + translate
M=np.diag([-1,1,1])                                                       # mirror about y-axis
P=np.c_[tri,np.ones(3)]
out=(H@M@P.T).T[:,:2]
print("Transformed triangle:\n",np.round(out,3))
print("Det of 2x2 part (-1 means orientation flipped):",round(np.linalg.det((H@M)[:2,:2]),3))
fig,ax=plt.subplots(); 
for pts,l in [(tri,"original"),(out,"transformed")]:
    q=np.vstack([pts,pts[0]]); ax.plot(q[:,0],q[:,1],marker="o",label=l)
ax.set_aspect("equal"); ax.legend(); ax.grid(True); ax.set_title("Triangle transformation"); save("Task_05_triangle.png")
