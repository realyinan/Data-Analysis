# 需求：画出某城市11点到12点1小时内每分钟的温度变化折线图，温度范围在15度~18度
import matplotlib
import matplotlib.pyplot as plt
import random
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'


# 准备下x, y坐标轴数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 3) for i in x]

# 创建画布
plt.figure(figsize=(20, 8), dpi=70)

# 绘制折线图
plt.plot(x, y_shanghai, color='r', label='上海')
plt.plot(x, y_beijing, color='b', linestyle='--', label='北京')

# 添加x, y轴刻度
x_ticks_lable = ['11点{}分'.format(i) for i in x]
y_ticks = range(40)

# 修改x, y坐标轴的刻度显示
plt.xticks(x[::5], x_ticks_lable[::5])
plt.yticks(y_ticks[::5])

# 添加网格显示
plt.grid(True, linestyle='--', alpha=0.5)

# 添加描述信息
plt.xlabel('时间')
plt.ylabel('温度')
plt.title('中午11点0分到12点之间的温度变化图示', fontsize = 20 )

# 显示图例
plt.legend(loc="best")

# 展示图像
plt.show()