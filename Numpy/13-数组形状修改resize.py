import numpy as np

stock_change = np.random.uniform(0, 1, (4, 5))
print(stock_change)
print(stock_change.shape)
print('-------------------------')

# resize没有返回值，但是原数组发生了变化，只有这一个发生了变化。
stock_change.resize([5, 4])
print(stock_change)
print(stock_change.shape)