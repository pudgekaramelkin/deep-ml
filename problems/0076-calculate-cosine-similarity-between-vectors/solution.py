# def get_length_vector(v):
#     return sum(x ** 2 for x in v) ** 0.5

# def cosine_similarity(v1, v2):
#     """
#     Calculate the cosine_similarity of two vectors.
#     Args:
#         vec1 (numpy.ndarray): 1D array representing the first vector.
#         vec2 (numpy.ndarray): 1D array representing the second vector.
#     Returns:
#         The cosine_similarity of the two vectors.
#     """
#     vector_1, vector_2 = v1.tolist(), v2.tolist()

#     if len(vector_1) != len(vector_2):
#         return -1

#     dot_product = sum(x * y for x, y in zip(vector_1, vector_2))
#     length = get_length_vector(vector_1) * get_length_vector(vector_2)

#     return dot_product / length


import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    return (v1 @ v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))