# def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
#     if len(matrix) != 2 and len(matrix[0]) != 2:
#         return -1
    
#     a, b = matrix[0]
#     c, d = matrix[1]

#     mean = (a + d) / 2
#     product = a * d - b * c

#     eigenvalue_1 = mean + (mean ** 2 - product) ** 0.5
#     eigenvalue_2 = mean - (mean ** 2 - product) ** 0.5
#     return [eigenvalue_1, eigenvalue_2]

import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    if len(matrix) != 2 and len(matrix[0]) != 2:
        return -1

    matrix = np.asarray(matrix)

    return np.linalg.eigvals(matrix).real