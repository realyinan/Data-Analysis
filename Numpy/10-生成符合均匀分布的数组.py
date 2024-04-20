import numpy as np
from matplotlib import pyplot as plt

# np.random.uniform(low=0.0, high=1.0, size=None)
# 功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
# 参数介绍:
# low: 采样下界，float类型，默认值为0；
# high: 采样上界，float类型，默认值为1；
# size: 输出样本数目，为int或元组(tuple)类型，例如，size=(m,n,k), 则输出mnk个样本，缺省时输出1个值。
# 返回值：ndarray类型，其形状和参数size中描述一致。

x1 = np.random.uniform(-1, 1, 100000000)

plt.figure(figsize=(8, 6), dpi=70)

plt.hist(x1, 1000)

plt.show()