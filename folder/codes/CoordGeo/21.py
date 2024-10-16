#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/pratheek/Desktop/Latex/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
import ctypes
from ctypes import Structure, c_double

A = np.array(([3, -4,-5])).reshape(-1,1) 
B = np.array(([2,-3,1])).reshape(-1,1)  
C = np.array(([1,-2,7])).reshape(-1,1)  
# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Generate grid points for x and y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Calculate corresponding z values for each (x, y) pair to satisfy the plane equation
Z = (-2*X - Y + 7)

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5)
#ax.plot_surface(X, Y, Z, alpha=0.5,color="grey")

#Generating all lines
x_BC = line_gen(C,A)


#Plotting all lines
ax.plot(x_BC[0,:],x_BC[1,:], x_BC[2,:],label='$BC$')

# Scatter plot
colors = np.arange(2, 5)  # Example colors
tri_coords = np.block([A, B,C])  # Stack A, B, C vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['A', 'B','C']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    #ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i],f'{txt}',fontsize=12, ha='center', va='bottom')
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f}, {tri_coords[2, i]:.0f})',
             fontsize=12, ha='center', va='bottom')


ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Set limits and aspect ratio to magnify the plane
ax.set_xlim(-4, 4)  # Adjust limits based on your data
ax.set_ylim(-4, 4)  # Adjust limits based on your data
ax.set_zlim(-4, 4)  # Adjust limits based on your data
ax.set_box_aspect([1,1,1])  # Equal aspect ratio for x, y, and z axes
'''
ax.spines['left'].set_visible(False)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.xlabel('$x$')

plt.ylabel('$y$')

plt.legend(loc='best')

'''
ax.set_xlabel('$X$-Axis')
ax.set_ylabel('$Y$-Axis')
ax.set_zlabel('$Z$-Axis')
plt.grid() # minor
plt.axis('equal')
plt.title('Perpendicular Bisecting Plane of A and B', loc = 'right', pad = 15)
plt.show()
