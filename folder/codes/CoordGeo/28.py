# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math

num = 3
a = math.sqrt(num)

# Path to external scripts (update as per your setup)
import sys
sys.path.insert(0, '/home/pratheek/Desktop/Latex/matgeo/codes/CoordGeo')

# Local imports
from conics.funcs import circ_gen
from line.funcs import *

# Define two points (for later calculations)
x1 = np.array([5, 0]).reshape(-1, 1)
x2 = np.array([0, 5]).reshape(-1, 1)
p1= np.array([2.5, 2.5*a]).reshape(-1,1)
p2= np.array([2.5, -2.5*a]).reshape(-1, 1)


# Line parameters
n = np.array([1, 0]).reshape(-1, 1) 
c = 0
n1 = np.array([1, a]).reshape(-1, 1) 
c1 = 10
n2 = np.array([1, -1*a]).reshape(-1, 1) 
c2 = 10

# Solve for the center and radius of the circle
A = np.block([[2 * x1, 2 * x2, n], [1, 1, 0]]).T
b = -np.array([LA.norm(x1)**2, LA.norm(x2)**2, c]).reshape(-1, 1)
x = LA.solve(A, b)

# Center and radius of the circle
u = x[:2]
O = -u
f = x[2][0]
r = np.sqrt(LA.norm(u)**2 - f)
print(f"Circle Center: {O}, Radius: {r}")

# Generate circle points
x_circ = circ_gen(O, r)

# Generate tangents to the circle
k1 = -5
k2 = 5
x_A = line_norm(n, c, k1, k2)
x_B = line_norm(n1, c1, k1, k2)
x_C = line_norm(n2, c2, k1, k2)

# Plotting the circle and tangents
plt.plot(x_A[0, :], x_A[1, :], label='')
plt.plot(x_B[0, :], x_B[1, :], label='Tangent 1')
plt.plot(x_C[0, :], x_C[1, :], label='Tangent 2')
plt.plot(x_circ[0, :], x_circ[1, :], label='Circle')

# Labeling the points
colors = np.arange(1, 4)
tri_coords = np.block([p1, p2, O])
plt.scatter(tri_coords[0, :], tri_coords[1, :], c=colors)
vert_labels = ['$\mathbf{x}_1$', '$\mathbf{x}_2$', '$\mathbf{O}$']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0, i]:}, {tri_coords[1, i]:})',
                 (tri_coords[0, i], tri_coords[1, i]),
                 textcoords="offset points", xytext=(-20, 5), ha='center')

# Set axis properties
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Show the plot with equal scaling
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()

