import numpy as np
import numpy.linalg as LA

# Given matrix A
A = np.array([[-3, 2], [1, -1]])

# Identity matrix of the same size as A
I = np.eye(A.shape[0])

# Characteristic polynomial of A
# np.poly returns the coefficients of the characteristic polynomial
f = np.poly(A)

# Printing the characteristic equation


# Calculate A^2
A_squared = np.dot(A, A)

# Solve for k in the equation A^2 + I = kA
# Rearranging: A^2 - kA + I = 0
# This is a matrix equation; we can solve it by finding k that satisfies
# all elements in the matrix equation.

# For the 2x2 matrix, solve for k by equating corresponding elements
# k = (A^2 + I)[i][j] / A[i][j] for each i,j where A[i][j] != 0

k_values = []

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if A[i, j] != 0:
            k = (A_squared[i, j] + I[i, j]) / A[i, j]
            k_values.append(k)

# Ensure all k values are the same, otherwise there's no valid solution for k
if len(set(k_values)) == 1:
    k = k_values[0]
    print(f"{k}")
else:
    print("No single value of k satisfies the equation for all elements.")


