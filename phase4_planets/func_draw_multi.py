# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 matplotlib.pyplot 在Figure上创建子多个plot，并设置属性
# ------------------------(max to 80 columns)-----------------------------------


import matplotlib.pyplot as plt  # 约定俗成的写法plt
import numpy as np

# 两种方法实现
# https://www.cnblogs.com/xiaopengli/p/8058408.html
'''
在一块画布 - Figure上创建多个子plot

如果需要绘制多幅图表的话，可以给Figure传递一个整数参数指定图表的序号，
如果所指定序号的绘图对象已经存在的话，将不创建新的对象，而只是让它成为当前绘图对象。

'''


def draw_bar2(
    title, label_name,
    x_label, x_data,
    y_label, y_data
):

    # 绘图
    plt.bar(x=x_data, height=y_data, label=label_name, color='steelblue')

    # 替换字体，以便 matplotlib 能够显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # MAC
    #plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

    # 设置标题
    plt.title(title)
    # 为两条坐标轴设置名称
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # 显示图例
    plt.legend()
    # plt.show()

    return plt
