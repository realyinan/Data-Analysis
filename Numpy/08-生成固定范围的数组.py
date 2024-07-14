import numpy as np

# np.linspace (start, stop, num, endpoint)
# 创建等差数组 — 指定数量
# 参数:
# start:序列的起始值
# stop:序列的终止值
# num:要生成的等间隔样例数量，默认为50
# endpoint:序列中是否包含stop值，默认为ture

a = np.linspace(0, 100, 11)
print(a)

# np.arange(start,stop, step, dtype)
# 创建等差数组 — 指定步长
# 参数
# step:步长,默认值为1

b = np.arange(10, 50, 2)
print(b)

# np.logspace(start,stop, num)
# 创建等比数列
# 参数:
# num:要生成的等比数列数量，默认为5
c = np.logspace(0, 2, 5)
print(c)