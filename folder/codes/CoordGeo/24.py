

import sys  # for path to external scripts
sys.path.insert(0, '/home/pratheek/Desktop/Latex/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Given points
A = np.array(([14 / 5, 1, -1])).reshape(-1, 1)
B = np.array(([4, 5, 1])).reshape(-1, 1)
C = np.array(([3, 9, 4])).reshape(-1, 1)
D = np.array(([-4, 4, 4])).reshape(-1, 1)

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Coefficients of the plane equation: ax + by + cz + d = 0
a, b, c, d = 5, -7, 11, 4

# Generate grid points for x and y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Calculate corresponding z values for each (x, y) pair to satisfy the plane equation
Z = (-a * X - b * Y - d) / c

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, color='grey')

# Scatter plot for point A
ax.scatter(A[0], A[1], A[2], c='r', marker='o', label='A')

# Scatter plot for triangle vertices D, B, C
tri_coords = np.block([A, D, B, C])  # Stack A, D, B, C vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=['r', 'b', 'g', 'c'], marker='o')

# Add labels for A, D, B, C with coordinates
vert_labels = ['A', 'D', 'B', 'C']
for i, txt in enumerate(vert_labels):
    coord_label = f'{txt} ({tri_coords[0, i]:.2f}, {tri_coords[1, i]:.2f}, {tri_coords[2, i]:.2f})'
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], coord_label, fontsize=10, ha='center', va='bottom')

# Set axis labels
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

# Set limits for axes
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

# Set equal aspect ratio
ax.set_box_aspect([1, 1, 1])

# Grid and show plot
plt.grid(True)
plt.show()

