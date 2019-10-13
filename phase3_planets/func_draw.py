# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   编制行星数据分析 （绘图函数库）
# ------------------------(max to 80 columns)-----------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import *


def draw_bar_vertical(title, label_name, x_label, x_data, y_label, y_data):
    '垂直条形图'

    '''
    几种调整中文字体的方法
    https://www.jb51.net/article/134546.htm


    https://blog.csdn.net/qq_29750461/article/details/100560859
        用print(matplotlib.matplotlib_fname())获取字体配置文件
        修改字体配置文件，添加 SimHei 或其他中文字符集
        重启电脑
    '''

    # 绘图
    '''
    x: 为一个标量序列，确定x轴刻度数目
    height: 和x对应，确定y轴的刻度
    width: 决定单个直方图的宽度,效果见图2
    '''
    plt.bar(x=x_data, height=y_data, label=label_name, color='steelblue')

    # 替换字体，以便 matplotlib 能够显示中文
    #plt.rcParams['font.sans-serif'] = ['FangSong']
    # plt.rcParams['font.sans-serif']=['SimHei']
    # plt.rcParams['font.family']='sans-serif'
    #plt.rcParams['axes.unicode_minus'] = False
    # 定义自定义字体，文件名从查看系统中文字体中来
    myfont = FontProperties(fname='C:\\Windows\\Fonts\\simfang.ttf')

    # MAC
    #plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

    # 设置标题
    #plt.title(title, fontproperties="System")
    plt.title(title, fontproperties=myfont)
    # 为两条坐标轴设置名称
    plt.xlabel(x_label, fontproperties=myfont)
    plt.ylabel(y_label, fontproperties=myfont)
    # 显示图例
    plt.legend()
    plt.show()

    return


def draw_bar_horizontal(title, label_name, x_label, x_data, y_label, y_data):
    '水平条形图'

    # 绘图
    # barh()表示绘制水平方向的条形图，基本使用方法为：
    # barh(y, width, height=0.8,align='center')
    plt.barh(y=x_data, width=y_data, height=0.8,
             label=label_name, color='steelblue')

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


def draw_bar_2serials(
        title, label_name, numbers,
        x_label, y_label,
        x1_data, y1_data,
        x2_data, y2_data,
):

    index = np.arange(numbers)
    bar_width = 0.3

    # 画第一个条形图
    plt.bar(x=index, height=y1_data,
            label=label_name[0], width=bar_width, color='b')
    # 叠加
    plt.bar(x=index + bar_width, height=y2_data,
            label=label_name[1], width=bar_width, color='r')

    # 替换字体，以便 matplotlib 能够显示中文
    # 可使用 get_fonts.py 查看所有的字体 （ 中文字体的拼音）
    plt.rcParams['font.sans-serif'] = ['FangSong']

    # 设置标题
    plt.title(title)

    # 设置网格
    plt.grid(True)
    plt.grid(color='r', linestyle='--')  # 修改网格颜色，类型为虚线

    # 为x,y坐标轴设置名称
    # plt.xlabel(x_label)
    plt.xticks(range(0, 7), x1_data)
    # plt.ylabel(y_label)

    # 显示图例
    plt.legend()
    plt.show()

    return


def draw_2D_planet(title, planet_names, planet_radius):
    '''
    圆的标准方程(x-a)²+(y-b)²=r²中
    有三个参数a、b、r，即圆心坐标为(a，b)，只要求出a、b、r，这时圆的方程就被确定，
    因此确定圆方程，须三个独立条件，
    其中圆心坐标是圆的定位条件，半径是圆的定形条件。
    '''
    start = 0
    stop = 2 * np.pi
    point_num = 100
    # 设置 x 值
    deta = np.linspace(start, stop, point_num, endpoint=True)

    radius = planet_radius.tolist()
    cnt = 0
    for r in radius:
        x = r * np.cos(deta)
        y = r * np.sin(deta)
        plt.plot(x, y, label=('%s' % planet_names[cnt]))
        cnt += 1

    plt.axis('scaled')  # 调整 x，y轴比例
    plt.rcParams['font.sans-serif'] = ['SimHei']    # 设置字体
    plt.title(title)    # 设置标题
    plt.grid(True)      # 设置网格
    plt.grid(color='r', linestyle='--')  # 修改网格颜色，类型为虚线
    plt.legend()        # 制作图例
    plt.show()          # 显示图像

    return
