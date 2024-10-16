import numpy as np

# Direction vector of the line
d = np.array([2, 3, 6])

# Normal vector of the plane
n = np.array([10, 2, -11])

# Dot product of d and n
dot_product = np.dot(d, n)

# Magnitudes of d and n
magnitude_d = np.linalg.norm(d)
magnitude_n = np.linalg.norm(n)

# Sine of the angle
sin_theta = abs(dot_product) / (magnitude_d * magnitude_n)

# Angle in radians
theta_rad = np.arcsin(sin_theta)

# Convert the angle to degrees
theta_deg = np.degrees(theta_rad)

print(f"The angle between the line and the plane is approximately {theta_deg:.2f} degrees.")

