import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')

print(data['open'].add(10))