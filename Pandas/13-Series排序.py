import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')

data_1 = data['high']
print(data_1)
print('--------------------------------------')
print(data_1.sort_values(ascending=True))
print('--------------------------------------')
print(data_1.sort_index())