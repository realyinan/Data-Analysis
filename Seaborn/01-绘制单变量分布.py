import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

# seaborn.distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, color=None)
# 上述函数中常用参数的含义如下：
# (1) a：表示要观察的数据，可以是 Series、一维数组或列表。
# (2) bins：用于控制条形的数量。
# (3) hist：接收布尔类型，表示是否绘制(标注)直方图。
# (4) kde：接收布尔类型，表示是否绘制高斯核密度估计曲线。
# (5) rug：接收布尔类型，表示是否在支持的轴方向上绘制rugplot。表示是否在图的底部添加小绒毯图，显示数据点的分布。

np.random.seed(0)
arr = np.random.randn(500)  # 确定随机数生成器的种子,如果不使用每次生成图形不一样
sns.displot(arr, bins=20, kde=True, rug=True)
plt.show()