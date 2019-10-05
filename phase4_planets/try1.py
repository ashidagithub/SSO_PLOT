# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   编制行星数据分析（创建矩阵）
# ------------------------(max to 80 columns)-----------------------------------
import numpy as np

'''
# 单个行星数据转换成矩阵 (错误：数据类型不同)
data = ('Earth', 12756, 5.9650E+24)
print(data)

planet = np.asarray(data)
print(planet)
'''

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
print(pName)
print(pName.dtype)

pD = np.asarray(row1)
print(pD)
print(pD.dtype)

pM = np.asarray(row2)
print(pM)
print(pM.dtype)
