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

# 房源数量分析
new_df = pd.DataFrame({'区域': file_data['区域'].unique(), '数量': [0]*13})
# print(new_df)

area_count = file_data.groupby(['区域']).count()
new_df['数量'] = area_count.values
# print(new_df)

df_all = pd.DataFrame({'区域':file_data['区域'].unique(),
              '房租金额':[0]*13,
              '总面积':[0]*13})

df_all['房租金额'] = file_data.groupby(['区域'])['价格(元/月)'].sum().values
df_all['总面积'] = file_data.groupby(['区域'])['面积(㎡)'].sum().values

df_all['每平方的房租'] = round(df_all['房租金额']/df_all['总面积'], 2)
# print(df_all)

df_merge = pd.merge(new_df, df_all, on='区域')
# print(df_merge)

# 画图
# plt.figure(figsize=(15, 10), dpi=70)
fig, ax1 = plt.subplots(1, 1, figsize=(12, 8), dpi=70)

ax1.bar(df_merge['区域'], df_merge['数量'], color='orange', label='数量')
ax1.set_ylabel('数量')
plt.legend(loc='upper left')


ax2 = ax1.twinx()
ax2.plot(df_merge['区域'], df_merge['每平方的房租'], 'or-', label='价格')
for x, y in enumerate(df_merge['每平方的房租']):
    ax2.text(x, y, y)
ax2.set_ylabel('价格')
plt.legend(loc='upper right')

plt.show()