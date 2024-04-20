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
count = data.pivot_table(['posi_neg'], index='week')
print(count)
