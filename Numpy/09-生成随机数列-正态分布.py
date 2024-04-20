import numpy as np
from matplotlib import pyplot as plt

# np.random.normal(loc=0.0, scale=1.0, size=None)
# loc：float
# 此概率分布的均值（对应着整个分布的中心centre）
# scale：float
# 此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
# size：int or tuple of ints
# 输出的shape，默认为None，只输出一个值

# 生成均值为1.75，标准差为1的正态分布数据，100000000个
x1 = np.random.normal(1.75, 1, 100000000)

plt.figure(figsize=(8, 6), dpi=70)

plt.hist(x1, 1000)

plt.show()