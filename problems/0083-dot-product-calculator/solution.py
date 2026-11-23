import numpy as np

def calculate_dot_product(vec1, vec2):
    vec1, vec2 = vec1.tolist(), vec2.tolist()
    return sum(x * y for x, y in zip(vec1, vec2))