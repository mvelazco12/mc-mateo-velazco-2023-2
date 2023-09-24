import math

def taylor_series(x, n):
    result = 0
    for i in range(n + 1):
        result += (-x) ** i / math.factorial(i)
    return result

x_base = 0.5
x_estimation = 0.505

for n in range(16):
    estimation = taylor_series(x_estimation - x_base, n)
    real = math.exp(-x_estimation)
    error = abs(real - estimation)
    relative_error_percent = (error / real) * 100

    print(f"Orden {n}: Estimación = {estimation}, Error relativo (%) = {relative_error_percent}")
