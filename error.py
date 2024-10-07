import torch
print(torch.cuda.is_available())  # This should return True if CUDA is available
print(torch.version.cuda)          # This shows the CUDA version PyTorch is compiled with
