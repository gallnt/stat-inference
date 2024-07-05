import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# Parameters for the hypergeometric distribution
N = 30
K = 5
n = 4

k = np.arange(n + 1)
F_k = hypergeom.cdf(k, N, K, n)

plt.plot(k, F_k, 'bo')
plt.xlabel("X")
plt.ylabel("cdf of X")
plt.title("Hypergeometric(30, 5, 4)")
plt.show()