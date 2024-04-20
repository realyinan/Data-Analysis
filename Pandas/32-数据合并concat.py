import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')
print(data)
p_change = data['p_change']
p_counts = pd.cut(p_change, bins = [-100, -7, -5, -3, 0, 3, 5, 7, 100])
dummies = pd.get_dummies(p_counts, prefix='rise')
print(dummies)
data_1 = pd.concat([data, dummies], axis=1)
print(data_1)