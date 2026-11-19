import numpy as np, math
from _common import section
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
section("E. RELATED CASE: banking - adding 10 cents one million times")
total = 0.0
for _ in range(1_000_000): total += 0.1
print("Naive sum      :", repr(total), "error:", abs(total-100000))
print("math.fsum      :", repr(math.fsum([0.1]*1_000_000)))
cents = sum([10]*1_000_000)/100
print("Integer cents  :", cents)
acc=np.float32(0)
for _ in range(100_000): acc+=np.float32(0.1)
print("float32, 100,000 additions of 0.1 ->",acc,"(true 10000): single precision drifts far more")
