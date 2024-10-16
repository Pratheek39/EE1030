import sympy as sp

def find_second_slope_fraction(m1, theta_deg):
    # Define the symbols
    m2 = sp.Symbol('m2')

#Convert angle from degrees to radians
    theta_rad = sp.rad(theta_deg)

#Calculate tan(theta)
    tan_theta = sp.tan(theta_rad)

#Solve the equation tan(theta) = |(m1 - m2) / (1 + m1 * m2)|
#We have two cases for the absolute value
#Case 1: tan(theta) = (m1 - m2) / (1 + m1 * m2)
    equation1 = sp.Eq(tan_theta, (m1 - m2) / (1 + m1 * m2))

#Case 2: tan(theta) = (m2 - m1) / (1 + m1 * m2)
    equation2 = sp.Eq(tan_theta, (m2 - m1) / (1 + m1 * m2))

#Solve the equations for m2
    m2_solutions1 = sp.solve(equation1, m2)
    m2_solutions2 = sp.solve(equation2, m2)

    return m2_solutions1, m2_solutions2

#Example usage
m1 = 1/2  # Slope of the first line
theta_deg = 45  # Angle between the two lines in degrees

m2_values1, m2_values2 = find_second_slope_fraction(m1, theta_deg)

print("The possible slopes of the second line are:")
for value in m2_values1:
    print(f"m2 = {value}")
for value in m2_values2:
    print(f"m2 = {value}")
