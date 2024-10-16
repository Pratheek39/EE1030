import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Creating matrices
m1 = np.array(([1, -3, 2])).reshape(-1, 1)  # Direction vector of first line
m2 = np.array(([2, 3, 1])).reshape(-1, 1)   # Direction vector of second line
P1 = np.array(([1, 2, 3])).reshape(-1, 1)   # Point on the first line
P2 = np.array(([4, 5, 6])).reshape(-1, 1)   # Point on the second line
b = P2 - P1
A = np.block([m1, m2])

# Eigenvalue decomposition of A'A
Dv, Pv = LA.eig(A.T @ A)

# Singular values of A
Stemp = np.sqrt(Dv)

# SVD, A = U S V
U_1, s, V_1 = LA.svd(A)

# Function to generate points along a line
def line_gen(P, m, t):
    return P + t * m

# Generate points for line 1 (P1 + λ m1)
t1 = np.linspace(-5, 5, 100)
line1_points = np.array([line_gen(P1, m1, t) for t in t1])

# Generate points for line 2 (P2 + μ m2)
t2 = np.linspace(-5, 5, 100)
line2_points = np.array([line_gen(P2, m2, t) for t in t2])

# Finding the shortest distance between the two lines
n = np.cross(m1.T, m2.T).T  # Normal vector to both direction vectors
n = n / LA.norm(n)  # Normalize the normal vector

# Finding the point of closest approach using projection
d = np.dot(b.T, n) * n
P_closest_on_L1 = P1 + np.dot((P2 - P1).T, m1) * m1 / LA.norm(m1)**2
P_closest_on_L2 = P2 + np.dot((P1 - P2).T, m2) * m2 / LA.norm(m2)**2

# Generate points for the line of shortest distance
shortest_line_points = np.hstack((P_closest_on_L1, P_closest_on_L2))

# Plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plotting the first line
ax.plot(line1_points[:, 0], line1_points[:, 1], line1_points[:, 2], label="Line 1", color='b')

# Plotting the second line
ax.plot(line2_points[:, 0], line2_points[:, 1], line2_points[:, 2], label="Line 2", color='r')

# Plotting the shortest distance line
ax.plot(shortest_line_points[0, :], shortest_line_points[1, :], shortest_line_points[2, :], label="Shortest Line", color='g', linestyle='--')

# Scatter points for closest points on both lines
ax.scatter(P_closest_on_L1[0], P_closest_on_L1[1], P_closest_on_L1[2], color='black', label='Closest on Line 1')
ax.scatter(P_closest_on_L2[0], P_closest_on_L2[1], P_closest_on_L2[2], color='orange', label='Closest on Line 2')

# Axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set limits
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

plt.legend()
plt.show()

