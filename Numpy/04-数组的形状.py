import numpy as np

# 一维数组
a = np.array([1, 2, 3, 4])
# 二维数组
b = np.array(
[
    [1, 2, 3],
    [4, 5, 6]
])
# 三维数组
c = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ]
)
print(a.shape)
print(a.ndim)
print(b.shape)
print(b.ndim)
print(c.shape)
print(c.ndim)
