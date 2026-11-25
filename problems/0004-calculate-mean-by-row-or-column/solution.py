def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'column':
        return [sum(list(col)) / len(col) for col in zip(*matrix)]
    else:
        return [sum(col) / len(col) for col in matrix]

# import numpy as np

# def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
#     matrix_np = np.asarray(matrix)
#     axis = 0 if mode == 'column' else 1
#     return np.mean(matrix_np, axis=axis)