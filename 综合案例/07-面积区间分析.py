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

# 查看房屋的最大面积和最小面积
print(f"房屋最大面积是{file_data['面积(㎡)'].max()}平米")
print(f"房屋最大面积是{file_data['面积(㎡)'].min()}平米")

# 查看房租的最高值和最小值
print(f"房租最高价格为每月{file_data['价格(元/月)'].max()}元")
print(f"房租最高价格为每月{file_data['价格(元/月)'].min()}元")
 
# 面积划分
area_divide = [1, 30, 50, 70, 90, 120, 140, 160, 1200]
area_cut = pd.cut(list(file_data['面积(㎡)']), area_divide)
area_cut_data= area_cut.describe()
print(area_cut_data)

# 图形可视化
area_per = (area_cut_data['freqs'].values)*100
labels = ['30平米以下', '30-50平米', '50-70平米', '70-90平米','90-120平米','120-140平米','140-160平米','160平米以上']
plt.figure(figsize=(12, 8), dpi=70)
plt.axes(aspect=1)
plt.pie(x=area_per, labels=labels, autopct='%.2f%%', shadow=False)
plt.legend(loc='upper right')
plt.show()
