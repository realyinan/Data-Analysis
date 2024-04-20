import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 如果我们想Rating的分布情况
data = pd.read_csv('案例\data\IMDB-Movie-Data.csv')

plt.figure(figsize=(10, 8), dpi=70)

plt.hist(data['Rating'].values, bins=20)

min = data['Rating'].min()
max = data['Rating'].max()
t1 = np.linspace(min, max, num=21)
plt.xticks(t1)

plt.grid()
plt.show()