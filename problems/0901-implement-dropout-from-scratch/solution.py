import torch

def dropout(x, p= 0.5, training= True):
    if not training or p == 0.0:
        return x 
    mask = torch.rand_like(x) > p 
    return x * mask.to(x.dtype) / (1.0 - p)
