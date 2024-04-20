import numpy as np

a = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

a1 = np.array(a)  # 深拷贝

a2 = np.asarray(a)  # 浅拷贝
print(a)
print(a1)
print(a2)
print('---------------------------------')
a[0, 0] = 100
print(a)
print(a1)
print(a2)