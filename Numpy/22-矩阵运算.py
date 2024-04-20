import numpy as np

a = np.array([
    [80, 86],
    [82, 80],
    [85, 78],
    [90, 90],
    [86, 82],
    [82, 90],
    [78, 80],
    [92, 94]
    ])
b = np.array([[0.7], 
              [0.3]])
print(np.matmul(a, b))
print(np.dot(a, b))

# 二者都是矩阵乘法。 np.matmul中禁止矩阵与标量的乘法。 在矢量乘矢量的內积运算中，np.matmul与np.dot没有区别。