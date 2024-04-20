import numpy as np
import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')
p_change = data['p_change']
print(p_change)

# 自动分成差不多数量的类别
qcut = pd.qcut(p_change, 10)
print(qcut)
print(qcut.value_counts())  # 统计分组次数

# 指定分组区间
bins = [-100, -7, -5, -3, 0, 3, 5, 7, 100]
p_count = pd.cut(p_change, bins)
print(p_count)
print(p_count.value_counts())