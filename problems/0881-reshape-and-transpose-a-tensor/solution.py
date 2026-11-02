import torch

def flatten_then_reshape(x, new_shape=(3,2)):
    # TODO: flatten x to 1-D, then rearrange into new_shape
    return x.flatten().reshape(new_shape)

def transpose_last_two(x):
    # TODO: swap the last two dimensions of x
    return x.transpose(-1,-2)
