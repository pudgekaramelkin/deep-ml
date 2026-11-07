import torch
import numpy as np
from typing import List

def log_softmax(scores: List[float]) -> torch.Tensor:
    """
    Compute the log-softmax of a 1D list of scores using PyTorch.
    Args:
        scores: list of floats
    Returns:
        torch.Tensor of log-softmax values
    """
    exp_sum_log = np.log(np.sum(np.exp(scores)))
    result = scores - exp_sum_log
    return torch.tensor(result)
