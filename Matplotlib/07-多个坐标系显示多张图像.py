import matplotlib
import matplotlib.pyplot as plt
import random
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'

# 准备下x, y坐标轴数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 3) for i in x]

# 创建画布
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=70)

# 绘制折线图
axes[0].plot(x, y_shanghai, color='r', label='上海')
axes[1].plot(x, y_beijing, color='b', linestyle='--', label='北京')

# # 添加x, y轴刻度
x_ticks_lable = ['11点{}分'.format(i) for i in x]
y_ticks = range(40)

# # 修改x, y坐标轴的刻度显示
axes[0].set_xticks(x[::6], x_ticks_lable[::6])
axes[0].set_yticks(y_ticks[::5])
axes[1].set_xticks(x[::6], x_ticks_lable[::6])
axes[1].set_yticks(y_ticks[::5], )

# # 添加网格显示
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[1].grid(True, linestyle='--', alpha=0.5)

# # 添加描述信息
axes[0].set_xlabel('时间')
axes[0].set_ylabel('温度')
axes[0].set_title('中午11点0分到12点之间的温度变化图示', fontsize = 20)
axes[1].set_xlabel('时间')
axes[1].set_ylabel('温度')
axes[1].set_title('中午11点0分到12点之间的温度变化图示', fontsize = 20)

# # 显示图例
# plt.legend(loc="best")
axes[0].legend(loc='best')
axes[1].legend(loc='best')

# 展示图像
plt.show()