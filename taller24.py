import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

points = np.array([[0, 2], [1, 4], [2, 5], [3, 4], [4, -3], [5, 1], [6, 12]])
x_values = points[:, 0]
y_values = points[:, 1]

def lagrange_interpolation(points, x):
    def L(k, x):
        result = 1.0
        for i, p in enumerate(points):
            if i != k:
                result *= (x - points[i, 0]) / (points[k, 0] - points[i, 0])
        return result

    def P(x):
        result = 0.0
        for k in range(len(points)):
            result += points[k, 1] * L(k, x)
        return result

    return P(x)

lagrange_estimation = lagrange_interpolation(points, 4.75)
print(f"Estimación de f(4.75) usando interpolación de Lagrange: {lagrange_estimation}")

cs = CubicSpline(x_values, y_values)
cubic_spline_estimation = cs(4.75)
print(f"Estimación de f(4.75) usando trazadores cúbicos: {cubic_spline_estimation}")

xs = np.arange(0, 6, 0.1)
ys = cs(xs)

plt.plot(x_values, y_values, 'o', label='Data Points')
plt.plot(xs, ys, label='Cubic Spline')
plt.axvline(x=4.75, color='r', linestyle='--', label='x=4.75')
plt.legend()
plt.show()
