import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(FIG, exist_ok=True)
def section(t): print(f"\n=== {t} ===")
def save(name):
    plt.tight_layout(); plt.savefig(os.path.join(FIG, name), dpi=110); plt.close()
