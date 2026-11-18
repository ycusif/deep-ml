
import torch
import torch.nn.functional as F

def conv2d_via_unfold(x, W, b, stride=1, padding=0):

    # EXTRACT DIMENSIONS
    N, C_in, H, W_in = x.shape
    C_out, _, kH, kW = W.shape

    # CALCULATE SPATIAL DIMENSIONS (OUTPUT HEIGHT AND WIDTH)
    H_out = (H + 2 * padding - kH) // stride + 1
    W_out = (W_in + 2 * padding - kW) // stride + 1

    # UNFOLDING: EXTRACT INPUT PATCHES AND ARRANGE THEM AS COLUMNS
    x_unfolded = F.unfold(
        x,
        kernel_size=(kH, kW),
        padding=padding,
        stride=stride
    )

    # FLATTEN THE WEIGHTS TO MATCH THE DIMENSION OF EACH INPUT PATCH
    W_flat = W.flatten(start_dim=1)  # start_dim=1 preserves the filter dimension

    # MULTIPLY WEIGHTS BY UNFOLDED INPUT TO CALCULATE DOT PRODUCTS
    output = W_flat @ x_unfolded

    # RESHAPE TO THE DESIRED OUTPUT SHAPE
    output = output.reshape(N, C_out, H_out, W_out)

    # APPLY THE BIAS TO EVERY POSITION IN ITS CORRESPONDING CHANNEL (BROADCASTING)
    output = output + b.reshape(1, C_out, 1, 1)

    return output

