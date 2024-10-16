#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Secion Formula


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/pratheek/Desktop/Latex/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen






# Define points A and B as column vectors
A = np.array([[7], [-1]]) # Point A as a 2x1 column vector
B = np.array([[-3], [-4]]) # Point B as a 2x1 column vector

# Combine A and B into a single 2x2 matrix
AB = np.hstack((A, B)) # [A B]

# Define the weight vector n
n = np.array([3/5, 2/5]).reshape(-1, 1) # n = [3/5, 2/5]^T

# Compute the point C
C = np.dot(AB, n) # C = [A B] * n

# Display the result
print("Matrix AB:\n", AB)
print("Weight vector n:\n", n)
print("Resulting point C:\n", C)
import numpy as np

# Define points A and B as column vectors
A = np.array([[7], [-1]]) # Point A as a 2x1 column vector
B = np.array([[-3], [-4]]) # Point B as a 2x1 column vector

# Combine A and B into a single 2x2 matrix
AB = np.hstack((A, B)) # [A B]

# Define the weight vector n
n = np.array([3/5, 2/5]).reshape(-1, 1) # n = [3/5, 2/5]^T

# Compute the point C
C = np.dot(AB, n) # C = [A B] * n

# Display the result
print("Matrix AB:\n", AB)
print("Weight vector n:\n", n)
print("Resulting point C:\n", C)
import numpy as np

# Define points A and B as column vectors
A = np.array([[7], [-1]]) # Point A as a 2x1 column vector
B = np.array([[-3], [-4]]) # Point B as a 2x1 column vector

# Combine A and B into a single 2x2 matrix
AB = np.hstack((A, B)) # [A B]

# Define the weight vector n
n = np.array([3/5, 2/5]).reshape(-1, 1) # n = [3/5, 2/5]^T

# Compute the point C
C = np.dot(AB, n) # C = [A B] * n

# Display the result
print("Matrix AB:\n", AB)
print("Weight vector n:\n", n)
print("Resulting point C:\n", C)

#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

#Labeling the coordinates
tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,-10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
# use set_position
ax = plt.gca()
#ax.spines['top'].set_color('none')
#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
#plt.xlabel('$x$')
#plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
