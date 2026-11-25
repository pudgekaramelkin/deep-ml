def matrixmul_manual(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    p1 = len(a[0])
    p2 = len(b)

    if p1 != p2:
        return -1

    m = len(a)
    p = len(b[0])

    result = [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]

    return result

import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    a = np.asarray(a)
    b = np.asarray(b)

    m, p1 = a.shape
    p2, n = b.shape

    if p1 != p2:
        return -1

    return a @ b 