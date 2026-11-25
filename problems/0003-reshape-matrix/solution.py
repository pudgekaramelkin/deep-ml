def reshape_matrix_manual(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
   rows, cols = new_shape
   if rows <= 0 or cols <= 0:
       return []

   flatten = [item for sublist in a for item in sublist]
   if len(flatten) != rows * cols:
       return []

   return [flatten[i * cols : (i + 1) * cols] for i in range(rows)]

import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    try:
        return np.array(a).reshape(new_shape).tolist()
    except ValueError:
        return []
