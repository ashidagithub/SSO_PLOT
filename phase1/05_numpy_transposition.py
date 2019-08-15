# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 numpy 的数组转置方法
# ------------------------(max to 80 columns)-----------------------------------

import numpy as np

row = 2
col = 3
a = np.arange(row * col).reshape(row, col)

# 方法一： 使用 .T 进行简单转置
print(a)
print(a.T)

# 方法二： 使用 .transpose 进行简单转置
print ('对换数组：')
print (np.transpose(a))
