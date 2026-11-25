def calculate_dot_product_manual(vec1, vec2):
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The dot product of the two vectors.
    """
    vector_1, vector_2 = vec1.tolist(), vec2.tolist()
    
    if len(vector_1) != len(vector_2):
        return -1
    
    return sum(x * y for x, y in zip(vector_1, vector_2))

import numpy as np

def calculate_dot_product(vec1, vec2):
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The dot product of the two vectors.
    """
    return vec1 @ vec2