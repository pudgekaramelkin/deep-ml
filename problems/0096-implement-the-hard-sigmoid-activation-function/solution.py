import torch

def hard_sigmoid(x: float) -> float:
    """
    Implements the Hard Sigmoid activation function using PyTorch.
    Uses the Keras convention: 0.2*x + 0.5, clamped to [0, 1].

    Args:
        x (float): Input value

    Returns:
        float: The Hard Sigmoid of the input
    """
    result = 0

    if x >= 2.5:
        result = 1
    elif x > -2.5 and x < 2.5:
        result = 0.2 * x + 0.5
    
    return result