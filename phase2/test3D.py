import matplotlib as mpl

from mpl_toolkits.mplot3d import Axes3D

import numpy as np

import matplotlib.pyplot as plt

import math


mpl.rcParams['legend.fontsize'] = 10



fig = plt.figure()

ax = fig.gca(projection='3d')

'''theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)

z = np.linspace(-2, 2, 100)

r = z**2 + 1

x = r * np.sin(theta)

y = r * np.cos(theta)'''

start = -10
stop = 10
point_num = 999
x = np.linspace(start, stop, point_num, endpoint=False)
y = 1 - x
z = x*x/(x+2)+y*y/(y+1)

ax.plot(x, y, z, label='parametric curve')

ax.set_xlabel('X Label')

ax.set_ylabel('Y Label')

ax.set_zlabel('Z Label')


# set min
zm = z.min()
y_zm = 5
x_zm = 1 - 5
ax.scatter(x_zm, y_zm, zm, c='r', marker='o')

ax.legend()



plt.show()
