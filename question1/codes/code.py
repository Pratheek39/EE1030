import numpy as np
import ctypes
import matplotlib.pyplot as plt

# Load the shared object file
lib = ctypes.CDLL('./code.so')

# Define points A and B as numpy arrays
A = np.array([6.0, -4.0], dtype=np.float32)
B = np.array([-2.0, -7.0], dtype=np.float32)

# Ratio k
k = 3

# Create an array to hold the result
C = np.zeros(2, dtype=np.float32)

# Call the C function
lib.sect(A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), 
         B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), 
         ctypes.c_float(k), 
         C.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))

print(f"Point C: {C}")

# Plotting the points
plt.figure(figsize=(10, 8))

# Plot points A, B, and C
plt.plot(A[0], A[1], 'ro', label='Point A (6,-4)')
plt.plot(B[0], B[1], 'bo', label='Point B (-2,-7)')
plt.plot(C[0], C[1], 'go', label=f'Point C ({C[0]:.2f},{C[1]:.2f})')

# Draw line segment AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', label='Line AB')

# Annotate the points
plt.text(A[0], A[1], ' A', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='red')
plt.text(B[0], B[1], ' B', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='blue')
plt.text(C[0], C[1], f' C ({C[0]:.2f},{C[1]:.2f})', fontsize=12, verticalalignment='bottom', horizontalalignment='left', color='green')

# Label the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set title
plt.title('Section Formula: Dividing Line Segment in a Given Ratio')

# Set axis limits
plt.xlim(min(A[0], B[0], C[0]) - 1, max(A[0], B[0], C[0]) + 1)
plt.ylim(min(A[1], B[1], C[1]) - 1, max(A[1], B[1], C[1]) + 1)

# Add grid and show axes
plt.grid(True)

# Show legend
plt.legend()

# Display the plot
plt.show()

