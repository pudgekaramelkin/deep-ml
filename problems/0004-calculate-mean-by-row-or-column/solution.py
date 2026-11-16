import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    matrix_np = np.array(matrix)
    axis = 0 if mode == 'column' else 1
    return np.mean(matrix_np, axis=axis)