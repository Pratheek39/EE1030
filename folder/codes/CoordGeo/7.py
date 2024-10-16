import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys               #for path to external scripts
sys.path.insert(0, '/home/pratheek/Desktop/Latex/matgeo/codes/CoordGeo')        #path to my scripts

#local imports
from conics.funcs import circ_gen
from line.funcs import *

# Points x1 and x2 (diametrically opposite)
x1 = np.array([1, 4]).reshape(-1, 1) 
x2 = np.array([3, -10]).reshape(-1, 1) 

# Calculate center (O) and radius (r)
O = (x1 + x2) / 2  # Midpoint formula
r = LA.norm(x1 - x2) / 2  # Half of the distance between x1 and x2
print(x2)
# Generating circle
x_circ = circ_gen(O, r)

# Generating line segment joining x1 and x2
line_segment = np.hstack((x1, x2))

# Plotting all lines and circles
plt.plot(x_circ[0, :], x_circ[1, :], label=r'$Circle$')
plt.plot(line_segment[0, :], line_segment[1, :], label='Line joining $\mathbf{x}_1$ and $\mathbf{x}_2$', color='orange')

colors = np.arange(1, 4)
# Labeling the coordinates
tri_coords = np.block([x1, x2, O])
plt.scatter(tri_coords[0, :], tri_coords[1, :], c=colors)
vert_labels = [r'$\mathbf{x}_1$', r'$\mathbf{x}_2$', r'$\mathbf{O}$']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]),  # Point to label
                 textcoords="offset points",  # How to position the text
                 xytext=(-20,5),  # Distance from text to points (x,y)
                 ha='center')  # Horizontal alignment

# Customizing the plot
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid()  # minor
plt.axis('equal')

plt.show()

