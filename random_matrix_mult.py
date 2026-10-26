import numpy as np

# Create a 3x6 matrix with random integers from -10 to 10
A = np.random.randint(-10, 11, (3, 6))

print("Matrix A:")
print(A)

# Transpose of A
AT = A.T

print("\nTranspose of A:")
print(AT)

#A*AT
A_AT = A @ AT

print("\nA × AT:")
print(A_AT)

# AT × A
AT_A = AT @ A

print("\nAT × A:")
print(AT_A)
