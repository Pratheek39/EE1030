import numpy as np
import matplotlib.pyplot as plt

# Function to calculate intersection of two lines
def line_isect(n1, c1, n2, c2):
    # Solving the system of equations represented by the lines
    A = np.array([n1.flatten(), n2.flatten()]).T
    b = np.array([c1, c2])
    return np.linalg.solve(A, b)

# Given lines: -x + 4y = 3 and 4x + y = 11
# Normal vectors and intercepts
n1 = np.array([-1, 4])  # For the first line
c1 = 3                   # Intercept for the first line
n2 = np.array([4, 1])    # For the second line
c2 = 11                  # Intercept for the second line

# Calculate intersection point
intersection_point = line_isect(n1, c1, n2, c2)

# Generate line points for plotting
def line_eq(n, c, x_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = (c - n[0] * x) / n[1]  # Rearranging the line equation
    return np.array([x, y])

# Generate lines for plotting
x_A = line_eq(n1, c1, (-2, 5))
x_B = line_eq(n2, c2, (-2, 5))

# Plotting the lines
plt.plot(x_A[0, :], x_A[1, :], label='Line 1: $-x + 4y = 3$')
plt.plot(x_B[0, :], x_B[1, :], label='Line 2: $4x + y = 11$')

# Mark the intersection point
plt.scatter(*intersection_point, color='red', label='Intersection Point', zorder=5)
plt.annotate(f'({intersection_point[0]:.2f}, {intersection_point[1]:.2f})',
             xy=intersection_point, xytext=(-30,10),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))

# Customize plot
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.axis('equal')
plt.title('Intersection of Two Lines')
plt.xlabel('$x$')
plt.ylabel('$y$')

# Show plot
plt.show()
