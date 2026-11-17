import io
import torch
import torch.nn as nn

def copy_weights(src, dst):
    buffer= io.BytesIO()
    torch.save(src.state_dict(), buffer)
    buffer.seek(0)
    dst.load_state_dict(torch.load(buffer))