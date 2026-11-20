"""Task 04 - real-world adaptation (E)."""
import numpy as np, math
from common import section
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
