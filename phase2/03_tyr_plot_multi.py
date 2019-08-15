# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 matplotlib.pyplot 在Figure上创建子多个plot，并设置属性
# ------------------------(max to 80 columns)-----------------------------------


import matplotlib.pyplot as plt  # 约定俗成的写法plt
import numpy as np

'''
在一块画布 - Figure上创建多个子plot

如果需要绘制多幅图表的话，可以给Figure传递一个整数参数指定图表的序号，
如果所指定序号的绘图对象已经存在的话，将不创建新的对象，而只是让它成为当前绘图对象。

'''

'''
# Try1 --------------------------------------------------------
fig1 = plt.figure(2)
plt.subplot(211)
# subplot(211)把绘图区域等分为2行*1列共两个区域，然
# 后在区域1（上区域）中创建一个轴对象
plt.subplot(212)  # 在区域2（下区域）创建一个轴对象
plt.show()

# Try2 --------------------------------------------------------
fig1 = plt.figure(3)  # 弹出对话框时的标题，如果显示的形式为弹出对话框的话
plt.subplot(221)
plt.subplot(222)
plt.subplot(212)
plt.subplots_adjust(left=0.08, right=0.95, wspace=0.25, hspace=0.45)
# subplots_adjust的操作时类似于网页css格式化中的边距处理，左边距离多少？
# 右边距离多少？这取决于你需要绘制的大小和各个模块之间的间距
plt.show()

'''

# Try3 --------------------------------------------------------
row = 5
col = 5
fig, axes = plt.subplots(row, col)  # 定一个2*2的plot
axes[0, 0].set(title='Upper Left')
axes[0, 1].set(title='Upper Right')
axes[1, 0].set(title='Lower Left')
axes[1, 1].set(title='Lower Right')

# 通过Axes的flat属性进行遍历
for ax in axes.flat:   # 展平处理
    #     xticks和yticks设置为空置
    ax.set(xticks=[], yticks=[])
plt.show()
