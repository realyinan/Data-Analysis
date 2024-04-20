import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

# 设置中文字体
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'

file_data = pd.read_csv('综合案例\data\链家北京租房数据.csv')

# 删除重复值
file_data = file_data.drop_duplicates()
 
# 删除空值
file_data = file_data.dropna()
 
# 面积数据类型转换
data_new = np.array([])
data_area = file_data['面积(㎡)']

for i in data_area:
    data_new = np.append(data_new, i[:-2])
data_new = data_new.astype(np.float64)

file_data['面积(㎡)'] = data_new
 
# 户型数据转换
housetype_data = file_data['户型']
temp_list = []
for i in housetype_data:
    new_info = i.replace('房间', '室')
    temp_list.append(new_info)
file_data['户型'] = temp_list

# 户型分析
type_data = file_data.groupby('户型').count()['区域']
type_data = type_data.sort_values(ascending=False)
type_data = type_data[type_data > 50]
print(type_data)

# 画图
plt.barh(type_data.index, type_data.values)
plt.xlim(0, 2500)

plt.xlabel("数量")
plt.ylabel("户型种类")
plt.title("北京地区各户型房屋数量")

# 给每个条添加数字
for x, y in enumerate(type_data):
    print(x, y)
    plt.text(y+0.5, x-0.2, y)

plt.show()