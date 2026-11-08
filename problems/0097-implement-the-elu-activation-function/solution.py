import torch
import torch.nn.functional as F

def elu(x: float, alpha: float = 1.0) -> float:
    """
    Compute the ELU activation function using PyTorch.

    Args:
        x (float): Input value
        alpha (float): ELU parameter for negative values (default: 1.0)

    Returns:
        float: ELU activation value rounded to 4 decimal places
    """
    exp_item = torch.exp(torch.tensor(x)).item()
    return alpha * (exp_item - 1)