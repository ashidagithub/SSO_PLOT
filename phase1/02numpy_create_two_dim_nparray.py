# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习多维数组的创建
# ------------------------(max to 80 columns)-----------------------------------


import numpy as np

# ------------- 直接创建多维数组  nparray -------------------
print('----- 直接创建多维数组 cutting line -----')
# 默认为浮点数 - 常用于初始化
x = np.zeros([4, 5])  # 4行5列
print(x)
print(x.shape)

# 设置类型为整数 - 常用于初始化
y = np.zeros(([4, 5]), dtype=np.int)
print(y)
print(y.shape)

# ------------- 将列表或元组转化为多维数组  nparray -------------------
print('----- 将列表或元组转化为多维数组 cutting line -----')
# 从已有列表创建 np 数组
x = [[1, 2], [3, 4]]
a = np.asarray(x)
print(a)

# 将元组转换为 ndarray:
x = ((1, 2, 3), (4, 5, 6))
a = np.asarray(x)
print(a)

# 将列表转换成 ndarray 并更改其类型
x = [[1, 2], [3, 4]]
a = np.asarray(x, dtype=float)
print(a)

# ------------- 按指定的数值范围生成一维数组  nparray -------------------
print('----- 按指定的数值范围生成多维数组 cutting line -----')
# 生成 2x3 的数组:
row1 = [1,2,3]
row2 = [1,2,3]
x = np.asarray([row1,row2])
print(x)

# 将一个序列转换成 nXm 方阵
total = 100
row = 10
col = 10
x=np.arange(total).reshape(row,col)
print(x)
