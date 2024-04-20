import seaborn as sns
from matplotlib import pyplot as plt

# seaborn.boxplot(x=None, y=None, hue=None, data=None, orient=None, color=None,  saturation=0.75, width=0.8)
# 常用参数的含义如下:
# (1) palette：用于设置不同级别色相的颜色变量。---- palette=["r","g","b","y"]
# (2) saturation：用于设置数据显示的颜色饱和度。---- 使用小数表示

tips = sns.load_dataset('tips')

sns.boxplot(x='day', y='total_bill', hue='time', data=tips, palette=['g', 'b'], saturation=0.5)

plt.show()