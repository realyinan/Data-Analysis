import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('案例\data\IMDB-Movie-Data.csv')

# 得出评分的平均数
avg = data['Rating'].mean()
print(avg)

# 得出导演人数信息
count = np.unique(data['Director']).shape[0]
print(count)
