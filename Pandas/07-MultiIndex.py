import pandas as pd
import numpy as np

df = pd.DataFrame({'month': [1, 4, 7, 10],
                    'year': [2012, 2014, 2013, 2014],
                    'sale':[55, 40, 84, 31]})
print(df)
print(df.set_index(['year', 'month']))
print(df.set_index(['year', 'month']).index)


array = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
df1 = pd.MultiIndex.from_arrays(array, names=['num', 'color'])
print(df1)
