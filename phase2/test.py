# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 matplotlib.pyplot 初步知识
# ------------------------(max to 80 columns)-----------------------------------


import matplotlib.pyplot as plt  # 约定俗成的写法plt
import numpy as np
# Try 3 ----------------------------------------------------------
# try3 简单的二次函数作图

# 设置 x 定义域
start = 0.01
stop = 100
# 设置 x 样本数
point_num = 987
# 设置 x 值
x = np.linspace(start, stop, point_num, endpoint=False)
# 获得 y 值
y = x * (x - 8) / (x - 9)
# 用 (x, y) 点作图
plt.plot(x, y)
plt.show()

# 定义一次函数并作图
#y = x*(x-8)/(x-9)
#y = (2*x*x-3*x+2)/(4-x*x)
#z = x*x/(x+2)+y*y/(y+1)
plt.plot(x, y)

# 在ipython的交互环境中需要这句话才能显示出来
plt.show()
print(y.min())
