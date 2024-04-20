import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')

print(data.loc['2018-02-27':'2018-02-22', 'open'])
print(data.iloc[:3, :5])