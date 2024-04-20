import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 如果我们想Runtime (Minutes)的分布情况
data = pd.read_csv('案例\data\IMDB-Movie-Data.csv')

plt.figure(figsize=(20, 8), dpi=70)

plt.hist(data['Runtime (Minutes)'].values, bins=20, alpha=0.75)

min = data['Runtime (Minutes)'].min()
max = data['Runtime (Minutes)'].max()
t1 = np.linspace(min, max, 21)
plt.xticks(t1)

plt.grid()
plt.show()