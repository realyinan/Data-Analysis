import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')
print(data['close'])
data['close'] = 1
print(data)