import torch

def selu(x: torch.Tensor) -> torch.Tensor:
    """
    Implements the SELU (Scaled Exponential Linear Unit) activation function.

    Args:
        x: Input tensor

    Returns:
        SELU activation tensor
    """
    alpha = 1.6732632423543772
    scale = 1.0507009873554804
    if x < 0:
        return alpha * scale * (torch.exp(x) - 1)
    return scale * x