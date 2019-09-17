# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 matplotlib.pyplot 初步知识
# ------------------------(max to 80 columns)-----------------------------------


import matplotlib.pyplot as plt  # 约定俗成的写法plt
import numpy as np

'''
# Try 1 ----------------------------------------------------------
# try1 简单的正弦余弦图
# 设置起始数值，以及取样点数
start = -np.pi
stop = np.pi
point_num = 10
# 设置x值， -π to+π的256个值
x = np.linspace(start, stop, point_num, endpoint=True)

# 首先定义两个函数（正弦&余弦）
C = np.cos(x)
S = np.sin(x)
plt.plot(x, C)
plt.plot(x, S)

# 在ipython的交互环境中需要这句话才能显示出来
plt.show()

# Try 2 ----------------------------------------------------------
# try2 简单的一次函数作图
start = 1
stop = 100
point_num = 50
# 设置 x 值
x = np.linspace(start, stop, point_num, endpoint=True)

# 设置 a，b
a = 3
b = 4

# 定义一次函数并作图
y = a * x + b
plt.plot(x, y)

# 在ipython的交互环境中需要这句话才能显示出来
plt.show()

# Try 3 ----------------------------------------------------------
# try3 简单的二次函数作图
start = -1000
stop = 1000
point_num = 10
# 设置 x 值
x = np.linspace(start, stop, point_num, endpoint=True)

# 设置 a，b, c
a = 3
b = 4
c = 5
# 定义一次函数并作图
y = a * x * x + b * x + c
plt.plot(x, y)

# 在ipython的交互环境中需要这句话才能显示出来
plt.show()
'''

# Try 4 ----------------------------------------------------------
# try4 高中其他函数作图
start = -10
stop = 10
point_num = 100
# 设置 x 值
x = np.linspace(start, stop, point_num, endpoint=True)
#y = 2 * x / (x * x + 1) - 2
y = x * x * np.exp(x)
'''
np 的数学公式参见
https://www.cnblogs.com/keepgoingon/p/7137448.html
'''
plt.plot(x, y)

# 在ipython的交互环境中需要这句话才能显示出来
plt.show()
