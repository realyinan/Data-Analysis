import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')

print(data.query('open<24 & open>23'))
print(data[data['open'].isin([23.53, 23.85])])