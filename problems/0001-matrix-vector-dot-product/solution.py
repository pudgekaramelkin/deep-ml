def matrix_dot_vector_manual(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float] | int:
  if not a or len(a[0]) != len(b):
    return -1

  return [sum(x * y for x, y in zip(row, b)) for row in a]

import numpy as np

def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float] | int:
    try:
        arr_a = np.array(a)
        arr_b = np.array(b)
        if arr_a.ndim != 2 or arr_b.ndim != 1 or arr_a.size == 0:
            return -1
        return (arr_a @ arr_b).tolist()
    except ValueError:
        return -1
