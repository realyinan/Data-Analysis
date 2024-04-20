import numpy as np

stock_change = np.random.uniform(0, 1, (4, 5))

# reshape 有返回值，返回的是变形后的数组，但原数组没有发生变化。
print(stock_change)
print(stock_change.shape)
print('-----------------------------------')

print(stock_change.reshape([5, 4]))
print(stock_change.reshape([5, 4]).shape)
print('-----------------------------------')

print(stock_change.reshape([-1, 2]))
print(stock_change.reshape([-1, 2]).shape)  # -1: 表示通过待计算
print('-----------------------------------')

print(stock_change)
print(stock_change.shape)

