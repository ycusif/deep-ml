import torch 
def linear_forward(x,W,b):
    y= x@ W.T + b
    return (y)
