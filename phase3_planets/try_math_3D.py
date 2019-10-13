
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

start = 0.01
stop = 1
point_num = 97
x = np.linspace(start, stop, point_num, endpoint=False)
y = 1 - x
z = x * x / (x + 2) + y * y / (y + 1)
print(z.min())

ax.plot(x, y, z, label='parametric curve')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

print(z.min())
# set min
'''zm = z.min()
y_zm = 5
x_zm = 1 - 5
ax.scatter(x_zm, y_zm, zm, c='r', marker='o')'''

ax.legend()

plt.show()
