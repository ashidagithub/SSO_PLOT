# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 numpy 一些常用操作方法
# ------------------------(max to 80 columns)-----------------------------------

import numpy as np


'''
numpy.ndarray.flat
是一个数组元素迭代器，不改变数组内容，将多维数组变成数列输出:
'''
print('\n----- .flat --- cutting line ---')
row = 2
col = 4
a = np.arange(row * col).reshape(row, col)

for row in a:
    print(row)
print('当前数组形状是: ', a.shape)

# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
for element in a.flat:
    print(element)
print('使用 flat 迭代后的', end='')
print('当前数组形状是: ', a.shape)


'''
numpy.ndarray.flatten
返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：

ndarray.flatten(order='C')
参数说明：

order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
'''
print('\n----- .flatten --- cutting line ---')
row = 2
col = 5
a = np.arange(row * col).reshape(row, col)

print(a)
print('当前数组形状是: ', a.shape)

print('\n')
print('以 C 风格顺序展开的数组：')
print(a.flatten(order='C'))
print('使用 flatten 展开后的', end='')
print('当前数组形状是: ', a.shape)

print('\n')
print('以 F 风格顺序展开的数组：')
print(a.flatten(order='F'))
print('使用 flatten 展开后的', end='')
print('当前数组形状是: ', a.shape)


'''
numpy.ravel
numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图
（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。

该函数接收两个参数：

numpy.ravel(a, order='C')
参数说明：

order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。

'''
print('\n----- .ravel --- cutting line ---')
row = 2
col = 5
a = np.arange(row * col).reshape(row, col)

print(a)
print('当前数组形状是: ', a.shape)

print('\n')
print('以 C 风格顺序展平的数组：')
print(a.ravel(order='C'))
print('使用 ravel 展平后的', end='')
print('当前数组形状是: ', a.shape)

print('\n')
print('以 F 风格顺序展平的数组：')
print(a.ravel(order='F'))
print('使用 ravel 展平后的', end='')
print('当前数组形状是: ', a.shape)

'''
numpy.squeeze
函数从给定数组的形状中删除 “一维” 的条目
从数组的形状中删除单维度条目，即把shape中为1的维度去掉
'''
print('\n----- .squeeze --- cutting line ---')
x = 1
y = 1
z = 5
a = np.arange(x * y * z).reshape(x, y, z)

print('a=', a)
print('当前数组形状是: ', a.shape)
print('\n')

b = np.squeeze(a)
print('b=', b)
print('使用 squeeze 降维后的', end='')
print('当前数组形状是: ', b.shape)

print('数组 a 和 b 的形状比较（降维）：')
print(a.shape, b.shape)

'''
numpy.concatenate
用于沿指定轴连接相同形状的两个或多个数组

'''
print('\n----- .concatenate --- cutting line ---')

row = 3
col = 4
print('---第一个数组---')
a = np.arange(row * col).reshape(row, col)
print(a)
print('---第二个数组---')
b = np.arange(row * col).reshape(row, col)
print(b)

print('\n')
print('沿轴 0 连接两个数组：')
print(np.concatenate((a, b)))

print('\n')
print('沿轴 1 连接两个数组：')
print(np.concatenate((a, b), axis=1))
