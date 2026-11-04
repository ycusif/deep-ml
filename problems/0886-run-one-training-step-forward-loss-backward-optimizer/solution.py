import torch
import torch.nn.functional as F

def train_one_step(model, x, y, lr):
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)
    
    optimizer.zero_grad()
    pred = model(x)
    loss = F.mse_loss(pred, y)
    loss.backward()
    optimizer.step()
    
    return loss.item()