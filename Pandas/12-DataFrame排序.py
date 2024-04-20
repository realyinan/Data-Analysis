import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')

# 排序有两种形式，一种对于索引进行排序，一种对于内容进行排序

# 使用df.sort_values(by=, ascending=)
# 单个键或者多个键进行排序,
# 参数：
# by：指定排序参考的键
# ascending:默认升序
# ascending=False:降序
# ascending=True:升序
print(data.sort_values(by='open', ascending=True))
print('-----------------------------------------------')
print(data.sort_values(by='open', ascending=False))
print('-----------------------------------------------')
print(data.sort_values(by=['open', 'high']))
print('--------------------------------------------------')
# 使用df.sort_index给索引进行排序
print(data.sort_index())
