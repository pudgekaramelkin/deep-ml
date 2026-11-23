# def matrixmul(a:list[list[int|float]],
#               b:list[list[int|float]])-> list[list[int|float]]:
#     m, p = len(a), len(b)
#     if m == 0 or p == 0:
#         return -1
#     n = len(b[0])
#     if n == 0 or p != len(a[0]):
#         return -1

#     result = [[0] * n for _ in range(m)]
#     for i in range(m):
#         for j in range(n):
#             row, column = a[i], [x[j] for x in b]
#             summary = sum(x * y for x, y in zip(row, column))
#             result[i][j] = summary
#     return result

import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    a_arr, b_arr = np.array(a), np.array(b)
    m, p1 = a_arr.shape
    p2, n = b_arr.shape
    if p1 != p2 or m == 0 or n == 0:
        return -1
    result = a_arr @ b_arr
    return result.tolist()