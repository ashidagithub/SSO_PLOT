# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   编制行星数据分析 （一维矩阵运算）
# ------------------------(max to 80 columns)-----------------------------------
import math
import numpy as np

# 多个行星数据转换成矩阵  ---------
# 从 EXCEL 复制数据，组成3个一维数组（元组）
# Name of the planet 行星名称
row0 = ('Earth', 'Mercury', 'Venus', 'Mars',
        'Jupiter', 'Saturn', 'Uranus', 'Neptune')
# Diameter of planet 行星直径 单位（km）
row1 = (12756, 4878, 12104, 6794,
        142984, 120540, 51118, 49532)
# Mass of planet 行星质量 单位（kg）
row2 = (5.9650E+24, 3.3022E+23, 4.8690E+24, 6.4219E+23,
        1.9000E+27, 5.6846E+26, 8.6810E+25, 1.0247E+26)

pName = np.asarray(row0)
pD = np.asarray(row1)
pM = np.asarray(row2)

print('\n-----行星半径系数-----')
rate_radius = 0.5
print(rate_radius)
print(type(rate_radius))
# 矩阵定义方式
#rate_radius = np.asarray([0.5])
# print(rate_radius)
# print(rate_radius.dtype)

# 转换为半径并输出   矩阵*单个数字 （广播）
print('\n-----行星半径 (Planet Radius)-----')
pR = pD * rate_radius
print(pR)
print(pR.dtype)

# 转换为体积并输出 （矩阵中的幂函数）
print('\n-----行星体积 (Planet Volumne)-----')
rate_volume = 4 / 3 * math.pi
pV = np.power(pR, 3) * rate_volume
print(pV)
print(pV.dtype)

# 计算密度 （矩阵*单个数字， 普通的 math幂函数
print('\n-----行星密度 (Planet Density)-----')
pP = pM * 1000 / (pV * math.pow(10, 15))
print(pP)
print(pP.dtype)
