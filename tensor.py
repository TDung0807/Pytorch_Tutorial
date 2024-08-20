import torch

array_a = [1,2,3,4,5]
array_b = [6,7,8,9,10]
# Create two tensors from the arrays
tensor_a = torch.tensor(array_a)

print(tensor_a.device)
print(tensor_a.dtype)
tensor_b = torch.tensor(array_b)

# Subtract tensor_b from tensor_a 
tensor_c = tensor_a.subtract(tensor_b)
# Multiply each element of tensor_a with each element of tensor_b
tensor_d = tensor_a.multiply(tensor_b)
# Add tensor_c to tensor_d
tensor_e = tensor_c + tensor_d
print(tensor_e)