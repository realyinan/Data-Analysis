import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')

# apply(func, axis=0)
# func:自定义函数
# axis=0:默认是列，axis=1为行进行运算
# 定义一个对列，最大值-最小值的函数

print(data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0))
print(data[['open', 'close']].max())
