
import torch

def batchnorm2d(x, gamma, beta, eps=1e-5):
    # Compute mean and variance for each channel over N, H, W
    mean = x.mean(dim=(0, 2, 3), keepdim=True)
    var = x.var(dim=(0, 2, 3), keepdim=True, unbiased=False)

    # Normalize
    x_hat = (x - mean) / torch.sqrt(var + eps)

    # Broadcast gamma and beta across N, H, W
    gamma = gamma.view(1, -1, 1, 1)
    beta = beta.view(1, -1, 1, 1)

    return gamma * x_hat + beta

torch.manual_seed(0)
x = torch.randn(8, 4, 6, 6)
gamma = torch.ones(4)
beta = torch.zeros(4)

output = batchnorm2d(x, gamma, beta)

print(f"output.shape: {output.shape}")
print(output.mean(dim=(0, 2, 3)))
