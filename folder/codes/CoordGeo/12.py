import matplotlib.pyplot as plt
import numpy as np

# Define the equations of the lines
def line1(x):
    return (6 - x) / 2  # Rearranged from x + 2y = 6 to y = (6 - x) / 2

def line2(x):
    return (2 * x - 12) / 5  # Rearranged from 2x - 5y = 12 to y = (2x - 12) / 5

# Generate x values for plotting
x_values = np.linspace(-2, 10, 400)

# Calculate y values based on the line equations
y_values_line1 = line1(x_values)
y_values_line2 = line2(x_values)

# Calculate the point of intersection
# Solve the system of equations:
# x + 2y = 6
# 2x - 5y = 12

# Rearranging and solving the system using numpy
A = np.array([[1, 2], [2, -5]])
B = np.array([6, 12])
intersection = np.linalg.solve(A, B)

# Plot the lines
plt.plot(x_values, y_values_line1, label='x + 2y = 6', color='blue')
plt.plot(x_values, y_values_line2, label='2x - 5y = 12', color='red')

# Plot the point of intersection
plt.scatter(intersection[0], intersection[1], color='green', label=f'Intersection ({intersection[0]:.1f}, {intersection[1]:.1f})')

# Label the intersection point
plt.text(intersection[0] + 0.1, intersection[1] - 0.3, f'({intersection[0]:.1f}, {intersection[1]:.1f})', fontsize=12, color='green')

# Label the axes
plt.xlabel('x')
plt.ylabel('y')

# Setting axis limits
plt.xlim(-2, 10)
plt.ylim(-2, 10)

# Adding a grid
plt.grid(True)

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()

