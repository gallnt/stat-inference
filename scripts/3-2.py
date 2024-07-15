import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# Parameters for the hypergeometric distribution
N = 100
K = [6, 7, 8, 9, 10]
colors = ['red', 'orange', 'yellow', 'green', 'blue']
n = 4

k = np.arange(n + 1)
for i in range(len(K)):
    F_k = hypergeom.cdf(k, N, K[i], n)
    plt.plot(k, F_k, color=colors[i], marker='o', linestyle='')

plt.xlabel("X")
plt.ylabel("cdf of X")
plt.title("Hypergeometric(100, K, 4)")
plt.show()