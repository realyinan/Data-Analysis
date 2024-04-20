import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')
print(data)
print(data.head())
data = data.drop(["ma5","ma10","ma20","v_ma5","v_ma10","v_ma20"], axis=1)
print(data)