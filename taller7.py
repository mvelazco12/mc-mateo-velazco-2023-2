import math

x = 0.73
n = 0
approx = 1
ea = 100

while ea > 0.000001:
    term = (x**n)/math.factorial(n)
    approx += term
    if approx != 0:
        ea = abs((approx - 1/math.exp(x))/approx) * 100
    n += 1

print("Aproximación 2:")
print("Valor aproximado: ", round(approx, 8))
print("Error relativo porcentual: ", round(ea, 8), "%")
print("Número de iteraciones: ", n)

