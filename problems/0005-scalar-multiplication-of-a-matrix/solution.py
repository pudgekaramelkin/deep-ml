def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = [[scalar * row for row in col] for col in matrix]
    return result

# import numpy as np

# def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
#     result = np.array(matrix) * scalar
#     return result.tolist()