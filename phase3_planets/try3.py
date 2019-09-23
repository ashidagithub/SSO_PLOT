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
pR = pD * 0.5
pV = np.power(pR, 3) * (4 / 3 * math.pi)
pP = pM * 1000 / (pV * math.pow(10, 15))

# 表面重力
print('\n-----行星表面重力 (Planet g)-----')
G = 6.67259 * math.pow(10, -11)
pg = G * pM / (pR**2) / math.pow(10, 6)
print(pg)

# 逃逸速度 (escape velocity )  （矩阵中的平方根函数）
print('\n-----行星逃逸速度 (Planet escape velocity)-----')
pVe = np.sqrt(2 * G * pM / pR / 1000) / 1000
print(pVe)
