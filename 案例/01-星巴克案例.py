import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 获取数据
starbucks = pd.read_csv('案例\data\directory.csv')

# 分组聚合
count = starbucks.groupby(['Country']).count()  # 国家分组
count_1 = starbucks.groupby(['Country', 'State/Province']).count()
print(count)
print(count_1)

# 画图
count['Brand'].plot(kind='bar', figsize=(12, 5))

# 展示
plt.show()