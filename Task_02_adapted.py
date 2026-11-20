"""Task 02 - real-world adaptation (E)."""
import numpy as np
from common import section
section("E. RELATED CASE: IoT soil-moisture sensor (raw ADC 0-1023 -> %)")
raw = np.array([820,790,760,700,640,590,560,540,520,510,505,500])
dry, wet = 850, 350                      # calibration values
pct = (dry - raw) / (dry - wet) * 100
print("Moisture %:", np.round(pct, 1))
print("Mean moisture: %.1f %%" % pct.mean())
print("Readings below 30 % threshold (need irrigation):", int((pct < 30).sum()), "of", len(pct))
