import torch

def softplus(x: float) -> torch.Tensor:
    t = torch.tensor(x, dtype=torch.float32)
    
    if t > 0:
        return t + torch.log(1 + torch.exp(-t))
    else:
        return torch.log(1 + torch.exp(t))