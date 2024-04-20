import numpy as np
# np.ones(shape, dtype)
# np.ones_like(a, dtype)
# np.zeros(shape, dtype)
# np.zeros_like(a, dtype)
arr_1 = np.ones([4, 8])
print(arr_1)

arr_2 = np.zeros([4, 8])
print(arr_2)

arr_3 = np.zeros_like(arr_1)
print(arr_3)

arr_4 = np.ones_like(arr_2)
print(arr_4)