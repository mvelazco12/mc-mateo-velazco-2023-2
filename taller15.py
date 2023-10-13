import numpy as np

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join([str(elem) for elem in fila]))

def gauss_jordan(matriz):
    n = len(matriz)
    matriz_extendida = np.concatenate((matriz, np.identity(n)), axis=1)

    for i in range(n):
        divisor = matriz_extendida[i][i]
        matriz_extendida[i] = matriz_extendida[i] / divisor

        for j in range(n):
            if i != j:
                factor = matriz_extendida[j][i]
                matriz_extendida[j] = matriz_extendida[j] - factor * matriz_extendida[i]

    inversa = matriz_extendida[:, n:]
    return inversa

A = np.array([[3, 2, 2], [3, 1, -3], [1, 0, -2]])
B = np.array([[1, 2, 0, 4], [2, 0, -1, -2], [1, 1, -1, 0], [0, 4, 1, 0]])

inversa_A = gauss_jordan(A)
inversa_B = gauss_jordan(B)

print("Inversa de la matriz A:")
imprimir_matriz(inversa_A)
print("\nInversa de la matriz B:")
imprimir_matriz(inversa_B)
