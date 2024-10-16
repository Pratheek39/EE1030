import matplotlib.pyplot as plt
import numpy as np

# Coordinates of points A and B
A = np.array([7, 6])
B = np.array([3, 4])

# Midpoint of A and B
midpoint = (A + B) / 2

# Slope of line AB
slope_AB = (B[1] - A[1]) / (B[0] - A[0])

# Slope of the perpendicular bisector (negative reciprocal of slope_AB)
slope_perp_bisector = -1 / slope_AB

# Equation of the perpendicular bisector: y = mx + c
# y - y1 = m(x - x1), where (x1, y1) is the midpoint
c = midpoint[1] - slope_perp_bisector * midpoint[0]

# Generating x values for the plot
x_values = np.linspace(0, 10, 400)

# Corresponding y values for the perpendicular bisector
y_values = slope_perp_bisector * x_values + c

# Plotting points A and B
plt.scatter(A[0], A[1], color='red', label='Point A(7, 6)')
plt.scatter(B[0], B[1], color='blue', label='Point B(3, 4)')

# Plotting the line AB
plt.plot([A[0], B[0]], [A[1], B[1]], color='green', linestyle='--', label='Line AB')

# Plotting the perpendicular bisector
plt.plot(x_values, y_values, color='purple', label='Perpendicular Bisector')

# Plotting the midpoint
plt.scatter(midpoint[0], midpoint[1], color='orange', label='Midpoint')

# Labeling the points
plt.text(A[0] + 0.1, A[1] - 0.2, 'A(7, 6)', fontsize=12, color='red')
plt.text(B[0] + 0.1, B[1] - 0.2, 'B(3, 4)', fontsize=12, color='blue')
plt.text(midpoint[0] + 0.1, midpoint[1] + 0.2, f'Midpoint({midpoint[0]:.1f}, {midpoint[1]:.1f})', fontsize=12, color='orange')

# Labeling the axes
plt.xlabel('x')
plt.ylabel('y')

# Setting axis limits
plt.xlim(0, 10)
plt.ylim(0, 10)

# Adding a grid
plt.grid(True)

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()

