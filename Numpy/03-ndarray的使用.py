import numpy as np

# ndarray 多维数组
score = np.array( 
 [[80, 89, 86, 67, 79],
 [78, 97, 89, 67, 81],
 [90, 94, 78, 67, 74],
 [91, 91, 90, 67, 69],
 [76, 87, 75, 67, 86],
 [70, 79, 84, 67, 84],
 [94, 92, 93, 67, 64],
 [86, 85, 83, 67, 80]])

# 数组维度的元组
print(score.shape)
print(score.shape[0])
# 数组维数
print(score.ndim)
# 数组中的元素数量
print(score.size)
# 一个数组元素的长度（字节）
print(score.itemsize)
# 数组元素的类型
print(score.dtype)
