import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the C library
lib = ctypes.CDLL('./code.so')  # Path to the compiled C library

# Define argument and return types for the C function
lib.direction_cosines.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float,
                                  ctypes.c_float, ctypes.c_float, ctypes.c_float,
                                  ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]

# Function to call the C code
def calculate_direction_cosines(x1, y1, z1, x2, y2, z2):
    l = ctypes.c_float()
    m = ctypes.c_float()
    n = ctypes.c_float()
    
    lib.direction_cosines(x1, y1, z1, x2, y2, z2, ctypes.byref(l), ctypes.byref(m), ctypes.byref(n))
    
    return l.value, m.value, n.value

# Coordinates of points P and Q
P = np.array([4, 3, -5])
Q = np.array([-2, 1, 8])

# Call the C function to calculate direction cosines
l, m, n = calculate_direction_cosines(P[0], P[1], P[2], Q[0], Q[1], Q[2])
print(f"Direction cosines: l = {l}, m = {m}, n = {n}")

# 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points P and Q
ax.scatter(P[0], P[1], P[2], color='red', label='Point P (4, 3, -5)')
ax.scatter(Q[0], Q[1], Q[2], color='blue', label='Point Q (-2, 1, 8)')

# Plot line joining P and Q
line = np.array([P, Q])
ax.plot(line[:, 0], line[:, 1], line[:, 2], color='green', label='Line PQ')

# Plot the coordinate axes

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
# Set limits
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Show the plot
plt.legend()
plt.show()

