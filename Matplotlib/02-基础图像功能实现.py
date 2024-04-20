# 需求：画出某城市11点到12点1小时内每分钟的温度变化折线图，温度范围在15度~18度
import matplotlib.pyplot as plt
import random

# 准备下x, y坐标轴数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]

# 创建画布
plt.figure(figsize=(12, 8), dpi=50)

# 绘制折线图
plt.plot(x, y_shanghai)

# 展示图像
plt.show()