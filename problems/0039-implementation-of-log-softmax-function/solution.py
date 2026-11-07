import torch
from typing import List

def log_softmax(scores: List[float]) -> torch.Tensor:
    x = torch.tensor(scores, dtype=torch.float32)

    x = x - torch.max(x)
    exp_sum_log = torch.log(torch.sum(torch.exp(x)))

    return x - exp_sum_log