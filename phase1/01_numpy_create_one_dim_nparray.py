# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习一维数组的创建
# ------------------------(max to 80 columns)-----------------------------------
    

import numpy as np

# ------------- 直接创建一维数组  nparray -------------------
print('----- 直接创建一维数组 cutting line -----')
# 默认为浮点数 - 常用于初始化
x = np.zeros(5)
print(x)

# 设置类型为整数 - 常用于初始化
y = np.zeros((5,), dtype=np.int)
print(y)

# ------------- 将列表或元组转化为一维数组  nparray -------------------
print('----- 将列表或元组转化为一维数组 cutting line -----')
# 从已有列表创建 np 数组
x = [1, 2, 3]
a = np.asarray(x)
print(a)

# 将元组转换为 ndarray:
x = (1, 2, 3)
a = np.asarray(x)
print(a)

# 将列表转换成 ndarray 并更改其类型
x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)


# ------------- 按指定的数值范围生成一维数组  nparray -------------------
print('----- 按指定的数值范围生成一维数组 cutting line -----')
# 生成 0 到 5 的数组:
x = np.arange(5)
print(x)

# 设置了 dtype
x = np.arange(5, dtype=float)
print(x)

# 设置了起始值、终止值及步长：
x = np.arange(10, 20, 2)
print(x)

x = np.arange(50, 30, -2)
print(x)

'''
更专业的方法 - 等差数列
numpy.linspace 函数
用于创建一个一维数组，数组是一个等差数列构成的

参数说明：

参数	描述
start	序列的起始值
stop	序列的终止值，如果endpoint为true，该值包含于数列中
num	要生成的等步长的样本数量，默认为50
endpoint	该值为 ture 时，数列中中包含stop值，反之不包含，默认是True。
retstep	如果为 True 时，生成的数组中会显示间距，反之不显示。
dtype	ndarray 的数据类型

'''
print('----- 设置等差数列 cutting line -----')
# 设置起始点为 1 ，终止点为 10，数列个数为 19或20
a = np.linspace(1, 10, 19)
print(a)

# 设置元素全部是1的等差数列：
a = np.linspace(1, 1, 10)
print(a)

# 将 endpoint 设为 false，不包含终止值：
a = np.linspace(10, 20,  5, endpoint=False)
print(a)

'''
更专业的方法 - 等比数列
numpy.logspace 函数
用于创建一个于等比数列

base 参数意思是取对数的时候 log 的下标。

参数	描述
start	序列的起始值为：base ** start
stop	序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
num	要生成的等步长的样本数量，默认为50
endpoint	该值为 ture 时，数列中中包含stop值，反之不包含，默认是True。
base	对数 log 的底数。
dtype	ndarray 的数据类型

'''
print('----- 设置等比数列 cutting line -----')
# 默认底数是 10
a = np.logspace(1.0,  2.0, num=10)
print(a)


# 将对数的底数设置为 2 :
a = np.logspace(0, 9, num=10, base=2)
print(a)
