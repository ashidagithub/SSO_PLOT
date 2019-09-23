# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   编制行星数据分析 （绘图函数库）
# ------------------------(max to 80 columns)-----------------------------------
import numpy as np
import matplotlib.pyplot as plt


def draw_bar1(title, x_label, x_data, y_label, y_data, label_name):

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
    plt.show()

    return
