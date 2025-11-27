import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

np.random.seed(0)

# Distribution parameters
mu = 90
sigma = 25
x = mu + sigma * np.random.randn(5000)
num_bins = 25

# Plot
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)

# Best-fit line
y = stats.norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '--')

ax.set_xlabel('Example Data')
ax.set_ylabel('Probability density')
sTitle = f'Histogram {len(x)} entries into {num_bins} Bins: μ={mu}, σ={sigma}'
ax.set_title(sTitle)

fig.tight_layout()

# ✅ Set your actual Windows Save Path
sPathFig = r"C:/Atiya/FY-MSC-IT/Data Science/DS PractsDU-Histogram.png"

# Ensure folder exists
os.makedirs(os.path.dirname(sPathFig), exist_ok=True)

# Save image
fig.savefig(sPathFig)
print("Histogram saved to:", sPathFig)

plt.show()
