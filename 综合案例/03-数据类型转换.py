import numpy as np
import pandas as pd

file_data = pd.read_csv('综合案例\data\链家北京租房数据.csv')

# 删除重复值
file_data = file_data.drop_duplicates()
# print(file_data.info())

# 删除空值
file_data = file_data.dropna()
# print(file_data.info())

# 面积数据类型转换
data_new = np.array([])
data_area = file_data['面积(㎡)']

for i in data_area:
    data_new = np.append(data_new, i[:-2])
data_new = data_new.astype(np.float64)

file_data['面积(㎡)'] = data_new
# print(file_data.info())

# 户型数据转换
housetype_data = file_data['户型']
temp_list = []
for i in housetype_data:
    new_info = i.replace('房间', '室')
    temp_list.append(new_info)
file_data['户型'] = temp_list

print(file_data.head())
print(file_data.info())