import torch

def sigmoid(z: float) -> float:
    """
    Compute the sigmoid activation function.
    Input:
      - z: float or torch scalar tensor
    Returns:
      - sigmoid(z) as Python float rounded to 4 decimals.
    """
    result = 1 / (1 + torch.exp(torch.tensor(-z)))
    return result.item()

def swish(x: torch.Tensor) -> torch.Tensor:
    """
    Implements the Swish activation function.

    Args:
        x: Input tensor

    Returns:
        The Swish activation value as a tensor
    """
    result = x.item()
    result *= sigmoid(result)

    return torch.tensor(result)