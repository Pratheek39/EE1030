import numpy as np

# Define the vectors
A = np.array([3, 5, 4])
B = np.array([1, 1, 1])

# Calculate the dot product of A and B
dot_product = np.dot(A, B)

# Calculate the magnitudes of A and B
magnitude_A = np.linalg.norm(A)
magnitude_B = np.linalg.norm(B)

# Calculate the cosine of the angle using the dot product formula
cos_theta = dot_product / (magnitude_A * magnitude_B)

# Calculate the angle in radians
theta_radians = np.arccos(cos_theta)

# Convert the angle to degrees
theta_degrees = np.degrees(theta_radians)

# Print the angle
print(f"The angle between vectors A and B is {theta_degrees:.2f} degrees")

