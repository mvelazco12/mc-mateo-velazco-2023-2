def gausjordanmatrix(matrix):
    n = len(matrix)
    
    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        
        pivot = matrix[i][i]
        for j in range(i, n+1):
            matrix[i][j] /= pivot
        
        for j in range(n):
            if j != i:
                factor = matrix[j][i]
                for k in range(i, n+1):
                    matrix[j][k] -= factor * matrix[i][k]
    
    solutions = [row[-1] for row in matrix]
    return solutions

coefficients = [
    [1, 1, 0, 5],
    [3, 3, 4, 23],
    [4, 0, 1, 30]
]

solutions = gausjordanmatrix(coefficients)
print("Solution:")
print("x1 =", solutions[0])
print("x2 =", solutions[1])
print("x3 =", solutions[2])
