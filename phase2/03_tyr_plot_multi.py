# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 matplotlib.pyplot 在Figure上创建子多个plot，并设置属性
# ------------------------(max to 80 columns)-----------------------------------


import matplotlib.pyplot as plt  # 约定俗成的写法plt
import numpy as np
import os

def get_path (no):
    img_path =  os.getcwd() + '\\saved_imgs\\test_try%d.png' % no
    return img_path

# 两种方法实现
# https://www.cnblogs.com/xiaopengli/p/8058408.html
'''
在一块画布 - Figure上创建多个子plot

如果需要绘制多幅图表的话，可以给Figure传递一个整数参数指定图表的序号，
如果所指定序号的绘图对象已经存在的话，将不创建新的对象，而只是让它成为当前绘图对象。

'''
img_dpi = 80


# Try1 --------------------------------------------------------
fig1 = plt.figure()
plt.subplot(211)
# subplot(211)把绘图区域等分为2行*1列共两个区域，然
# 后在区域1（上区域）中创建一个轴对象
plt.subplot(212)  # 在区域2（下区域）创建一个轴对象
'''
保存Figure对象

最后一项操作就是保存，我们绘图的目的是用在其他研究中，
或者希望可以把研究结果保存下来，并通过 Web 展示，此时需要的操作时save。
'''
plt.savefig(get_path(1), dpi=img_dpi)  # 默认像素dpi是80
plt.show()


# Try2 --------------------------------------------------------
fig2 = plt.figure()  # 弹出对话框时的标题，如果显示的形式为弹出对话框的话
pst1 = plt.subplot(221)
pst2 = plt.subplot(222)
pst3 = plt.subplot(212)

plt.subplots_adjust(left=0.08, right=0.95, wspace=0.25, hspace=0.45)
# subplots_adjust的操作时类似于网页css格式化中的边距处理，左边距离多少？
# 右边距离多少？这取决于你需要绘制的大小和各个模块之间的间距
print(type(pst1))

plt.savefig(get_path(2), dpi=img_dpi)  # 默认像素dpi是80
plt.show()


# Try3 --------------------------------------------------------
row = 2
col = 2
fig3 = plt.figure()
ax1 = fig3.add_axes([0.1,0.1,0.8,0.8])
ax2 = fig3.add_axes([0.25,0.25,0.4,0.4])
print(type(ax1))

plt.savefig(get_path(3), dpi=img_dpi)  # 默认像素dpi是80
plt.show()

# Try4 --------------------------------------------------------
# 高级用法，直接把子图设置成数组形式
fig4, axes = plt.subplots(row, col)  # 定一个2*2的plot
axes[0, 0].set(title='Upper Left')
axes[0, 1].set(title='Upper Right')
axes[1, 0].set(title='Lower Left')
axes[1, 1].set(title='Lower Right')

# 通过Axes的flat属性进行遍历
for ax in axes.flat:   # 展平处理
    #     xticks和yticks设置为空置
    ax.set(xticks=[], yticks=[])  # 不要 x 和 y 轴的数值

plt.savefig(get_path(4), dpi=img_dpi)  # 默认像素dpi是80
plt.show()
