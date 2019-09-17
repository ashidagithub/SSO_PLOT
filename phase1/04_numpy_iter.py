# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 numpy 的迭代功能
# ------------------------(max to 80 columns)-----------------------------------

import pdb
import numpy as np

'''
NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。
迭代器最基本的任务的可以完成对数组元素的访问。
'''

print('----- 任意一个 nparray 的迭代 cutting line -----')
# 接下来我们使用 arange() 函数创建一个 2X3 数组，并使用 nditer 对它进行迭代。
a = np.arange(10).reshape(2, 5)
print('原始数组是：')
print(a)
print('\n')
print('迭代输出元素：')
for x in np.nditer(a):
    print(x, end=", ")
print('\n')

'''
以上实例不是使用标准 C 或者 Fortran 顺序，选择的顺序是和数组内存布局一致的，
这样做是为了提升访问的效率，默认是行序优先（row-major order，或者说是 C-order）。

这反映了默认情况下只需访问每个元素，而无需考虑其特定顺序。
我们可以通过迭代上述数组的转置来看到这一点，
并与以 C 顺序访问数组转置的 copy 方式做对比
'''
print('----- 任意一个 nparray 的按C-order 或 T-order迭代 cutting line -----')
a = np.arange(10).reshape(2, 5)
print('原始数组是：')
print(a)
print('\n')

print('按行优先方式 C-order 迭代输出元素：')
for x in np.nditer(a, order='C'):
    print(x, end=", ")
print('\n')

print('按列优先方式 F-order 迭代输出元素：')
for x in np.nditer(a, order='F'):
    print(x, end=", ")
print('\n')
