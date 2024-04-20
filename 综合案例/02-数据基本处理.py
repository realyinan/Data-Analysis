import numpy as np
import pandas as pd

file_data = pd.read_csv('综合案例\data\链家北京租房数据.csv')

# 删除重复值
print(file_data.duplicated())
file_data = file_data.drop_duplicates()
print(file_data.info())

# 删除空值
file_data = file_data.dropna()
print(file_data.info())