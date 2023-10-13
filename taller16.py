import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X_vals = np.array([[0], [1], [2], [3], [4], [5], [6], [7]])
y_vals = np.array([7, 5, 6, 3, 4, 2.5, 2, 0.5])

model = LinearRegression()
model.fit(X_vals, y_vals)

y_pred = model.predict(X_vals)

print('Coeficiente a:', model.coef_[0])
print('Intersección b:', model.intercept_)

plt.scatter(X_vals, y_vals, color='blue')
plt.plot(X_vals, y_pred, color='red', linewidth=2)
plt.title('Regresión lineal por mínimos cuadrados')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
