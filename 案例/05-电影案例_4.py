from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# 如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
data = pd.read_csv('案例\data\IMDB-Movie-Data.csv')

temp_list = [i.split(',') for i in data['Genre']]
genre_list = np.unique([i for j in temp_list for i in j])
 
temp_df = pd.DataFrame(np.zeros([data.shape[0], genre_list.shape[0]]), columns=genre_list)

for i in range(1000):
    temp_df.loc[i,temp_list[i]] = 1
count = temp_df.sum().sort_values()

# 画图
count.plot(kind='bar', figsize=(10, 8),colormap='cool')

plt.show()