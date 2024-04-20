import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# seaborn.jointplot(x, y, data=None, kind='scatter', stat_func=None, color=None, ratio=5, space=0.2, dropna=True)
# 上述函数中常用参数的含义如下：
# (1) kind：表示绘制图形的类型。
# (3) color：表示绘图元素的颜色。
# (4) height：用于设置图的大小(正方形)。
# (5) ratio：表示中心图与侧边图的比例。该参数的值越大，则中心图的占比会越大。
# (6) space：用于设置中心图与侧边图的间隔大小。

# 绘制散点图
df = pd.DataFrame({'x': np.random.randn(500), 'y': np.random.randn(500)})

sns.jointplot(x = 'x', y = 'y', data=df, kind='scatter', color='r', height=5, ratio=8, space=1)

plt.show()