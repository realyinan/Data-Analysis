import seaborn as sns
from matplotlib import pyplot as plt

# seaborn.stripplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, jitter=False)
# 上述函数中常用参数的含义如下
# (1) x，y，hue：用于绘制长格式数据的输入。
# (2) data：用于绘制的数据集。如果x和y不存在，则它将作为宽格式，否则将作为长格式。
# (3) jitter：表示抖动的程度(仅沿类別轴)。当很多数据点重叠时，可以指定抖动的数量或者设为True使用默认值。

dataset = sns.load_dataset('tips')
print(dataset.head())
# sns.stripplot(x='day', y='total_bill', hue='time', data=dataset, jitter=True)

# 还可调用 swarmplot0函数绘制散点图，该函数的好处是所有的数据点都不会重叠，可以很清晰地观察到数据的分布情况，
sns.swarmplot(x='day', y='total_bill', hue='time', data=dataset)
plt.show()