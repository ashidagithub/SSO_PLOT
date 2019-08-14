# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 广播 broadcast 功能
# ------------------------(max to 80 columns)-----------------------------------

import numpy as np


'''
广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式，
对数组的算术运算通常在相应的元素上进行。

如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，
那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。
'''
# ------------- 两个数组相乘  broadcast -------------------
print('----- 两个数组相乘 cutting line -----')
a = np.array([1,2,3,4])
print(a.shape)
b = np.array([10,20,30,40,50])
print(b.shape)

if a.shape == b.shape:
    c = a * b
    print (c)
else:
    print('数组形状不同，无法相乘')
