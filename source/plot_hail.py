import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"D:\OneDrive\DATA\font\msyh.ttf", size=12)

iterables = [['3.21', '5.5', '10.0'], ['0', '0.01', '0.05', '0.1']]
index = pd.MultiIndex.from_product(iterables, names=['波长（cm）', '水膜厚度（cm）'])

array = np.array([[0.12, 0.91, 1.68, 1.50, 0.015, 0.19, 0.56, 0.94, 0.002, 0.051, 0.058, 0.08],
				   [1.21, 3.01, 3.72, 3.49, 0.18, 0.79, 2.48, 2.30, 0.011, 0.15, 0.34, 0.89],
				   [1.66, 3.46, 4.03, 3.79, 0.33, 1.22, 2.82, 2.60, 0.034, 0.19, 0.60, 1.18]])



df = pd.DataFrame(array.T, columns=['0.97', '1.93', '2.89'], index=index)
df.style.background_gradient(cmap='viridis')
# df.style.bar(align='mid')
# print(df.min().min())
# normal = plt.Normalize(df.min().min()-1, df.max().max()+1)
the_table=plt.table(cellText=df)
plt.show()