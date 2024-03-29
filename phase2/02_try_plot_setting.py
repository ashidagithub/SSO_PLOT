# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   练习 matplotlib.pyplot 在Figure上创建子plot，并设置属性
# ------------------------(max to 80 columns)-----------------------------------


import matplotlib.pyplot as plt  # 约定俗成的写法plt
import numpy as np

x = np.linspace(0, 10, 1000)  # X轴数据

y1 = np.sin(x)  # Y轴数据
y2 = np.cos(x**2)  # Y轴数据  x**2即x的平方

plt.figure(figsize=(16, 8))

plt.plot(x, y1, label="$sin(x)$", color="red", linewidth=2)  # 将$包围的内容渲染为数学公式
plt.plot(x, y2, "b--", label="$cos(x^2)$")
# 指定曲线的颜色和线性，如‘b--’表示蓝色虚线（b：蓝色，-：虚线）

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("Plot setting")

'''
使用关键字参数可以指定所绘制的曲线的各种属性：
label：给曲线指定一个标签名称，此标签将在图标中显示。
如果标签字符串的前后都有字符'$'，则Matplotlib会使用其内嵌的LaTex引擎将其显示为数学公式
color：指定曲线的颜色。颜色可以用如下方法表示
       英文单词
       以‘#’字符开头的3个16进制数，如‘#ff0000’表示红色。
       以0~1的RGB表示，如（1.0,0.0,0.0）也表示红色。
linewidth：指定权限的宽度，可以不是整数，也可以使用缩写形式的参数名lw。
'''

plt.ylim(-2, 2)  # Y limit
plt.legend()  # 显示左下角的图例

plt.show()
