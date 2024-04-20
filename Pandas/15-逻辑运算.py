import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')

print(data['open'] > 23)

# 逻辑判断的结果可以作为筛选的依据
print(data[data['open'] > 23].head())
# 完成多个逻辑判断
print(data[(data['open'] > 23) & (data['open'] < 24)].head())
