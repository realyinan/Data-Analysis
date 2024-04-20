import numpy as np
import pandas as pd

file_data = pd.read_csv('综合案例\data\链家北京租房数据.csv')
print(file_data.head(10))
print(file_data.shape)
print(file_data.info())
print(file_data.describe())