import numpy as np

# 当 np.where 只接收一个参数（条件）时，它返回满足该条件的元素的索引。

# 创建一个示例数组
array = np.array([10, 15, 20, 25, 30])

# 找到数组中所有可以被5整除的元素的位置
positions = np.where(array % 5 == 0)

# 输出结果
print("可以被5整除的元素的位置是: ", positions)

# 创建一个二维示例数组
array = np.array([
    [10, 22, 35],
    [45, 50, 61],
    [75, 80, 95]
])

# 找到二维数组中所有可以被5整除的元素的位置
positions = np.where(array % 5 == 0)

# 输出结果
print("可以被5整除的元素的位置是：", positions)

# 当 np.where 接收三个参数时，分别是条件、满足条件时的返回值、不满足条件时的返回值。

# 创建一个示例数组
array = np.array([10, 15, 20, 25, 30])

# 根据条件选择元素：如果元素可以被5整除，则返回原值，否则返回-1
result = np.where(array % 5 == 0, array, -1)

# 输出结果
print("根据条件选择的元素是：", result)

