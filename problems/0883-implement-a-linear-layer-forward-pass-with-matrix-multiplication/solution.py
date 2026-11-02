import torch

def linear_forward(x, W, b):
    return  x @ W.T + b
