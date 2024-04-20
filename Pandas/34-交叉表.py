import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('Pandas\data\stock_day.csv')
date = pd.to_datetime(data.index)
print(date)
print('-------------------------------------------')
data['week'] = date.weekday
print(data['week'])
print('-------------------------------------------')
data['posi_neg'] = np.where(data['p_change'] > 0, 1, 0)
print(data['posi_neg'])
print('-------------------------------------------')
count = pd.crosstab(data['week'], data['posi_neg'])
print(count)
print('-------------------------------------------')
sum = count.sum(axis=1).astype(np.float32)
print(sum)
print('-------------------------------------------')
pro = count.div(sum, axis=0)
print(pro)

# 画图展示
pro.plot(kind='bar', stacked=True)
plt.show()
