import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')

# 获取'2018-02-27'这天的'open'的结果
# 直接使用行列索引名字的方式，必须使用先列后行的方式。（先列后行）
# 也不可以直接使用切片
print(data)
print(data['open']['2018-02-27'])
 