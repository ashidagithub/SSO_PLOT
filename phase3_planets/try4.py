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

# 公转 revolution
# The period of revolution  公转周期（天）
row3 = (365.24, 87.97, 224.70, 686.98, 4332.43, 10832.33, 30680.34, 60191.91)
pPR = np.asarray(row3)

# Average revolution speed  平均公转速度（km/s)
row4 = (29.78, 47.87, 35.03, 24.13, 13.07, 9.69, 6.81, 5.43)
pVR = np.asarray(row4)

# 天文单位换算  1 A.U. = 149597870700 米
AU = 149597870700

# 公转周长-1 单位（km）
print('\n-----行星公转周长（km）是 (Circumference of revolution)-----')
pCR1 = pPR * 3600 * 24 * pVR
print(pCR1)

# 公转周长-2 单位（A.U.）
print('\n-----行星公转周长（A.U.）是 (Circumference of revolution)-----')
pCR2 = pCR1 *1000 / AU
print(pCR2)

#revolution radius
print('\n-----行星公转半径（A.U.）是 (The radius of revolution)-----')
pRR = pCR2 / 2 / math.pi
print(pRR)
