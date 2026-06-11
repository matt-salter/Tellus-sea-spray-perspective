#!/usr/bin/env python3

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter, NullFormatter

HERE = Path(__file__).resolve().parent
OUTDIR = HERE.parent

group_a = pd.read_csv(HERE / "Group_A.csv", header=None, names=["diameter_um", "concentration"])
group_b = pd.read_csv(HERE / "Group_B.csv", header=None, names=["diameter_um", "concentration"])

fig, ax = plt.subplots(figsize=(4.8, 3.8))

# Filled regions digitised from Blanchard and Woodcock (1957)
ax.fill(
    group_a["diameter_um"],
    group_a["concentration"],
    alpha=0.25,
    edgecolor="black",
    linewidth=1.0,
    label="Region A: open-sea breaking waves",
)

ax.fill(
    group_b["diameter_um"],
    group_b["concentration"],
    alpha=0.25,
    edgecolor="black",
    linewidth=1.0,
    label="Region B: waves breaking over rock",
)

ax.set_xscale("log")
ax.set_yscale("log")

ax.set_xlabel("Bubble diameter (µm)")
ax.set_ylabel("Bubble concentration\n(cc$^{-1}$ per 100 µm band width)")

ax.set_xlim(60, 600)
ax.set_ylim(0.003, 300)

ax.xaxis.set_major_locator(FixedLocator([100, 200, 300, 500]))
ax.xaxis.set_major_formatter(FixedFormatter(["100", "200", "300", "500"]))
ax.xaxis.set_minor_formatter(NullFormatter())

ax.legend(frameon=False, fontsize=8)
ax.tick_params(which="both", direction="in", top=True, right=True)

fig.tight_layout()

fig.savefig(OUTDIR / "Blanchard_Figure_4_redrawn.pdf")
fig.savefig(OUTDIR / "Blanchard_Figure_4_redrawn.png", dpi=300)

print(f"Saved: {OUTDIR / 'Blanchard_Figure_4_redrawn.pdf'}")
print(f"Saved: {OUTDIR / 'Blanchard_Figure_4_redrawn.png'}")