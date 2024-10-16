import numpy as np

# Normal vector of the plane 6x - 3y + 2z = -1
normal_vector = np.array([6, -3, 2])

# Magnitude of the normal vector
magnitude = np.linalg.norm(normal_vector)

# Unit vector in the direction of the normal vector
unit_vector = normal_vector / magnitude

# Direction cosines are the components of the unit vector
direction_cosines = unit_vector

# Print the direction cosines
print(f"Direction cosines of the unit vector perpendicular to the plane are: {direction_cosines}")

