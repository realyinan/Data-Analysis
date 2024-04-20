import pandas as pd
import numpy as np

data = pd.read_csv('Pandas\data\IMDB-Movie-Data.csv')
print(pd.notnull(data))
print(pd.isnull(data))
print(np.all(pd.notnull(data)))  # 里面有一个缺失值会返回false
print(np.any(pd.isnull(data)))  #  里面有一个缺失值会返回true
