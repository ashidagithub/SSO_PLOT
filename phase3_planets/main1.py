# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   编制行星数据分析 （主程序）
# ------------------------(max to 80 columns)-----------------------------------
import math
import numpy as np

from func_draw import *

# 多个行星数据转换成矩阵  ---------
# 从 EXCEL 复制数据，组成3个一维数组（元组）
# ----------------------------------------------------
# Name of the planet 行星名称
row0 = ('Earth', 'Mercury', 'Venus', 'Mars',
        'Jupiter', 'Saturn', 'Uranus', 'Neptune')
# Diameter of planet 行星直径 单位（km）
row1 = (12756, 4878, 12104, 6794,
        142984, 120540, 51118, 49532)
# Mass of planet 行星质量 单位（kg）
row2 = (5.9650E+24, 3.3022E+23, 4.8690E+24, 6.4219E+23,
        1.9000E+27, 5.6846E+26, 8.6810E+25, 1.0247E+26)
# The period of revolution  公转周期（天）
row3 = (365.24, 87.97, 224.70, 686.98, 4332.43, 10832.33, 30680.34, 60191.91)
# Average revolution speed  平均公转速度（km/s)
row4 = (29.78, 47.87, 35.03, 24.13, 13.07, 9.69, 6.81, 5.43)

# ----------------------------------------------------
# 常数
G = 6.67259 * math.pow(10, -11)
AU = 149597870700

# ----------------------------------------------------
# 基本信息
pName = np.asarray(row0)
pD = np.asarray(row1)

pM = np.asarray(row2)

# 体积密度
pR = pD * 0.5
pV = np.power(pR, 3) * (4 / 3 * math.pi)
pP = pM * 1000 / (pV * math.pow(10, 15))

# 速度
pg = G * pM / (pR**2) / math.pow(10, 6)
pVe = np.sqrt(2 * G * pM / pR / 1000) / 1000

# 公转 revolution
pPR = np.asarray(row3)
pVR = np.asarray(row4)

pCR1 = pPR * 3600 * 24 * pVR
pCR2 = pCR1 * 1000 / AU

# Try1 开始画图
draw_bar1('行星直径对比', 'Planet Name', pName, 'Planet Diameter', pD, '千米(km)')
draw_bar1('行星质量对比', 'Planet Name', pName, 'Planet Mass', pM, '千克(kg)')

# Try2 --------------------------------------------------------
fig2 = plt.figure()  # 弹出对话框时的标题，如果显示的形式为弹出对话框的话
pst1 = plt.subplot(221)
pst2 = plt.subplot(222)
pst3 = plt.subplot(212)
