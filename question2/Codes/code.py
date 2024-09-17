import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the C library
lib = ctypes.CDLL('./code.so')  # Path to the compiled C library

# Define argument and return types for the C function
lib.direction_cosines.argtypes = [
    ctypes.c_float, ctypes.c_float, ctypes.c_float,
    ctypes.c_float, ctypes.c_float, ctypes.c_float,
    ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)
]

# Function to call the C code to calculate direction cosines
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

# Calculate angles with respect to the axes
def calculate_angle(cosine_value):
    return np.degrees(np.arccos(cosine_value))

# Angles between the line and the X, Y, Z axes
angle_x = calculate_angle(l)
angle_y = calculate_angle(m)
angle_z = calculate_angle(n)

print(f"Angle with X-axis: {angle_x:.2f} degrees")
print(f"Angle with Y-axis: {angle_y:.2f} degrees")
print(f"Angle with Z-axis: {angle_z:.2f} degrees")

# 3D plotting with a more spacious layout
fig = plt.figure(figsize=(10, 8))  # Larger figure size for better spacing
ax = fig.add_subplot(111, projection='3d')

# Plot points P and Q
ax.scatter(P[0], P[1], P[2], color='red', s=100, label='Point P (4, 3, -5)')  # Increased point size
ax.scatter(Q[0], Q[1], Q[2], color='blue', s=100, label='Point Q (-2, 1, 8)')

# Plot line joining P and Q
line = np.array([P, Q])
ax.plot(line[:, 0], line[:, 1], line[:, 2], color='green', linewidth=2, label='Line PQ')  # Thicker line

# Plot the coordinate axes with extended limits
ax.plot([0, 15], [0, 0], [0, 0], color='black', linestyle='--', linewidth=1, label='X-axis')
ax.plot([0, 0], [0, 15], [0, 0], color='black', linestyle='--', linewidth=1, label='Y-axis')
ax.plot([0, 0], [0, 0], [0, 15], color='black', linestyle='--', linewidth=1, label='Z-axis')

# Annotate angles clearly at positions closer to the axes
ax.text(10, 0, 0, f'Angle with X-axis\n{angle_x:.2f}°', color='black', fontsize=12, horizontalalignment='center', verticalalignment='center')
ax.text(0, 10, 0, f'Angle with Y-axis\n{angle_y:.2f}°', color='black', fontsize=12, horizontalalignment='center', verticalalignment='center')
ax.text(0, 0, 10, f'Angle with Z-axis\n{angle_z:.2f}°', color='black', fontsize=12, horizontalalignment='center', verticalalignment='center')

# Set labels and title
ax.set_xlabel('X-axis', labelpad=15)
ax.set_ylabel('Y-axis', labelpad=15)
ax.set_zlabel('Z-axis', labelpad=15)
ax.set_title('Line PQ and Angles with Coordinate Axes', pad=20)

# Set extended limits for more space
ax.set_xlim([-10, 15])
ax.set_ylim([-10, 15])
ax.set_zlim([-10, 15])

# Display legend with better spacing
plt.legend(loc='upper left', fontsize=10)

# Show the plot
plt.show()

