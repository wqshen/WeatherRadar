import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"D:\OneDrive\DATA\font\msyh.ttf", size=12)


x = np.array([0.5, 1, 5, 10, 20, 50, 100, 200])
y1 = np.array([0.11, 0.22, 1.1, 2.2, 4.4, 11, 22, 44])
y2 = np.array([0.003, 0.007, 0.061, 0.151, 0.375, 1.25, 3.08, 7.65])
y3 = np.array([0.001, 0.002, 0.014, 0.033, 0.0732, 0.214, 0.481, 1.083])
y4 = np.array([0.00015, 0.0003, 0.0015, 0.003, 0.006, 0.015, 0.030, 0.060])

# plt.plot(x, y1, label="0.9cm")
plt.plot(x, y2, label="3.2cm")
plt.plot(x, y3, label="5.6cm")
plt.plot(x, y4, label="10.0cm")

plt.xlabel("雨强（mm/h）", fontproperties=font)
plt.legend()
plt.title("不同雨强降水对不同波长的电磁波衰减系数", fontproperties=font)
plt.show()
