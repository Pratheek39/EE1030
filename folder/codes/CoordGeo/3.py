# Code by GVV Sharma
# September 12, 2023
# Revised July 21, 2024
# Released under GNU GPL
# Section Formula

import sys  # for path to external scripts
import os   # Import os module to work with directories
sys.path.insert(0, '/home/pratheek/Desktop/Latex/matgeo/codes/CoordGeo')
# path to my scripts

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg  # Corrected typo

# Local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# If using termux
import subprocess
import shlex
# End if

# Given points
P = np.array(([-1, 3])).reshape(-1, 1)
Q = np.array(([2, 5])).reshape(-1, 1)

# Ratio
n = 2/3

# Point
R = (Q + n * P) / (1 + n)  # calculating the coordinate points of R which divides the join between the two points
# print(R)

# Generating all lines
x_PQ = line_gen(P, Q)

# Plotting all lines
plt.plot(x_PQ[0, :], x_PQ[1, :], label='$PQ$')

# Labeling the coordinates
tri_coords = np.block([[P, Q, R]])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['P', 'Q', 'R']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f})',
                 (tri_coords[0, i], tri_coords[1, i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(20, -10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center

# Set axis appearance
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.legend(loc='best')
plt.grid()  # minor
plt.axis('equal')

# Save or show the plot
output_dir = 'chapters/10/7/2/1/figs/'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'fig.pdf'))


