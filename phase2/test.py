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
start = 0.01
stop = 1
point_num = 97
# 设置 x 值
x = np.linspace(start, stop, point_num, endpoint=False)
y = 1 - x
z = x*x/(x+2)+y*y/(y+1)

# 定义一次函数并作图
#y = x*(x+8)/(x-1)
#y = (2*x*x-3*x+2)/(4-x*x)
#z = x*x/(x+2)+y*y/(y+1)
plt.plot(x, y, z)

# 在ipython的交互环境中需要这句话才能显示出来
plt.show()
print(y.min())
