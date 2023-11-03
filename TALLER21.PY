import numpy as np
from scipy.stats import linregress

x1 = np.array([1, 1, 2, 3, 1, 2, 3, 3])
x2 = np.array([0, 1, 1, 2, 2, 3, 3, 1])
y = np.array([1.6, 3, 1.1, 1.3, 3.2, 3.3, 1.8, 0])

A = np.vstack([x1, x2, np.ones(len(x1))]).T
m, n, c = np.linalg.lstsq(A, y, rcond=None)[0]

slope, intercept, r_value, p_value, std_err = linregress(y, m*x1 + n*x2 + c)

print(f"La función lineal ajustada es: y = {m:.2f}x1 + {n:.2f}x2 + {c:.2f}")
print(f"El coeficiente de correlación (r) es: {r_value:.2f}")
