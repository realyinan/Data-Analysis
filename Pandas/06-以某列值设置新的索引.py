import pandas as pd
import numpy as np

# set_index(keys, drop=True)
# keys : 列索引名成或者列索引名称的列表
# drop : boolean, default True.当做新的索引，删除原来的列

df = pd.DataFrame({'month': [1, 4, 7, 10],
                    'year': [2012, 2014, 2013, 2014],
                    'sale':[55, 40, 84, 31]})
print(df)
print(df.set_index('month'))
print(df.set_index(['month', 'year']))
